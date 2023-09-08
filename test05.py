#หาพื้นที่สีเหลี่ยมและสามเหลี่ยม รับกว้าง-ยาว /ฐาน-สูง
def inputWitdhlong():
    wi=float(input('ความกว้าง'))
    lo=float(input('ความยาว'))
    return wi,lo
def inputbasehigh():
    ba=float(input('ฐาน'))
    hi=float(input('ความสูง'))
    return ba,hi
def CalANDShowSquare(wi,lo):
    area = wi*lo
    print (f'สี่เหลี่ยมกว้าง {wi} ยาว {lo} มีพื้นที่ {area} ')
def CalANDShowTriangle(ba,hi):
    area = ba*hi /2
    print (f'สามเหลี่ยมฐาน {ba} สูง {hi} มีพื้นที่ {area}')
wi,lo =inputWitdhlong()
CalANDShowSquare(wi,lo)
print ('----------------------------------')
ba , hi = inputbasehigh()
CalANDShowTriangle(ba,hi) 