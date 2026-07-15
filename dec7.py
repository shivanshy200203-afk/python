# Access ‘history’ Key From a Nested Dictionary
student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}

history_grades = student["grades"]["history"] 

print("history_grades",history_grades)