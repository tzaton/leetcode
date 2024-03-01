# Write your MySQL query statement below
select p.name
from SalesPerson p
left join Orders o
on o.sales_id = p.sales_id
left join Company c
on o.com_id = c.com_id
group by p.name
having sum(case when c.name = 'RED' then 1 else 0 end) = 0