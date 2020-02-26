ssq = 0
suma = 0
for i in range(0, 101):
  suma += i
  ssq += i*i
suma = suma*suma
print(suma-ssq)