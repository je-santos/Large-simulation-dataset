# Large-simulation-dataset repo (DRP-372)

Physical processes in porous materials are of research interest due to their inherent geometric complexity. The equations that describe these processes are well-understood; however, approximating them numerically often requires extensive computational resources. 
Here we present transport simulation results and geometric features carried-out on samples hosted on the Digital Rocks Portal.  We hope that the scale and diversity of this dataset can offer unparalleled opportunities to researchers who are benchmarking simulators, training machine learning models, and developing correlations to acquire new insights into physical processes in porous media.

Sample names follow the convention:
    DigitalRocksPortalProjectNumber_SampleNumber_Size
    
    
    
## Usage

Example for downloading and loading into memory every datatype in our dataset

```python
from urllib.request import urlretrieve
from hdf5storage import loadmat
from pandas import read_csv

# URLs
url_drp  = 'https://www.digitalrocksportal.org'
url_proj = url_drp + '/projects/374/images'
num_bin, num_elec, num_nano, num_geom = 311368, 331861, 334591, 332438 # file locations (DRP URLs)

# download the files from the portal
for name, num in zip( ['bin','elec','nano','geom'],
                      [num_bin, num_elec, num_nano, num_geom] ):
    urlretrieve( f'{url_proj}/{num}/download' , im_name:=f'{name}.mat')
    
# nanosim log
urlretrieve( f'{url_proj}/334590/download' , '1MPa_log.csv')
# minkowski log
urlretrieve( f'{url_proj}/332437/download' , 'mink_log.csv')

# binary image (0 in the pore-space 1 in the solid-space)
bin_im    = loadmat('bin.mat')['bin']

# geometrical properties
geoms      = loadmat('geom.mat')
mink_funcs = read_csv('mink_log.csv', header=None)

# Electrical conductivity simulations
elec_sim  = loadmat('elec.mat')
ix        = elec_sim['Ix'] # conductivity in x-dir
iy        = elec_sim['Iy'] # conductivity in y-dir
iz        = elec_sim['Iz'] # conductivity in z-dir
pot       = elec_sim['phi'] # electric potential

# Flow with nanoconfinement simulations
nano_sim = loadmat('nano.mat')
pressure = nano_sim['rho'] # fluid pressure
ux       = nano_sim['ux'] # velocity in x-dir
uy       = nano_sim['uy'] # velocity in y-dir
uz       = nano_sim['uz'] # velocity in z-dir
mfp      = nano_sim['mfp'] # normalized mean free path

nanosim_data = read_csv('1MPa_log.csv', header=None)
```

## Version 1.0
This version includes 256^3 and 480^3 volumes that were sampled from binary images hosted on the DRP. Slip flow (at 5 confinement pressures), single-phase LBM, and electrical simulations were performed on each sample. We also include ten features and four Minkowski functionals to characterize the geometry of the void space.

```python
#----------------------------
# Load data in Python:
#----------------------------
from hdf5storage import loadmat

from pandas import read_csv

# Load binary, simulation results, and features (.mat) as 3D Numpy array
mat_data = loadmat('<FILENAME>.mat')['<KEY>']

# Load Minkowski Functionals (.csv) as Pandas dataframe
mf = read_csv('<FILENAME>.csv', delimiter=’ ’)
```

```matlab
%----------------------------
% Load data in Matlab:
% ----------------------------
% Load binary, simulation results, and features (.mat)
    
load('<FILENAME>.mat')

% Load Minkowski Functionals (.csv) as table (access variables with mf.<KEY>)
    
mf = readtable ('minkowski.csv')
```


