-- script that prepares a MySQL server for the project:
-- Create the database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creates an user in the database
CREATE USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grants privileges
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';
-- Grants all privileges
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
-- Grants select privileges to the user
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
