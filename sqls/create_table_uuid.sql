CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE users_uuid_name (
  id_name UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name VARCHAR(100)
);

INSERT INTO users_uuid_name (name) VALUES ('Alice');

SELECT id_name, name FROM users_uuid_name;

INSERT INTO users_uuid_name (name)
VALUES
('Alice'),
('Bob'),
('Charlie');

UPDATE users_uuid_name
SET name = 'UpdatedName'
WHERE id_name = '48655869-c0a9-4426-9aad-5e895fb0f621';

DELETE FROM users_uuid_name
WHERE id_name = '93c29359-51e7-4342-aafd-000b5945ef61';

