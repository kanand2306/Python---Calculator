import math
import cmath
import statistics
import numpy as np
from Len_conv import *
from Sci_Const import *


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def squ(a):
    return a**2
def power(a,b):
    return a**b
def fac(a):
    x = lambda a : 1 if a <= 1 else a*x(a-1)
    return x(a)
def sqrt(a):
    return a**0.5
def ceil(a):
    return math.ceil(a)
def floor(a):
    return math.floor(a)
def log10(a):
    return math.log10(a)
def log2(a):
    return math.log2(a)
def exp(a):
    return math.exp(a)
def tenpow(a):
    return 10**a
def sin(a):
    return math.sin(a)
def cos(a):
    return math.cos(a)
def tan(a):
    return math.tan(a)
def degrees(a):
    return math.degrees(a)
def radian(a):
    return math.radians(a)
def hypt(a,b):
    return math.hypot(a,b)
def mean(lis):
    n=len(lis)
    s=sum(lis)
    return s/n
def median(lis):
    n=len(lis)
    lis.sort()
    if n%2==0:
        m1=lis[n//2]
        m2=lis[n//2-1]
        m=m1+m2
    else:
        m=lis[n//2]
    return m
def mode(lis):
    return statistics.mode(lis)
def var(lis):
    return np.var(lis)
def stdev(lis):
    return np.std(lis)
def discount(p,d):
    a=p-(p*d/100)
    return a
def gst(p,r):
    a=(p/100)*r
    return p+a
def si(p,r,t):
    return (p*r*t)/100
def ci(p,r,t):
    a=p*(pow((1+r/100),t))
    return a-p
def permutation(n,r):
    a=math.factorial(n)
    b=math.factorial(n-r)
    return a/b
def combination(n,r):
    a=math.factorial(n)
    b=math.factorial(r)*math.factorial(n-r)
    return a/b
def quad(a,b,c):
    d=(b**2)-(4*a*c)
    r1=(-b-cmath.sqrt(d))/(2*a)
    r2=(-b-cmath.sqrt(d))/(2*a)
    return [r1,r2]
def And(a,b):
    return a&b
def Or(a,b):
    return a|b
def Not(a):
    return ~a
def Xor(a,b):
    return a^b
def peri_sq(a):
    return 4*a
def peri_rect(a,b):
    return 2*(a+b)
def peri_trian(a,b,c):
    return a+b+c
def circum(a):
    return 2*math.pi*a
def area_sq(a):
    return a**2
def area_rect(a,b):
    return a*b
def area_cir(a):
    return math.pi*pow(a,2)
def area_tri(a,b,c):
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s*c))**0.5
    return area
def cel_to_fah(c):
    return (c*1.8)+32
def fah_to_cel(f):
    return (f-32)*0.56
def dec_to_bin(a):
    return bin(a)
def dec_to_oct(a):
    return oct(a)
def dec_to_hex(a):
    return hex(a)

print("\n********Scientific Calci***********")

cal=input("\nOperations:\n\n1  : ADD\n2  : SUB\n3  : MULTIPLY\n4  : DIVIDE\n5  : SQUARE\n6  : POWER\n7  : Factorial\n8  : SQUARE ROOT\n9  : CEIL\n10 : FLOOR\n11 : Log10\n12 : Log2\n13 : Exp\n14 : 10th Power\n15 : Sin\n16 : Cos\n17 : Tan\n18 : Degrees to Radian\n19 : Radian to Degree\n20 : Hypotenuse\n21 : Mean\n22 : Median\n23 : Mode\n24 : Variance\n25 : Standard Deviation\n26 : Discount\n27 : GST\n28 : SI\n29 : CI\n30 : Permutation\n31 : Combination\n32 : Quadratic Equation\n33 : AND\n34 : OR\n35 : NOT\n36 : XOR\n37 : Perimeter of Square\n38 : Perimeter of Rectangle\n39 : Perimeter of Traingle\n40 : Circumference of Circle\n41 : Areas of Square\n42 : Area of Rectangle\n43 : Area of Circle\n44 : Area of Traingle\n45 : Celsius to Fahrenheit\n46 : Fahrenheit to Celsius\n47 : Decimal to Binary\n48 : Decimal to Octal\n49 : Decimal to Hexadecimal\n50 : Length Conversion\n51 : Universal Constants\n52 : Solve Expression\n\nEnter your choice : ")

if cal=='1' or cal=='2' or cal=='3' or cal=='4' or cal=='6' or cal=='20' or cal=='26' or cal=='27' or cal=='30' or cal=='31' or cal=='33' or cal=='34' or cal=='36' or cal=='38' or cal=='42':
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
elif cal=='28' or cal=='29' or cal=='32' or cal=='39' or cal=='44':
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
    c=int(input("Enter 3rd number: "))
elif cal=='21' or cal=='22' or cal=='23' or cal=='24' or cal=='25':
    print("Enter the values separting by space: ")
    lis=[int(item) for item in input().split()]
elif cal=='50' or cal=='51':
    pass
elif cal=='52':
    s=input("Enter any expression: ")
else:
    a=int(input("Enter the number: "))



if cal=='1':
    print("\nOutput= ",add(a,b))

elif cal=='2':
    print("\nOutput= ",sub(a,b))

elif cal=='3':
    print("\nOutput= ",mul(a,b))

elif cal=='4':
    print("\nOutput= ",div(a,b))

elif cal=='5':
    print("\nOutput= ",squ(a))

elif cal=='6':
    print("\nOutput= ",power(a,b))

elif cal=='7':
    print("\nOutput= ",fac(a))

elif cal=='8':
    print("\nOutput= ",sqrt(a))

elif cal=='9':
    print("\nOutput= ",ceil(a))

elif cal=='10':
    print("\nOutput= ",floor(a))

elif cal=='11':
    print("\nOutput= ",log10(a))

elif cal=='12':
    print("\nOutput= ",log2(a))

elif cal=='13':
    print("\nOutput= ",exp(a))

elif cal=='14':
    print("\nOutput= ",tenpow(a))

elif cal=='15':
    print("\nOutput= ",sin(a))

elif cal=='16':
    print("\nOutput= ",cos(a))

elif cal=='17':
    print("\nOutput= ",tan(a))

elif cal=='18':
    print("\nOutput= ",degrees(a))

elif cal=='19':
    print("\nOutput= ",radian(a))

elif cal=='20':
    print("\nOutput= ",hypt(a,b))

elif cal=='21':
    print("\nOutput= ",mean(lis))

elif cal=='22':
    print("\nOutput= ",median(lis))

elif cal=='23':
    print("\nOutput= ",mode(lis))

elif cal=='24':
    print("\nOutput= ",var(lis))

elif cal=='25':
    print("\nOutput= ",stdev(lis))

elif cal=='26':
    print("\nOutput= ",discount(a,b))

elif cal=='27':
    print("\nOutput= ",gst(a,b))

elif cal=='28':
    print("\nOutput= ",si(a,b,c))

elif cal=='29':
    print("\nOutput= ",ci(a,b,c))

elif cal=='30':
    print("\nOutput= ",permutation(a,b))

elif cal=='31':
    print("\nOutput= ",combination(a,b))

elif cal=='32':
    print("\nOutput= ",quad(a,b,c))
    
elif cal=='33':
    print("\nOutput= ",And(a,b))

elif cal=='34':
    print("\nOutput= ",Or(a,b))

elif cal=='35':
    print("\nOutput= ",Not(a))

elif cal=='36':
    print("\nOutput= ",Xor(a,b))

elif cal=='37':
    print("\nOutput= ",peri_sq(a))

elif cal=='38':
    print("\nOutput= ",peri_rect(a,b))

elif cal=='39':
    print("\nOutput= ",peri_trian(a,b,c))

elif cal=='40':
    print("\nOutput= ",circum(a))

elif cal=='41':
    print("\nOutput= ",area_sq(a))

elif cal=='42':
    print("\nOutput= ",area_rect(a,b))

elif cal=='43':
    print("\nOutput= ",area_cir(a))

elif cal=='44':
    print("\nOutput= ",area_tri(a,b,c))

elif cal=='45':
    print("\nOutput= ",cel_to_fah(a))

elif cal=='46':
    print("\nOutput= ",fah_to_cel(a))

elif cal=='47':
    print("\nOutput= ",dec_to_bin(a))

elif cal=='48':
    print("\nOutput= ",dec_to_oct(a))

elif cal=='49':
    print("\nOutput= ",dec_to_hex(a))

elif cal=='50':
    length()

elif cal=='51':
    consts()

elif cal=='52':
    print("\nOutput= ",eval(s))

else:
    print("Wrong input")








    
