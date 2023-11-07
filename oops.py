#class
# class java:
#     a = 10
# #object
# class html(java):
#     b = 20
# obj = html
# print(obj.a)
# print(obj.b)

# #inhertance
#single inhertance
# class python:
#     c = 10
# class html(python):
#     d = 200
# obj = html
# print(obj.c)
# print(obj.d)    

#multilevel inhertance
# class html:
#     a = 100
# class java(html):
#     b = 200
# class css(java):
#     c = 300
# obj = css
# print(obj.a)
# print(obj.b)
# print(obj.c)

#muliple inhertance
# class java:
#     a = 200
# class html:
#     b = 300
# class css(java , html):
#     c = 300
# obj = css
# print(obj.a)
# print(obj.b)
# print(obj.c)


#polymorephism
class java:
    a = 10
class html(java):
    a = 20
class css(html):
    a = 30
obj1 = java()
obj2 = html()
obj3 = css()

print(obj1.a)
print(obj2.a)
print(obj3.a)