def space_search(tab, cut):
    trouve = True
    jump = 0
    print(tab)
    while cut > 0 and trouve:
        if tab[cut] == ' ':
            jump = cut
            trouve = False
        cut -= 1
    print(tab[0:cut+1])
    return jump

global x, y

def dict_slice(d):
    for x in d.values():
        #z = int(self.safezone_rect.width)
        #x = [i[j:j+z] for i in x for j in range(0, len(i), z)]
        for y in range(len(x)):
            list_slice(x, y)

def list_slice(x, y):
    if len(x[y]) > 30:
        z = 30
        tourne = True
        while z >= 0 and tourne:
            if x[y][z] == ' ':
                saut = z
                tourne = False
            z -= 1
        print(x[:saut])
        x[y] = x[:saut]
        print(x[saut+1:], y+1)
        x.insert(x[saut+1:], y+1)

d = {'a': ['Oh bah non Benjamin quand même pas!', 'feur feur feur ratio feur', 'ceci est un placeholder n y prêtez pas attention'],
     'b': ['Oh bah non Benjamin quand même pas!', 'feur feur feur ratio feur', 'ceci est un placeholder n y prêtez pas attention'],
     'c': ['Oh bah non Benjamin quand même pas!', 'feur feur feur ratio feur', 'ceci est un placeholder n y prêtez pas attention']}
print(dict_slice(d))

'''
t = ['smflkdmslfkmsldkfmlsdkfmlsdkfmlksdf', 'flksjdf', 'klsdfkj', 'a', 'fsdlkfjmlg,;c!:!§%mkgpqozkketmlsd,mlfk']
p = [i[j:j+7] for i in t for j in range(0, len(i), 7)]
m = ['Oh bah non Benjamin quand même pas!', 'feur feur feur ratio feur', 'ceci est un placeholder n y prêtez pas attention']
#n = [i[j:space_search(i, j+30)] for i in m for j in range(0, len(i), 30)]
n = [i.rsplit(' ') for i in m]
nmax = 30
o = [' '.join(i[j:space_search(' '.join(i), j+nmax)]) for i in n for j in range(0, len(i), nmax)]
print(o)
'''