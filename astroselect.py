# https://www.youtube.com/watch?v=3LopI4YeC4I

import numpy as np

n_sim = 1000
n_astronaut = 18300
n_selected = 11

weight_luck = 0.05
weight_skill = 1 - weight_luck

avg_skills = np.zeros(n_sim)
avg_lucks = np.zeros(n_sim)
skill_alone = np.zeros(n_sim)

for i in range(n_sim):
    gen_luck = np.random.uniform(0, 100, size=n_astronaut)
    gen_skill = np.random.uniform(0, 100, size=n_astronaut)
    score = weight_skill * gen_skill + weight_luck * gen_luck
    top_n = np.argsort(score)[-n_selected:]
    avg_skills[i] = gen_skill[top_n].mean()
    avg_lucks[i] = gen_luck[top_n].mean()

    # how many would still be in top n based on skill alone (i.e., no luck)
    gen_luck[top_n] = 0.0
    new_score = weight_skill * gen_skill + weight_luck * gen_luck
    new_top_n = np.argsort(new_score)[-n_selected:]
    still_in = np.intersect1d(top_n, new_top_n)
    skill_alone[i] = len(still_in)


print(avg_lucks.mean(), avg_lucks.std())
print(avg_skills.mean(), avg_skills.std())
print(skill_alone.mean(), skill_alone.std())
