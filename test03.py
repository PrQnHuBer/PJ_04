#fuction 3 No parameter / Have return
#ถ้าReturn มากกว่าหนึ่ง ให้สร้างตัวแปรมาเก็บค่าก่อน
def funcA():
    print ('a')
    print ('b')
    print ('c')
    return "abc"
def funcB():
    return 999,True,10+20
print(funcA())
a,b,c =funcB()
print(f'{a},{b},{c}')
