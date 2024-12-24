# docker/mysql/Dockerfile
FROM mysql:8.0

# コンテキストが「プロジェクトルート(.)」なので、コピー元に "docker/mysql/" が必要
COPY docker/mysql/my.cnf /etc/mysql/conf.d/
COPY docker/mysql/init.sql /docker-entrypoint-initdb.d/
