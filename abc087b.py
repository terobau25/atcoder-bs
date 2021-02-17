a=int(input())
b=int(input())
c=int(input())
x=int(input())
num_com=0
for n_500 in range(0,a+1):
    for n_100 in range(0,b+1):
       for n_50 in range(0,c+1):
           if n_500*500+n_100*100+n_50*50==x:
               num_com+=1
print(num_com)

