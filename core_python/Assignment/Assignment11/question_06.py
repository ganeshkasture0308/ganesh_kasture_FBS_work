a = list(map(int, input("Enter elements of first list separated by space: ").split()))
b = list(map(int, input("Enter elements of second list separated by space: ").split()))
union = list(set(a + b))
print("Union of lists:", union)
