import pandas as pd
import pickle
import multiprocessing as mp

# read the pickle files
pickle_off = open("edges.pickle","rb")
G = pickle.load(pickle_off)
pickle_off = open("reduced_data.pickle","rb")
cut_table = pickle.load(pickle_off)
user_locations = cut_table.groupby(['user', 'location id']).size().reset_index(name='counts')
ids = tuple(user_locations.user.value_counts().index)
L = 500
edges = []
for i in range(L-1):
    a = ids[i]
    for j in range(i+1, L):
        b = ids[j]
        edges.append((a, b))

def get_score(x):
    s_table = cut_table[cut_table.user==x[0]]
    t_table = cut_table[cut_table.user==x[1]]
    share = set(s_table['location id']).intersection(t_table['location id'])
    st, ts = 0, 0
    if len(share) > 20:
        for i in share:
            time1 = s_table[s_table['location id']==i]['check-in time'].max()
            time2 = t_table[t_table['location id']==i]['check-in time'].min()
            if time2 < time1:
                st += 1
            if time2 > time1:
                ts += 1
        # ask if are friends
        label = 'friends' if (x[0], x[1]) in G.edges() else 'non'
        pair = f'{x[0]}-{x[1]}' if st < ts else f'{x[1]}-{x[0]}'
        return pair, max(st, ts), label

pool = mp.Pool(processes=4)
results = pool.map(get_score, edges)
results = [x for x in results if x!=None]
pd.DataFrame(results, columns=['pair', 'score', 'friends']).to_csv('pair_scores.csv', index=False)


