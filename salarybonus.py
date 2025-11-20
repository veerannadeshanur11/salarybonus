import sys

# Check if salary argument is provided
if len(sys.argv) != 2:
    print("Usage: python salary_bonus.py <salary>")
    sys.exit(1)

# Read salary from system argument
salary = float(sys.argv[1])

# Calculate bonus (10%)
bonus = salary * 0.10

# Total salary
total_salary = salary + bonus

# Output results
print("Employee Salary:", salary)
print("Bonus (10%):", bonus)
print("Total Salary After Bonus:", total_salary)
