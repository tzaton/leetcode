# Write your MySQL query statement below

select x.student_id, x.student_name, x.subject_name, count(e.student_id) as attended_exams
from (
select s.student_id, s.student_name, u.subject_name
from Students s
cross join Subjects u
) x
left join Examinations e
on x.student_id = e.student_id
and x.subject_name = e.subject_name
group by x.student_id, x.student_name, x.subject_name
order by x.student_id, x.subject_name
