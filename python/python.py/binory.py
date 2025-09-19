roll_numbers=[1,7,10,12,13,6,25,14,9,25,40,44,33,]
roll_numbers.sort()
def binary_search(roll_numbers, target):
    left = 0
    right = len(roll_numbers)-1
    while left <= right:
        mid = (left + right)//2
        if roll_numbers[mid]==target:
            return True
        elif roll_numbers[mid] < target:
            left = mid + 1
        else:
            right =mid-1
    return False
print("Roll no of the Student :",roll_numbers)
target_roll=int(input("inter roll no to check the attendence(1 to 50)  :  "))
if binary_search(roll_numbers, target_roll):
    print("Roll no",target_roll, " is attend the training program")
else:
    print("Roll no",target_roll, " is NOT attend the training program")