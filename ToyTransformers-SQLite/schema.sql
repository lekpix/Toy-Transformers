CREATE TABLE toy_tb (
id SERIAL PRIMARY KEY,
name varchar,
toyname varchar);

DROP TABLE toy_tb;

SELECT * FROM toy_tb;
DELETE  FROM toy_tb WHERE toyname='optimusprime';