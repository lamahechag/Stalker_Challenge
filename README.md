# Stalker_Challenge

1. In the first notebook `Data exploration and reduction.ipynb` you can find the data exploration and iterations analysis to reduce the data to find the solutions.
You will need the files `Gowalla_edges.txt` and `Gowalla_totalCheckins.txt` to create the reduced pickle files `edges.pickle, reduced_data.pickle`.

2. In the second notebook `Highest Scores.ipynb`, you can find the final results and the answers for the highest scores pairs.

## Setup
- Install Conda
- Create env and init notebook server
```
$ conda create -n stalker python=3.6 matplotlib networkx scipy multiprocessing pandas ipykernel numpy
$ source activate stalker
$ python -m ipykernel install --user
$ jupyter notebook
```
