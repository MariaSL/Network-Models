# Network-Models
Erdos-Renyi and Watts-Strogatz models.
##Purpose
School project for the course in Information Retrieval (2015).
##Description
Implementation of Erdos-Renyi and Watts-Strogatz models using networkx.
##Stack
Python 2.7
Libraries: NetworkX, Numpy, Matplotlib, Math
##How to run
To see the results of Erdos-Renyi model simply run ERModel.py file.
To see the results of Watts-Strogatz model simply run WSModel.py file.
##Notes
You can see how models perform with different parameters. It is important to mention however, that for Erdos-Renyi model the large number of `max_nodes` (8000-10000) results in a very long computation time. For `max_nodes = 3000` and `delta = 20`, the computation time was more than 15 minutes.
For full description, formulas and plots check my report in "Docs" folder.