CREATE DATABASE IF NOT EXISTS gitea;

CREATE USER IF NOT EXISTS 'gitea'@'%' IDENTIFIED BY 'gitea';

GRANT ALL PRIVILEGES ON gitea.* TO 'gitea'@'%';

FLUSH PRIVILEGES;
