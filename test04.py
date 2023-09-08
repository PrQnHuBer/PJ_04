#functions 4 Have parameters / Have returns
def funcA(n1,n2):
    print(f'n1 is{n1}')
    print(f'n2 is{n2}')
    return n1+n2
def funcB(name,year):
    return f'สวัสดี {name}',2023-year
print(f'sum is{funcA(10,20)}')
A,B=funcB('สมชาย',2000)
print(f'{A} อายุ {B} ปี')