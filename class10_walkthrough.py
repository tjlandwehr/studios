# Walkthrough
# Write a GPA calculator program that takes grade data for a student and prints the resulting GPA. The output should look something like this:

# Your grade (0.0-4.0): 4
# # credits: 3
# Enter another grade? [y/n]: y
# Your grade (0.0-4.0): 4
# # credits: 2
# Enter another grade? [y/n]: n
# Your GPA is: 4.0
# We’ll need to use a while loop for the input portion of the program, and store the entered data in a list that contains dictionaries. Each item in the list should look something like:

# { 'grade': 3.0, 'credits': 3}
# To calculate the GPA you’ll need the idea of a quality score. A quality score is the number of credits for the class multiplied by the point score. For example, if you get a B (3.0) in a class worth 3 credits, the quality score is 9.0. The GPA for a student is the sum of the quality scores divided by the total number of credits.

# This will be written locally in a code editor, and run at the command line.

"""
A program to take grade input and calculate a student's GPA
"""

grades = []

continue_entry = True

# gather grade information
while continue_entry:
    grade = input("Your grade (0.0-4.0): ")
    credits = input("# credits: ")

    # store grades
    grades.append({'grade': float(grade), 'credits': int(credits)})

    user_wants_to_continue = input("Enter another grade? [y/n]: ")
    if user_wants_to_continue == 'n':
        continue_entry = False


# compute GPA
total_quality_score = 0
total_credits = 0

# calculate quality scores and total
for grade_info in grades:
    total_quality_score += (grade_info['grade'] * grade_info['credits'])
    total_credits += grade_info['credits']

gpa = total_quality_score / total_credits
print("Your GPA is:", gpa)