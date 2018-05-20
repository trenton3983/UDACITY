SELECT tags.key, tags.value, COUNT(*) as count
FROM (SELECT * FROM nodes_tags
	UNION ALL
		SELECT * FROM ways_tags) tags
WHERE tags.type='tiger'
GROUP BY tags.value
ORDER BY count DESC
