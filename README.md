# Network-Models #
Erdos-Renyi and Watts-Strogatz models.

## Purpose ##
The project I did for my Information Retrieval course. This project is solely for sharing my implementation, not for further development.

## Description ##
Example implementation of the Erdos-Renyi and Watts-Strogatz graph network models using networkx in Python.

## Stack ##
* Language : Python 2.7
* Libraries : NetworkX, Numpy, Matplotlib, Math
    
## How to run ##
* Erdos-Renyi model : run `src/ERModel.py`
* Watts-Strogatz model : run `src/WSModel.py`

## Notes ##
* You can modify the parameters for each model in their respective source files (e.g. `a = watts_strogatz_model(500, 4, 0.001)` in `src/WSModel.py`) to see how the results vary.
* For the Erdos-Renyi model the large number of `max_nodes` (8000-10000) results in a very long computation time. For `max_nodes = 3000` and `delta = 20`, the computation time was more than 15 minutes.
* For a full description, formulas and plots check my report in the `docs` folder.

