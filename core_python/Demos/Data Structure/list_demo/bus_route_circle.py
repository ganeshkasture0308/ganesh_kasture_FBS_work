location=['s1','s2','s3','s4','s5','s6']
distance=[1000,2500,3400,4800,2200,6200]
price=5
source=input("enter the starting point source:")
destination=input("enter the destination:")

i_src=location.index(source)
i_dest=location.index(destination)

i=i_src
total_dist=0
while(i!=i_dest):
    total_dist=total_dist+distance[i]
    if(i==len(location)-1):
        i=0
    else:
        i=i+1
print(total_dist)
tic_price=(total_dist/1000)*5
print(tic_price)