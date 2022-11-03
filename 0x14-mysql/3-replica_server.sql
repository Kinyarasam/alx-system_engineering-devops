--
-- CREATE USER replica_user
--
CREATE USER IF NOT EXISTS 'replica_user'@'localhost' IDENTIFIED WITH mysql_native_password BY '';
GRANT ALL PRIVILEGES ON *.* TO 'replica_user'@'localhost' WITH GRANT OPTION;

SHOW GRANTS FOR 'holberton_user'@'localhost';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;

--
-- DISPLAY PRIVILEGES FOR 'holberton_user' USER
--
SHOW GRANTS FOR 'holberton_user'@'localhost';
