class Queue:
    def __init__(self):
        self.data=[]
    def enqueue(self,data):
        self.data.append(data)
    def dequeue(self):
        self.data.pop(0)
    def print_Q(self):

        if len(self.data)==0:
            print("NOTHING IN QUEUE")
        else:
            print("OUT<-",end=" ")
            for i in range(len(self.data)):
                print(self.data[i],end="-")
            print("<-IN")
if __name__ == '__main__':
    queue = Queue()
    while 1:
        n=int(input("Enter\n1->To print Queue\n2->To enqueue a data to Queue\n3->To dequeue  data from start\n4 To exit\nEnter your input ::"))
        if n==1:
            queue.print_Q()
        elif n==2:
            data=int(input("Enter a value to add :"))
            queue.enqueue(data)
        elif n==3:
            queue.dequeue()
        elif n==4:
            print("Thanks!")
            quit()
        else :
            print("Enter a valid input(integer between (1,4) both inclusive)")
