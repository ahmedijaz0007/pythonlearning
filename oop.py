class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for i in self.marks:
            sum = sum+i
        return sum/len(self.marks)




s1 = Student("Ali",[50,60,40])
print(s1.get_avg())

        