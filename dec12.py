'''"Salary" print karo.
"City" print karo.
Agar "City" na ho to "No City Found" print karo.
Department" print karo.
'''
employee = {
    "Name": "Rohan",
    "Salary": 50000,
    "Department": "IT"} 
employee["Salary"]
employee["City"] = "lucknow"
employee.get("City" , "No City Found")
print(employee)