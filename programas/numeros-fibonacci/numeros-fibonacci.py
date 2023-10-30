def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    
    elem_1 = elem_2 = 1
    soma = 0

    for i in range(3, n+1):
        soma = elem_1 + elem_2
        elem_1, elem_2 = elem_2, soma
    
    return soma

for n in range(1, 10):
    print(n, '->', fib(n))