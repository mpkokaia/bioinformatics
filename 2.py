Pp = dict()
Pp['0'] = 0.5
Pp['1'] = 1. - Pp['0']
Pm = dict()
Pm['0'] = 0.9
Pm['1'] = 1. - Pm['0']
Psp = 0.5
Psm = 1. - Psp
Ppp = 0.5
Ppm = 1. - Ppp
Pmm = 0.5
Pmp = 1. - Pmm

emission = '0010101010100000000111010111'
result = ''

Ppc = Psp
Pmc = Psm

V = [[], []]

P = [[], []]

for el in emission:
    dpp = Ppc * Ppp * Pp[el]
    dmp =  Pmc * Pmp * Pp[el]
    if dpp < dmp:
        P[0].append(1)
        Ppc = dmp
    else:
        P[0].append(2)
        Ppc = dpp

    d = [Ppc * Ppm * Pm[el], Pmc * Pmm * Pm[el]]
    Pmn = max(d)
    if Pmn == d[0]:
        P[1].append(1)
    else:
        P[1].append(2)

    Pmc = Pmn
    V[0].append(Ppc)
    V[1].append(Pmc)

m = max(V[0][len(V[0]) - 1], V[1][len(V[1]) - 1])
c = 0
if m == V[0][len(V[0]) - 1]:
    c = P[0][len(V[0]) - 1]
    result = '+'
else:
    c = P[1][len(V[0]) - 1]
    result = '-'


for i in xrange(len(V[1]) - 1, 0, -1):
    c = P[c - 1][i]
    if c == 1:
        result = '+' + result
    else:
        result = '-' + result


print 'V = '
for line in V:
    print line

print '\n\n\nP = '
for line in P:
    print line

print emission
print result