SELECT * FROM Employee;
SELECT * FROM Invoice;
SELECT * FROM Album;
SELECT * FROM Artist;
SELECT * FROM Customer;
SELECT * FROM Genre;
SELECT * FROM InvoiceLine;
SELECT * FROM MediaType;
SELECT * FROM Playlist;
SELECT * FROM PlaylistTrack;
SELECT * FROM sqlite_master;
SELECT * FROM Track;
SELECT Composer, sum(milliseconds), sum(bytes) FROM Track WHERE Composer = 'Wolfgang Amadeus Mozart';
SELECT min(Total), max(TOTAL), avg(Total) FROM Invoice WHERE BillingCountry = 'Germany';

SELECT Composer, COUNT(*)
FROM Track
GROUP BY Composer
ORDER BY COUNT(*)
DESC
LIMIT 10;

SELECT Name, Milliseconds
FROM Track
WHERE Milliseconds > 2500000
AND Milliseconds < 2600000
ORDER BY Milliseconds;

SELECT Artist.Name, Album.Title
FROM Album JOIN Artist
ON Album.ArtistId = Artist.ArtistId
WHERE Name = 'Iron Maiden'
OR Name = 'Amy Winehouse';

SELECT BillingCountry, COUNT(*)
FROM Invoice
GROUP BY BillingCountry
ORDER BY COUNT(*) DESC
LIMIT 3;

SELECT Customer.Email, Customer.FirstName, Customer.LastName, sum(Invoice.Total)
FROM Customer JOIN Invoice
ON Customer.CustomerId = Invoice.CustomerId
GROUP BY Customer.CustomerId
ORDER BY sum(Invoice.Total)
DESC
LIMIT 1;

SELECT Customer.Email, Customer.FirstName, Customer.LastName, Genre.Name
FROM Customer JOIN Invoice
ON Customer.CustomerId = Invoice.CustomerId
JOIN InvoiceLine
ON Invoice.InvoiceId = InvoiceLine.InvoiceId
JOIN Track
ON InvoiceLine.TrackId = Track.TrackId
JOIN Genre
ON Track.GenreId = Genre.GenreId
WHERE Genre.Name = 'Rock'
GROUP BY Customer.Email
ORDER BY Customer.Email
ASC;

SELECT BillingCity, SUM(Total)
FROM Invoice
GROUP BY BillingCity
ORDER BY SUM(Total)
DESC
LIMIT 1;

SELECT Invoice.BillingCity, COUNT(Invoice.Total) as INVT, Genre.Name
FROM Invoice JOIN InvoiceLine
ON Invoice.InvoiceId = InvoiceLine.InvoiceId
JOIN Track
ON InvoiceLine.TrackId = Track.TrackId
JOIN Genre
ON Track.GenreId = Genre.GenreId
WHERE Invoice.BillingCity = 'Prague'
GROUP BY Genre.Name
ORDER BY INVT
DESC
LIMIT 3;

SELECT Artist.Name, COUNT(Genre.Name) as GENA
FROM Genre JOIN Track
ON Genre.GenreId = Track.GenreId
JOIN Album
ON Track.AlbumId = Album.AlbumId
JOIN Artist
ON Album.ArtistId = Artist.ArtistId
WHERE Genre.Name = 'Rock'
GROUP BY Artist.Name
ORDER BY GENA
DESC
LIMIT 10;

SELECT Invoice.BillingCity, COUNT(Track.TrackId) as TRID
FROM Invoice JOIN InvoiceLine
ON Invoice.InvoiceId = InvoiceLine.InvoiceId
JOIN Track
ON InvoiceLine.TrackId = Track.TrackId
JOIN Genre
ON Track.GenreId = Genre.GenreId
WHERE Genre.Name = 'Alternative & Punk' AND Invoice.BillingCountry = 'France'
GROUP BY Invoice.BillingCity
ORDER BY TRID
DESC;

SELECT sum(total)
FROM (SELECT COUNT(*) AS total
FROM Invoice
GROUP BY BillingCountry
ORDER BY total DESC
LIMIT 5);

SELECT BillingCity, BillingState, BillingCountry, Total
FROM Invoice,
  (SELECT avg(Total) as average
  FROM Invoice) AS subquery
WHERE Total > average;

SELECT FirstName, LastName, BillingCity, BillingState, BillingCountry, Total
FROM Invoice JOIN Customer
    ON Invoice.CustomerId = Customer.CustomerId,
  (SELECT avg(Total) AS average
  FROM Invoice) AS subquery
WHERE Total > average
ORDER BY Total;

SELECT Genre.Name, MediaType.Name, COUNT(MediaType.Name) as cnt
FROM Track JOIN Genre
ON Track.GenreId = Genre.GenreId
JOIN MediaType
ON Track.MediaTypeId = MediaType.MediaTypeId
WHERE Genre.Name = 'Pop'
GROUP BY MediaType.Name;

SELECT COUNT(DISTINCT(Invoice.CustomerId))
FROM Invoice JOIN InvoiceLine
ON Invoice.InvoiceId = InvoiceLine.InvoiceId
JOIN Track
ON InvoiceLine.TrackId = Track.TrackId
JOIN Genre
ON Track.GenreId = Genre.GenreId
WHERE Genre.Name = 'Jazz';

SELECT Genre.Name, Track.Milliseconds, COUNT(Genre.Name) as CNT
FROM Track JOIN Genre
    ON Track.GenreId = Genre.GenreId,
  (SELECT avg(Track.Milliseconds) AS AVG
    FROM Track) AS subquery
WHERE Track.Milliseconds < AVG
GROUP BY Genre.Name
ORDER BY CNT DESC

SELECT Genre.Name, (sum(Track.Milliseconds)/360000.0) as Total_Hours, COUNT(Genre.Name) as CNT
FROM Track JOIN Genre
    ON Track.GenreId = Genre.GenreId,
  (SELECT avg(Track.Milliseconds) AS AVG
    FROM Track) AS subquery
WHERE Track.Milliseconds < AVG
GROUP BY Genre.Name
ORDER BY CNT DESC