amt=int(input("enter the amount:"))

if(amt>0):
    if(amt>50):
        if(amt>100):
            print("Amount is greater than 100.")
        
        else:
            print("Amount is greater than 50 but less than 100.")

    else:
        print("Amount is greater than 0 but less than 50.")
else:
    print("Amount is less than 0.")


