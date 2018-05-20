SELECT tags.value, COUNT(*) as count
FROM (SELECT * FROM nodes_tags
	UNION ALL
		SELECT * FROM ways_tags) tags
WHERE tags.key='postcode'
GROUP BY tags.value
ORDER BY count DESC;