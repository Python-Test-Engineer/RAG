CREATE TABLE images (
     id SERIAL PRIMARY KEY,
     image bytea
 );

 -- Insert a PNG image as base64
INSERT INTO images (image)
VALUES (decode('iVBORw0KGg...AAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==', 'base64'));

 -- Retrieve the image as base64
SELECT encode(image, 'base64') FROM images WHERE id = 1;