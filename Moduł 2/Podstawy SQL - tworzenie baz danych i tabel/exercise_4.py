CREATE TABLE Cinemas ( id serial, name char(255), address TEXT, PRIMARY KEY(id));

CREATE TABLE Movies (id serial, name char(255), description TEXT, rating int, PRIMARY KEY(id));

CREATE TABLE Tickets (id serial, quantity int, price real, PRIMARY KEY(id));

CREATE TABLE Payments (id serial, type char(255), date date, PRIMARY KEY(id));
