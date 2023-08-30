FROM harbor.methodot.com/cloudtogo/python:3.6.12-alpine3.12
RUN mkdir /code
WORKDIR /code
RUN pip install -i http://mirrors.aliyun.com/pypi/simple  --upgrade pip --trusted-host mirrors.aliyun.com && \
pip install --upgrade setuptools -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com && \
pip install urllib3==1.26.15 -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com
COPY requirements.txt /code/
RUN pip install -i http://mirrors.aliyun.com/pypi/simple --no-cache-dir -r requirements.txt --trusted-host mirrors.aliyun.com
COPY . /code/
CMD ["streamlit","run", "./chart_st.py"]