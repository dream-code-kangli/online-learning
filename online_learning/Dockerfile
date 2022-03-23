FROM python:3.7

LABEL Author="dreamcode"

ENV TZ=Asia/Shanghai
# 设置 python 环境变量
# 设置不生成字节码文件
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /var/www/online_learning
COPY . ./

RUN apt-get update && apt-get install -y netcat \
    && python -m pip install --upgrade pip \
    && pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip install uwsgi -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 8997

# 数据迁移，并使用 uwsgi 启动服务
ENTRYPOINT [ "sh", "-x", "./start.sh" ]
