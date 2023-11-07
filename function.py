#parameter 

def python(a):
    print(a)
python(10)
python(20)
#non parameter
def python():
    a = 10
    b =20
    print(a + b)
python()

#lambda

x = lambda a,b,c,d : a + b + c + d
print(x(10,20,30,40))