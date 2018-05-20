SELECT contrib.user, COUNT(*) as count
FROM (SELECT user FROM nodes
	UNION ALL SELECT user FROM ways) contrib
GROUP BY contrib.user
ORDER BY count DESC
LIMIT 10;