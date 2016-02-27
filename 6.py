import pygraphviz as pgv

data = {('A', 'B'): 5, ('A', 'C'): 4, ('A', 'D'): 7, ('A', 'E'): 6, ('A', 'F'): 8,
        ('B', 'C'): 7, ('B', 'D'): 10, ('B', 'E'): 9, ('B', 'F'): 11,
        ('C', 'D'): 7, ('C', 'E'): 6, ('C', 'F'): 8,
        ('D', 'E'): 5, ('D', 'F'): 9,
        ('E', 'F'): 8}

matrix = {}
for k in data:
    matrix[(k[1], k[0])] = data[k]
    matrix[k] = data[k]

replacement = {}
while len(matrix) != 2:
    new_matrix = {}
    kmin = min(matrix, key=matrix.get)
    vmin = matrix[kmin]
    knew = kmin[0] + kmin[1]
    dist = vmin / 2.0
    replacement[knew] = {kmin[0]: dist,
                         kmin[1]: dist}
    for k in matrix:
        if k == kmin:
            continue
        elif k == (kmin[1], kmin[0]):
            continue
        elif k[0] == kmin[0]:
            d1 = matrix[k]
            d2 = matrix.get((kmin[1], k[1]), d1)
            new_matrix[(knew, k[1])] = (d1 + d2) / 2.0
            new_matrix[(k[1], knew)] = (d1 + d2) / 2.0
        elif k[0] == kmin[1]:
            d1 = matrix[k]
            d2 = matrix.get((kmin[0], k[1]), d1)
            new_matrix[(knew, k[1])] = (d1 + d2) / 2.0
            new_matrix[(k[1], knew)] = (d1 + d2) / 2.0
        elif k[1] != kmin[0] and k[1] != kmin[1]:

            new_matrix[k] = matrix[k]
    matrix = new_matrix
kmin = min(matrix, key=matrix.get)
vmin = matrix[kmin]
knew = kmin[0] + kmin[1]
dist = vmin / 2.0
replacement[knew] = {kmin[0]: dist,
                     kmin[1]: dist}
print replacement
A = pgv.AGraph()
for k in replacement:
    for l in replacement[k]:
        A.add_edge(l, k)
        edge = A.get_edge(l, k)
        edge.attr['label'] = replacement[k][l]
A.layout()
A.draw('UPGMA.png')
