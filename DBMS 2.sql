--Write at least10 SQL queries for suitable database application using SQL DML statements. Note: Instructor
--will design the queries which demonstrate the use of concepts like all types of Join ,Sub-Query and View.

--Create table as follows:
Books: (book_id, title, author_id, publisher_id, genre, price, published_date)
Authors: (author_id, name, country)
Members: (member_id, name, membership_date)
BorrowedBooks: (borrow_id, book_id, member_id, borrow_date, due_date, return_date)
Publishers: (publisher_id, name, country)

--QUERIES:
SELECT bb.borrow_id, b.title, m.name AS member_name, a.name AS author_name, bb.borrow_date
FROM BorrowedBooks bb
JOIN Books b ON bb.book_id = b.book_id
JOIN Members m ON bb.member_id = m.member_id
JOIN Authors a ON b.author_id = a.author_id;

SELECT b.title, m.name AS member_name, bb.borrow_date, bb.due_date
FROM Books b
LEFT JOIN BorrowedBooks bb ON b.book_id = bb.book_id
LEFT JOIN Members m ON bb.member_id = m.member_id;

SELECT a.name AS author_name, b.title
FROM Authors a
RIGHT JOIN Books b ON a.author_id = b.author_id;

SELECT m.name AS member_name, b.title
FROM Members m
CROSS JOIN Books b;

SELECT b1.title AS book1, b2.title AS book2, a.name AS author_name
FROM Books b1
JOIN Books b2 ON b1.author_id = b2.author_id AND b1.genre = b2.genre AND b1.book_id <> b2.book_id
JOIN Authors a ON b1.author_id = a.author_id;

SELECT title, price
FROM Books
WHERE price > (SELECT AVG(price) FROM Books);

SELECT title
FROM Books b
WHERE NOT EXISTS (SELECT 1 FROM BorrowedBooks bb WHERE bb.book_id = b.book_id);

SELECT name
FROM Members m
WHERE EXISTS (SELECT 1 FROM BorrowedBooks bb WHERE bb.member_id = m.member_id);

CREATE VIEW FrequentBooks AS
SELECT b.book_id, b.title, COUNT(bb.borrow_id) AS borrow_count
FROM Books b
JOIN BorrowedBooks bb ON b.book_id = bb.book_id
GROUP BY b.book_id, b.title
HAVING COUNT(bb.borrow_id) > 5;

SELECT * FROM FrequentBooks;

SELECT title
FROM Books
WHERE author_id IN (
    SELECT a.author_id
    FROM Authors a
    JOIN Publishers p ON a.country = p.country
);
