#!/bin/bash
# 从第一行到最后一行分别表示：
# 1. 等待 MySQL 服务启动后再进行数据迁移。nc 即 netcat 缩写
# 2. 收集静态文件到根目录 static 文件夹，
# 3. 生成数据库可执行文件，
# 4. 根据数据库可执行文件来修改数据库
# 5. 用 uwsgi 启动 django 服务
# 6. tail 空命令防止 web 容器执行脚本后退出
while ! nc -z db 3306 ; do
    echo "Waiting for the MySQL Server"
    sleep 3
done

python manage.py collectstatic --noinput
python manage.py makemigrations user snippets link_resource
python manage.py migrate
uwsgi --ini /var/www/online_learning/uwsgi.ini
tail -f /dev/null

exec "$@"
