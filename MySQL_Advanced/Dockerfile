FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=my-secret-pw

COPY ./ /docker-entrypoint-initdb.d/

EXPOSE 3306

CMD ["mysqld"]