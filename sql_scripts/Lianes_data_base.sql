DROP SCHEMA IF EXISTS liane_library;
CREATE SCHEMA liane_library;
USE liane_library;
Create table books (
   title VARCHAR(100) NOT NULL,
   author VARCHAR(100) NOT NULL,
   genre VARCHAR(50),
   published_year INT,
   isbn VARCHAR(13) PRIMARY KEY
);
Create table friends (
    friend_name VARCHAR(13) NOT NULL,
    max_loans INT DEFAULT 2 NOT NULL, 
    notes TEXT,
    friend_id INT AUTO_INCREMENT PRIMARY KEY
    );
Create table loans (
    loan_id VARCHAR(13),
    book_id VARCHAR(13),
    friend_id INT,
    loan_date DATE DEFAULT (CURRENT_DATE()),
    return_date DATE,
	last_contact DATE,
    next_contact DATE,
    note TEXT,
    FOREIGN KEY (book_id) REFERENCES books(isbn),
    FOREIGN KEY (friend_id) REFERENCES friends(friend_id)
    );
SELECT * FROM loans;
 
    
    
