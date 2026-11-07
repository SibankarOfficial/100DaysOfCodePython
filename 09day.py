# dictionary = {"key":"value",
#               "language":"python",
#               "target":"data science"
# }



# #operation on dictionary

# empty_list = []

# empty_dictionary = {}



# dictionary["target"] = "Data Engineer"
# dictionary["job"] = "12 lpa job"


# for item in dictionary:
#     print(item)
#     print(dictionary[item])


# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores. 



# Write a program that converts their scores to grades.



# By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values. 



# The final version of the student_grades dictionary will be checked. 



# **DO NOT** modify lines 1-7 to change the existing student_scores dictionary. 



# This is the scoring criteria: 

# - Scores 91 - 100: Grade = "Outstanding" 

# - Scores 81 - 90: Grade = "Exceeds Expectations" 

# - Scores 71 - 80: Grade = "Acceptable" 

# - Scores 70 or lower: Grade = "Fail" 


# student_scores = {"raju": 67, "ruma": 86, "siba":76, "krisna":99}





# student_grades = {}

# for key in student_scores:
#     score = student_scores[key]
#     grade = ""

#     if score >= 90 and score <=100:
#         grade = "Outstanding"
#     elif score >=81 and score <= 90:
#         grade= "Exceeds Expectations"
#     elif score >=71 and score <= 80:
#         grade= "Acceptable"
#     elif score <= 70:
#         grade= "Fail"
#     else:
#         print("score out of 100 not allowed")

#     student_grades[key] = grade

# print(student_grades)["kolkata","delhi","mumbai"]

# travel_log = {
#     "west_bengal":{
#         "cities_visited":["kolkata","joypur","digha","haorah"],
#         "total_visit":34
#     },
#     "odisha":{
#         "cities_visited":["puri","konarok","udaygiri","chilkah"],
#         "total_visit":4
#     },
# }
# nested_list = ["a","b",["c","d"]]

# print(travel_log["west_bengal"]["cities_visited"][2])


### Blind auction program

print("Blind auction program")
def heighest_bidder(bid_dictionary):
    heighest_bid = 0
    heighest_bid_name = ""
    for key in bid_dictionary:
        if bid_dictionary[key] > heighest_bid:
            heighest_bid = bid_dictionary[key]
            heighest_bid_name = key
        

    print(heighest_bid,heighest_bid_name)
bid_dictionary = {}
other_bidder = True

while other_bidder: 
    name = input("what is your name?\n")
    bid = int(input("whats your bid? $"))
    bid_dictionary[name] = bid

    should_bid = input("are there any other bidders? type 'yes' or 'no'").lower()
    if should_bid == 'no':
        other_bidder = False
        heighest_bidder(bid_dictionary)
    elif should_bid == "yes":
         other_bidder = True
    else:
        print('please type yes or no')











