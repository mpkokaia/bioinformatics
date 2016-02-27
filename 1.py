p_prob = {'0': 0.5, '1': 0.5}
m_prob = {'0': 0.9, '1': 0.1}
init_p_prob = 0.5
init_m_prob = 0.5
pp_prob = 0.5
pm_prob = 0.5
mm_prob = 0.5
mp_prob = 0.5


emission = '0100101'
result = ''

prob_if_m = []
way_if_m = []
prob_if_p = []
way_if_p = []

init_m_prob = init_m_prob * m_prob[emission[0]]
init_p_prob = init_p_prob * p_prob[emission[0]]

if init_m_prob < init_p_prob:
    way_if_m.append('m')
    prob_if_m.append(init_p_prob)
    way_if_p.append('m')
    prob_if_p.append(init_p_prob)
else:
    way_if_m.append('p')
    prob_if_m.append(init_m_prob)
    way_if_p.append('p')
    prob_if_p.append(init_m_prob)


for el in emission[1:]:
    # if p
    mp = init_m_prob * mp_prob * p_prob[el]
    pp = init_p_prob * pp_prob * p_prob[el]
    if mp < pp:
        way_if_p.append('p')
        tmp_p_prob = pp
        prob_if_p.append(pp)
    else:
        way_if_p.append('m')
        tmp_p_prob = mp
        prob_if_p.append(mp)
    # if m
    pm = init_p_prob * pm_prob * m_prob[el]
    mm = init_m_prob * mm_prob * m_prob[el]
    if mm < pm:
        way_if_m.append('p')
        tmp_m_prob = pm
        prob_if_m.append(pm)
    else:
        way_if_m.append('m')
        tmp_m_prob = mm
        prob_if_m.append(mm)
    init_m_prob = tmp_m_prob
    init_p_prob = tmp_p_prob

prob_if_p = prob_if_p[::-1]
prob_if_m = prob_if_m[::-1]
way_if_p = way_if_p[::-1]
way_if_m = way_if_m[::-1]

if prob_if_p[0] > prob_if_m[0]:
    way = way_if_p[0]
    result += '+'
else:
    way = way_if_m[0]
    result += '-'

for i in range(1, len(prob_if_m)):
    if way == 'p':
        result += '+'
        way = way_if_p[i]
    else:
        result += '-'
        way = way_if_m[i]

print emission
print result[::-1]
