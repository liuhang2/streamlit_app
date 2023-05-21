import streamlit as st
import streamlit.components.v1 as components
import requests,json,re
from bs4 import BeautifulSoup
# import gpt4free
# from gpt4free import Provider,usesless
from content_st import neirong
from content1_st import neirong2
class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        app = st.sidebar.radio(
            '🌍导航页',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()
def page0():
    st.sidebar.write('___________________________')
    option=st.sidebar.radio("👇内容章节",['背景介绍','基础用法','提供示例','角色扮演','"标准"提示','经验法则'])
    if option=='背景介绍':
        st.markdown(neirong().intro)
    elif option=='基础用法':
        st.markdown(neirong().prompting)
    elif option=='提供示例':
        st.markdown(neirong().instructions)
    elif option=='角色扮演':
        st.markdown(neirong().roles)
    elif option=='"标准"提示':
        st.markdown(neirong().standard_prompt)
    elif option=='经验法则':
        st.markdown(neirong().more_on_prompting)
    
def page4():
    st.sidebar.write('___________________________')
    option=st.sidebar.radio("👇内容章节",['简单介绍','写作&博客','广告文案','内容总结','学习助理','学习各国语言','代码助理'])
    if option=='简单介绍':
        st.markdown(neirong2().introduction)
    elif option=='写作&博客':
        st.markdown(neirong2().writing)
    elif option=='广告文案':
        st.markdown(neirong2().ads)
    elif option=='内容总结':
        st.markdown(neirong2().summarize)
    elif option=='学习助理':
        st.markdown(neirong2().study_tool)
    elif option=='学习各国语言':
        st.markdown(neirong2().english)
    elif option=='代码助理':
        st.markdown(neirong2().coding)
def page1():
    st.sidebar.write('___________________________')
    st.sidebar.markdown("""Chatgpt本质上大语言模型，这种大语言模型有很多，以下这些是比较好用的，
    大多数属于无脑操作，简单容易上手""")

    xuze=st.sidebar.radio('',['Zi Chat','Bc Chat','Claued','Forefront','ChartExcel','P Chat'],horizontal=True)
    if xuze =='Zi Chat':
        st.markdown("""_此产品如果回复为英文时，记得加上**中文**提示词_
    """)
        ct=st.container()
        prompt=ct.text_input('请输入问题，按回车')
        res_ans=None
        if prompt!='':
            response = gpt4free.Completion.create(Provider.You, prompt=prompt)
            res_ans=response.encode().decode('unicode_escape')
        #files=st.file_uploader('数据文件📈')
        if res_ans  is None:
            ct.text_area('回答🛠️','',height=600)
        else:
            ct.caption('回答🛠️')
            ct.markdown(res_ans)
    if xuze=='Bc Chat':
        lin_1="""
          <style type="text/css">
        .css{
            width: 100%;
            height: 100vh;  /* 视口的100%高度 */
            border: 0;   /* 把他自带的边框去掉，不然会有违和感 */
        }
        </style>
        <iframe src="https://chatbot.theb.ai/" class="css" ></iframe>
        """
        st.markdown(lin_1,unsafe_allow_html=True)
#         res=requests.get('https://chatbot.theb.ai/')
#         soup=BeautifulSoup(res.content,'html.parser')
#         st.markdown(soup,unsafe_allow_html=True)
        #components.iframe("https://chatbot.theb.ai/")
    if xuze=='You Chat':
        lin_1="""
          <style type="text/css">
        .css{
            width: 100%;
            height: 100vh;  /* 视口的100%高度 */
            border: 0;   /* 把他自带的边框去掉，不然会有违和感 */
        }
        </style>
        <iframe src="https://you.com/" class="css" ></iframe>
        """
        st.markdown(lin_1,unsafe_allow_html=True)
    if xuze=='Claued':
        lin_1="""
          <style type="text/css">
        .css{
            width: 100%;
            height: 100vh;  /* 视口的100%高度 */
            border: 0;   /* 把他自带的边框去掉，不然会有违和感 */
        }
        </style>
        <iframe src="https://chat-gpt-next-web-cc8c-liuhang2.vercel.app//#/chat" class="css" ></iframe>
        """
        st.markdown(lin_1,unsafe_allow_html=True)
    if xuze=='Forefront':
        st.write('BAI Chat，由 Little B 使用 OpenAI 的 GPT-3.5 构建的人工智能聊天机器人,即开即用')
    if xuze=='ChartExcel':
        lin_1="""
          <style type="text/css">
        .css{
            width: 100%;
            height: 100vh;  /* 视口的100%高度 */
            border: 0;   /* 把他自带的边框去掉，不然会有违和感 */
        }
    </style>
    <iframe src="https://chatexcel.com/convert" class="css" ></iframe>
        """
        st.markdown(lin_1,unsafe_allow_html=True)
    if xuze=='P Chat':
        #components.iframe("https://www.hayo.com/login",height=800)
        lin_1="""
          <style type="text/css">
        .css{
            width: 100%;
            height: 100vh;  /* 视口的100%高度 */
            border: 0;   /* 把他自带的边框去掉，不然会有违和感 */
        }
    </style>
    <iframe src="https://rw8n6lc6.cn/" class="css"></iframe>
        """
        st.markdown(lin_1,unsafe_allow_html=True)
        
        
    
#     if prompt!='':
#         apiKey = "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"
#         url = "https://api.openai.com/v1/engines/text-davinci-003/completions"
#         headers={"Content-Type":"application/json",
#                   "Authorization":"Bearer " + apiKey}
#         data={'prompt':prompt,'max_tokens':1024,'temperature':0.1}
#         res=requests.post(url,headers=headers,data=json.dumps(data))
#         res_ans=res.json()['choices'][0]['text']



    
def page2():
    st.sidebar.write('___________________________')
    if st.sidebar.button('视频制作'):
        st.markdown("""
            ## 介绍
            众所周知，2022年被称为“AIGC元年”，AI绘画、AI聊天机器人等纷纷爆火，人工智能强大到引发对于人的可替代性思考……今年，很多AI视频剪辑工具也被陆续推出，平时花大量时间想文案、剪视频、做营销的我尝试了很多AI工具，发现它们可以一键生成效率倍增，简直是营销神器！接下来我梳理了四个AIGC平台的使用对比，大家可以根据需求自取哦~
            | 平台                | 核心功能       | 数字人模板数           |数字人定制|会员费用|
            |---------------------|----------------|------------------------|----------|--------|
            | [硅基智能](https://website.guiji.ai/)|语音识别、语义理解、语音合成、音意理解、对话管理、知识图谱、克隆人|204人|支持8000/年|2380/年 限时长|
            | [KreadoAI](https://www.kreadoai.com)|国内与海外AI数字人口播视频生成、真人实拍模特/虚拟人物融合口播视频创作、AI生成营销文案|近70人|支持|目前免费|
            |[风平智能](https://fullpeace.cn/)|数字人直播、AI短视频生产、虚拟人数字人IP定制|约十几种（主推定制）|支持|企业视频版13800元/年  企业高级版26800元/年
            | [闪剪](https://shanjian.tv/)  |图文一键转视频、AI智能完成直播切片、AI自动批量自动创作短视频、在线视频编辑器|168人|不支持|298/月
            """)
        st.markdown("""
            ## 总结：  
    1.[硅基智能](https://website.guiji.ai/)  
    硅基智能提供数字人技术解决方案，主要应用于金融、保险、医疗等领域。硅基智能的数字人技术具有高度的安全性和自然语言交互能力，可以实现高度个性化的数字人服务。数字人模板数量较多，覆盖各种场景，而且支持数字人定制，可以根据客户需求进行定制化服务，定制数字人的形象、动作、说话等都十分自然，因此可以为用户带来更加全面逼真的数字人体验。但使用会员费用较高，一般人可能会望而却步。

    2.[KreadoAI](https://www.kreadoai.com)  
    Kreado的数字人技术具有高度的自然语言交互能力和虚拟形象表现能力，主要应用于游戏、电商、娱乐等领域。目前市面上很多做得好的AI视频工具都是收费使用，价格高低不等，但是KreadoAI可以免费使用。此外，它支持140余种多语种语音合成，智能生成的营销文案高效又保质，可以根据场景需要选择数字人说话语气，为数字人语音注入情感，让出海营销更加便捷高效。免费使用、无需下载、用完即走，这些特点也让很多新手小白开始大胆尝试数字人视频创作。

    3.[风平智能](https://fullpeace.cn/)  
    风平智能通过AI深度神经网络生成技术生成的数字人形象，主播外观形象上更加逼真，在直播过程中，虚拟主播还可以实时回答观众的问题，互动性和精准性更强，因此在数字人直播和数字人IP定制方面表现较为出色。风平智能的数字人技术主要应用于短视频、直播、教育等领域。

    4.[闪剪](https://shanjian.tv/)  
    闪剪是一款短视频制作工具，它可以帮助用户快速制作高质量的短视频内容，同时也提供了一些虚拟数字人模板，可以让用户在短视频中添加虚拟数字人。视频模板丰富，提供多个智能配音员和多样化背景音乐，操作简单，基于单一素材拆分、重组、包装，智能生产海量的差异化短视频内容，轻松进行视频创作。还有直播快剪功能，非常适合直播运营新手，轻松实现短视频引流。
        """)
    if st.sidebar.button('视频教学'):
        st.title('待开发')
    
def page3():
    st.sidebar.write('___________________________')               
    baidu='''
    <div style='overflow:hidden'>
    <form  action="http://www.baidu.com/baidu" >
    <input class='bdtext' type="text"  name="word"  size="30">
    <input class='bdbtn' type="submit" value="百度搜索">
    </form>
    </div>
    '''
    st.sidebar.markdown(baidu,unsafe_allow_html=True)
    option=st.sidebar.radio('',['竞对'])
    if option=='竞对':
        wai_gua="""
            <style type="text/css">
        .css{
            width: 100%;
            height: 100vh;  /* 视口的100%高度 */
            border: 0;   /* 把他自带的边框去掉，不然会有违和感 */
        }
        </style>
        <iframe src="https://www.learnprompt.pro/docs/intro" class="css" scrolling="auto" ></iframe>
            """
        st.markdown(wai_gua, unsafe_allow_html=True)
def main():
    app = MultiApp()
    app.add_app('基础介绍🧱',page0)
    app.add_app('案例升级📲',page4)
    app.add_app("CHATGPT👾", page1)
    #app.add_app("CHATGPT平替产品🤖", page4)
    app.add_app("视频制作导航📽️", page2)
    app.add_app("Result1⚙️", page3)
    app.run()
if __name__ == '__main__':
    st.set_page_config(page_title="Chart Cool App",page_icon="🧊",layout="wide")
    main()
    pass
