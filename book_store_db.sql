CREATE TABLE books (
    book_id varchar (5)  PRIMARY KEY NOT NULL,
    title VARCHAR(40),
    author VARCHAR(20),
    year INT,
    price DECIMAL(10, 2),
    review INT(5)
);

INSERT INTO books (book_id, title, author, price, year, review) VALUES
('b1', 'An Artist of the Floating World', 'Kazuo Ishiguro', 18.99, 2013, 5),
('b2', 'Otherlands: A World in the Making', 'Dr Thomas Halliday', 8.49, 2023, null),
('b3', 'Against the Loveless World', 'Susan Abulhawa', 8.99, 2021, 4),
('b4', 'The Limits', 'Nell Freudenberger', 19.82, 2024, null),
('b5', 'Cahokia Jazz', 'Francis Spufford', 8.49, 2023, 4),
('b6', 'Whiskey Tender', 'Deborah Taffa', 8.99, 2024, null),
('b7', 'The Island of Missing Trees', 'Elif Shafak', 8.99, 2022, null),
('b8', 'Talking at Night', 'Claire Daverley', 13.50, 2023, null),
('b9', 'A Little Life', 'Hanya Yanagihara', 10.99, 2016, null),
('b10', 'Small Pleasures', 'Clare Chambers', 8.99, 2021, null),
('b11', 'Thinking, Fast and Slow', 'Daniel Kahneman', 12.50, 2012, null);


drop table  if exists orders;
CREATE TABLE orders (
    date DATETIME,
    order_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    customer_name VARCHAR(40),
    book_id VARCHAR(5),
    sales DECIMAL(10, 2),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

INSERT INTO orders (date, order_id, customer_name, book_id, sales)
VALUES
('2024-01-15', 1, 'Amaleta Gwillym', 'b10', 12.50),
('2024-01-23', 3, 'Philipa Gath', 'b4', 8.49),
('2024-01-29', 27, 'Farrell Gusney', 'b9', 8.99),
('2024-01-30', 24, 'Catherina Strover', 'b2', 8.49),
('2024-02-16', 9, 'Latrena Welbeck', 'b8', 10.99),
('2024-02-18', 17, 'Sherill McQuade', 'b4', 8.49),
('2024-02-22', 8, 'Katherina Vuitton', 'b6', 8.99),
('2024-02-22', 28, 'Garvey Krysztofowicz', 'b1', 18.99),
('2024-02-23', 4, 'Marion Stronghill', 'b10', 12.50),
('2024-02-24', 21, 'Stanley Giovannacci', 'b4', 8.49),
('2024-02-25', 5, 'Odele Jzhakov', 'b5', 8.99),
('2024-02-25', 18, 'Maighdiln Aked', 'b5', 8.99),
('2024-02-28', 11, 'Oralle Powney', 'b11', 12.50),
('2024-02-28', 12, 'Wenona Mepsted', 'b1', 18.99),
('2024-02-29', 7, 'Elizabeth MacGown', 'b3', 19.82),
('2024-03-04', 30, 'Bellina Treadgear', 'b5', 8.99),
('2024-03-14', 16, 'Saidee Olivo', 'b3', 19.82),
('2024-03-15', 25, 'Artur Wareham', 'b10', 12.50),
('2024-03-15', 26, 'Aaren Giorgiutti', 'b5', 8.99),
('2024-03-18', 2, 'Bowie Hince', 'b10', 12.50),
('2024-03-22', 10, 'Gabe Leipold', 'b11', 12.50),
('2024-03-27', 6, 'Leanor Trazzi', 'b8', 10.99),
('2024-03-30', 19, 'Ingar Tellenbroker', 'b6', 8.99),
('2024-04-01', 14, 'Adah Giacobazzi', 'b8', 10.99),
('2024-04-02', 22, 'Byron Pontin', 'b4', 8.49),
('2024-04-03', 20, 'Alfredo Warder', 'b2', 8.49),
('2024-04-03', 15, 'Haskel Rootham', 'b2', 8.49),
('2024-04-05', 29, 'Gawain Shinfield', 'b1', 18.99),
('2024-04-09', 23, 'Priscella Sooper', 'b9', 8.99),
('2024-04-10', 13, 'Randolf Baroc', 'b8', 10.99);
 
 
 CREATE TABLE book_stock (
    book_id VARCHAR (5),
    stock_quantity INT,
    waitlist BOOLEAN DEFAULT FALSE,
    waitlist_date DATETIME,
    waiting_days INT,
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

INSERT INTO book_stock (book_id, stock_quantity, waitlist, waitlist_date, waiting_days)
VALUES
('b1', 10, FALSE, '2024-04-30 12:00', 20),
('b2', 5, TRUE, '2024-05-06 08:00', 25),
('b3', 0, FALSE, NULL, NULL),
('b4', 3, TRUE, '2024-05-05 10:00', 25),
('b5', 7, FALSE, NULL, NULL),
('b6', 2, TRUE, '2024-05-10 13:45', 20),
('b7', 0, FALSE, NULL, NULL),
('b8', 1, FALSE, NULL, NULL),
('b9', 4, TRUE, '2024-05-01 16:30', 20),
('b10', 8, FALSE, NULL, NULL),
('b11', 3, TRUE, '2024-05-06 09:30', 25);

select * from book_stock;
