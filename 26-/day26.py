#list comprehension
#a way of creating new lists from a list
import random

# new_list = [new_item for item in list]
# conditional list comprehension
# new list = [new_item for item in list if test]

name = "Angela"
new_list = [letter for letter in name]

rangee = range(1,5)
new_range = [n * 2 for n in rangee]

print(new_range)

#Dictionary comprehension

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Freddie', 'Eleanor']

student_scores = {name:random.randint(1,101) for name in names}

print(student_scores)

passed_students = {name:score for (name,score ) in student_scores.items() if score>=60}

print(passed_students)


# iterate through pandas dict
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

for (key,value) in student_dict.items():
    print(value) #not useful as it just gives us names of column for key and all values in both columns for values

import pandas

student_data_frame = pandas.DataFrame(student_dict)

#iterrows()

for(index, row) in student_data_frame.iterrows():
    print(row.student)#gives all students
    #each row is a panda series dataframe


