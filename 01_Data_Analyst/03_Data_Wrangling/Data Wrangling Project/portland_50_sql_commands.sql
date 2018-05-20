"Contributing Users"
SELECT e.user, COUNT(*) as count
FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e
GROUP BY e.user
ORDER BY count DESC
LIMIT 10;

"Number of Unique Users"
SELECT COUNT(DISTINCT(e.uid))
  FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways) e;

"Postal Code"
SELECT tags.value, COUNT(*) AS count
FROM (SELECT * FROM nodes_tags
  UNION ALL
    SELECT * FROM ways_tags) tags
WHERE tags.key='postcode'
GROUP BY tags.value
ORDER BY count DESC;

"Top Cities"
SELECT tags.value, COUNT(*) AS count
FROM (SELECT * FROM nodes_tags
  UNION ALL
    SELECT * FROM ways_tags) tags
WHERE tags.key LIKE 'city'
GROUP BY tags.value
ORDER BY count DESC;

"Top nodes_tags key values"
SELECT key, COUNT(*) as count
FROM nodes_tags
GROUP BY key
ORDER BY count DESC
LIMIT 10;

"Top Amenities"
SELECT value, COUNT(*) as count
FROM nodes_tags
WHERE key='amenity'
GROUP BY value
ORDER BY count DESC;

"Top Cuisines"
SELECT nodes_tags.value, COUNT(*) as num
FROM nodes_tags
  JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value='restaurant') i
  ON nodes_tags.id=i.id
WHERE nodes_tags.key='cuisine'
GROUP BY nodes_tags.value
ORDER BY num DESC;

SELECT nodes_tags.value, COUNT(*) as num
FROM nodes_tags
  JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value LIKE '%coffee') i
  ON nodes_tags.id=i.id
GROUP BY nodes_tags.value
ORDER BY num DESC;

SELECT value, COUNT(*) as num
FROM nodes_tags
GROUP BY key
ORDER BY num DESC ;

"Number of Nodes"
SELECT COUNT(*) FROM nodes;

"Number of Ways"
SELECT COUNT(*) FROM ways;

SELECT DISTINCT
  round(lat, 1), round(lon, 1)
FROM nodes;

"Postal Code"
SELECT DISTINCT(tags.value)
FROM (SELECT * FROM nodes_tags
  UNION ALL
    SELECT * FROM ways_tags) tags
WHERE tags.key='postcode';