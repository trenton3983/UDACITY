SELECT value, COUNT(*) as count
FROM nodes_tags
WHERE key='cuisine'
GROUP BY value
ORDER BY count DESC;