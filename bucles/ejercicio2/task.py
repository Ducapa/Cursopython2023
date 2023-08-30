num=int(input("Introduce un número entero positivo:"))
a=""
for i in range(1,num+2,2):
    a=a+str(i)+", "
print(a, end="")
