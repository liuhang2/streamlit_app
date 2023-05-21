class neirong2():
    introduction="""
    # 简单介绍

恭喜你! 现在你已经学会了如何编写提示语。本节主要讨论的是如何使用提示语来解决我们在日常或工作中遇到的任务。如果你已经有了一个提示语集，如何决定哪些提示语适合手头的任务？在本节中，我们将通过一些实际例子来给你提供灵感。在挑选案例的时候，我们更加希望展示的是如何将复杂的工作任务拆解成相互关联的小任务。例如在PPT制作中，我们就可以通过以下几个步骤：

1. 创意生成
2. 细化创意要求和背景，生成具体页数的PPT
3. 通过角色扮演，要求 ChatGPT 精简第一页的内容
4. 按照第一页的精简风格，提炼余下的PPT
5. 内容页可以按照举例子，时间轴等不同排序方式进行二次调整
6. 根据前面的内容生成封面页和背景图

通过拆解PPT制作这一大任务，1-6分别变成了文本生成，文本总结，结构化数据生成，文本精简等任务，而这些任务往往已有公开的指令集或者我们使用上一章节的思路可以快速完成提示的编写。
    
    """
    writing="""
    # 写作&博客

在 ChatGPT 的帮助下，文本内容的产出，尤其是撰写博客文章的过程得到了进一步的简化。你可以让 ChatGPT 激发你的灵感，也可以让它美化你的文章内容。

这里我们希望能通过prompt写出一篇以“ChatGPT对社会各行各业的影响”为主题的博客。

本页我们希望你可以使用 ChatGPT 网页版，利用 ChatGPT 写作的过程应该是迭代的：你应该编写提示，查看模型输出的内容，调整输出的内容，然后重复此过程。

:::note
下面的案例中，绿色高亮代表的是ChatGPT生成的内容。
:::

## 创意生成

第一步我们可以通过提示激发 ChatGPT 的创造力。我们只给一个大致的方向，让它拟定一个跟自己相关的文章标题。

```text

我想编写一篇以“ChatGPT对社会各行各业的影响”为主题的博客，需要你帮我拟定一个能吸引人点击的标题，标题中必须带有“ChatGPT”，你会怎么写呢？

// highlight-start

以下是几个可能的标题供你参考：

1. ChatGPT：颠覆社会的新力量
2. 探索ChatGPT在各行各业的应用与影响
3. ChatGPT：改变我们未来的智能化解决方案
4. ChatGPT：人工智能时代的先锋之一
5. ChatGPT：如何在数字化时代中提升社会效率与生产力

以上标题旨在吸引读者的兴趣，并强调ChatGPT对于各行各业的影响力和潜在作用。你可以根据你的实际情况和读者对象来选择最适合的标题。

//highlight-end
```

## 生成大纲

看上去第1个标题会更加吸引人的眼球，下面我们使用角色扮演，让ChatGPT扮演业内专家来给出文章的大纲。

```text
我想让你扮演一个业内专家，你深耕于人工智能领域，了解人工智能对各行各业的影响，你将编写一篇叫做“ChatGPT：颠覆社会的新力量”的博客。在博客里，你打算列出3个被ChatGPT影响的行业，分析出行业本身的背景以及ChatGPT对业内人士的帮助。首先你要写出的是文章的大纲。大纲的内容要看上去一目了然，有参考性意义。

// highlight-start

好的，下面是“ChatGPT：颠覆社会的新力量”博客文章的大纲：

I. 引言
A. 简介ChatGPT和人工智能的背景
B. 文章的主要目的

II. 行业1：医疗保健
A. 医疗保健的背景和挑战
B. ChatGPT在医疗保健中的应用
C. ChatGPT对医疗保健带来的影响

III. 行业2：金融服务
A. 金融服务的背景和挑战
B. ChatGPT在金融服务中的应用
C. ChatGPT对金融服务带来的影响

IV. 行业3：教育
A. 教育的背景和挑战
B. ChatGPT在教育中的应用
C. ChatGPT对教育带来的影响

V. 结论
A. 总结ChatGPT对社会各行各业的影响
B. 探讨ChatGPT未来的发展前景

VI. 参考文献

这个大纲旨在提供一个简单清晰的框架来展示ChatGPT在三个不同行业的应用，并分析其带来的影响。在每个行业的部分，我们将讨论该行业面临的挑战和问题，以及ChatGPT在该领域的应用，最后总结出ChatGPT对该行业带来的影响。在结论中，我们将综合讨论ChatGPT对各个行业的影响，并讨论ChatGPT的未来发展前景。

//highlight-end
```

## 内容生成

有了不错的大纲后，我们就可以用这个大纲让 ChatGPT 写一篇完整的博客文章。

```text

用这个大纲写一篇博文

// highlight-start

随着人工智能技术的不断发展，ChatGPT作为一种自然语言处理技术，在各行各业的应用越来越广泛。本文将探讨ChatGPT如何影响了以下五个行业。

一、新闻媒体行业

作为一种自然语言处理技术，ChatGPT可以帮助新闻媒体快速生成新闻稿件，减少新闻编辑的工作量，提高稿件的质量。此外，ChatGPT还可以根据用户的兴趣和需求，为用户推荐个性化的新闻内容，提升用户体验。

二、金融行业

ChatGPT在金融行业的应用非常广泛。它可以被用来分析市场趋势、预测金融风险、进行智能投资等。此外，ChatGPT还可以为银行提供自然语言的客服解决方案，使得客户可以更加便捷地进行咨询和操作。

三、教育行业

ChatGPT可以为教育行业提供智能化的教育解决方案。例如，它可以被用来生成自然语言的教学材料、进行个性化的教育推荐和评估、智能化的辅导等。这些功能有助于提高学生的学习效率和学习成绩，推动教育行业的数字化升级。

四、医疗行业

医疗领域需要大量的病例数据和医疗知识，而ChatGPT能够帮助医生快速地对病例进行诊断和治疗方案的生成。此外，ChatGPT还可以被用来进行药物研究和开发、进行医疗知识的智能化管理等。

五、广告营销行业

ChatGPT可以被用来进行智能化的广告营销，例如智能化的广告投放、智能化的营销分析、个性化的广告推荐等。这些功能有助于提高广告的精准度和效果，推动广告营销的数字化转型。

总的来说，ChatGPT作为一种自然语言处理技术，在各行各业都有着广泛的应用前景。它可以帮助行业提高效率、提升用户体验、推动数字化转型，为人类智慧的拓展和提升做出贡献。

//highlight-end
```
    
    """
    ads="""
    # 广告文案

ChatGPT 可以帮助我们生成广告文案和宣传图片，这对营销品牌建设很有帮助。通常，一个产品会有一个主要的广告词，传达设计理念或宣传产品的好处。我们可以尝试直接生成文案，看看 ChatGPT 有没有好的创意。假设我们的产品是一款登山鞋，我们要怎么得到令人满意的文案和宣传图片呢？

## 背景查询

ChatGPT 能帮助你快速熟悉一个领域的背景情况。我们会在后面的章节会进一步介绍如何把ChatGPT打造成一个学习助手。

```text

我想给我的产品做一个广告文案和图片，我需要注意什么？请按照列表的形式列出要点

// highlight-start

如果你要为你的产品制作广告文案和图片，以下是需要注意的要点：

目标受众：你需要确定你的目标受众是谁，以便能够制作出吸引他们的广告。

独特卖点：你需要确定你的产品的独特卖点，并在广告中突出展示。

简洁明了：广告文案需要简短明了，能够快速传递产品信息。

视觉效果：广告图片需要有吸引人的视觉效果，能够吸引目标受众的眼球。

色彩搭配：选择合适的色彩搭配，能够让广告更加吸引人。

标题和描述：广告文案的标题和描述需要能够吸引目标受众，并传递产品信息。

呼吁行动：在广告文案中加入呼吁行动，引导目标受众采取行动，比如购买产品或了解更多信息。

合法合规：广告需要合法合规，遵守相关法律法规，不得夸大产品效果或虚假宣传。

测试优化：制作完成后，需要进行测试和优化，确保广告能够达到预期效果。

媒体选择：根据目标受众的特点和广告预算，选择合适的媒体投放广告，以获得最佳效果。

//highlight-end
```

不得不说，这里面有些点是我这个外行人第一次了解到的。那么我们接着可以让 ChatGPT 给我们生成完整的广告方案。

## 广告方案

ChatGPT产生了一个非常完整的宣传活动。我们可以按照其输出的第2和第3点，根据**轻量化、防滑、透气**的特点，进一步开发我们的标题和文案。我们还可以使用**外观、材料和细节**等元素，生成能够吸引人们购买的图片。


```text

我的产品是一款登山鞋，给我一个完整的广告方案。请按照列表形式输出。

// highlight-start

以下是一份适用于你的登山鞋的完整广告方案：

目标受众：喜欢户外运动、热爱徒步登山的人群。

广告平台：社交媒体平台、搜索引擎广告。

广告文案：简洁明了，突出产品的独特卖点和优势，比如轻量化、防滑、透气等，同时引导用户采取行动，比如购买或了解更多信息。

广告图片：采用高品质的图片展示产品的外观、材质和细节，吸引目标受众的眼球。

PPC关键词：根据你提供的信息，选择适合的PPC关键词，可以使用搜索引擎广告或社交媒体广告，引导目标受众了解更多产品信息。

社交媒体平台：选择适合你目标受众的社交媒体平台，比如微信、微博、抖音等，进行广告投放。

搜索引擎广告：使用谷歌广告等搜索引擎广告平台，选择适合的关键词，进行广告投放。

KOL合作：选择有影响力的户外运动领域KOL合作，增加品牌曝光率。

官网优化：针对关键词进行网站优化，提高官网在搜索引擎的排名，增加流量和销量。

活动营销：开展品牌活动，比如优惠促销、线下活动等，吸引目标受众的参与，增加品牌忠诚度。

数据追踪：通过Google Analytics等数据追踪工具，对广告效果进行监测和分析，及时调整广告策略，优化广告效果。

合法合规：广告需要遵守相关法律法规，确保不夸大产品效果或虚假宣传。

//highlight-end
```

## 宣传图片

让我们开始来做个宣传图片吧：

```text
我需要生成登山鞋的宣传图片。

这个图片宣传目的是作为我的登山鞋的广告图片。

在图片中突出登山鞋的耐用性，防水性和舒适性。
我希望这个图片是在登山的场景。

你帮我详细描述一下这个广告图片。

// highlight-start
好的，我可以帮你描述一下这个登山鞋的宣传图片。这张图片应该能够吸引登山爱好者的眼球，并突出登山鞋的耐用性、防水性和舒适性。

首先，这个场景应该是在山上或山脚下的登山道路上。可以选择一个有挑战性的山路，以展示登山鞋的性能。建议选择一个光线明亮的天气，以突出登山鞋的色彩和细节。

在图片中应该有一位穿着这款登山鞋的登山者。这个人应该是穿着全套登山装备，例如登山杖、头灯、登山帽等等，以突出整个登山者的专业性。

这款登山鞋应该占据图片的主要位置。可以在图片中用近景来突出登山鞋的细节。鞋面上的细节和织物纹理应该清晰可见。同时，要展示登山鞋的功能性，例如，可以拍摄鞋底的防滑设计，以及鞋面的防水材料。

最后，建议加入一些文字来描述这款登山鞋的特点，例如“耐用、防水、舒适”，可以加在图片的角落或边缘，以便于消费者了解产品信息。

总之，这个登山鞋的宣传图片应该是高清晰度的，场景真实自然的，突出登山鞋的特点，吸引登山者的目光，并促进产品的销售。

//highlight-end
```

:::note
- 这里我用了一个开箱即食的图片生成网站[Stable Diffusion Online](https://stablediffusionweb.com/#demo)，你可以将这一步生成得到描述文本复制到Stable Diffusion Playground并一键生成。
- 后续的课程会讲到如何写文生图的提示。
:::

```text

用英文描述这张图片

// highlight-start

Sure, I can help you describe this promotional image for your hiking shoes. The image should be set in a hiking environment and highlight the durability, waterproofing, and comfort of the shoes. A hiker wearing the shoes should be featured on a challenging trail or at the foot of a mountain, showcasing the shoe's performance. The image should also emphasize the details and functionality of the hiking shoe, such as the slip-resistant sole and waterproof material. Additionally, some text can be added to the corner or edge of the image to describe the product's features.

//highlight-end
```

最终我们成功生成了4张图片，

![shoes](./img/shoes.png)


## 广告文案

有了宣传图案，我们接下来尝试生成广告文案。

```text

根据上面的图片生成对应的广告文案，要求体现产品的轻量化、防滑、透气，文案在100字以内。

// highlight-start

登山路漫漫，伴你攀登山峰的，是脚底下的这双伴侣。我们的登山鞋轻量舒适，透气排汗，即使是陡峭的山路也能让你脚踏实地。专为登山者设计的防滑鞋底，确保你的每一步都牢牢落地。无论你走过多少座山峰，这双鞋将成为你最值得信赖的装备。

//highlight-end
```

如果你觉得它生成的方案不过简洁，也不够创意性，不妨尝试给它几个例子。

<div trydyno-embed="" openai-model="text-davinci-003" initial-prompt="Example #1: 想做就做。 不做下一个谁，做第一个我！\n\nExample #2: 征服自己，心就是最野的山。\n\nExample #3: 把最会玩的心，装进一件最懂你的身体。
\n\n按照上面广告文案的写作风格写一段登山鞋的广告文案,字数在20字内。" initial-response="" max-tokens="256" box-rows="18" model-temp="0。7" top-p="1.0">
    <noscript>Failed to load Dyno Embed: JavaScript must be enabled</noscript>
</div>

## 产品命名

除了宣传图片和广告文案，一个富有创意的产品名称将会脱颖而出，使你的产品更具吸引力，还可以增加销售额。

```text

帮我给我的登山鞋产品想10个创意性强的产品名，能让人联想到爬山和登山鞋的联系。

// highlight-start

1. 峰逐者（Peak Pursuer）
2. 登巅之心（Summit Soul）
3. 登高之步（Altitude Stride）
4. 瞬越山峰（Peak Leaper）
5. 山路领袖（Trail Leader）
6. 崖行者（Cliff Trekker）
7. 稳足攀登（Steadfast Ascent）
8. 山径漫步（Mountain Ramble）
9. 峰峦之王（Peak Monarch）
10.登峰造极（Ultimate Summit）

//highlight-end
```

到这里，我们的产品名，产品文案，宣传图片都已全部生成。
    
    """
    summarize="""

# 内容总结

ChatGPT 可以通过分析内容并生成一个浓缩版本来总结文本。这对节省时间和精力很有帮助，特别是在阅读长篇文章、研究论文或报告时。

## 通用总结

你所要做的就是把具体的文字复制并粘贴到提示中，并要求ChatGPT对所选文本进行简化总结。这里我们参考openai官网提供的例子**Summarize for a 2nd grader**来总结一下**木星**的维基百科

<div trydyno-embed="" openai-model="text-davinci-003" initial-prompt="Summarize this for a second-grade student:\n\n Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter.[19] When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows,[20] and is on average the third-brightest natural object in the night sky after the Moon and Venus." initial-response="Jupiter is the fifth planet from the Sun and is very big and bright. It can be seen with our eyes in the night sky and it has been known since ancient times. Its name comes from the Roman god Jupiter. It is usually the third brightest object in the night sky after the Moon and Venus." max-tokens="64" box-rows="18" model-temp="0.7" top-p="1.0">
    <noscript>Failed to load Dyno Embed: JavaScript must be enabled</noscript>
</div>

## 概念性总结

Ted Chiang曾经在纽约客上发表文章，称ChatGPT为**互联网的有损压缩**。那么我们同样可以通过提示来生成总结，并不需要粘贴额外的文字。

<div trydyno-embed="" openai-model="text-davinci-003" initial-prompt="Summarize for me what Jupiter is, like I'm 8 years old" initial-response="Jupiter is the biggest planet in our solar system. It's very far away, but we can see it in the night sky. It's big and bright and looks like a star. Jupiter is a gas giant and is made of mostly gas and liquids, just like Saturn. It has big, swirling storms and colorful stripes on it. It's very interesting and fun to look at." max-tokens="256" box-rows="18" model-temp="0.8" top-p="1.0">
    <noscript>Failed to load Dyno Embed: JavaScript must be enabled</noscript>
</div>

概念性总结对于我们一开始想要快速了解某个概念的简要总结来说非常有帮助。

## 大纲式总结

除了摘要这种形式外，你还可以要求 ChatGPT 为长文本写提纲。这样你可以一次性看到整篇文章的主线或框架。

以下是ChatGPT对维基百科上 [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT#cite_note-guardianpos-4) 页面上的提纲。

这里我使用了角色扮演类的提示，让 ChatGPT 扮演一个文档大纲生成器，并且定义了两个关键词组。当我还没输入“生成大纲”时，ChatGPT 会在读取完成后输出“读取完毕”，而不是直接生成大纲。

![outline](./img/outline.png)

![read](./img/read_complate.png)

最终生成的大纲如下：

```text
//highlight-start

Sure, based on the text you provided, here is the outline:

I. Introduction

- Overview of ChatGPT
- Built on GPT-3.5 and GPT-4 models
- Fine-tuned using supervised and reinforcement learning techniques

II. Fine-tuning Process

- Reinforcement learning from human feedback (RLHF)
- Supervised learning and human trainers
- Proximal Policy Optimization (PPO)

III. Infrastructure and Data Collection

- Microsoft Azure supercomputing infrastructure
- User data collection and feedback

IV. Features

- Versatility in various domains
- Ability to remember previous prompts in a conversation
- Attempts to reduce harmful and deceitful responses
- Filtering of potentially offensive queries
- Plugin support for ChatGPT

V. Conclusion

- Speculations on potential uses of ChatGPT
- Continued improvements and upgrades by OpenAI

//highlight-end
```

## 维基百科式总结

除了大纲和概要之外，还有一种适合我们日常阅读习惯的格式，那就是维基百科。这里我同样是使用角色扮演，生成 **AI**（Artificial intelligence）的总结。

>I want you to act as a Wikipedia page. I will give you the name of a topic, and you will provide a summary of that topic in the format of a Wikipedia page. Your summary should be informative and factual, covering the most important aspects of the topic. Start your summary with an introductory paragraph that gives an overview of the topic. My first topic is "Artificial intelligence"

下面是部份的生成结果。

```text
//highlight-start

Artificial Intelligence (AI) refers to the development of computer systems that can perform tasks that would typically require human intelligence, such as learning, problem-solving, decision making, and natural language processing. AI involves the creation of algorithms and computer programs that can process large amounts of data and make predictions or decisions based on that data.

The history of AI dates back to the 1950s, when researchers began developing computer programs that could play chess and solve mathematical problems. Over the years, AI has advanced significantly, and today, it is used in a wide range of industries, including healthcare, finance, and transportation.

...
//highlight-end
```
就个人而言，我会更喜欢维基百科这种长度适中的总结形式。了解不同形式的总结能帮助我们更快更好的阅读长文本和了解概念。

## PDF&DOC文档总结

这里我推荐的是[ChatPDF](https://www.chatpdf.com/)和[ChatDoc](https://chatdoc.com/)。

它们可以在文件上传后回答关于文件内容的问题。根据你的问题，它们可以在文件中找到相关段落，并用自然语言回复你的问题。同时，它们还会提供相应的页码或章节信息，以便你能轻松查看原文。

更多好用的工具请关注我们**工具推荐**章节。
    
    """
    study_tool="""
    
    # 学习助理

ChatGPT 作为学习助理的强大是在于对个人需求的定制化回复。

1. **建立知识网络** 建立新知识和已有知识的链接。在知识之间建立链接不仅可以产生新的灵感而且还会在大脑的信息之间建立新的连接，让我们提取知识更加的可靠、高效。通过查看更多的例子可以帮助我们理解知识，例如在学习新概念时，可以向 ChatGPT 获取例子来帮助理解。

2. **实时反馈** ChatGPT 可以根据你的学习情况进行监测和分析，并及时给出学习反馈和建议。你可以借助 ChatGPT 来了解自己的学习进度和水平，甚至可以要求 ChatGPT 提供试题来验证自己的掌握程度，也可以在学习概念知识时也可以通过用自己的话解释概念，并向 ChatGPT 索取反馈验证自己的描述是否有误。

3. **学习计划** ChatGPT 还可以为你提供时间管理和学习计划的建议。

这里我尝试用ChatGPT来学习**ChatGPT内在的技术原理**。（套娃🪆）

## 解释术语

从维基百科中我们可以看到 ChatGPT 的定义

**ChatGPT is a member of the generative pre-trained transformer (GPT) family of language models.**

这一句解释可能对初学者不够友好。ChatGPT 是能够以一种更易于理解的方式分解复杂的概念，从而加快你的学习速度。在这里我们首先想了解到的就是：

- 什么是语言模型（language models）？
- ChatGPT 和语言模型有什么关系？

```text

你现在是一个AI专家，语言学家和教师，你目标是让我理解语言模型的概念，理解ChatGPT跟语言模型之间的关系。你的工作是以一种易于理解的方式解释这些概念。这可能包括提供例子，提出问题或将复杂的想法分解成更容易理解的小块。现在我第一个问题是“什么是语言模型？”

// highlight-start

语言模型是一种计算机程序，其目标是对给定的一段自然语言文本进行建模。在计算机科学中，我们给定一个预定义的语言，然后建立一个模型来预测给定的句子是否符合该语言，并给出这个句子的合理性打分。

例如：如果我们要建立英语语言模型，我们需要先收集一些英文文本，并使用这些文本来训练模型。这个模型将学习英语的语法规则、单词之间的关联以及其他语言特征，例如在英语里单词的顺序在很大程度上决定了句子的意义。

接下来，我们需要给这个模型一个句子，让它预测这个句子是否是一个正确的英语句子，以及该句子的合理性得分是多少。经过训练的语言模型可以用于自然语言处理任务，例如文本生成、自动问答和机器翻译等。 

ChatGPT就是一种基于语言模型的人工智能算法，它可以用于生成自然语言文本，如对话、新闻、小说等。它使用类似于上述的方法进行建模和训练，可以预测和生成给定主题和上下文的合法、自然语言句子。

//highlight-end
```

通过 ChatGPT，我们得到了新的知识，这时候我们便可以让 ChatGPT 以生活常见的例子为例，结合新的知识建立我们的知识网络。

```text

用生活常见例子讲解“语言模型“和”ChatGPT“之间的联系，以及”ChatGPT“的独特之处

// highlight-start

好的，我们可以想象一下你在和你的朋友聊天时，你会最终产生一些自然的对话内容。这些内容通常是基于对言语和语义规则的归纳和总结得出的，换句话说，它们是基于你的自然语言模型。你已经获得了很多经验，已经学会了如何用语言表达自己的想法，并且预测对话的正确性和连贯性。

现在，我们可以将这种自然语言模型扩展到计算机上，让它自动生成人类语言。ChatGPT就是这样的一个模型。ChatGPT是基于深度学习技术的模型，它可以学习许多不同的语言模式，在输出文本时，它可以使用这些模式来自动产生新的合法、自然的文本内容。

独特之处在于，ChatGPT是一种基于接收输入文本和自动生成下一段文本的迭代算法。这使得ChatGPT可以在不断接受和生成文本的过程中不断改进自己的语言模型。例如，我们可以使用ChatGPT来训练一些基于聊天数据的应用程序，使得它们可以根据用户输入产生自然的响应。这种应用程序可以被用于虚拟助手、智能客服、在线客户支持等领域。

//highlight-end
```

## 实时反馈

我打算将 ChatGPT 打造成一个虚拟教师，它可以出一些填空题，通过我的回答来给出我对当前知识点的掌握程度分数。

:::note
角色扮演类提示语并不仅仅适用于对话的开头，你在每一轮对话中都可以使用。但是需要注意的是，对话历史会对后续输出产生影响。
:::

```text

我希望你作为教师，能够对我理解之后的输出评分。

1-10分代表了掌握的程度。分数越高越好。

你会根据掌握的程度的好坏给我出填空题目。

当我根据你的题目回复之后，你需要对我的掌握程度重新打分。

// highlight-start

好的，让我们来试试这个方式。首先，这是第一个填空题：语言模型是一种计算机程序，其目标是对给定的一段 ____________ 文本进行建模。

请在下划线处填上适当的单词。

分值： 8/10

//highlight-end

自然语言

// highlight-start

正确！你的理解程度很高。下面是下一个填空题：

ChatGPT是基于深度学习技术的 ____________算法，它可以在输出文本时自动产生新的合法、自然的文本内容。

请在下划线处填上适当的单词。

分值： 9/10

//highlight-end
```

更有趣的是，你可以让ChatGPT根据你的知识掌握程度自动调整题目的难度，同时你也不必局限于填空题。发挥你的想象力，ChatGPT将成为你贴心的学习助手。

## 学习计划

掌握到学习技巧后，如何制定高效、可操作和可量化的学习计划呢？ChatGPT 可以帮助我们解决这个问题。我们的学习目标是学会**使用prompt**，现在就让我们看看ChatGPT会给我们带来什么惊喜吧！。

```text

你是一个人工智能专家和学习规划管理专家，现在需要你根据我学习的目标【学会prompt编写】为我制定一个详细的学习计划，必须包含以下要点：

1.要有详细的周计划，且必须包含具体的学习行动；

2.要以表格形式呈现；

3.必须具有专业性指导意见，与学习目标强相关性且可实践，此句不要直接引用。

// highlight-start

好的，为了帮助你学会prompt编写，我建议你按照以下学习计划进行学习：

| 学习时间 | 学习行动 |
| -------- | -------- |
| 第一周   | 学习自然语言生成、Seq2Seq模型、RNN模型的基础知识；同时了解GPT的结构和工作原理 |
| 第二周   | 学习GPT-2和GPT-3等预训练模型，并了解如何使用它们生成文本 |
| 第三周   | 学习Prompt编写的理论知识，包括Prompt的结构、要素、写作规范等；同时，开始编写简单的Prompt，并使用GPT模型进行训练 |
| 第四周   | 进一步学习Prompt编写的高级技巧，例如如何识别模型训练中的偏见和错误，如何调参优化模型性能等。同时，开始编写更加复杂的Prompt，并对模型性能进行评估。|
| 第五周   | 继续练习Prompt编写并进行优化。此外，还可以探索其他自然语言生成技术，例如条件变分自动编码器（Conditional Variational Autoencoder，CVAE）等，并将其与Prompt编写技术结合起来。 |
| 第六周   | 回顾所学知识和技能，并准备编写更加复杂和高效的Prompt。同时，开始应用所学技能到实际场景中，例如编写自动问答系统、虚拟客服等应用。 |

上述计划是一个基础性的学习计划，你可以根据自己的学习情况进行调整和修改，同时在整个学习过程中，我建议你保持每周10小时以上的学习时间。另外，还可以尝试参与实践性项目、阅读相关文献以及结合开源工具和平台开展模型训练等。希望以上学习计划能够对你有所帮助。

//highlight-end
```

ChatGPT生成了markdown格式的回复。用 ChatGPT 定制学习计划需要留意两个点：

- 基础内容要求详细：想要达到定制化学习的效果，需要给 ChatGPT 提供详细的基础内容，例如对这个知识点是否有一定的基础，难点和重点等。
- 需要不断调整：在学习过程中会不断遇到新的问题，好的学习计划需要不断地调整。当你觉得原计划中存在问题时，及时对计划进行调整，以适应新的情况。
    """
    english="""
    # 学习各国语言

过去，我们学语言需要花费很多时间来学习各种材料，再联系老师修改口语、作文等，十分费时费力。有了 ChatGPT 之后，我们就相当于有一个免费的，实时反馈的语言学习助手，大大节省了我们的时间。下面我将以英文的雅思学习为例子，结合口语和写作，介绍如何利用 ChatGPT 来学习语言。

## 口语

### 插件安装

正式开始之前，我们要先完成插件的安装。通过谷歌插件[Voice Control for ChatGP](https://chrome.google.com/webstore/detail/voice-control-for-chatgpt/eollffkcakegifhacjnlnegohfdlidhn)，ChatGPT 的输入和输出都能变换为语音形式。

重新刷新进入ChatGPT，我们可以看到界面下方出现了语言输入按键，点击即可进行语言输入。ChatGPT 回复的内容将会朗诵出来，这样一来我们可以练习口语了。

![en](./img/input.png)

:::note
语音输入键的右边可以选择语言，所以理论上可以实现任何语言的口语对练。
:::

### 口语练习

首先我们利用角色扮演提示让 ChatGPT 模仿雅思面试官。

```text
I want you to act as an IELTS Speaking Test interviewer and talk to me like an IELTS speaking test interview.

Ask one question at a time

// highlight-start

Sure, I can do that! Let's begin.

First, could you please introduce yourself? What is your name, where are you from, and what do you do?

// highlight-end

Sure, my name is Emily and I am from the United States. Currently, I work as a graphic designer for a digital marketing agency. I have always had a passion for creativity and design, which led me to pursue a degree in graphic design. In my free time, I enjoy exploring new art exhibits and experimenting with different art techniques. I am also an avid traveler and enjoy immersing myself in new cultures and experiences. I am excited to take the IELTS exam and showcase my English language skills.

```

当回答完这个熟悉的问题之后，我们就可以开始口语练习了。

```text
// highlight-start

Great, Emily! It's nice to meet you. Let's move on to the first part of the IELTS Speaking Test.Here is the first question:

1. Let's start by talking about your current job. What are your main responsibilities as a graphic designer at your digital marketing agency?

// highlight-end

Certainly. As a graphic designer at my digital marketing agency, my main responsibilities include creating visual concepts and designs for a wide range of digital media platforms including websites, social media platforms, and email marketing campaigns. I use various design software to develop and execute creative ideas that meet the clients' needs and effectively communicate their message to the target audience. 

// highlight-start

That sounds like a challenging and rewarding role. Let's move on to the next question:

2. How did you become interested in graphic design, and what inspired you to pursue it as a career?

// highlight-end

Sure. When I was in high school, I was introduced to the world of digital design, and I knew that this was the path I wanted to take. I enrolled in a graphic design program at university, where I learned the fundamentals of design, typography, color theory, and composition. I was particularly drawn to the challenge of creating designs that were both visually pleasing and functional, and that could effectively communicate a message to the audience.

```

在整个流程中，ChatGPT会像雅思口语考官一样一个接一个地询问问题，每当你回答后，它还会简短地回应一下。当 Part1 结束时，它会询问你是否已准备好进入Part2。

![part2](./img/part2.png)

完成口语部份的考试之后，你还可以让 ChatGPT 给你点评不足之处。

![score](./img/score.png)


### 口语示例

如果你的基础比较薄弱，雅思口语的时候没有思路，你还可以让 ChatGPT 直接生成对应的口语示例。

```text

Answer IELTS Speaking Part2: Describe a period in history that you want to know

// highlight-start

Sure, I'd be happy to help you with that. Here's a sample answer for the IELTS Speaking Part 2 prompt, "Describe a period in history that you want to know":

I'm quite interested in history, and there are many periods that fascinate me. However, one that I'm particularly intrigued by is the Ancient Egyptian era, which spanned from around 3100 BC to 30 BC.

Egyptian civilization is one of the oldest and most enduring in the world, and it has left behind a rich legacy of art, architecture, and mythology that continues to capture people's imaginations to this day. I would love to learn more about the daily lives of ordinary Egyptians, as well as the pharaohs and other rulers who held power during that time.

One aspect of Ancient Egypt that I find particularly fascinating is their belief in an afterlife and the elaborate preparations they made for it, including building pyramids and tombs and creating intricate burial rituals. I would also be interested in learning more about the hieroglyphic writing system they used to record their history and religious beliefs.

Of course, there are many mysteries and unanswered questions about Ancient Egypt that continue to intrigue scholars and historians, such as how the pyramids were built and what caused the downfall of the civilization. Exploring these mysteries and learning more about this fascinating period in human history would be an incredible adventure, and I hope to have the opportunity to do so someday.

// highlight-end
```

依照雅思口语的评估标准，我会给这个回答6.5-7分的得分。总体来看，ChatGPT生成的答案结构有序、逻辑性强，对问题做出了明确的回应，并且运用了多样的句子结构。

## 写作

### 写作示例

这里我们可以让ChatGPT根据你的目标分数，直接生成对应的写作示例。

```text
Please write a band 8 IELTS. Task 2 essay for this question:

Some people think the government should pay for health care and education, but others believe it is not the government's responsibility. Discuss both views and give your opinion.

// highlight-start

In recent years, the issue of whether the government should fund health care and education has become a topic of intense debate. While some individuals believe that the government has a duty to finance these essential services, others argue that it is not the government's responsibility. In this essay, we will explore both perspectives and provide our opinion.

On the one hand, some individuals believe that the government should fund health care and education because these services are fundamental rights that every citizen deserves. For example, health care is essential for maintaining good health, and it should be provided to all citizens regardless of their income. Education is also a right that every individual should have access to, regardless of their financial background, as it allows individuals to achieve their full potential and contribute to society. Therefore, the government should play a significant role in financing these services to ensure that everyone has access to them.

On the other hand, there are those who argue that the government should not be responsible for funding health care and education, as this should be left to individuals and private institutions. According to this perspective, the government's primary role is to maintain law and order and provide essential services such as security and infrastructure. It is the responsibility of individuals to pay for their health care and education, either through private insurance or personal savings. In this way, the burden of funding these services is shifted away from the government and onto individuals.

In my opinion, while individuals have a role to play in financing their health care and education, the government should also play a significant role in funding these services. Health care and education are fundamental rights that every individual deserves, and it is the government's responsibility to ensure that these rights are upheld. The government should provide essential services such as health care and education to ensure that all citizens have access to them, regardless of their financial background. However, this funding should be done in a way that is sustainable and equitable, so that the burden is not placed solely on taxpayers.

In conclusion, the issue of whether the government should fund health care and education is a complex one. While some argue that the government should not be responsible for financing these services, I believe that the government has a duty to ensure that all citizens have access to essential services such as health care and education. It is only through government funding that we can ensure that these services are accessible to all individuals, regardless of their financial background.

// highlight-end
```

我们来简单分析一下 ChatGPT 写的这篇作文: 

- 从文章结构上看，文章扣题严谨，展开充分。先是指出政府应该资助医疗保健和教育，因为这些服务是每个公民应得的基本权利。紧接着反驳第一段的观点，强调了医疗保健和教育服务应该留给个人和私人机构。然后表述自己的观点：**In my opinion, while individuals have a role to play in financing their health care and education, the government should also play a significant role in funding these services.**

- 从词汇上看，整篇文章符合初学者的水平，没有使用生涩难懂的词汇，反而能帮助我们学习词汇在文章中的用法，例如“intense debate”、“regardless”和“play a significant role”。

- 从理解记忆上看，ChatGPT 生成的文章结构较为固定和公式化，这有助于雅思考生拆解、模仿和快速上手。在雅思这种标准化、学术化考试中，使用这种结构更符合要求。当然，写作水平高的作者可以运用设问、倒叙、插叙甚至意识流等组织手段，但这些手法并不完全适用于雅思考试的要求。

### 写作批改 

在学习过程中，我们可以将自己的写作交由 ChatGPT 来批改。ChatGPT 能够根据官方四个维度的评分标准给出更多建议，同时生成修改后的作文，让我们通过具体的内容和批改意见来快速定位自身的不足之处。

```text

I would like you to act as an English teacher for IELTS writing corrections and give me feedback on my writing samples, including suggestions for improvement and correction of any errors.

The IELTS writing is marked on four dimensions:
1. Task Response
2. Coherence and cohesion
3. lexical resource
4. grammatical range and accuracy

My essay was as follows:
###
More and more young people choose to stop studying in schools and cannot be employed after graduation in many countries. Youth unemployment might be terrible for self-development of individuals and steady social development.

For young people, unemployment is a realistic problem they face. No jobs means no income and cannot provide a single person with basic living materials and good which they want to improve themselves. Also, without being employed, youths have a lot of spare time when they have nothing to do and this might cause some social issues. For instance, there will be many factories and companies who need employees to do the work cannot produce enough goods which the society asks for. As a result, the economy might slow down or even decline. Simultaneously, young people who have no salaries but
plenty of time might be a trigger of increasing social criminals

In order to deal with youth unemployment, the government can carry out policies to encourage some young people who want to develop themselves to go back to schools for further education and help some of them who want to work learn some practical skills. Moreover, young people themselves should think about their future employment before they leave schools through some career development courses which can be provided by schools.

In conclusion, youth unemployment might be a big issue for development of the individuals and the society. To solve this problem, the governmental policies and individual career development courses can help.
###

Please suggest improvements and correct errors in accordance with the four dimensions of the marking scheme.

// highlight-start

Sure, I'd be happy to help you with your essay! Here's my feedback based on the four dimensions of the IELTS writing marking scheme:

Task Response:
Your essay addresses the prompt of youth unemployment, its impact on individuals and society, and suggests solutions to the problem. However, there are some areas where you can further develop your ideas to make your response more comprehensive and persuasive.

Coherence and Cohesion:
Your essay is organized into three paragraphs, which is a good start. However, there are some issues with coherence and cohesion. For example, in the second paragraph, you discuss the impact of youth unemployment on society, but then you shift to discussing the impact on individuals. It would be better to separate these points into two different paragraphs to create a more organized and coherent essay. Additionally, there are some awkward sentences that could be rephrased for better clarity.

Lexical Resource:
Your essay uses a range of vocabulary, but there are some errors in word choice and usage. For instance, in the first paragraph, you use the word "good" instead of "goods", and in the second paragraph, you use "trigger of increasing social criminals" instead of "cause an increase in crime rates." Try to pay closer attention to your word choice to ensure accuracy and clarity.

Grammatical Range and Accuracy:
There are some grammatical errors in your essay, such as missing articles, subject-verb agreement errors, and awkward phrasing. For example, in the first sentence, "cannot be employed after graduation in many countries" should be "cannot find employment after graduation in many countries." It would be helpful to proofread your work carefully to catch these errors and improve the overall accuracy of your writing.

Here is a revised version of your essay with suggested improvements:

More and more young people are choosing to stop studying in schools and are unable to find employment after graduation in many countries. Youth unemployment can have a significant impact on both individual self-development and overall social development.

Unemployment poses a realistic problem for young people, as it means no income and an inability to provide for basic living necessities, let alone the resources necessary for self-improvement. Furthermore, a lack of employment means that many companies and factories may not be able to produce enough goods to meet society's demands, which could lead to a decline in the economy. Additionally, idle young people with plenty of spare time may be more likely to turn to crime, which can have a negative impact on society.

To address youth unemployment, the government can implement policies to encourage young people to pursue further education or learn practical skills that will improve their employability. In addition, schools can provide career development courses that help students make informed decisions about their future employment prospects.

In conclusion, youth unemployment is a significant issue that requires both government intervention and individual action. By investing in education and skills training, young people can improve their chances of finding meaningful employment and contribute to the development of their communities.

// highlight-end
```
    
    """
    coding="""
    # 代码助理

你可以使用 ChatGPT 进行代码生成、生成测试用例、注释、审查和漏洞检测。

## 代码生成

我们可以让 ChatGPT 自动生成一个排序算法中的快速排序的Python代码。

<div 
trydyno-embed="" 
openai-model="text-davinci-003" 
initial-prompt="I want you to work as a junior python programmer. Please write a python code for a quick sort algorithm." 
initial-response="" 
max-tokens="512" 
box-rows="5" 
model-temp="0.7" 
top-p="1.0">
    <noscript>Failed to load Dyno Embed: JavaScript must be enabled</noscript>
</div>

简单的代码生成对于 ChatGPT 来说小事一桩。

## 测试用例

用例来源出自[StuGRua](https://juejin.cn/post/7211716002382528573)

在待测函数函数定义清晰的情况下，单元测试可以通过 ChatGPT 来生成。

```text

写下列代码中CompressPicture函数的单测，要求覆盖全部逻辑。
断言使用require包。
测试用例以testCases的形式输出。

// CompressPicture the picture by resizing it to the specified width.
func CompressPicture(picData []byte, width uint) ([]byte, error) {
   // Decode the input image.
   oldBuffer := bytes.NewBuffer(picData)
   inputImg, _, err := image.Decode(oldBuffer)
   if err != nil {
      return nil, err
   }
   // Resize the image to the specified width.
   outputImg := resize.Resize(width, 0, inputImg, resize.Lanczos3)
   // Encode the output image as PNG and write it to a buffer.
   newBuffer := new(bytes.Buffer)
   err = png.Encode(newBuffer, outputImg)
   if err != nil {
      return nil, err
   }
   // Return the compressed image as a byte slice.
   return newBuffer.Bytes(), nil
}

// highlight-start

# ChatGPT生成代码块如下：

func TestCompressPicture(t *testing.T) {
   // Setup test data
   imgData, err := os.ReadFile("test-image.png")
   if err != nil {
      t.Fatalf("failed to read test image file: %v", err)
   }
   testCases := []struct {
      name  string
      width uint
   }{
      {"compress with a valid width", 500},
      {"compress with an invalid width", 0},
   }
   for _, tc := range testCases {
      t.Run(tc.name, func(t *testing.T) {
         // Invoke the function being tested.
         compressedData, err := CompressPicture(imgData, tc.width)

         // Check the result.
         if err != nil {
            t.Fatalf("unexpected error: %v", err)
         }
         if len(compressedData) == 0 {
            t.Fatalf("compressed data is empty")
         }
         create, err := os.Create("test-image-compressed.png")
         if err != nil {
            return
         }
         defer create.Close()
         _, err = create.Write(compressedData)
      })

   }
}

// highlight-end
```

ChatGP T单次对话有长度限制，所以一次尽量只进行一个函数的单元测试生成。

## 代码注释 & 格式优化

ChatGPT 可以通过阅读代码，理解函数的输入、输出、功能以及用途，然后生成相应的 API 文档和注释。

```text
Please add line comments to this Python code and reformat it to make it easier to read:

import openai
openai.api_key = "YOUR_API_KEY"

def generate_response(prompt):
    response = openai.Completion.create(engine="davinci",prompt=prompt,temperature=0.5,max_tokens=1024,n=1,stop=None)
    return response.choices[0].text.strip()

while True:
    prompt = input("请输入你的问题：")
    response = generate_response(prompt)
    print("答案：", response)
```

ChatGPT给每一句话都加上了解释，并且将过长的语句转化成更加易读的格式。

```python
import openai  # Import the openai module

# Set the API key for the openai module
openai.api_key = "YOUR_API_KEY"  # Replace with your actual OpenAI API key

# Define a function for generating a response from OpenAI's language model given a prompt
def generate_response(prompt):
    # Create an OpenAI completion with the specified parameters
    response = openai.Completion.create(
        engine="davinci",  # Use the 'davinci' language model
        prompt=prompt,  # Use the provided prompt
        temperature=0.5,  # Use a temperature of 0.5, which means the model will generate diverse responses
        max_tokens=1024,  # Generate up to 1024 tokens of output
        n=1,  # Generate a single response
        stop=None  # Do not use a stop sequence to end the generated text
    )
    # Extract the generated text from the response and return it
    return response.choices[0].text.strip()

# Continuously prompt the user for questions and generate responses using the generate_response function
while True:
    prompt = input("Please enter your question: ")  # Prompt the user for a question
    response = generate_response(prompt)  # Generate a response to the question using the generate_response function
    print("Answer:", response)  # Print the generated response
```

## 代码调试

通过之前的几个步骤，你已经了解了如何编写正确且具有测试用例的代码。

在日常开发中，除了编写代码之外，我们还会遇到两个比较棘手的开发步骤。一个是解决运行现有的代码后出现的错误；另一个是如何在当前编程语言中复现其他编程语言已经支持的处理逻辑呢？

我们先解决第一个问题。一般来说，写完代码后运行，如果代码中有错误，解释器会提示错误信息，按照提示信息，通常可以很快找出错误并进行修改。但有时候错误提示信息不是那么明确，当你检查了几遍仍然无法找出问题，就会比较困扰。ChatGPT 可以结合已有的错误信息，帮助我们分析代码中潜在的问题。

这里我选择了一个stack overflow上**python跟SQL数据库连接错误**的例子：[Error while trying to connect to sql server with python using pyodbc](https://stackoverflow.com/questions/64209295/error-while-trying-to-connect-to-sql-server-with-python-using-pyodbc)

ChatGPT扮演成了一个python专家：

```text
You are a python expert who can pinpoint errors in your code through error messages and provide easy-to-understand solutions.

error```
Traceback (most recent call last):
File "[test.py](http://test.py/)", line 7, in <module>
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL
Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
pyodbc.InterfaceError: ('28000', "[28000] [Microsoft][ODBC Driver 17 for SQL Server][SQL
Server]Login failed for user 'SA'. (18456) (SQLDriverConnect); [28000] [Microsoft][ODBC
Driver 17 for SQL Server][SQL Server]Login failed for user 'SA'. (18456)")

code```

import pyodbc

server = 'SERVER'

database = 'DBNAME'

username = 'SA'

password = 'SQLPWD'

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

Please analyse "code" for possible causes, solutions and the correct code depending on the "error”.  

// highlight-start

The error message indicates that the login for the SQL Server failed for the user 'SA'. There could be several reasons for this error, but one possible reason is that the provided password is incorrect or the 'SA' account is disabled. Here are some steps to troubleshoot and fix the error:

Verify the username and password: Double-check that the provided username and password are correct. You can try logging in to the SQL Server using these credentials to ensure that they are valid.

Check if the 'SA' account is disabled: If the 'SA' account is disabled, you will not be able to log in to the SQL Server using this account. You can check the account status in SQL Server Management Studio or by running a query on the server:

// highlight-end
```

```python
SELECT name, is_disabled
FROM sys.sql_logins
WHERE name = 'SA'
```

```text
// highlight-start
If the 'is_disabled' column value is 1, then the account is disabled. To enable the account, you can run the following query:
// highlight-end
```

```python
ALTER LOGIN SA WITH PASSWORD = '<new_password>', CHECK_POLICY = OFF, CHECK_EXPIRATION = OFF;
```

```text
// highlight-start

Note that it's not recommended to use the 'SA' account for regular database operations as it has elevated privileges.

Check the SQL Server authentication mode: If the SQL Server authentication mode is set to 'Windows Authentication mode only', you will not be able to log in using SQL Server authentication. You can check the authentication mode in SQL Server Management Studio by right-clicking on the server instance, selecting Properties, and navigating to the Security tab.

// highlight-end
```

ChatGPT 给出的解决方法是：

- 验证用户名和密码
- 检查 "SA "账户是否被禁用
- 检查SQL Server的认证模式

而网页中最受欢迎的回复是：

- SA被禁止访问
- 服务器认证选择错误
- SQL服务器没有开放远程访问

通过比较，我们很容易得到ChatGPT在代码调试方面的可行性。

## 代码互翻

ChatGPT 提供的另一个非常有用的功能是能够将程序从一种语言移植到另一种语言。

这里我在 Leetcode 找了一道常见算法题[**最长回文子串**](https://leetcode.cn/problems/longest-palindromic-substring/)的 C++ 实现，转化成 Python 语言。

:::note
最长回文子串题目：

给你一个字符串 s，找到 s 中最长的回文子串。
如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
:::

```text
You are an expert program developer with extensive experience in writing C++ and Python. Please convert this C++ program to Python:

code```
class Solution {
public:
    string longestPalindrome(string s) {
        int len=s.size();
        if(len==0||len==1)
            return s;
        int start=0;
        int max=1;
        vector<vector<int>>  dp(len,vector<int>(len));
        for(int i=0;i<len;i++)
        {
            dp[i][i]=1;
            if(i<len-1&&s[i]==s[i+1])
            {
                dp[i][i+1]=1;
                max=2;
                start=i;
            }
        }
        for(int l=3;l<=len;l++)
        {
            for(int i=0;i+l-1<len;i++)
            {
                int j=l+i-1;
                if(s[i]==s[j]&&dp[i+1][j-1]==1)
                {
                    dp[i][j]=1;
                    start=i;
                    max=l;
                }
            }
        }
        return s.substr(start,max);
    }
};
```

ChatGPT输出的代码部份如下：

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0 or n == 1:
            return s
        start = 0
        max_len = 1
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
            if i < n - 1 and s[i] == s[i+1]:
                dp[i][i+1] = 1
                start = i
                max_len = 2
        for l in range(3, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                if s[i] == s[j] and dp[i+1][j-1] == 1:
                    dp[i][j] = 1
                    start = i
                    max_len = l
        return s[start:start+max_len]
```

代码顺利通过测试：

![code](./img/code_res.png)

##  IDE 推荐

这里我推荐的是[Cursor.so](https://www.cursor.so/)，它本身是一个集成了 GPT-4, 国内直接可以访问的，优秀而强大的免费代码生成器，可以帮助你快速编写、编辑和讨论代码。它支持多种编程语言，如 Python, Java, C#, JavaScript 等，并且可以根据你的输入和需求自动生成代码片段。
    
    """
