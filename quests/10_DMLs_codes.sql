CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE students_01 (
  id_name UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name VARCHAR(100),
  age INT
);