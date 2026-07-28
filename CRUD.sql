USE Liane_library;
# Create New_Book
#INSERT INTO Students (first_name, last_name, class, contact_number) 
#VALUES ('John', 'Doe', '10', '015365455897');
INSERT INTO books (title, author, isbn)
VALUES ('test buch', 'test author', '1234567891011');
SELECT * FROM books; 
SELECT book_id 
FROM loans
WHERE return_date = NULL;

UPDATE loans
SET return_date = '2026-07-09'
WHERE loan_id = '234';

DELETE FROM books
WHERE book_id = '1234567891011';


