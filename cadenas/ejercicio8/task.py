pre= input("Introduce el precio del producto con dos decimales:")
print(pre[:pre.find(".")], "colones y", pre[pre.find(".")+1:], "céntimos.")