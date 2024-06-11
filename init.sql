CREATE USER postgres WITH PASSWORD 'pwd123';
CREATE DATABASE himanshu;
GRANT ALL PRIVILEGES ON DATABASE himanshu TO postgres;

CREATE TABLE car (
    model_id INTEGER PRIMARY KEY,
    model_name VARCHAR(100),
    category_name VARCHAR(100)
);

INSERT INTO car (model_id, model_name, category_name) VALUES (1234, 'virtus', 'sedan');