--
-- CREATE DATABASE
--
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;

--
-- CREATE TABLE WITHIN tyrell_corp
--
CREATE TABLE IF NOT EXISTS nexus6 (
	PRIMARY KEY(`id`),
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(256) NOT NULL
);

INSERT INTO nexus6 (name) VALUES ("Leon");

--
-- GRANT 'holberton_user' SELECT permission.
--
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'holberton_user'@'localhost';
