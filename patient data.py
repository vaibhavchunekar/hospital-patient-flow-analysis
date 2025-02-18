# Read the patient data
print("Welcome to Patient Data System")
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Establish a connection to the database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Idian123#",
    database="hospital"
)

# Check if the connection was successful
if connection.is_connected():
    print("Connected to the database")

# Create a cursor object using the con
# nection
cursor = connection.cursor()

# Define the query
query = "SELECT * FROM hospital_data"

# Execute the query
cursor.execute(query)

# Fetch all rows from the result of the query
data = cursor.fetchall()

# Print the data
for row in data:
    print(row)

# Load data into a pandas DataFrame
data_frame = pd.read_sql(query, connection)

# Print the DataFrame
print(data_frame)

# Summary statistics
print(data_frame.describe())

# Select specific columns
patient_injury_deposit = data_frame[['Type_of_Admission', 'Admission_Deposit']]
print(patient_injury_deposit)

# Visualize arrival times
sns.histplot(data_frame['Type_of_Admission'], bins=24, kde=False, color='blue')
plt.title('Patient in Hospital')
plt.xlabel('Type_of_Admission')
plt.ylabel('Admission_Deposit')
plt.show()

# Boxplot of wait times by department
sns.boxplot(x='Type_of_Admission', y='Admission_Deposit', data=patient_injury_deposit)
plt.title('Patient Information')
plt.xlabel('Type_of_Admission')
plt.ylabel('Admission_Deposit')
plt.show()

# Close the cursor and connection
cursor.close()
connection.close()
