def linear_search(rollno,target):
    
    for roll in rollno:
        if roll == target:
            return True
    return False

rollno =[1,7,10,12,13,6,25,14,9]

print("roll no of the student :",rollno)

target_roll=int(input("inter roll no to check the attendence  :  "))

if linear_search(rollno, target_roll):
    print("Roll no",target_roll, " is attend the training program")
    
else:
    print("Roll no",target_roll, " is  NOT  attend the training program")