-- Creates the table id_not_null on my MySQL server with default value 1 for id
-- Use ALTER TABLE id_not_null ALTER COLUMN id DROP DEFAULT to delete the default constraint
CREATE TABLE IF NOT EXISTS id_not_null
(
	id INT DEFAULT (1),
	name VARCHAR(256)
);
