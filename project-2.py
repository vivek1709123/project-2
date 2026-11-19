print("welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("select an option")
    print("1.Generte a Pattern")
    print("2.Analyzer a Range of Numbers")
    print("3.Exit")

    choice =int(input("enter your choice:"))

    if choice<=0:
        print("Invaild your choice,Enter your vaild choice")
        continue


    elif choice == 1:

        x=int(input("enter your rows number:"))

        for i in range(1,x+1):
            for j in range(1,i+1):
                 print("*",end=" ")
            print()

    elif choice == 2:

        start=int(input("enter your start number of range :"))
        end=int(input("enter your end number of range :"))

        total_sum = 0
        for i in range(start,end+1):
            if i % 2 == 0:
                print(f"{i} is even")
            else:
                print(f"{i} is odd")
            total_sum +=i
        print(f"The sum of numbers from{start} to {end} is: {total_sum}")

    elif choice == 3:
        print("Exiting the program.Goodbye!")
        break


