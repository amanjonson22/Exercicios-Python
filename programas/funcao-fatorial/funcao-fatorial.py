def funcao_fatorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    return n * funcao_fatorial(n - 1)

for n in range(1, 6):
    print(n, funcao_fatorial(n))