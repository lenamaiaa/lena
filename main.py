students = []
while True:
   print("please input your choise")
   print("1- add students ")
   print("2- print students")
   print("3- exit")
   choice = input()
   if choice == "1":
       std = input("please input new student name\n")
       students .append(std)
   elif choice == "2" :
        print(students)
   elif choice =="3":
       print("your index range from 0 to " + str(len(students) - 1))
       index = int(input("please input student index \n"))
       print(students[index])
   elif choice == "4":
       break
   else:
       print("invalid input")
       continue
   print("thanks")



