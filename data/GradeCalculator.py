import matplotlib.pyplot as plt

def student_grade(name): #OPTION 1
    s_id = None
    file = open("data/students.txt", "r")
    for each_line in file:
        id = each_line[:3].strip()    #reads ID number
        file_name = each_line[3:].strip() #reads rest which is student name
        if name == file_name: #compares inputted student name and what is in file
            s_id = id
            break #don't need to keep looking in students.txt
    file.close()

    if s_id is None: #if s_id was not equal to id this happens
        print("Student not found")
        return

#####find submissions
    submissions = []
    file = open("data/submissions.txt" , "r")
    for line in file:
        specific_id , assignment_id, percentage = line.split()
        if specific_id == s_id: #if they match then we store in submissions list
            submissions.append({
                "assignment_id": assignment_id,
                "percentage": float(percentage)

            })
    file.close()

#####find weights in assignments.txt
    weights = {}
    file = open("data/assignments.txt", "r")
    for line in file:
        each_q = line.split()
        assign_name = each_q[0]
        assign_id = each_q[1]
        assign_weight = int(each_q[2])

        weights[assign_id] = assign_weight #we can find the weight of an assignment by using assign_id as its key
    file.close()

#####find total points and percent
    total = 0
    max = 1000
    for submission in submissions:
        assignment_id = submission["assignment_id"]
        percentage = submission["percentage"]

        if assignment_id in weights:
            weight = weights[assignment_id]
            total += (percentage / 100) * weight
    grade_percentage = (total / max) * 100
    print(f"{name}'s grade: {round(grade_percentage)}%")

def assignment_stats(a_name): #OPTION 2
    finding_id = None
    file = open("data/assignments.txt", "r")
    for line in file:
        each_q = line.split()
        assign_name = each_q[0]
        if a_name == assign_name: #if what user gave matches name of assignment
            finding_id = each_q[1] #now we know that assignment's id
            break
    file.close()

    if finding_id is None: #doesn't exit after iterating
        print(f"Assignment {a_name} not found.")
        return
#####now we want all submissions for the specific assignment
    scoring = []
    file = open("data/submissions.txt" , "r")
    for line in file:
        specific_id , submission_assign_id, percentage = line.split()
        if submission_assign_id == finding_id: #if they match
            scoring.append(float(percentage)) #store percent for that assignment
    file.close()

    if not scoring: #0 matching id's added in list
        print(f"No submissions found for assignment {a_name}")
#####calculate max min and average
    else:
        min_score = min(scoring)
        max_score = max(scoring)
        average_score = sum(scoring) / len(scoring)

        print(f"Statistics for assignment {a_name}: ")
        print(f"Minimum score: {min_score}")
        print(f"Maximum score: {max_score}")
        print(f"Average score: {round(average_score, 2)}%")


def assignment_graph(assignment_name): #OPTION 3
    finding_id = None
    file = open("data/assignments.txt", "r")
    for line in file:
        each_q = line.split()
        assign_name = each_q[0]
        if assign_name == assignment_name:  # if what user gave matches name of assignment
            finding_id = each_q[1]  # now we know that assignment's id
            break
    file.close()

    if finding_id is None:
        print(f"Assignment {assignment_name} not found.")
        return
####take all scores for specific assignment
    scores = []
    file = open("data/submissions.txt" , "r")
    for line in file:
        specific_id, submission_assign_id, percentage = line.split()
        if submission_assign_id == finding_id: #if id asked for matches current iterating id
            scores.append(float(percentage)) #storing percent for specific assignment
    file.close()

    if not scores:
        print(f"No submissions found for assignment {assignment_name}.")
        return
#####CREATE HISTOGRAM!!
    plt.hist(scores, bins = [0,25,50,75,100], edgecolor = 'black')
    plt.title(f"Score Distribution for {assignment_name}")
    plt.xlabel("Scores Range")
    plt.ylabel("Number of Submissions")

    plt.xticks([12.5, 37.5, 62.5, 87.5], ['0-25', '50-75', '75-100'])

    plt.show()

def menu():
    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")

    ask = input("Enter your selection: ")

    if ask == "1":
        name = input("What is the student's name: ")
        student_grade(name)
    elif ask == "2":
        assignment_name = input("What is the assignment name: ")
        assignment_stats(assignment_name)
    elif ask == "3":
        assignment_name = input("What is the assignment name: ")
        assignment_graph(assignment_name)
    else:
        print("Invalid selection. Please choose 1, 2, or 3.")

