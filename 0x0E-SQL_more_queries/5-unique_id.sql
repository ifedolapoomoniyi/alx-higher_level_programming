-- Creates the table unique_id
-- unique_id description: id INT with the default value 1 and unique, name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
