marks = int(input("Enter your marks: "))

if(marks<0):
    print("marks cannot be negative, please enter valid input")

elif(marks>=330):
    print("you can aim for IIT bomaby")

elif(marks<=330 and marks>=280):
    print("you can aim for IIT delhi")

elif(marks<=280 and marks>=240):
    print("you can aim for IIT madras")

elif(marks<=240 and marks>=200):
    print("you can aim for IIT kharagpur")

elif(marks<=200 and marks>=150):
  print ("you can aim for new IITS")

elif(marks<=150 and marks>=100):
   print("you canaim for some branches at IITs")

elif(marks<=100 and marks>=50):
    print("its very diificult to aim for any branch in IITs")

elif(marks<=50 and marks>=1):
    print("Be better prepared next time")

else:
    print("you got zero marks")

print("Thank you,and be pride of yourself because it takes courage to even give india's toughest exam")
