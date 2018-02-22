import pandas as pd
import pickle
import multiprocessing as mp

# read the pickle files
pickle_off = open("edges.pickle","rb")
G = pickle.load(pickle_off)
pickle_off = open("reduced_data.pickle","rb")
cut_table = pickle.load(pickle_off)

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
        return f'{x[0]}-{x[1]}', max(st, ts)

pool = mp.Pool(processes=4)
results = pool.map(get_score, list(G.edges()))
results = [x for x in results if x!=None]
pd.DataFrame(results, columns=['pair', 'score']).to_csv('friends_score.csv', index=False)
