SELECT * FROM table_name WHERE elektronegativitet < 2;

SELECT * FROM table_name ORDER BY smeltepunkt ASC;

UPDATE table_name SET kogepunkt = 100 WHERE grundstof = 'Helium';

INSERT INTO table_name (grundstof, masse, periode, gruppe, smeltepunkt, kogepunkt, elektronegativitet) 
VALUES ('Ny grundstof', 10.0, 3, 5, 500, 1000, 1.5);

