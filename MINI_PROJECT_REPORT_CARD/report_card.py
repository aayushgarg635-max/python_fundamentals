print("--STUDENT REPORT CARD--")

studentname = input("Enter the name: ")
studentrollno = input("Roll number: ")

subjects = ["Maths","physics","chemistry","English","Computer"]

engmarks = int(input("Enter the number: "))
phymarks = int(input("Enter the number: "))
compmarks = int(input("Enter the number: "))
mathmarks = int(input("Enter the number: "))
chemmarks = int(input("Enter the number: "))


Totalmarks = engmarks+phymarks+compmarks+mathmarks+chemmarks
print(Totalmarks) 

if(engmarks<33 or chemmarks<33 or phymarks<33 or mathmarks<33 or compmarks<33):
    print("FAIL,prepare for supllementary")

elif(Totalmarks>=450):
    print("you did great and got grade A")

elif(Totalmarks>=400):
    print("you did nice and got grade B")

elif(Totalmarks>=350):
    print("you did average and got grade C")

elif(Totalmarks>=300):
    print("you did below average and got grade D")

elif(Totalmarks>=200):
    print("you have just passed the examination")

elif(Totalmarks>=140):
    print(" you need much improvement better luck next time")

else:
    print("Failed")

percentage = Totalmarks/500 * 100
print(percentage)

print("Name:", studentname)
print("Roll Number:", studentrollno)

print("English:",engmarks)
print("Physics:",phymarks)
print("chemistry:",chemmarks)
print("Maths:",mathmarks)
print("computer:",compmarks)

print("percentage:",percentage,"%")
print("TotalMarks:",Totalmarks,"/500")





