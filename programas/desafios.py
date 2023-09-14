#C = int(input()) 
#for i in range (C): 
#    N = int(input())
#    if N >= 100 or N <= 1000000:
#        if N <= 8000:
#            print('Inseto')
#        else:
#            print('Mais de 8000!')

#T = int(input())

#for i in range(T):
#    N, K = input().split()
#    N = int(N)
#    K = int(K)
#    total = int(int(N % K) + int(N / K))

#    print(total)

a = input() 
b = input() 
c = input() 

if a == 'vertebrado': 
    if b == 'ave':
        
        if c == 'carnivoro':
            print('aguia')
        
        elif c == 'onivoro':
            print('pomba')
    
    elif b == 'mamifero':
        
        if c == 'onivoro':
            print('homem')
        
        elif c == 'herbivoro':
            print('vaca')

elif a == 'invertebrado':
    
    if b == 'inseto':
        
        if c == 'hematofago':
            print('pulga')
        
        elif c == 'herbivoro':
            print('lagarta')
        
    elif b == 'anelideo':

        if c == 'hematofago':
            print('sangessuga')
        
        elif c == 'onivoro':
            print('minhoca')