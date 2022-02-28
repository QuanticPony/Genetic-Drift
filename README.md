# Genetic-Drift
A simple genetic drift simulation with Python. From [Wikipedia](https://en.wikipedia.org/wiki/Genetic_drift): 

Genetic drift (allelic drift or the Sewall Wright effect) is the change in the frequency of an existing gene variant (allele) in a population due to random sampling of organisms. The alleles in the offspring are a sample of those in the parents, and chance has a role in determining whether a given individual survives and reproduces. 

A population's allele frequency is the fraction of the copies of one gene that share a particular form.

Genetic drift may cause gene variants to disappear completely and thereby reduce genetic variation. It can also cause initially rare alleles to become much more frequent and even fixed. 


## Operation modes and global variables:
Inside [genetic-drift-simulation.py](genetic-drift-simulation.py) there are 3 global variables used in the simulation:
* `N_INDIVIDUALS` (int): number of individuals in the simulation. The number of offsprings is allways the same and equal to this number.
* `HISTOGRAM` (bool): changes the operating mode from ploting single simulations (`False`) to ploting the average time of disappearance of a gene variant for each allele frequency (`True`).
* `BINS` (int): the number of bins when `HISTOGRAM == True`.
