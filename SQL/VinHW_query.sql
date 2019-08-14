-- 1. List the following details of each employee: employee number, last name, first name, gender, and salary.

-- using join implicitly
select e.emp_no, e.last_name, e.first_name, e.gender, s.salary from employees e, 
salaries s where e.emp_no = s.emp_no

--alternatively the same query can be written as (using join explicitly)
select e.emp_no, e.last_name, e.first_name,  e.gender, s.salary from employees e
join salaries s on e.emp_no = s.emp_no

--2. List employees who were hired in 1986.
select e.emp_no, e.last_name, e.first_name, e.hire_date from employees e
where e.hire_date >= '1986/01/01' and e.hire_date <= '1986/12/31'

--3. List the manager of each department with the following information: 
--department number, department name, the manager's employee number, last name, first name, 
--and start and end employment dates.

select dm.dept_no, d.dept_name, dm.emp_no, e.last_name, e.first_name,
		dm.from_date as Start_Date, dm.to_date as End_Date 
from dept_manager dm, departments d, employees e 
where dm.dept_no = d.dept_no and dm.emp_no = e.emp_no;

--4. List the department of each employee with the following information: 
--employee number, last name, first name, and department name.

select e.emp_no, e.last_name, e.first_name, d.dept_name 
from employees e, dept_emp de, departments d
where e.emp_no = de.emp_no and de.dept_no = d.dept_no;

--5. List all employees whose first name is "Hercules" and last names begin with "B."
select e.first_name, e.last_name from employees e
where e.first_name = 'Hercules' and e.last_name like 'B%'

--6. List all employees in the Sales department, 
--including their employee number, last name, first name, and department name.

select  d.dept_name, de.emp_no, e.last_name, e.first_name
from dept_emp de, departments d, employees e 
where de.dept_no = d.dept_no and de.emp_no = e.emp_no and d.dept_name like 'Sale%';

--7. List all employees in the Sales and Development departments, 
--including their employee number, last name, first name, and department name.

select  d.dept_name, de.emp_no, e.last_name, e.first_name
from dept_emp de, departments d, employees e 
where de.dept_no = d.dept_no and de.emp_no = e.emp_no 
       and (d.dept_name = 'Development' or d.dept_name = 'Sale');
	   
--8. In descending order, list the frequency count of employee last names, 
--i.e., how many employees share each last name.

select last_name, count(last_name) as frequency
from employees group by last_name
order by count(last_name) desc;





