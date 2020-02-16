palindrome = []
n = []

for i in range(100, 999):
  for j in range(100, 999):
    n = str(i*j).split()[0]
    if n[0] == n[-1] and n[1] == n[-2] and n[2] == n[-3]:
      palindrome.append(i*j)

print(max(palindrome))