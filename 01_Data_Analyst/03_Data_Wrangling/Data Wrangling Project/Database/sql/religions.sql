SELECT nodes_tags.value, COUNT(*) as count
FROM nodes_tags
	join (select distinct(id) from nodes_tags where value='place_of_worship') i
	on nodes_tags.id=i.id
where nodes_tags.key='religion'
group by nodes_tags.value
order by count desc