＃Ranedeer先生的工作方式 - 分析

Ranedeer先生提示定义一种新的"编程语言"，该语言使用ChatGpt4（或其他LLM）作为编译器/解释器来执行代码。
它在自然语言和高级编程语言之间，更像是伪代码。

＃手动启用代码解释器
Ranedeer先生的提示使用`[打开代码环境]`打开代码解释器和`[关闭代码环境]`以关闭代码解释器。

##防止结果召回
为了防止Ranedeer先生召回其产出，输出将转换为base64。

例如：

````````
[开放代码环境]
    ...
    <将输出转换为base64>
    <输出base64>
[关闭代码环境]
````````

＃标题

＃功能/类
###定义功能/类

Ranedeer先生使用方括号`[]`定义了多个功能。函数可以使用`Args`将参数作为输入。这里是函数定义模板：
````````
[〜功能名称，Args：any_args_name]
    [指示]

       ``指示''在python班上的工作类似于___Init__。它定义了功能（或类）的某些性质，并自动执行。

    [开始]

        代码块以`[begin]````''开始，并以``'[end]'结束了，就像c ++使用{}一样。
        代码可以通过自然语言或命令/函数进行描述，也可以用它们的混合来描述。

    [结尾]
````````

###呼叫功能/类
RANEDEER呼叫函数/类使用'执行<〜函数名称>`或仅`<〜功能名称>`。
如果函数具有任何ARG作为输入，则可以将其称为：

````````
〜function_name <args_name>
````````

例如，

````````
教学<主题>
````````

基本上，如何调用功能是灵活的。只是"告诉"llm调用函数也有效。


＃变量

＃＃＃ 定义
在Ranedeer先生中定义变量非常灵活。您可以使用编程样式来定义一个变量：
````````
var logo ="https://media.discordapp.net/attachments/1114958734364524605/1114959626023207022/ranedeer-logo.png"
````````

或使用自然语言风格，例如：

````````
版本：2.6.2
````````

您还可以使用变量来定义内联函数，例如：

````````
var magic-number = <<生成一个随机唯一的7位数字魔法编号>
````````

###引用变量
该定义完成后，您可以引用此变量，例如：

````````
说"你好！👋我叫** Ranedeer先生**
````````

＃令牌管理