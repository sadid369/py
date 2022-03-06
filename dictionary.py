# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# #TODO-1: Create an empty dictionary called student_grades.

# student_grades= {}
# #TODO-2: Write your code below to add the grades to student_grades.👇
# for name in student_scores:
#     print(name)
#     print(student_scores[name])
#     if student_scores[name] >=91 and student_scores[name]<=100:
#       student_grades[name] = "Outstanding"
#     elif student_scores[name] >=81 and student_scores[name] <=90:
#         student_grades[name] = "Exceeds Expectations"
#     elif student_scores[name] >=71 and student_scores[name] <=80:
#         student_grades[name] = "Acceptable"
#     elif student_scores[name] <=70:
#         student_grades[name] = "Fail"
# # 🚨 Don't change the code below 👇
# print(student_grades)

travel_log = [
    {
        "country":"France",
        "cities_visited":["Paris","Lille","Dijon"],
        "total_visits":12
     
     },
    {
        "country":"Germany",
        "cities_visited":["Berlin","Hamburg","Stuttgart"],
        "total_visits":5
     
     }
]
for key in travel_log:
    for key2 in key:
        for key3 in key2:
          print(key3)




