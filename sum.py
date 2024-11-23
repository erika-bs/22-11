def sum(n):
     if n <= 0:
          raise ValueError("O valor de n deve ser um inteiro positivo")
     if n ==1:
          return 1
     else:
          return n + sum(n-1)

n = 5
result = sum(n)
print(f"O somatório de 1 até {n} é {result}")