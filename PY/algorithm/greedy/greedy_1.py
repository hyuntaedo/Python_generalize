n = 1260
count = 0
array = [500,400,50,10]

for coin in array:
    count += n // coin
    n %= coin

print(count)
    
