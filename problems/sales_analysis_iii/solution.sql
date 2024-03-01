# Write your MySQL query statement below
select p.product_id, p.product_name
from Product p
join Sales s
on p.product_id = s.product_id
group by p.product_id, p.product_name
having min(sale_date) between '2019-01-01' and '2019-03-31'
and max(sale_date) between '2019-01-01' and '2019-03-31'