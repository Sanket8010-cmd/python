def sel(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(min_index, n):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

no_student = int(input("Enter the number of students: "))
mark = []

for student_mark in range(no_student):
    student_mark_value = float(input(f"Enter the mark of student {student_mark + 1}: "))
    mark.append(student_mark_value)

sel(mark)

print("Sorted Marks:", mark)

top_5 = mark[-5:]  # last 5 elements (top 5 highest since list is sorted in ascending order)
top_5.reverse()

print(f"Top 5 student marks are: {top_5}")
