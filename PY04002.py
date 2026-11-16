class Rectangle:
    def __init__(self, x,y, color):
        self.x = x
        self.y = y
        self.c = color
    def perimeter(self):
        return (self.x + self.y) * 2
    def area(self):
        return self.x * self.y
    def color(self):
        res = str(self.c).capitalize()
        return res

arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print('INVALID')