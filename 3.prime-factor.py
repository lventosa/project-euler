def largestPrimeFactor(num, d = 2):
  while d < num:
    if num%d == 0:
      num = num / d
      d = 2
    else:
      d = d + 1
  return num

print(largestPrimeFactor(600851475143)) 
