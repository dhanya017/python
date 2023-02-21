  
a=[]
top=-1
n=int(input("Enter size of array:"))
ab=1
while (ab!=0):
    print("choice\n1.push\n2.pop\n3.display\n")
    ch=int(input("enter choice:"))
    if(ch==1):
        b=int(input("Enter value to be pushed:"))
        if(top<n):
            a.append(b)
            top=top+1
        else:
            print("Stack is full")
    elif(ch==2):
        c=int(input("Enter value to be poped:"))
        if(top==-1):
            print("Stack empty")
        else:
            a.remove(c)
            top=top-1
            print("deleted item "+str(c))
    elif(ch==3):
        if(top==-1):
            print("Stack is empty")
        else:
            print(a)
    else:
        print("Invalid choice")
    ab=int(input("Do you want to continue(0/1):"))




