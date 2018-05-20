SELECT nodes_tags.value, COUNT(*) as count
FROM nodes_tags
	JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE
			value='restaurant' or value='fast_food') i
	ON nodes_tags.id=i.id
WHERE nodes_tags.key='cuisine'
GROUP BY nodes_tags.value
ORDER BY count DESC;