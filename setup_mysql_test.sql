-- Purpose: Prepare a MySQL server for testing purposes.
-- Usage: cat setup_mysql_test.sql | mysql -hlocalhost -uroot -p

-- Create a new database for the application.
CREATE DATABASE IF NOT EXISTS `hbnb_test_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create a new user for the application.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant the new user all privileges on the new database.
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privileges on performance_schema to the new user.
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush the privileges to ensure they take effect.
FLUSH PRIVILEGES;
