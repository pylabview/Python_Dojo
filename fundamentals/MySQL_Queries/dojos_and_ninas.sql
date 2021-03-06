
-- Adding three dojos
INSERT INTO dojos (name)
VALUES ('SFO'),
		('BOSTON'),
		('AUSTIN');

-- Deleting the tree dojos added 
SET SQL_SAFE_UPDATES = 0;
DELETE FROM dojos;

-- Adding three dojos again
INSERT INTO dojos (name)
VALUES ('SFO'),
		('BOSTON'),
		('AUSTIN');

-- Create 3 ninjas that belong to the first dojo: SFO
INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Jose','Smith',23,4),
		('Mat','Ward',21,4),
        ('Rod','Wall',22,4);

-- Create 3 ninjas that belong to the first dojo: BOSTON
INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Martha','Smith',23,5),
		('Liz','Jiang',21,5),
        ('Mary','Chen',22,5);

-- Create 3 ninjas that belong to the first dojo: AUSTIN
INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Fred','Smith',20,6),
		('Ann','Cho',21,6),
        ('Maria','Juarez',22,6);

-- Retrieve all the ninjas from the first dojo: SFO
SELECT * from ninjas
WHERE dojo_id = 4; 

-- Retrieve all the ninjas from the last dojo: AUSTIN
SELECT * from ninjas
WHERE dojo_id = 6; 

-- Retrieve the last ninja's dojo
SELECT * from ninjas
order by id DESC LIMIT 1;
