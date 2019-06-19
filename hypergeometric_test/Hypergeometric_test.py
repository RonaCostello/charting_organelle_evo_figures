
# coding: utf-8

# In[41]:


from scipy.stats import hypergeom
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import os
import click

@click.command()
@click.option('--directory', prompt='directory where data is', help='specifiy the path to the directory where the data is')

def hypergeometric_test(directory):
    locations = ['C', 'M']

    # directory = '/Users/rona/data/teraserve/chapter-1/Wolfpsort/relocalisation_duplication'
    for i, item in enumerate(locations):
        file_1 = pd.read_csv(f"{directory}/output_{item}_gain.csv")
        file_2 = pd.read_csv(f"{directory}/output_{item}_loss.csv")

        x_gains = file_1['reloc_following_dup'].sum()
        M_gains = file_1['number_of_dups'].sum() + file_1['number_of_specs'].sum()
        n_gains = file_1['reloc_following_spec'].sum() + file_1['reloc_following_dup'].sum()
        N_gains = file_1['number_of_dups'].sum()
        print(item + ' gains')
        print(hypergeom.sf(x_gains-1, M_gains, n_gains, N_gains))

        x_losses = file_2['reloc_following_dup'].sum()
        M_losses = file_2['number_of_dups'].sum() + file_2['number_of_specs'].sum()
        n_losses = file_2['reloc_following_spec'].sum() + file_2['reloc_following_dup'].sum()
        N_losses = file_2['number_of_dups'].sum()

        print(item + ' losses')
        print(hypergeom.sf(x_losses-1, M_losses, n_losses, N_losses))

if __name__ == '__main__':
    hypergeometric_test()
