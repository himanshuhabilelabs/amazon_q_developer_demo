import pandas as pd
import matplotlib.pyplot as plt
import random
from faker import Faker

fake = Faker()

# Generate 100 employees
employees = []
for i in range(100):
    employee = {
        'Name': fake.name(),
        'Email': fake.email(),
        'Phone': fake.phone_number(),
        'Salary': random.randint(30000, 199999)
    }
    employees.append(employee)

# Create DataFrame
df = pd.DataFrame(employees)

# Save to Excel
df.to_excel('employees.xlsx', index=False)

# Get top 5 highest salary employees
top_5 = df.nlargest(5, 'Salary')

# Create pie chart
plt.figure(figsize=(10, 8))
plt.pie(top_5['Salary'], labels=top_5['Name'], autopct='%1.1f%%', startangle=90)
plt.title('Top 5 Highest Salary Employees')
plt.axis('equal')
plt.tight_layout()
plt.savefig('top_5_salaries_pie_chart.png', dpi=300, bbox_inches='tight')
plt.show()

print("Excel file 'employees.xlsx' created successfully!")
print("Pie chart saved as 'top_5_salaries_pie_chart.png'")
print("\nTop 5 Highest Salary Employees:")
print(top_5[['Name', 'Salary']].to_string(index=False))