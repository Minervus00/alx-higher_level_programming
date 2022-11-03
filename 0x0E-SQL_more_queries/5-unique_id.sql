-- Creates the table unique_id on your MySQL server
-- With default id and unique values for id
CREATE TABLE IF NOT EXISTS unique_id
(
	id INT DEFAULT (1) UNIQUE,
	name VARCHAR(256)
);
