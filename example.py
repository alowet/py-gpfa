# Example script to run methods on sample data

# Code modified from the version by Byron Yu byronyu@stanford.edu, John Cunningham jcunnin@stanford.edu

from extract_traj import extract_traj
from data_simulator import load_data
import numpy as np

# set random seed for reproducibility
np.random.seed(0)

RUN_ID = 1
OUTPUT_DIR = './output/'+str(RUN_ID)+'/'
INPUT_FILE = '../em_input.mat'

x_dim = 3 # latent dimention
method = 'gpfa'

# Load data
# TODO
dat = load_data(INPUT_FILE)

# Extract trajectories
result = extract_traj(output_dir=OUTPUT_DIR, data=dat, method=method, x_dim=x_dim)

# Orthonormalize trajectories
# TODO

# Plot trajectories in 3D space
# TODO

# Cross-validation to find optimal state dimensionality
# TODO