
    

def a(a, a1):
    #adds two number of a and a1 together and return it
    a2 = a + a1
    if(a >= a1 or a <= a1 or a == a1):
        print(a2)
def aa(b, b1):
    #subtracts two number of b and b1 together and returns it 
    b2 = b - b1 
    if(b >= b1 or b <= b1 or b == b1):
        print(b2)
def aAa(c, c1):
    #multiples things together 
    c2 = c * c1 
    if(c >= c1 or c <= c1 or c == c1):
        print(c2)
def aaaa(d,d1):
    #divides d and d1
    return d/d1
def aaaaaAaaaa(f,f1):
    return "Jason messed this up"

while(True):
    print("1. add")
    print("2. subtract")
    print("3. multiply")

    b = int(input("Choose: "))
    if(b == 1):
        x = int(input("input: "))
        y = int(input("input: "))
        a(x,y)
    if(b == 2):
        x = int(input("input: "))
        y = int(input("input: "))
        aa(x,y)     
    if(b == 3):
        x = int(input("input: "))
        y = int(input("input: "))
        aAa(x,y)
    else:
        aaaaaAaaaa(a, a)
            

