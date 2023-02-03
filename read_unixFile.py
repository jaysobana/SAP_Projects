var_key=[]
with open("key.txt", "r") as file:
    for y in file:
        var_key.append(y)
    print(var_key)
    col=int(var_key[0])
    row=int(var_key[1])
        
sec_list=[]
with open("secret.txt", "r") as file:
    for x in file:
        ##print(x)
        sec_list.append(x.strip())
        ##sec_list

##print(sec_list)    
z=0
with open("public.txt", "w") as file:
    for i in range(0,row):
        var_secret=""
        for j in range(0,col):
           ##print(i,j,sec_list[z])
           ##var_secret.append(str(sec_list[z]))
           var_secret=var_secret+str(sec_list[z])
           ##print(var_secret)
           z=z+1
           ##print("z:",z)
        print(var_secret)
        file.write(str(var_secret) + "\n")
        
