count = 6
num = 17
prime = [2, 3, 5, 7, 11, 13]

while(count < 10001):
    for i in range(len(prime)):
        if(num%prime[i] == 0):
            break
        if(num%prime[i] != 0 and i == count - 1):
            prime.append(num)
            count = count + 1
    num = num + 2
print(prime[10000])