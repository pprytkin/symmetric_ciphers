def encrypt(k, m):
    m = list(m)
    for i in range(len(m)):
        m[i] = ord(m[i]) + k
        m[i] = chr(m[i])
    m = "".join(m)
    print(m)

def decrypt(k, c):
    c = list(c)
    for i in range(len(c)):
        c[i] = ord(c[i]) - k
        c[i] = chr(c[i])
    c = "".join(c)
    print(c)

def decrypt_2(n):
    text = n
    symbol = list(set(text))
    max = 0
    sym = ''
    for i in range(len(symbol)):
        count = text.count(symbol[i])
        if count > max:
            max = count
            sym = symbol[i]
    k = ord(sym) - ord(' ')
    n = list(n)
    for i in range(len(n)):
        n[i] = ord(n[i]) - k
        n[i] = chr(n[i])
    n = "".join(n)
    print(n)

def encrypt_vij(k, m):
    while len(k)<len(m):
        k=k*2
    k = list(k)
    m = list(m)
    for i in range(len(m)):
        m[i] = ord(m[i]) + int(k[i])
        m[i] = chr(m[i])
    m = "".join(m)
    print(m)

def decrypt_vij(k, m):
    while len(k)<len(m):
        k=k*2
    k = list(k)
    m = list(m)
    for i in range(len(m)):
        m[i] = ord(m[i]) - int(k[i])
        m[i] = chr(m[i])
    m = "".join(m)
    print(m)



        
while True:
    cmd = input()

    if cmd == 'en':
        encrypt(int(input()), input())
    elif cmd == 'de':
        decrypt(int(input()), input())
    elif cmd == 'de2':
        decrypt_2(input())
    elif cmd == 'en_v':
        encrypt_vij(input(), input())
    elif cmd == 'de_v':
        decrypt_vij(input(), input())
