def main():

    lst = []
    while(1):
        print("1: Append, 2:Display, 3: Remove, 4: Exit")
        choice = int(input())
        if choice==1:
            num = int(input("Enter number: "))
            lst.append(num)
        elif choice==2:
            print(lst)
        elif choice==3:
            num = int(input("Enter number: "))
            lst.remove(num)
            print(lst)
        elif choice==4:
            break

if __name__=="__main__":
    main()
