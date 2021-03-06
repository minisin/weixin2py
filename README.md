#weixin2py--微信公众平台接口程序

### 1.简介

* 使用python2.7和django 1.5.1开发的微信公众平台服务端程序，可以自动回复用户发来微信的消息。
* 最初的启发来自“武大助手”，类似的平台，提供校园信息服务&服务微信化
* 有什么 意见或者建议请发issue

### 2. 特性
* 当用户发来第一条消息的时候，自动检测用户是否存在并生成一个唯一的用户（使用openid），存储到数据库。
* 将从腾讯微信服务器接收到的消息转化为对象并可以让处理视图使用。
* 实现了自动回复用户消息，您可以自定义您的消息回复函数，构建一个新的django视图以完成处理。（例如，当用户输入“天气”，您可以定义一个消息匹配和获取天气的函数，給用户返回一个天气消息）
* 用户当前菜单功能状态存储（使用简单的session数组），例如，用户进入“绑定”功能，内存中的session字典将记录用户进入了绑定功能，并将接下来用户输入的信息交给绑定验证函数进行处理，而不是一级菜单的处理函数处理。由于功能较为简单，并未使用数据库存储，您可以根据自己的需要更改这个方式。
* 少许额外功能，例如绑定，还有适合本学校的成绩查询脚本。
* 消息模版，存储在weixin2py/templates下，方便使用render_to_response进行处理。

需要可使用版本请移步：[这里](https://github.com/winkidney/weixin2py/tree/release1.0) 

 [博客](http://blog.sina.com/winkidney) 

 [My-github](http://github.com/winkidney)

by winkidney 20130818


