p_prob = {'0': 0.1, '1': 0.9}
m_prob = {'0': 0.9, '1': 0.1}
init_p_prob = 0.5
init_m_prob = 0.5
pp_prob = 0.8
pm_prob = 0.2
mm_prob = 0.7
mp_prob = 0.3
emissions = '11001010100000000001010001101111'

fprob_if_p = [init_p_prob * p_prob[emissions[0]]]
fprob_if_m = [init_m_prob * m_prob[emissions[0]]]
for el in emissions[1:]:
    sum_p_probs = (fprob_if_p[-1] * pp_prob * p_prob[el] +
                   fprob_if_m[-1] * mp_prob * p_prob[el])
    sum_m_probs = (fprob_if_p[-1] * pm_prob * m_prob[el] +
                   fprob_if_m[-1] * mm_prob * m_prob[el])
    fprob_if_p.append(sum_p_probs)
    fprob_if_m.append(sum_m_probs)

bprob_if_p = [1]
bprob_if_m = [1]
for el in emissions[::-1]:
    sum_p_probs = (bprob_if_p[-1] * pp_prob * p_prob[el] +
                   bprob_if_m[-1] * pm_prob * p_prob[el])
    sum_m_probs = (bprob_if_p[-1] * mp_prob * m_prob[el] +
                   bprob_if_m[-1] * mm_prob * m_prob[el])
    bprob_if_p.append(sum_p_probs)
    bprob_if_m.append(sum_m_probs)

bprob_if_p = bprob_if_p[::-1]
bprob_if_m = bprob_if_m[::-1]
if_p = []
if_m = []
for i, el in enumerate(emissions):
    summ = ((fprob_if_p[i] * bprob_if_p[i] / p_prob[el]) +
            (fprob_if_m[i] * bprob_if_m[i] / m_prob[el]))
    if_p.append(round(fprob_if_p[i] * bprob_if_p[i] / (summ * p_prob[el]), 2))
    if_m.append(round(fprob_if_m[i] * bprob_if_m[i] / (summ * m_prob[el]), 2))

print '+'
print if_p
print '-'
print if_m
