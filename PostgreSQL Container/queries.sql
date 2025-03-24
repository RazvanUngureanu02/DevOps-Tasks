-- 1. Total angajați
SELECT COUNT(*) AS total_employees FROM employees;

-- 2. Angajații din departamentul 'IT'
SELECT first_name, last_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE d.department_name = 'IT';

SELECT 
    d.department_name,
    MAX(s.salary) AS max_salary,
    MIN(s.salary) AS min_salary
FROM 
    departments d
JOIN 
    employees e ON d.department_id = e.department_id
JOIN 
    salaries s ON e.employee_id = s.employee_id
GROUP BY 
    d.department_name
ORDER BY 
    d.department_name;
