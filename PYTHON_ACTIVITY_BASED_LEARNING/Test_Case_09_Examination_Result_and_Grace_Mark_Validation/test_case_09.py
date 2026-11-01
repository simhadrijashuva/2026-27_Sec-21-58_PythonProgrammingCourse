# Case Study 9: Examination Result and Grace Marks
marks = []

for i in range(3):
    mark = int(input("Enter marks for subject " + str(i + 1) + ": "))
    marks.append(mark)

valid = True
for mark in marks:
    if mark < 0 or mark > 100:
        valid = False

if not valid:
    print("Invalid marks!")
else:
    failed_count = 0
    grace_index = -1

    for i in range(3):
        if marks[i] < 35:
            failed_count = failed_count + 1
            if marks[i] >= 30:
                grace_index = i

    if failed_count == 1 and grace_index != -1:
        grace = 35 - marks[grace_index]
        marks[grace_index] = 35
        print("Grace marks awarded:", grace)

    print("Final marks:", marks)

    passed = True
    for mark in marks:
        if mark < 35:
            passed = False

    if passed:
        print("RESULT: PASS")
    else:
        print("RESULT: FAIL")
