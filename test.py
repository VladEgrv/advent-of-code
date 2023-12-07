input = {1: [[75, 68, 35, 36, 86, 83, 30, 11, 14, 59], [86, 25, 63, 57, 59, 91, 68, 14, 72, 32, 36, 74, 66, 44, 30, 28, 11, 35, 75, 34, 55, 83, 69, 56, 38]]}
for key, value in input.items():
    counter = 0
    print(value[0])
    print(value[1])
    for i in value[1]:
        if i in value[0]:
            counter += 1

print(counter)
