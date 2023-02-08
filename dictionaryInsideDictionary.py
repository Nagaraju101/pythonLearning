import pprint

employeee = { 'Robin': {'age': 25, 'salary': 35000},
               'Maryam':{'age': 25, 'salary': 50000, 'joindate': '22-Mar-2023'} ,
               'Jeff': {'age': 40, 'salary': 75000} , 
               'Mac': {'height': 6.1, 'projects': {'project1': 'ETL', 'project2': 'Big Data', 'project3': 'Pyspark'}}
            }     

print(employeee['Robin'])

pprint.pprint(employeee)