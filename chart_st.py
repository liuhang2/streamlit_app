import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import Bigbook
#import init_streamlit
import mul_st
st.set_page_config(page_title="Chart Cool App",page_icon="🌐",layout='wide',initial_sidebar_state="auto")
hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


with open('./auth.yaml','r',encoding='utf-8') as file:
    result=file.read()
    config = yaml.load(result, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
chang_streamlit="""
<script>
    function f(x) {
        let x=document.getElementsByClassName("css-1yjuwjr effi0qh3");
        x[0].html = "Hello World!"
    }
</script>
"""

st.markdown(chang_streamlit, unsafe_allow_html=True)

name, authentication_status, username = authenticator.login('登入', 'main')
if authentication_status:
    col1,col2 =st.columns([1,2])
    with st.sidebar:
        st.subheader(f'欢迎 *{name}*')
        authenticator.logout('登出', 'main', key='unique_key')
#     with col1:
#         st.subheader(f'欢迎 *{name}*')
#     with col2.container():
#         authenticator.logout('Logout', 'main', key='unique_key')
    #st.title('Some content')
    #Bigbook.main()
    mul_st.main()
    chang_streamlit="""
    <script>
        function f(x) {
            let x = document.getElementsByClassName("css-1q8dd3e edgvbvh9");
            x[0].html = "Hello World!"
        }
    </script>
    """
    st.markdown(chang_streamlit, unsafe_allow_html=True)
    
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('请填入用户名(username)和密码(password)')
