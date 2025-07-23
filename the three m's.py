import random
def mean(x):
    num = 0
    for i in x:
        num += i
    
    return num / len(x)
    
def median(x):
    y = x[:]
    y.sort()
    a = y[round(len(y) / 2)]
    if len(x) % 2 == 0:
        a += y[round(len(y) / 2) + 1]
        a /= 2
    
    return a
    
def mode(x):
    a = {}
    b = []
    for i in x:
        if i not in a:
            a[i] = 0
        d = a[i]

        d = d + 1
        
        a[i] = d
    for key in a:
        b.append(a[key])
    b.sort()
    b.reverse()
    for key in a:
        if a[key] == b[0]:
            
            return key
    
    

x = [random.randint(0, 100) for _ in range(50)]
z = x[:]


print("Mean: ")
print(mean(x))
x = z
print("Median: ")
print(median(x))
x = z
print("Mode: ")
print(mode(x))
x = z
print(x)
