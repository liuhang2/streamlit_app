FROM python:3.8.8
RUN mkdir /code
WORKDIR /code
RUN  pip install -i http://mirrors.aliyun.com/pypi/simple  --upgrade pip --trusted-host mirrors.aliyun.com && \
pip install --upgrade setuptools -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com && \
pip install urllib3==1.26.15 -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com && \
pip install streamlit -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com  &&\
pip install pyyaml -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com &&\
pip install pathlib -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com 
COPY . /code/
CMD ["streamlit","run", "./chart_st.py"]