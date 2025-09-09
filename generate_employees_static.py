import pandas as pd
import matplotlib.pyplot as plt

# Static employee data (100 employees)
employees = [
    {"Name": "John Smith", "Email": "john.smith@company.com", "Phone": "+1-555-0101", "Salary": 185000},
    {"Name": "Sarah Johnson", "Email": "sarah.johnson@company.com", "Phone": "+1-555-0102", "Salary": 192000},
    {"Name": "Michael Brown", "Email": "michael.brown@company.com", "Phone": "+1-555-0103", "Salary": 178000},
    {"Name": "Emily Davis", "Email": "emily.davis@company.com", "Phone": "+1-555-0104", "Salary": 195000},
    {"Name": "David Wilson", "Email": "david.wilson@company.com", "Phone": "+1-555-0105", "Salary": 188000},
    {"Name": "Lisa Anderson", "Email": "lisa.anderson@company.com", "Phone": "+1-555-0106", "Salary": 165000},
    {"Name": "Robert Taylor", "Email": "robert.taylor@company.com", "Phone": "+1-555-0107", "Salary": 172000},
    {"Name": "Jennifer Martinez", "Email": "jennifer.martinez@company.com", "Phone": "+1-555-0108", "Salary": 158000},
    {"Name": "William Garcia", "Email": "william.garcia@company.com", "Phone": "+1-555-0109", "Salary": 145000},
    {"Name": "Amanda Rodriguez", "Email": "amanda.rodriguez@company.com", "Phone": "+1-555-0110", "Salary": 167000},
    {"Name": "James Lee", "Email": "james.lee@company.com", "Phone": "+1-555-0111", "Salary": 134000},
    {"Name": "Michelle White", "Email": "michelle.white@company.com", "Phone": "+1-555-0112", "Salary": 156000},
    {"Name": "Christopher Harris", "Email": "christopher.harris@company.com", "Phone": "+1-555-0113", "Salary": 142000},
    {"Name": "Jessica Clark", "Email": "jessica.clark@company.com", "Phone": "+1-555-0114", "Salary": 149000},
    {"Name": "Daniel Lewis", "Email": "daniel.lewis@company.com", "Phone": "+1-555-0115", "Salary": 138000},
    {"Name": "Ashley Walker", "Email": "ashley.walker@company.com", "Phone": "+1-555-0116", "Salary": 163000},
    {"Name": "Matthew Hall", "Email": "matthew.hall@company.com", "Phone": "+1-555-0117", "Salary": 151000},
    {"Name": "Stephanie Allen", "Email": "stephanie.allen@company.com", "Phone": "+1-555-0118", "Salary": 144000},
    {"Name": "Andrew Young", "Email": "andrew.young@company.com", "Phone": "+1-555-0119", "Salary": 137000},
    {"Name": "Nicole King", "Email": "nicole.king@company.com", "Phone": "+1-555-0120", "Salary": 159000},
    {"Name": "Joshua Wright", "Email": "joshua.wright@company.com", "Phone": "+1-555-0121", "Salary": 146000},
    {"Name": "Megan Lopez", "Email": "megan.lopez@company.com", "Phone": "+1-555-0122", "Salary": 153000},
    {"Name": "Ryan Hill", "Email": "ryan.hill@company.com", "Phone": "+1-555-0123", "Salary": 141000},
    {"Name": "Rachel Scott", "Email": "rachel.scott@company.com", "Phone": "+1-555-0124", "Salary": 148000},
    {"Name": "Brandon Green", "Email": "brandon.green@company.com", "Phone": "+1-555-0125", "Salary": 135000},
    {"Name": "Samantha Adams", "Email": "samantha.adams@company.com", "Phone": "+1-555-0126", "Salary": 162000},
    {"Name": "Kevin Baker", "Email": "kevin.baker@company.com", "Phone": "+1-555-0127", "Salary": 147000},
    {"Name": "Lauren Gonzalez", "Email": "lauren.gonzalez@company.com", "Phone": "+1-555-0128", "Salary": 154000},
    {"Name": "Tyler Nelson", "Email": "tyler.nelson@company.com", "Phone": "+1-555-0129", "Salary": 139000},
    {"Name": "Brittany Carter", "Email": "brittany.carter@company.com", "Phone": "+1-555-0130", "Salary": 157000},
    {"Name": "Justin Mitchell", "Email": "justin.mitchell@company.com", "Phone": "+1-555-0131", "Salary": 143000},
    {"Name": "Kayla Perez", "Email": "kayla.perez@company.com", "Phone": "+1-555-0132", "Salary": 150000},
    {"Name": "Nathan Roberts", "Email": "nathan.roberts@company.com", "Phone": "+1-555-0133", "Salary": 136000},
    {"Name": "Alexis Turner", "Email": "alexis.turner@company.com", "Phone": "+1-555-0134", "Salary": 161000},
    {"Name": "Zachary Phillips", "Email": "zachary.phillips@company.com", "Phone": "+1-555-0135", "Salary": 145000},
    {"Name": "Danielle Campbell", "Email": "danielle.campbell@company.com", "Phone": "+1-555-0136", "Salary": 152000},
    {"Name": "Aaron Parker", "Email": "aaron.parker@company.com", "Phone": "+1-555-0137", "Salary": 140000},
    {"Name": "Heather Evans", "Email": "heather.evans@company.com", "Phone": "+1-555-0138", "Salary": 155000},
    {"Name": "Jordan Edwards", "Email": "jordan.edwards@company.com", "Phone": "+1-555-0139", "Salary": 133000},
    {"Name": "Crystal Collins", "Email": "crystal.collins@company.com", "Phone": "+1-555-0140", "Salary": 158000},
    {"Name": "Sean Stewart", "Email": "sean.stewart@company.com", "Phone": "+1-555-0141", "Salary": 144000},
    {"Name": "Vanessa Sanchez", "Email": "vanessa.sanchez@company.com", "Phone": "+1-555-0142", "Salary": 149000},
    {"Name": "Eric Morris", "Email": "eric.morris@company.com", "Phone": "+1-555-0143", "Salary": 137000},
    {"Name": "Tiffany Rogers", "Email": "tiffany.rogers@company.com", "Phone": "+1-555-0144", "Salary": 160000},
    {"Name": "Adam Reed", "Email": "adam.reed@company.com", "Phone": "+1-555-0145", "Salary": 146000},
    {"Name": "Courtney Cook", "Email": "courtney.cook@company.com", "Phone": "+1-555-0146", "Salary": 153000},
    {"Name": "Jacob Bailey", "Email": "jacob.bailey@company.com", "Phone": "+1-555-0147", "Salary": 141000},
    {"Name": "Melissa Rivera", "Email": "melissa.rivera@company.com", "Phone": "+1-555-0148", "Salary": 148000},
    {"Name": "Cody Cooper", "Email": "cody.cooper@company.com", "Phone": "+1-555-0149", "Salary": 135000},
    {"Name": "Amber Richardson", "Email": "amber.richardson@company.com", "Phone": "+1-555-0150", "Salary": 159000},
    {"Name": "Trevor Cox", "Email": "trevor.cox@company.com", "Phone": "+1-555-0151", "Salary": 142000},
    {"Name": "Kelly Howard", "Email": "kelly.howard@company.com", "Phone": "+1-555-0152", "Salary": 151000},
    {"Name": "Marcus Ward", "Email": "marcus.ward@company.com", "Phone": "+1-555-0153", "Salary": 138000},
    {"Name": "Jasmine Torres", "Email": "jasmine.torres@company.com", "Phone": "+1-555-0154", "Salary": 156000},
    {"Name": "Lucas Peterson", "Email": "lucas.peterson@company.com", "Phone": "+1-555-0155", "Salary": 143000},
    {"Name": "Monica Gray", "Email": "monica.gray@company.com", "Phone": "+1-555-0156", "Salary": 150000},
    {"Name": "Caleb Ramirez", "Email": "caleb.ramirez@company.com", "Phone": "+1-555-0157", "Salary": 136000},
    {"Name": "Sierra James", "Email": "sierra.james@company.com", "Phone": "+1-555-0158", "Salary": 157000},
    {"Name": "Hunter Watson", "Email": "hunter.watson@company.com", "Phone": "+1-555-0159", "Salary": 144000},
    {"Name": "Destiny Brooks", "Email": "destiny.brooks@company.com", "Phone": "+1-555-0160", "Salary": 152000},
    {"Name": "Ian Kelly", "Email": "ian.kelly@company.com", "Phone": "+1-555-0161", "Salary": 139000},
    {"Name": "Paige Sanders", "Email": "paige.sanders@company.com", "Phone": "+1-555-0162", "Salary": 154000},
    {"Name": "Blake Price", "Email": "blake.price@company.com", "Phone": "+1-555-0163", "Salary": 147000},
    {"Name": "Jenna Bennett", "Email": "jenna.bennett@company.com", "Phone": "+1-555-0164", "Salary": 145000},
    {"Name": "Mason Wood", "Email": "mason.wood@company.com", "Phone": "+1-555-0165", "Salary": 134000},
    {"Name": "Gabrielle Barnes", "Email": "gabrielle.barnes@company.com", "Phone": "+1-555-0166", "Salary": 158000},
    {"Name": "Cole Ross", "Email": "cole.ross@company.com", "Phone": "+1-555-0167", "Salary": 141000},
    {"Name": "Mariah Henderson", "Email": "mariah.henderson@company.com", "Phone": "+1-555-0168", "Salary": 149000},
    {"Name": "Garrett Coleman", "Email": "garrett.coleman@company.com", "Phone": "+1-555-0169", "Salary": 137000},
    {"Name": "Natalie Jenkins", "Email": "natalie.jenkins@company.com", "Phone": "+1-555-0170", "Salary": 155000},
    {"Name": "Devin Perry", "Email": "devin.perry@company.com", "Phone": "+1-555-0171", "Salary": 143000},
    {"Name": "Cassandra Powell", "Email": "cassandra.powell@company.com", "Phone": "+1-555-0172", "Salary": 151000},
    {"Name": "Jared Long", "Email": "jared.long@company.com", "Phone": "+1-555-0173", "Salary": 138000},
    {"Name": "Sabrina Patterson", "Email": "sabrina.patterson@company.com", "Phone": "+1-555-0174", "Salary": 156000},
    {"Name": "Cameron Hughes", "Email": "cameron.hughes@company.com", "Phone": "+1-555-0175", "Salary": 142000},
    {"Name": "Kimberly Flores", "Email": "kimberly.flores@company.com", "Phone": "+1-555-0176", "Salary": 148000},
    {"Name": "Austin Washington", "Email": "austin.washington@company.com", "Phone": "+1-555-0177", "Salary": 135000},
    {"Name": "Brianna Butler", "Email": "brianna.butler@company.com", "Phone": "+1-555-0178", "Salary": 153000},
    {"Name": "Colton Simmons", "Email": "colton.simmons@company.com", "Phone": "+1-555-0179", "Salary": 140000},
    {"Name": "Haley Foster", "Email": "haley.foster@company.com", "Phone": "+1-555-0180", "Salary": 147000},
    {"Name": "Seth Gonzales", "Email": "seth.gonzales@company.com", "Phone": "+1-555-0181", "Salary": 136000},
    {"Name": "Cheyenne Bryant", "Email": "cheyenne.bryant@company.com", "Phone": "+1-555-0182", "Salary": 154000},
    {"Name": "Tristan Alexander", "Email": "tristan.alexander@company.com", "Phone": "+1-555-0183", "Salary": 144000},
    {"Name": "Shelby Russell", "Email": "shelby.russell@company.com", "Phone": "+1-555-0184", "Salary": 150000},
    {"Name": "Dalton Griffin", "Email": "dalton.griffin@company.com", "Phone": "+1-555-0185", "Salary": 139000},
    {"Name": "Mackenzie Diaz", "Email": "mackenzie.diaz@company.com", "Phone": "+1-555-0186", "Salary": 157000},
    {"Name": "Bryce Hayes", "Email": "bryce.hayes@company.com", "Phone": "+1-555-0187", "Salary": 145000},
    {"Name": "Katelyn Myers", "Email": "katelyn.myers@company.com", "Phone": "+1-555-0188", "Salary": 152000},
    {"Name": "Wyatt Ford", "Email": "wyatt.ford@company.com", "Phone": "+1-555-0189", "Salary": 141000},
    {"Name": "Allison Hamilton", "Email": "allison.hamilton@company.com", "Phone": "+1-555-0190", "Salary": 148000},
    {"Name": "Brayden Graham", "Email": "brayden.graham@company.com", "Phone": "+1-555-0191", "Salary": 137000},
    {"Name": "Jocelyn Sullivan", "Email": "jocelyn.sullivan@company.com", "Phone": "+1-555-0192", "Salary": 155000},
    {"Name": "Landon Wallace", "Email": "landon.wallace@company.com", "Phone": "+1-555-0193", "Salary": 143000},
    {"Name": "Mikayla Woods", "Email": "mikayla.woods@company.com", "Phone": "+1-555-0194", "Salary": 149000},
    {"Name": "Carson Cole", "Email": "carson.cole@company.com", "Phone": "+1-555-0195", "Salary": 138000},
    {"Name": "Jordyn West", "Email": "jordyn.west@company.com", "Phone": "+1-555-0196", "Salary": 156000},
    {"Name": "Hayden Jordan", "Email": "hayden.jordan@company.com", "Phone": "+1-555-0197", "Salary": 144000},
    {"Name": "Ariana Owens", "Email": "ariana.owens@company.com", "Phone": "+1-555-0198", "Salary": 151000},
    {"Name": "Parker Reynolds", "Email": "parker.reynolds@company.com", "Phone": "+1-555-0199", "Salary": 140000},
    {"Name": "Skylar Fisher", "Email": "skylar.fisher@company.com", "Phone": "+1-555-0200", "Salary": 146000}
]

# Create DataFrame
df = pd.DataFrame(employees)

# Save to Excel
df.to_excel('employees.xlsx', index=False)

# Get top 5 highest salary employees
top_5 = df.nlargest(5, 'Salary')

# Create pie chart
plt.figure(figsize=(10, 8))
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
plt.pie(top_5['Salary'], labels=top_5['Name'], autopct='%1.1f%%', startangle=90, colors=colors)
plt.title('Top 5 Highest Salary Employees', fontsize=16, fontweight='bold')
plt.axis('equal')
plt.tight_layout()
plt.savefig('top_5_salaries_pie_chart.png', dpi=300, bbox_inches='tight')
plt.show()

print("Excel file 'employees.xlsx' created successfully!")
print("Pie chart saved as 'top_5_salaries_pie_chart.png'")
print("\nTop 5 Highest Salary Employees:")
for i, row in top_5.iterrows():
    print(f"{row['Name']}: Rs.{row['Salary']:,}")