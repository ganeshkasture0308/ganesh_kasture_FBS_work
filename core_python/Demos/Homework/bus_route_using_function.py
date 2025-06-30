loc=['S1','S2','S3','S4','S5','S6']
dist=[1000,2500,3400,4800,2200,6200]

price_peer_km=5

source=input("enter source station:")
distination=input("enter distination station:")

i_src=loc.index(source)
i_dest=loc.index(distination)

total_meters=0
i=i_src
while i!=i_dest:
    total_meters+=dist[i]
    i=(i+1)%len(loc)

total_km=total_meters/1000

ticket_price=total_km*price_peer_km

print(f'total distance from the {source} to {distination} is{total_km}km')

print(f'ticket price:rs {ticket_price}')