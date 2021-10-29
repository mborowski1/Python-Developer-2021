INSERT INTO Movies(name, description, rating) VALUES ('Matrix', 'Gernialny film', 10);

INSERT INTO Movies(name, description, rating) VALUES ('Gran Torino', 'Bardzo dobry film', 8);

INSERT INTO Movies(name, description, rating) VALUES ('Blade Runner 2049', 'Jeden z moich ulubionych filmów', 10);

INSERT INTO Movies(name, description, rating) VALUES ('Król Artur: Legenda miecza', 'Dobry film', 7);

INSERT INTO Tickets(quantity, price) VALUES (1, 10);

INSERT INTO Tickets(quantity, price) VALUES (1, 20);

INSERT INTO Tickets(quantity, price) VALUES (1, 30);

INSERT INTO Tickets(quantity, price) VALUES (1, 40);

SELECT * FROM Movies WHERE name LIKE 'W%';

SELECT * FROM Tickets WHERE price > 15.30;

SELECT * FROM Tickets WHERE quantity > 0;
