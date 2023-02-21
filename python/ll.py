class create:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class op:
    def __init__(self,head=None):
        self.head=head

    def insert_end(self,data):
        new=create(data)
        if(self.head):
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=new
        else:
            self.head=new
    
    def display(self):
        if(self.head):
            temp=self.head
            while(temp!=None):
                print(temp.data)
                temp=temp.next
        else:
            print("empty")
    def insert_front(self,data):
        new=create(data)
        new.next=self.head
        self.head=new
    def delete(self,dell):
        if(self.head):
            temp1=self.head
            while(temp1.data!=dell and temp1.next!=None):
                temp2=temp1
                temp1=temp1.next
            if(temp1.data==dell and temp1!=self.head):
                print("data deleted is "+str(temp1.data))
                temp2.next=temp1.next
                temp1=None
            elif(temp1==self.head):
                print("data deleted is "+str(temp1.data))
                self.head=temp1.next
                temp1=None
            else:
                print("Data not found")  
        else:
            print("Linked list empty")

ob1=op()
ob1.insert_end(10)
ob1.insert_end(20)
ob1.insert_end(19)
ob1.insert_front(21)
ob1.insert_front(11)
ob1.display()
ob1.insert_end(22)
ob1.display()
ob1.delete(19)
ob1.display()
ob1.delete(33)
ob1.display()
ob1.delete(11)
ob1.display()
ob1.delete(22)
ob1.display()




           


