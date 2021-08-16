# https://www.youtube.com/watch?v=3LopI4YeC4I

import numpy as np

n_sim = 1000
n_astronaut = 18300
n_selected = 11

weight_luck = 0.05
weight_skill = 1 - weight_luck

avg_skills = np.zeros(n_sim)
avg_lucks = np.zeros(n_sim)

for i in range(n_sim):
    gen_luck = np.random.uniform(0, 100, size=n_astronaut)
    gen_skill = np.random.uniform(0, 100, size=n_astronaut)
    score = weight_skill * gen_skill + weight_luck * gen_luck
    top_n = np.argsort(score)[-n_selected:]
    avg_skills[i] = gen_skill[top_n].mean()
    avg_lucks[i] = gen_luck[top_n].mean()

print(avg_lucks.mean(), avg_lucks.std())
print(avg_skills.mean(), avg_skills.std())
