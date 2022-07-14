SELECT * FROM users;

-- Adding three users
INSERT INTO users (first_name,last_name,email)
VALUES ('Jose', 'Smith', '123@gmail.com'),
		('Mat', 'Perez', '567@gmail.com'),
		('Kris', 'Wall', '891@gmail.com');
        
--  Retrieve first users using email 
SELECT * FROM users
WHERE email = '123@gmail.com';

-- Retrive last user using their id
SELECT * FROM users
WHERE id = 3;
 
--  Change the user with id=3 so their last name is Pancakes
 UPDATE users
 SET last_name = 'Pancakes'
 WHERE id =3;
 
 -- Delete the user with id=2 from the database 
DELETE FROM users
WHERE id =2;

SELECT * FROM users
order by first_name;
