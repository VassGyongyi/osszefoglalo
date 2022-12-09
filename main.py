import random
def program():
    szam = int(input('Adj meg egy számot:'))
    while not (szam >= 5 and szam <= 30):
        szam = int(input('Hiba! Adj meg egy számot 5 és 30 között: '))
    kereszt_nev = input('Adj meg egy keresztnevet: ')
    nev = input('Adj meg egy vezetéknevet és keresztnevet szóközzel elválasztva: ')+" "
    i = 0
    nev_seged = ""
    while nev[i] != " ":
        nev_seged += nev[i]
        i +=1
    print(nev_seged)

    szo = input('Adj meg egy minimum 3 betűs szót: ')
    while not(len(szo) > 2):
        szo = input('Adj meg egy minimum 3 betűs szót: ')
    k = len(szo)
    if ord(szo[0]) == ord(szo[k-1]) or ord(szo[k-1])-32 == ord(szo[0]):
        print('Egyforma a megadott szó első és utolsó betűje.')
    else:
        print('Nem egyforma az első és az utolsó betű.')
    if (ord(szo[0])> 64 and ord(szo[0] )< 92):
        print('Nagybetűvel kezdődik.')
    else:
        print('Nem nagybetűvel kezdődik')

    print('véletlen szám -5-15 között:')
    #print(int(random.randrange(-5, 15)))
    print(int(random.random()*20)-5)

    l = 1
    ot_vel = ""
    while(l < 6):
       vel = (int(random.random() * 20) - 5)
       if l < 5:
           ot_vel += str(vel) + ","
       else:
           ot_vel += str(vel)
       l += 1
    print(f'Öt db véletlen szám -5-15 között: {ot_vel}')
# 14.feladat
    lista = ['a', 3,'b', -5, 'c', 7]
    m = 0
    index = 1
    while (m < len(lista)-1):
        print(f'{lista[m]}. {index}. elem: {lista[m+1]}')
        m += 2
        index += 1

# 16. feladat
    n = 0
    velLista = []
    while(n < 5):
        velLista.append(int(random.random()*10)+5)
        n += 1
    print(f'Generált lista: {velLista}')
    oszto = velLista[4]
    print("17. feladat: %10.2f" % (szam/oszto))

# 18. feladat:
    oszt = lista[1]/velLista[2]
    print("18. feladat: %10.4f" % oszt)

# 19-21. feladat:
    p = 0
    osszeg= 0
    db_harom = 0
    while(p < len(velLista)):
        osszeg += velLista[p]
        if velLista[p] % 3 == 0:
            db_harom += 1
        p +=1
    atlag = osszeg/len(velLista)
    print(f'A lgenerált lista elemeinek összege: {osszeg}')
    print(f'A lista átlaga: {atlag}')
    print(f'{db_harom} db hárommal osztható szám van benne.')

# 22. feladat:
    legkisebb = 15
    legkisebb_index = 0
    legnagyobb = 0
    legnagyobb_index = 0
    q = 0
    while(q < len(velLista)):
        if (velLista[q] < legkisebb):
            legkisebb = velLista[q]
            legkisebb_index = q+1
        if (velLista[q] > legnagyobb):
            legnagyobb =velLista[q]
            legnagyobb_index = q+1
        q +=1
    print(f'Legkisebb a {legkisebb_index}. elem: {legkisebb}')
    print(f'Legnagyobb elem: a {legnagyobb_index}. elem: {legnagyobb}')

# 23. feladat:

    r = 0
    tizenharom = 0
    while(r < len(velLista) and tizenharom != 13):
        if velLista[r] == 13:
            tizenharom = 13
        r += 1
    if tizenharom == 13:
        print('Van közte 13-as.')
    else:
        print('Nincs közte 13-as.')

# 24. feladat:
    s = 0
    nagyobb = 11
    while( s < len(velLista) and nagyobb > 10):
        nagyobb = velLista[s]
        s += 1
    if nagyobb > 10:
        print('Minden eleme nagyobb, mint 10.')
    else:
        print('Nem minden eleme nagyobb, mint 10.')

program()
