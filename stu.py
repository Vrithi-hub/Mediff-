class Student:
    # Constructor
    def __init__(self, name, rollno, age, gender):
        self.name = name
        self.rollno = rollno
        self.age = age
        self.gender= gender
         
    # Function to create and append new student   
    def insert(self, Name, Rollno, age, gender ):
        # use  ' int(input()) ' method to take input from user
        ob = Student(Name, Rollno, age, gender )
        ls.append(ob)
  
    # Function to display student details     
    def display(self, ob):
            print("Name   : ", ob.name)
            print("RollNo : ", ob.rollno)
            print("age : ", ob.age)
            print("gender : ", ob.gender)
            print("\n")    
         
    # Search Function    
    def search(self, rn):
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                return i       
  
    # Delete Function                                  
    def delete(self, rn):
        i = obj.search(rn)  
        del ls[i]
  
    # Update Function   
    def update(self, rn, No):
        i = obj.search(rn)
        roll = No
        ls[i].rollno = roll;
         
# Create a list to add Students
ls =[]
obj = Student('', 0, 0, '')
  
print("\nOperations used, ")
print("\n1.Accept Student details\n2.Display Student Details\n") 
print("3.Search Details of a Student\n4.Delete Details of Student")       
print("\n5.Update Student Details\n6.Exit")      
  
# ch = int(input("Enter choice:"))
# if(ch == 1):
obj.insert("A", 1, 100, "M")
obj.insert("B", 2, 90, "F")
obj.insert("C", 3, 80, "M")
         
# elif(ch == 2):
print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):    
    obj.display(ls[i])
             
# elif(ch == 3):
print("\n Student Found, ")
s = obj.search(2)
obj.display(ls[s])
         
# elif(ch == 4):
obj.delete(2)
print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):    
    obj.display(ls[i])
             
# elif(ch == 5):
obj.update(3, 2)
print(ls.__len__())
print("List after updation")
for i in range(ls.__len__()):    
    obj.display(ls[i])
             
# else:
print("Thank You !")
    