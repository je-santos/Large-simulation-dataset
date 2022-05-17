# Large-simulation-dataset repo (DRP-372)

Physical processes in porous materials are of research interest due to their inherent geometric complexity. The equations that describe these processes are well-understood; however, approximating them numerically often requires extensive computational resources. 
Here we present transport simulation results and geometric features carried-out on samples hosted on the Digital Rocks Portal.  We hope that the scale and diversity of this dataset can offer unparalleled opportunities to researchers who are benchmarking simulators, training machine learning models, and developing correlations to acquire new insights into physical processes in porous media.

Sample names follow the convention:
    DigitalRocksPortalProjectNumber_SampleNumber_Size

Version 1.0
-------------
This version includes 256^3 and 480^3 volumes that were sampled from binary images hosted on the DRP. Slip flow (at 5 confinement pressures), single-phase LBM, and electrical simulations were performed on each sample. We also include ten features and four Minkowski functionals to characterize the geometry of the void space.

----------------------------
Load data in Python:
----------------------------
from hdf5storage import loadmat

from pandas import read_csv

# Load binary, simulation results, and features (.mat) as 3D Numpy array
mat_data = loadmat('<FILENAME>.mat')['<KEY>']

# Load Minkowski Functionals (.csv) as Pandas dataframe
mf = read_csv('<FILENAME>.csv', delimiter=’ ’)

----------------------------
Load data in Matlab:
----------------------------
% Load binary, simulation results, and features (.mat)
load('<FILENAME>.mat')

% Load Minkowski Functionals (.csv) as table (access variables with mf.<KEY>)
mf = readtable ('minkowski.csv')


