n = 10 
 
n_1 = 0  
n_2 = 1  
count = 0  

while count < n:  
    print(n_1,end=' ')
    nth = n_1 + n_2 
    n_1 = n_2  
    n_2 = nth  
    count += 1  

print()
