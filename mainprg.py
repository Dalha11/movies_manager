from studentdbcode import StudentCode
from login import logincode
result = logincode()
if(result==False):
    exit()
object = StudentCode() 
print("---------------------------------------------")
print("          MOVIES INFORMATION            ")
print("---------------------------------------------")
while(True):
    print("      1. Add New Movie")
    print("      2. View")
    print("      3. Update")
    print("      4. Delete")
    print("      5. Search by Director")
    print("      6. Search by  number")
    print("      0. Exit")
    ch=int(input("             Enter choice : "))
    if ch==0:
        print("Thank you!!!")
        break
    elif ch==1:
        num = int(input("   Enter  num  : "))
        name=input("   Name : ")
        Director = input("   Director Name : ")
        Year = int(input("   Year : "))
        Genre = input("   Genre : ")
        Language = input(" Language : ")
        object.insert(num,name,Director,Year,Genre,Language)
    elif ch==2:
        object.select()
    elif ch==3:
        num=int(input("Enter  Number:"))
        result = object.selectbynum(num)
        if result==True:
            Director = input("Enter new Director : ")
            Year = int(input("Updated Year : "))
            object.update(num,director,year)
    elif ch==4:
        num=int(input("Enter Number:"))
        result = object.selectbynum(num)
        if result==True:            
            print("  1. Yes")
            print("  2. No")
            confirm = int(input("Are you sure to delete this data : "))            
            if confirm==1:
                object.delete(num)
            else:
                print("      delete cancelled")
    elif ch==5:
        director = input("director to search : ")
        object.selectbydirector(director)
    elif ch==6:
        num=int(input("Enter Number:"))
        object.selectbynum(num)
    else:
        print("Invalid Choice")
    print("\n\n")
    