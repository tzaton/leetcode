# Write your MySQL query statement below
select name, travelled_distance from (
select u.name, u.id, coalesce(sum(r.distance), 0) as travelled_distance
from Users u
left join Rides r
on u.id = r.user_id
group by u.name, u.id
) t
order by 2 desc, 1