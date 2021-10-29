CREATE TABLE Author (id serial, name text);
CREATE TABLE Book (id serial, ISBN varchar(13), name text, description text, is_loaned boolean DEFAULT False);
CREATE TABLE Client (id serial, first_name text, last_name text);
CREATE TABLE Category (id serial, name text);

INSERT INTO Author(name) VALUES ('John Ronald Reuel Tolkien');
INSERT INTO Author(name) VALUES ('Joanne Rowling');
INSERT INTO Author(name) VALUES ('Andrzej Pilipiuk');
INSERT INTO Author(name) VALUES ('Stephen King');
INSERT INTO Author(name) VALUES ('David Baldacci');

INSERT INTO Book(ISBN, name, description) VALUES ('9780618002221', 'The Fellowship of the Ring', 'Book about the Fellowship of the Ring');
INSERT INTO Book(ISBN, name, description) VALUES ('9780007203550', 'The Two Towers', 'Book about  the two towers');
INSERT INTO Book(ISBN, name, description) VALUES ('9780618002245', 'The Return of the King', 'A book about the return of the king');
INSERT INTO Book(ISBN, name, description) VALUES ('9781455586486', 'The Last Mile', 'A book about the last mile.');
INSERT INTO Book(ISBN, name, description) VALUES ('9781439148501', 'Under the Dome', 'A book about the dome.');
INSERT INTO Book(ISBN, name, description) VALUES ('9780307743688', 'The Stand', 'A book about the stand.');
INSERT INTO Book(ISBN, name, description) VALUES ('9788379642298', 'Konan Destylator', 'A book about Konan Destylator.');
INSERT INTO Book(ISBN, name, description) VALUES ('9788375745412', 'Kroniki Jakuba Wędrowycza', 'A book about Jakub Wędrowycz.');

