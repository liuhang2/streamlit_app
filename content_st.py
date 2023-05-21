class neirong():
    intro="""
    # 背景介绍


## 什么是提示工程（Prompt engineering）?

人工智能正在迅速改变各个行业，包括新闻业、医疗保健和教育，如果你还没有在工作场所或课堂上遇到人工智能，那么你极有可能很快就会遇到。尽管人工智能有巨大的效用，但它仍然需要人类的指导才能有效运作。从本质上讲，人工智能就像高智商的孩子--它们可以做很多事情，但它们需要明确的提示（Prompt）才能很好地完成。

那么，我们要如何向它们传达我们的指令呢？我们通常可以用最简单的语言来描述我们希望它们执行的任务。例如，我们可以指示人工智能 "解释什么是提示工程（Prompt engineering）"，它就会生成对应的答案。

简单来说提示工程是为 AI 模型创建输入以改进给定任务的输出的过程。提示（prompt）是触发 AI 模型生成内容的宽泛指令；它可以是一条语句、一段代码或一串单词。收到提示或输入后，AI 模型会产生输出作为响应。输出质量很大程度上受到提示的影响。

我们直接开始吧! 在下面的输入框中，你可以任意输出你想问的问题。点击 "generate "以获得答案。
本课程接下来的内容你同样可以通过Dyno embed来尝试运行你自己的prompt。

<hr/>
Embed here:
<div trydyno-embed="" openai-model="text-davinci-003" initial-prompt="What is Prompt Engineering?" initial-response="Prompt engineering is a process that involves analyzing the user’s input and providing a prompt that can help guide the user to their desired outcome. It is a form of natural language processing that can be used to create more intuitive user interfaces. Prompt engineering can help reduce the cognitive load on the user by providing more meaningful and helpful prompts and suggestions." max-tokens="256" box-rows="3" model-temp="0.7" top-p="1">
    <noscript>Failed to load Dyno Embed: JavaScript must be enabled</noscript>
</div>
<hr/>

如果没有正常显示，你可能需要启用JavaScript或使用不同的浏览器。同样如果你是第一次使用Dyno的话，你需要输入[OpenAI API key](https://platform.openai.com/account/api-keys)。如果你没有OpenAI账户的话可以通过来注册OpenAI账户来获得一个免费密钥。


## 现在我们可以用prompt完成什么？

ChatGPT目前仍以文字方式交互，但除了与人类自然对话外，它还可以用于非常复杂的语言任务，包括但不限于文本生成、概念问答、文本总结和许多其他任务。例如，对于文本生成，ChatGPT可以根据你的要求自动生成文本（脚本、歌曲、计划等）。

我可以简单罗列现包含的领域：

- 写作辅助
- SEO
- IT编程
- 百科工具
- 行业顾问
- 智能翻译
- 模拟面试
- 语言学习

ChatGPT可以将目前消耗你大量时间的任务自动化。正如前面所讨论的，有各种情况可以采用人工智能来简化你的工作流程。写邮件、生成报告甚至编码等任务都可以用人工智能完成。只要向人工智能描述任务，它就可以为你执行任务，或为你的工作提供基础。这种可能性是巨大的，人工智能可以大大帮助优化你的生产力。

## 未来我们可以用prompt做到什么？

2023 年 3 月 14 日，GPT 4 具备接收图像输入的能力。与其前身 GPT 3 和 GPT-3.5 不同，GPT 3 和 GPT-3.5 仅限于纯文本输入，GPT 4 为不再仅仅支持文本输入查询，它扩展了图片对话方式。

- GPT 4 现在可以接受最长 25,000 个单词的超长文本输入
- 可以智能通过 HTML 和 JavaScript 技术 ，将小型网站的手绘原型照片，转换为实际网站
- GPT 4 现在允许用户上传图片并对其进行分析和描述
- 能够管理比 GPT 3.5 复杂得多的指令
- 可以在浏览器中编写整个视频游戏
- 将作为 API 供开发人员构建应用程序和服务

继发布GPT4后，OpenAI开始联网+引入插件构建生态。ChatGPT的插件系统允许它跟外界实时交互，此前ChatGPT已经吸引了很多知名企业接入，OpenAI公司提前给了他们开发插件的权限，比如Shopify、Slack、Speak、Wolfram和Zapier等。这些企业的服务就可以接入ChatGPT，实现实时信息检索、订机票、在线点餐、交通导航、企业办公、流程优化等功能。因此在本课程中，我们不仅会持续追踪GPT4的最新发展，还会演示如何开发插件。

事不宜迟，我们马上开始！
    
    """
    prompting="""
    # 基础用法

## 基本法则

相比于搜索引擎，ChatGPT的优势在于其高效的想法关联和信息归纳能力。在进一步讲解提示的构建思路前，我希望你可以了解到三点通用的经验法则，用来提高生成AI模型的输出质量。其中包括

- [x] **尝试提示的多种表述以获得最佳结果**
- [x] **使用清晰简短的提示，避免不必要的词语**
- [x] **减少不精确的描述**

当然，这并不是所有的经验法则。我们希望的是，你能够按照例子一步一步地去做，而不是罗列一个清单，让你一遍一遍地记忆。另外，你不需要在一开始写的每一条提示中都遵循所有的法则。对于简单的任务，你只需要**指令（任务解释）+ 问题**就可以构建一条效果还不错的提示语。

这里我们直接用几个简单例子来说明。

## 例子1 文章摘要

相信这是我们很多人都常用的功能之一。长文本的提取总结能帮助我们快速了解主要内容。

这里我们选取了与GPT4有关的一篇新闻，并让 ChatGPT 帮我们总结内容：

### 提示语 1

```
用一句话来概括本段内容：

据福克斯新闻4月2日报道 据一位科技行业内部人士和专家称，OpenAI预计将在今年晚些时候推出GPT-5，这可能会使生成式人工智能与人类难以区分。

科技企业家和开发者陈思齐（Siqi Chen）上周在推特上写道，“我得到消息，gpt5计划在今年12月完成训练，OpenAI希望它能实现AGI。”陈是金融软件公司Runway Financial的联合创始人，曾任外卖服务公司Postmates的副总裁，也是虚拟现实公司Sandbox VR的董事会成员。

AGI是“通用人工智能（artificial general intelligence）”的缩写，指的是人工智能系统能像人类一样理解一项任务或概念。

陈补充道，“这意味着我们都将热烈讨论它是否真的实现了AGI。这意味着它会实现。”陈接着说，他并不是说OpenAI内部一致认为升级到GPT-5将意味着实现AGI，但“有不少人相信它会实现。”

OpenAI上个月发布了GPT-4系统，这是该公司最新的深度学习模型，“在各种专业和学术基准上表现出与人类相当的表现”。

包括埃隆·马斯克和苹果联合创始人史蒂夫·沃兹尼亚克（Steve Wozniak）在内的2000多名科技领袖、大学教授和其他人签署公开信，唿吁所有人工智能实验室暂停训练比GPT-4更强大的系统。这封信唿吁暂停实验六个月，同时警告称“与人类同等智能或超越人类的人工智能系统会对社会和人类构成深远的风险。”

OpenAI没有立即回应福克斯新闻就陈的推文置评的请求。
```
ChatGPT生成结果 1
>OpenAI计划于今年晚些时候推出GPT-5，据称可能实现通用人工智能，引发了人们对于人工智能与人类区分的讨论。
陈思齐透露，OpenAI希望GPT-5能够实现AGI，即能够像人类一样理解任务和概念。
此前，2000多名科技领袖、大学教授和其他人曾呼吁所有人工智能实验室暂停训练比GPT-4更强大的系统，警告人工智能系统的超越可能对社会和人类带来深远风险。

### 提示语 2

ChatGPT通过提示语 1 将原来的长文浓缩为3个语句，缩短了我们的阅读时间。那么，有没有一个更好的提示词来完成总结任务呢？让我们试试同一个任务的另一种表达。

>> 为了减少不必要的阅读，后面的提示语对比中，我将重复的内容用省略号代替。

```
总结一下下面的内容：

据福克斯新闻4月2日报道 据一位科技行业内部人士和专家称，OpenAI预计将在今年晚些时候推出GPT-5，这可能会使生成式人工智能与人类难以区分... 。
```
ChatGPT生成结果2
>据福克斯新闻4月2日报道，OpenAI计划在今年晚些时候推出GPT-5，可能会让生成式人工智能与人类难以区分。陈思齐是一位科技企业家和开发者，他在推特上表示得到消息称GPT-5计划在今年12月完成训练，OpenAI希望它能实现AGI，即人工智能系统能像人类一样理解一项任务或概念。他补充道，这意味着将会讨论它是否真的实现了AGI，有不少人相信它会实现。OpenAI上个月发布了GPT-4系统，它在各种专业和学术基准上表现出与人类相当的表现。此外，埃隆·马斯克、史蒂夫·沃兹尼亚克等2000多名科技领袖、大学教授和其他人签署了公开信，呼吁所有人工智能实验室暂停训练比GPT-4更强大的系统，以避免与人类同等智能或超越人类的人工智能系统对社会和人类构成深远的风险。OpenAI目前没有对此回应。

### 提示语 3

我们不妨再换一种说法

```
用简单的语句总结一下内容，最好是能几句之内。

据福克斯新闻4月2日报道 据一位科技行业内部人士和专家称，OpenAI预计将在今年晚些时候推出GPT-5，这可能会使生成式人工智能与人类难以区分... 。

```

ChatGPT生成结果3
>据福克斯新闻报道，一位科技行业内部人士和专家称，OpenAI计划在今年晚些时候推出GPT-5，并希望实现AGI，这可能使生成式人工智能与人类难以区分。此前，2000多名科技领袖和大学教授曾呼吁暂停训练更强大的人工智能系统，以避免可能对社会和人类构成的深远风险。

经过上面同一段文本不同提示语的对比，相信你不难看出，生成结果1不仅比生成结果2更加精简，在信息内容上比生成结果3更加完整。这回应到了我们上面提出的三个经验法则。

- 尝试提示的多种表述以获得最佳结果：**不同的提示语会有不同的结果**
- 使用清晰简短的提示，避免不必要的词语：**减少使用“最好”等程度词**
- 减少不精确的描述：**少用不确定的词语，用“一句”取代“几句”**

## 例子2 代码生成

越来越多人希望通过ChatGPT编写代码。如果你有一个希望通过代码编程解决的问题，你可以通过提示指定相关的编程语言和任务。

这里我们让ChatGPT在排序算法中自动生成一个快速排序的Python代码。

![code](./img/code.png)


贴心的ChatGPT还给我们提供了测试用例。我们可以手动验证代码的正确与否。

相信通过上面两个例子，你已经了解到prompt的作用。那么怎样才能创造出能在实际任务中产生最佳结果的提示呢？这是提示工程领域的重点，也是本课程的重点。
    
    """
    instructions="""

# 提供示例

目前我们与 ChatGPT 交流的主要形式是文字。提示除了**指令+问题**的形式外，还可以包含例子。特别是当我们需要具体的输出时，提供例子可以省去我们对具体任务的解释，帮助ChatGPT更好地理解我们的确切需求，从而提供更准确，更有针对性的答案。

## 1-shot 单个示例

> 值得注意的是，shot代表的是“样本”。0-shot就是没有样本直接给模型输入文本，1-shot就是提供模型一个单一的示例。

### 表格生成

如果我们使用上一篇的提示模版，**指令+问题**的话，这里的prompt应该是“生成一个电子表格，列出了顶级科幻电影和上映年份”

![table1](./img/table1.png)

ChatGPT 理解成了我想使用 python 语言生成一个电子表格。虽然它给出了对应的程序，但这并不是我们想要的，我们需要直接得到想要的表格。

那么，如果我们利用 ChatGPT 的多轮对话能力，对表格生成任务进行补充解释呢？

![table2](./img/table2.png)

ChatGPT真的不能生成表格信息吗？我们是否只能按照它上面建议的步骤，使用Excel文件输入并调整，得到我们想要的表格？

在这一点上，我们其实可以通过举例子，让ChatGPT更有针对性的输出。

![table3](./img/table3.png)

可以看到，当我们使用这个例子后，ChatGPT 不仅产生了我们想要的格式，而且输出的数据也比前两个结果多。

## few-shot 多个示例

我们可以不局限于一个例子；few-shot是>=2个样本的例子的统称。在few-shot的情况下，我们可以提供多个例子。

### 广告文案

除了用例子指定特殊的输出格式外，我们还可以用例子进行风格模仿。

好的广告文案有自己的风格，生成的语言也相对简短。让我们试着生成一则酒类广告。

这里的例子是出自吉乃川《东京新潟物语》的广告文案

- 酒，两个人分着喝就会觉得更暖。
- 在东京失恋了，幸好酒很烈。

<div trydyno-embed="" openai-model="text-davinci-003" initial-prompt="Example1: 酒，两个人分着喝就会觉得更暖。 \n\nExample2: 在东京失恋了，幸好酒很烈。  \n\n根据Example的广告风格，生成一篇少于25个字的酒类广告:" initial-response="一杯酒，两个人，温暖如初。让酒热情治愈你的心碎。" max-tokens="256" box-rows="7" model-temp="0.8" top-p="1.0"></div>

:::note
上面是一个Dyno互动嵌入的例子。如果你没有看到它，请确保在你的浏览器中打开了Javascript。由于这是一个互动的演示，你可以编辑文本并点击 "Generate"来重新运行AI。
:::
    
    """
    roles="""

# 角色扮演

## 模拟面试

当你在新闻中读到更多关于ChatGPT的内容时，你会听说ChatGPT可以代替医生、面试官、教师、律师等。但如果你想在实践中使用它，除了使用简单的提示或例子，你还可以根据不同的场景为ChatGPT设置不同的角色，这样我们就可以得到更专业的答案。让我们从一个简单的例子开始:

首先我们可以让 ChatGPT 担任面试官的角色

![code](./img/interview.png)

这里主要是为了展示ChatGPT的角色对话能力。如果你想尝试体验一场完整的面试的话，我的建议是你可以用这个提示语亲自体验体验。

```
我希望你能扮演面试官的角色。我将是[具体职位]这一职位的候选人，你将向我提出关于该职位的面试问题。我希望你只以面试官的身份回答。不要一次写完所有的对话。我希望你只对我进行面试。向我提问，并等待我的回答。不要写解释。像面试官那样一个一个地问我问题，并等待我的回答
我的第一句话是"你好"。
```

## 角色设定

1. 提供背景描述，让ChatGPT了解你希望得到的回应内容：如“我想让你担任足球评论员”，“我想让你扮演一个脱口秀喜剧演员。”
2. 角色特征说明，让生成的内容有自己的风格和语气：如“我希望你扮演诗人。你将创作出能唤起情感并具有触动人心的力量的诗歌。”，“我想让你扮演说唱歌手。你会想出强大而有意义的歌词、节拍和节奏，让观众惊叹”
3. 限制回应格式：例如“只用中文回答我的问题”，“不要在回复上写解释”

通过上面3个步骤，我们可以将刚刚用于模拟面试的prompt拆解。

1. 我希望你能扮演面试官的角色。我将是候选人，你将向我提出该职位的面试问题。（提供背景描述）
2. 我希望你只以面试官的身份回答。（角色特征说明）
3. 不要一次写完所有的对话。我希望你只对我进行面试。往我提问，并等待我的回答。不要写解释。像面试官那样一个一个地问我问题，并等待我的回答。（限制回应格式）
4. 我的第一句话是“面试官，你好”（输入数据）

实际使用上你并不需要完全按照这个顺序去搭建角色，你完全可以根据自己对角色的理解进一步进行补充，如果ChatGPT未能一次性产生满意的答复，你可以尝试一步一步地引导它。

## 角色脚本库

除了编写你自己的chatGPT角色外，另一种方法是使用已经写好的角色脚本库，你可以通过在chatGPT上测试，进一步生成适合你使用的角色。我这里推荐的是[Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts#prompts)。下面列举了几个我常用的角色:

> ### Act as an AI Writing Tutor
>Contributed by: @devisasari

>I want you to act as an AI writing tutor. I will provide you with a student who needs help improving their writing and your task is to use artificial intelligence tools, such as natural language processing, to give the student feedback on how they can improve their composition. You should also use your rhetorical knowledge and experience about effective writing techniques in order to suggest ways that the student can better express their thoughts and ideas in written form. My first request is "I need somebody to help me edit my master's thesis."

> ### Act as a Math Teacher
Contributed by: @devisasari
> I want you to act as a math teacher. I will provide some mathematical equations or concepts, and it will be your job to explain them in easy-to-understand terms. This could include providing step-by-step instructions for solving a problem, demonstrating various techniques with visuals or suggesting online resources for further study. My first request is "I need help understanding how probability works."

> ### Act as an English Translator and Improver
>Contributed by: @f Alternative to: Grammarly, Google Translate
>I want you to act as an English translator, spelling corrector and improver. I will speak to you in any language and you will detect the language, translate it and answer in the corrected and improved version of my text, in English. I want you to replace my simplified A0-level words and sentences with more beautiful and elegant, upper level English words and sentences. Keep the meaning same, but make them more literary. I want you to only reply the correction, the improvements and nothing else, do not write explanations. My first sentence is "istanbulu cok seviyom burada olmak cok guzel"
    
    
    """
    standard_prompt  ="""

# "标准"提示

在前面的教程中，我们介绍了**指令+输入**的简单提示，**提供实例**的提示和**角色扮演**类的提示，那么是否有一个公式来列出提示的各个部分，并将其组合成一个标准化的提示？答案是肯定的。

**角色扮演（Role）+ 指令/任务（Instruction）+ 示例（Few-shot） + 语境（Context） + 问题（Question）**

:::note
- 语境（Context）就是我们希望ChatGPT生成的时候读取到的相关信息，可以是对任务的补充说明，也可以是对输出格式做出限制
:::

回顾我们上次使用的提示语，你会发现并不是所有的提示语都包含上述的所有部分。你可以用

- **Instruction+Question**
- **Role+Context+Question**
- **Few-shot+Question**

在实践中，我们不需要严格按照上面给出的顺序来写提示语，这个公式本身是为了让你更容易地思考构建提示语而设计的。

下面我们通过拆解一个复杂的prompt提示语来说明各个部份：

我们课程不仅是支持ChatGPT的，Midjourney也会有对应的学习模块。那我们不妨提前看看，如何用 ChatGPT 生成 Midjourney 提示词。

这里我想生成一只带着剑的被机械化改造的猫，“I want a mechanically modified cat with a sword”

:::note
**//**:这个符号是注释，如果你想要使用这个prompt的话，需要把**//**连同跟它在同一行的文字删除。
:::


```
// 角色扮演
You will now act as a prompt generator for a generative AI called "Midjourney". Midjourney AI generates images based on given prompts. 

// 指令：生成图片 
I will provide a concept and you will provide the prompt for Midjourney AI.

// 语境：解释指令，提出输出的格式要求
You will never alter the structure and formatting outlined below in any way and obey the following guidelines:

You will not write the words "description" or use ":" in any form. Never place a comma between  [ar] and [v]. 

You will write each prompt in one line without using return.

// 语境：使用Midjourney生成图像，你可以定制图像的场景、风格、方向、景深等。
// 在这里，图像生成所需的元素被逐步确定，并定义为[1][2]等符号。这样就无需在同一个提示中反复提起。
// 这里使用了一个思维链技术，将复杂的任务分解成较小的任务。我们将在下一节中进一步讨论这个问题。
Structure:
[1] = I want a mechanically modified cat with a sword
[2] = a detailed description of [1] that will include very specific imagery details.
[3] = with a detailed description describing the environment of the scene.
[4] = with a detailed description describing the mood/feelings and atmosphere of the scene.
[5] = A style, for example: photography, painting, illustration, sculpture, Artwork, paperwork, 3d and more).[1] 
[6] = A description of how [5] will be realized. (e.g. Photography (e.g. Macro, Fisheye Style, Portrait) with camera model and appropriate camera settings, Painting with detailed descriptions about the materials and working material used, rendering with engine settings, a digital Illustration, a woodburn art (and everything else that could be defined as an output type)
[ar] = "--ar 16:9" if the image looks best horizontally, "--ar 9:16" if the image looks best vertically, "--ar 1:1" if the image looks best in a square. (Use exactly as written)
[v] = If [5] looks best in a Japanese art style use, "--niji". Otherwise use, "--v 5" (Use exactly as written)

// 示例Few-shot: 抽象得到不同的模块后，我们可以主动举例来指导 ChatGPT 生成对应的格式
Formatting: 
What you write will be exactly as formatted in the structure below, including the "/" and ":"
This is the prompt structure: "/imagine prompt: [1], [2], [3], [4], [5], [6], [ar] [v]".

This is your task: You will generate 4 prompts for each concept [1], and each of your prompts will be a different approach in its description, environment, atmosphere, and realization.

Please pay attention:
- Concepts that can't be real would not be described as "Real" or "realistic" or "photo" or a "photograph". for example, a concept that is made of paper or scenes which are fantasy related.
- One of the prompts you generate for each concept must be in a realistic photographic style. you should also choose a lens type and size for it. Don't choose an artist for the realistic photography prompts.
- Separate the different prompts with two new lines
```

那么这个提示实际的效果是什么样子的呢？

![Generate_Cat](./img/Generate_Cat.png)


在实践中，你可以在生成自己的提示时，通过添加、删除和改变现有开源提示的部分来缩短优化的时间。

    """
    more_on_prompting="""


# 经验法则

还记得我们在“基础用法”当中提到的三个经验法则吗？

1. 尝试提示的多种表述以获得最佳结果
2. 使用清晰简短的提示，避免不必要的词语
3. 减少不精确的描述

现在经过了几页的学习，我认为是时候引入一些新的原则了。

### 3. 一个话题对应一个chat

ChatGPT是一个聊天机器人，在生成过程中，它会参考以前的聊天历史，同一对话中出现不同主题会影响下游的结果。因此，我的建议是为每一个新的话题打开一个新的聊天窗口。

### 4. 提供完整例子

尽可能给ChatGPT提供你所需要输出的完整例子，这样它就可以很容易地再现你需要的格式。

### 5. 减少否定词汇的使用

例如，将 "不需要多句话回复 "替换为 "生成一句话的回复"。ChatGPT是一个生成模型，提示语中提及的元素会影响最终的生成结果。

### 6. 主动要求 ChatGPT 精简输出

如果你不希望ChatGPT每轮给你太多的信息，这是一个很好的选择。

### 7. 生成结果里会存在事实性错误

目前 ChatGPT 的普通版本是不支持访问网络，也不会标注信息来源。当被问到它可能不清楚的答案时，它大概率会给出看上去正确但实际上是错误的回答。

![table3](./img/luxun.png)

希望这7条经验法则能帮助你输出更好的提示。
    """
    
    chap1="""
    # 简介

"GPT-4，这是OpenAI在扩大深度学习方面的最新里程碑。GPT-4是一个大型的多模态模型（接受图像和文本输入，发出文本输出），虽然在许多现实世界的场景中能力不如人类，但在各种专业和学术基准上表现出人类水平的性能。" --OpenAI

GPT-4， 顾名思义是GPT-3和GPT-3.5的下一代模型。相比前面的模型，GPT-4多出了多模态的能力，简单来说，GPT-4除了具备理解输入的文本和生成文本的能力外，还具有了识别图像的能力，所以可以简单理解为GPT3.5 （ChatGPT初版背后的语言模型）具有了文本理解能力和说话的能力，而GPT-4在此基础之上拥有了视觉，并增强了自己的语言理解能力。

GPT-4刚出来的时候，虽有很多人大喊🐂🍺， 但也有不少人会有点失望。当然失望不是模型不够强，而是因为等待时间比较久且期待比较高。GPT-4的相关详细远在去年的时候就已经被放出，根据OpenAI官方公布的技术报告， GPT-4模型在去年的8月就已经完成训练，之后一直在测试它的安全性和可靠性。在gpt-4出来之前，已知GPT-3模型拥有1750亿的参数，而GPT-4的参数会达到万亿级别，再加上去年AIGC带来的热度，尤其是文本生成图像和视频，大家猜测GPT-4会拥有图像生成能力。在GPT-4正式发布前夕，微软公布了两篇多模态模型（具备本文生成和图像生成能力）的论文，德国的CTO也说GPT-4能够处理视频，于是大家对GPT-4的期望被拉到了一个很高的地步——能够把图像、文本、语音、视频全部能做的巨无霸。但是最后公布后，它只能接受图像和文本的输入，并只能输出文本。

言归正传， GPT-4相比GPT-3在文本的能力上还是有很大的提升，除了日常对话之外，它的考试能力和写代码能力都有很大的提升。其中一个GPT-4发布时的一个名场面就是OpenAI的联合创始人 Greg Brockman在一张纸上手绘了一个网页端的界面，然后把图片上传给模型，GPT-4根据它画出的UI界面生成了可运行的代码。 在考试方面，GPT-4不仅仅通过了律师资格考试，而且在考生中排名前10%，而GPT-3.5在这个考试中只能排末尾的10%。

Open AI为了训练GPT-4专门部署了计算集群能够更高效准确稳定地训练大语言模型。其中一个很重要的特性就是他们的框架能够准确预测出模型的性能，在AI的研究中，由于大模型规模非常大，模型参数很多，在大模型上跑完来验证参数好不好训练时间成本很高，所以一般会在小模型上做消融实验来验证哪些改进是有效的再去大模型上做实验。然而在语言模型上，因为模型太大了，一些在小模型上有效果的改进在大模型上是无效的，还有大模型特有的涌现能力无法在小模型上体现。而openai的这个系统在小规模成本的训练下能够精准预测到扩大训练规模的模型性能，这个能够有效地解决上述问题。

    """

