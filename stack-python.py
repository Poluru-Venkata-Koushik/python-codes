class stack:
    def __init__(self):
        self.data=[]

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return (len(self.data)==0)

    def push(self,add):
        self.data.append(add)

    def top(self):
        if self.is_empty():
            raise IndexError("Nothing is available in Stack")
        return self.data[-1]
    def pop_data(self):
        if self.is_empty():
            raise IndexError("Stack is Empty!")
        print("{} is popped".format(self.data[-1]))
        return self.data.pop()

    def print__(self):
        print("STACK:")
        if(self.data.__len__()==0):
            print("EMPTY STACK")
        for i in range(-1,(-(self.__len__()+1)),-1):
            print(self.data[i],sep="\n")

if __name__ == '__main__':
    Stack = stack()
    while 1:
        n=int(input("Enter\n1->To print stack\n2->To add a data to stack\n3->To pop data on top\n4 To exit\nEnter your input ::"))
        if n==1:
            Stack.print__()
        elif n==2:
            data=int(input("Enter a value to add :"))
            Stack.push(data)
        elif n==3:
            Stack.pop_data()
        elif n==4:
            print("Thanks!")
            quit()
        else :
            print("Enter a valid input(integer between (1,4) both inclusive)")
