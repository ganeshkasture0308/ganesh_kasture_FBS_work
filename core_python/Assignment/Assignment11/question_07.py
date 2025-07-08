a = list(map(int, input("Enter elements of first list separated by space: ").split()))
b = list(map(int, input("Enter elements of second list separated by space: ").split()))
intersection = list(set(a) & set(b))
print("Intersection of lists:", intersection)
