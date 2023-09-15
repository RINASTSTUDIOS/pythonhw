def prime():
    num = int(input("Asal olup olmadığını öğrenmek istediğin sayıyı gir:"))
    num2 = num ** (1/2)
    list=[]
    list2=[]
    i = 2
    while i<= num2:
        if i == 2 or i == 3:list.append(i)
        elif i%2==0 or i%3==0:pass
        elif (i+2)%2==0 or (i+2)%3==0:pass
        else:list.append(i)
        i+=6
    for numb in list:
        if num%numb==0:list2.append(0)
        else:list2.append(1)
    if 0 in list2:
        return "Asal değil"
    else: return "Asal"
def root(num1:int,num2:int):
    return num1 ** (1/num2)
def factorial(num:int):
    x = 1
    for i in range(1,num+1):
        x*=i
    return x
def power(num1:int,num2:int):
    return num1**num2
def av(list):
    if len(list)==0:return 0
    toplam = 0
    for nums in list:
        toplam+=float(nums)
    
    return toplam/len(list)
def circle_area(radius:float,pi:float):
    if 3<float(pi)<3.14 or float(pi) >= 3.15 or float(pi)<3:
        return("Hatalı pi")
    else:
        return float(pi)*(float(radius)**2)
def circle_perimeter(radius:float,pi:float):
    if 3 < float(pi) <3.14 or float(pi) >= 3.15 or float(pi) < 3:
        return("Hatalı pi")
    else:
        return 2*float(radius)*float(pi)
def hipotenus(num:float,num2:float):
    x = float(num)**2
    y = float(num2)**2
    return (x+y)**(1/2)
sonuc = hipotenus(3,4)
print(sonuc)