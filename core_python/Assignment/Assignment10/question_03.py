
numbers = [10, 25, 7, 99, 45]
if numbers[0] > numbers[1]:
    first = numbers[0]
    second = numbers[1]
else:
    first = numbers[1]
    second = numbers[0]

for i in range(2, len(numbers)):
    if numbers[i] > first:
        second = first
        first = numbers[i]
    elif numbers[i] > second and numbers[i] != first:
        second = numbers[i]
print("Second largest element:", second)
