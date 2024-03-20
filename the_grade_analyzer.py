'''3. The Grade Analyzer'''

student_grades = [85, 92, 78, 88, 95]

#Task 1: Code a function to calculate the average grade.
def average_grade(grade_list):
    average =sum(grade_list)//len(grade_list)
    return average

#Task 2: Implement a function to find the highest and lowest grade.
def high_low (grade_list):
    high = max(grade_list)
    low = min(grade_list)
    return high, low 

#Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).
def letter_grade(grade_list):
    for i in range(len(grade_list)):
        if grade_list[i] >= 90:
            print(f"{grade_list[i]} is an A")
        elif grade_list[i] >= 80:
            print(f"{grade_list[i]} is a B")
        elif grade_list[i] >= 70:
            print(f"{grade_list[i]} is a C")
        elif grade_list[i] >= 60:
            print(f"{grade_list[i]} is a D")
        else:
            print(f"{grade_list[i]} is a F")

#Test 
#print(average_grade(student_grades))
#print(high_low(student_grades))
#print(letter_grade(student_grades))