-- Purpose: Prepare a MySQL server for development purposes.
-- Usage: cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p

-- Create a new database for the application.
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create a new user for the application.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant the new user all privileges on the new database.
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privileges on performance_schema to the new user.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush the privileges to ensure they take effect.
FLUSH PRIVILEGES;
