-- Creating Authors table
CREATE TABLE Authors (
    author_id int PRIMARY KEY,
    name VARCHAR2(100) NOT NULL,
    birth_date DATE
);

-- Creating Publishers table
CREATE TABLE Publishers (
    publisher_id int PRIMARY KEY,
    name VARCHAR2(100) NOT NULL UNIQUE,
    address VARCHAR2(255)
);

-- Creating Books table with constraints and foreign keys
CREATE TABLE Books (
    book_id int PRIMARY KEY,
    title VARCHAR2(150) NOT NULL,
    author_id int NOT NULL,
    publisher_id int,
    price DECIMAL(8, 2) CHECK (price >= 0),
    published_date DATE,
    CONSTRAINT fk_author FOREIGN KEY (author_id) REFERENCES Authors(author_id),
    CONSTRAINT fk_publisher FOREIGN KEY (publisher_id) REFERENCES Publishers(publisher_id)
);



-- Creating a view to list books with their authors and publishers
CREATE VIEW BookDetails AS
SELECT 
    b.book_id, 
    b.title, 
    a.name AS author_name, 
    p.name AS publisher_name,
    b.price, 
    b.published_date
FROM 
    Books b
JOIN 
    Authors a ON b.author_id = a.author_id
LEFT JOIN 
    Publishers p ON b.publisher_id = p.publisher_id;


-- Creating an index on the Books table for the title column
CREATE INDEX idx_books_title ON Books (title);


-- Creating a sequence to auto-generate book IDs
CREATE SEQUENCE book_id_seq
START WITH 1
INCREMENT BY 1
NOCACHE;


-- Creating a synonym for the Books table
CREATE SYNONYM Syn_Books FOR Books;


-- Insert data into Authors
INSERT INTO Authors (author_id, name, birth_date) VALUES (1, 'George Orwell', TO_DATE('1903-06-25', 'YYYY-MM-DD'));
INSERT INTO Authors (author_id, name, birth_date) VALUES (2, 'J.K. Rowling', TO_DATE('1965-07-31', 'YYYY-MM-DD'));

-- Insert data into Publishers
INSERT INTO Publishers (publisher_id, name, address) VALUES (1, 'Penguin Books', '123 Penguin St, New York');
INSERT INTO Publishers (publisher_id, name, address) VALUES (2, 'Bloomsbury', '456 Bloomsbury Ave, London');

-- Insert data into Books
INSERT INTO Books (book_id, title, author_id, publisher_id, price, published_date) 
VALUES (book_id_seq.NEXTVAL, '1984', 1, 1, 15.99, TO_DATE('1949-06-08', 'YYYY-MM-DD'));
INSERT INTO Books (book_id, title, author_id, publisher_id, price, published_date) 
VALUES (book_id_seq.NEXTVAL, 'Harry Potter and the Philosopher''s Stone', 2, 2, 25.99, TO_DATE('1997-06-26', 'YYYY-MM-DD'));

10 QUERIES:
SELECT * FROM BookDetails;

SELECT title, price FROM Books WHERE price > 20;

SELECT a.name, COUNT(b.book_id) AS book_count
FROM Authors a
LEFT JOIN Books b ON a.author_id = b.author_id
GROUP BY a.name;

SELECT title, published_date FROM Books WHERE published_date < TO_DATE('2000-01-01', 'YYYY-MM-DD');

SELECT AVG(price) AS avg_price FROM Books;

SELECT title FROM Books WHERE title LIKE 'Harry%';

SELECT DISTINCT name FROM Publishers;

UPDATE Books SET price = price + 5 WHERE title = '1984';

DELETE FROM Books WHERE author_id = 1;

SELECT title FROM Books WHERE author_id = 2
UNION
SELECT title FROM Books WHERE publisher_id = 1;
