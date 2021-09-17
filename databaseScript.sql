CREATE DATABASE Phonebook;
CREATE TABLE City
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE Users
(
    id SERIAL PRIMARY KEY,
    user_name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(20),
    city_id INT ,
    FOREIGN KEY (city_id) REFERENCES City(id)
);



