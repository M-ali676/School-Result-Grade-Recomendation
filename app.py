#student grading system

print("****** Student Grading System ************")
student_count=1
while student_count <= 5:
    print(f"************* Student {student_count}*********")
    # Input
    name = input("Your Full Name:")
    perc = eval(input("Percentage:"))   
    # if-elif-else - Grade   
    if perc >= 90:
        grade= "A+"
        remark = "Wonder Full"
    elif perc >=80:
        grade = "A"
        remark = "Good"
    elif perc >=70:
        grade = "B+"
        remark = "Fair"
    elif perc >= 60:
        grade = "B"
        remark = "Average"   
    elif perc >=50:
        grade = "C"
        remark = "Below Average"
    elif perc >=40:
        grade = "D"
        remark = "Just Passed"
    else:
        grade="F"
        remark = "Failed!"
        
    ##nested if - for extra comments based on marks   
    if perc >=75:
        if perc >=95:
            special = "Topper Student! and eligible for 100% scholarship"
        else:
            special = "Eligible for 50% scholarship"
    else:
        if perc >= 60:
            special = "work more, Efforts more!"
        else:
            special = "Practice Regularly"      
    ##NEst Loop, For for extra subject analysis
            
    print(f"\n Dear {name}, Your Subjects:")
    subjects = ["Maths","Science","English"]
    
    for subject in subjects:
        if subject == "Maths":
            sub_marks = perc+ 5 #extra marks for maths
        elif subject == "Science":
            sub_marks = perc - 2 #science 
        else:
            sub_marks = perc - 3 # english 
            
        # Nested if in for loop
        
        if sub_marks >100:
            sub_marks = 100
        elif sub_marks <0:
            sub_marks =0
            
        print(f"{subject} : {sub_marks}")
        
#final result print karna
        
    print(f"\n Result for {name} \nPercentage: {perc} \nGrade: {grade} \nRemarks: {remark} \nSpecial: {special}")
        
    student_count = student_count+1 #incrementing while loop