#1.pass
#used to neglect blank indentation error
# for i in range (1,6):
#     pass


# #2.break
# #used to stop iteration
# for i in range(1,6):
#     print(i)
#     if(i==3):
#         break

# #3.continue
# #used to stop specific iteration and continue to other iteration
# for i in range(1,6):
#     if (i==3):
#         continue
#     print(i)


#4.else
#this block will execute when loop execute successfully
for i in range(1,6):
    print(i)
    if(i==3):
        break

else:
    print("else block executed!!!!")
