CREATE DATABASE phonebook;
CREATE TABLE city
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE users
(
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(20),
    city_id INT ,
    FOREIGN KEY (city_id) REFERENCES city(id)
);


