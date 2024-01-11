print("This calculator measures weighted GPA for multiple semesters.")
print("It assumes that the semesters are weighted equally.")
print("")

# sem represents the semesters you want to calculate for
sem = int(input("How many semesters do you want to calculate for? "))
c = int(input("How many classes do you have in each semester? "))

# Initialize empty variables
semester_GPAs = 0
letterGradesTotal = None

# Function to make sure loop does not keep asking letter grades when not needed
def checkExitCondition():
    letterGradesTotal = A + B + C + D + F
    if letterGradesTotal == c:
        return True
    else:
        return False

# Loop through each semester
for semester in range(1, sem + 1):
    print("Semester " + str(semester) + ":")
    
    A = B = C = D = F = 0
    letterGradesTotal = A + B + C + D + F

    while True:
        A = int(input("Total number of A's: "))
        if checkExitCondition() == True:
            break
        B = int(input("Total number of B's: "))
        if checkExitCondition() == True:
            break
        C = int(input("Total number of C's: "))
        if checkExitCondition() == True:
            break
        D = int(input("Total number of D's: "))
        if checkExitCondition() == True:
            break
        F = int(input("Total number of F's: "))
        letterGradesTotal = A + B + C + D + F
        if letterGradesTotal != c:
            print("Oops! The amount of letter grades doesn't match the number of classes.")
            exit()

    # Check if the total number of letter grades matches the total number of classes

    semester_GPA = (A * 4 + B * 3 + C * 2 + D * 1 + F * 0) / c
    semester_GPAs = semester_GPAs + semester_GPA

    print("GPA for Semester " + str(semester) + ": " + str(round(semester_GPA, 3)))
    print("")

cumulative_GPA = semester_GPAs / sem
print("Cumulative GPA for " + str(sem) + " semesters: " + str(round(cumulative_GPA, 3)))

