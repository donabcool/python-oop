
class getGradePoint:
#Initialize the variable
    def __init__(self,x):
        self.num = x
#
    def checkWeight(self,j):
            j=str(j).lower()
            if j == 'a':
                j = 5
            elif j == 'b':
                j = 4
            elif j == 'c':
                j = 3
            elif j == 'd':
                j = 2
            elif j == 'e':
                j = 1
            elif j == 'f':
                j = 0
            return j

    def multItems(self,a = 0):
        a = 0
        for i,j,k in self.num:
            a += self.checkWeight(j)*k
        return a

    def addDen(self, b = 0):
        b = 0
        for i,j,k in self.num:
            b += k
        return b

    def display(self,c = 0):
        print('CourseName : Grade : Credit Load')
        print('-'*30)
        for i,j,k in self.num:
            print(f'{i} : {j} : {k}')
        c = self.multItems() / self.addDen()
        print(f'CGPA : {c}')

howMany = int(input("How many courses?"))
data_list = []
for x in range(howMany):
    a = str(input(f'Name of course {x+1}?'))
    b = str(input('Grade?'))
    c = int(input('Credit load?'))
    data_list.append((a,b,c))
    print('-'*20)


p1 = getGradePoint(data_list)
p1.display()
