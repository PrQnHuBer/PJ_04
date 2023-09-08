#Fucntion 2   Have parameters / No return
#ข้อมูลที่เก็บได้จากparmeterจะต้องมาจากการCall fucntion
def fucnA(x,y):
    print ("Hi")
    z = x + y
    print (f'{x}+{y}={z}')
def fucnB(x):
    print (f'x is {x} 555...')
fucnA (10,20) #arguments คือข้อมูลที่ส่งไปให้ parameters
fucnA (5,5)
fucnB ("SAU")