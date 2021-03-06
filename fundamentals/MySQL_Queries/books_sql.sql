-- Create 5 different users: Jane Amsden, Emily Dixon, Theodore Dostoevsky, William Shapiro, Lao Xiu
INSERT INTO users(name)
VALUES ('Jane Amsden'),
		('Emily Dixon'),
        ('Theodore Dostoevsky'),
        ('William Shapiro'),
        ('Lao Xiu');

-- Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby
INSERT INTO books(title,num_of_pages)
VALUES ('C Sharp',240),
		('Java',320),
        ('Python',345),
        ('PHP',342),
        ('Ruby',276);

--  Change the name of the C Sharp book to C#
UPDATE books
SET title = 'C#'
WHERE id =1;

-- Change the first name of the 4th user to Bill
UPDATE users
SET name = 'Bill Shapiro'
WHERE id =4;

-- Have the first user favorite the first 2 books
INSERT INTO books_fav_list(book_id,user_id)
VALUES (1,1),
(2,1);

-- Have the second user favorite the first 3 books
INSERT INTO books_fav_list(book_id,user_id)
VALUES (1,2),
(2,2),
(3,2);

-- Have the third user favorite the first 4 books
INSERT INTO books_fav_list(book_id,user_id)
VALUES (1,3),
(2,3),
(3,3),
(4,3);

-- Have the fourth user favorite all the books
INSERT INTO books_fav_list(book_id,user_id)
VALUES (1,4),
(2,4),
(3,4),
(4,4),
(5,4);

-- Retrieve all the users who favorited the 3rd book
SELECT users.name FROM users
JOIN books_fav_list on users.id = user_id
JOIN books on books_fav_list.book_id = books.id
WHERE books.id = 3;

-- Remove the first user of the 3rd book's favorites
DELETE from books_fav_list
where book_id = 3 AND user_id = 1;


-- Have the 5th user favorite the 2nd book
INSERT INTO books_fav_list(book_id,user_id)
VALUES (2,5);

-- Find all the books that the 3rd user favorited
SELECT title from books
JOIN books_fav_list as faves on faves.book_id = books.id
WHERE faves.user_id = 3;

-- Query: Find all the users that favorited to the 5th book
SELECT name from users
JOIN books_fav_list as faves on users.id = faves.user_id
WHERE faves.book_id = 5;
