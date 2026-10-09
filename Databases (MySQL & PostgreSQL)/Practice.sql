-- Active: 1783696788047@@127.0.0.1@3306@facebook
SHOW TABLES;


CREATE TABLE  blogs(
  id INT PRIMARY KEY AUTO_INCREMENT,
  title varchar(255) NOT NULL,
  description text NOT NULL

);

DESCRIBE users;


SELECT * FROM users;

INSERT INTO users (name,age, adress)
 VALUES ('Ishtiak', '25','Dhaka'),
        ('Rifat', '30',NULL),
        ('Ahmed',10,'Chittagong'),
        ('Rana', 20, 'Khulna'),
        ('Sakib', 15, 'Barishal');

---1. Select All
SELECT * FROM users;

---2. Select Specific Columns
SELECT name, age FROM users;

---3. Aliasing Columns
SELECT name AS 'User Name', age AS 'User Age'
FROM users;

---4. Filtering data
SELECT * FROM users WHERE age > 20;
SELECT * FROM users WHERE name= 'Ishtiak';

---5. Aggregate Functions
SELECT COUNT(*) AS total_users FROM users;
SELECT AVG(age) AS average_age FROM users;
SELECT SUM(age) AS total_age FROM users;


---6.In and Not In
SELECT * FROM users WHERE age IN (10, 15, 20);
SELECT * FROM users WHERE age NOT IN (10, 15, 20);