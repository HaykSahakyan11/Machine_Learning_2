# Salaries

emp_1 = int(input())
emp_2 = int(input())
emp_3 = int(input())

if emp_1 > emp_2:
    emp_1, emp_2 = emp_2, emp_1

if emp_2 > emp_3:
    emp_2, emp_3 = emp_3, emp_2

if emp_1 > emp_3:
    emp_1, emp_3 = emp_3, emp_1

print(emp_3-emp_1)