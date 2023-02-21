a=[]
rear=-1
front=-1
n=int(input("Enter size of array:"))
ab=1
while (ab!=0):
    print("choice\n1.Enqueue\n2.Dequeue\n3.display\n")
    ch=int(input("enter choice:"))
    if(ch==1):
        b=int(input("Enter value to be Enqueued:"))
        if(front==-1):
            front=front+1
            rear=rear+1
            a.append(b)
        elif(rear<n-1):
            rear=rear+1
            a.append(b)
        else:
            print("QUEUE is full")
    elif(ch==2):
        if(front==-1):
            print("QUEUE empty")
        elif(rear==front):
            print("deleted item "+str(a[0]))
            del a[0]
            front=-1
            rear=-1   
        else:
            print("deleted item "+str(a[0]))
            del a[0]
            front=front+1    
    elif(ch==3):
        if(front==-1):
            print("QUEUE is empty")
        else:
            print(a)
    else:
        print("Invalid choice")
    ab=int(input("Do you want to continue(0/1):"))

