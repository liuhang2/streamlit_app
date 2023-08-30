FROM harbor.methodot.com/cloudtogo/python:3.6.12-alpine3.12
RUN mkdir /code
WORKDIR /code
RUN python3 pip install -i http://mirrors.aliyun.com/pypi/simple  --upgrade pip --trusted-host mirrors.aliyun.com && \
python3 pip install --upgrade setuptools -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com && \
python3 pip install urllib3==1.26.15 -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com && \
python3 pip install streamlit -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com  &&\
python3 pip install pyyaml -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com &&\
python3 pip install pathlib -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com 
COPY . /code/
CMD ["streamlit","run", "./chart_st.py"]