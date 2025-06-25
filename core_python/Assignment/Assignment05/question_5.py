# 5. Write a program to accept an integer amount from user and tell minimum  
# number of notes needed for representing that amount. (Use looping to optimize  
# the problem) 
amount = int(input("Enter the amount: "))
notes = [2000, 500, 200, 100, 50, 20, 10]
note_count = {}
for note in notes:
    if amount >= note:
        count = amount // note         
        amount = amount % note         
        note_count[note] = count       
print("Minimum number of notes:")
for note in note_count:
    print(f"{note} x {note_count[note]}")
