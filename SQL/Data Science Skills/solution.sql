select candidate_id
from candidates
where skill in ('Python','Tableau','PostgreSQL')
group by candidate_id
having count(DISTINCT skill) = 3;