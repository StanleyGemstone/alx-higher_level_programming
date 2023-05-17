-- script that creates the MySQL database hbtn_0d_2
-- script that creates the MySQL user user_0d_2
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_2';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT PRIVILEGES SELECT ON * . * TO 'user_0d_2'@'localhost';
