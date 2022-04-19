# Large-simulation-dataset

Physical processes in porous materials are of research interest due to their inherent geometric complexity. The equations that describe these processes are well-understood; however, approximating them numerically often requires extensive computational resources. 

Here we present transport simulation results and geometric features carried-out on samples hosted on the Digital Rocks Portal.  We hope that the scale and diversity of this dataset can offer unparalleled opportunities to researchers who are benchmarking simulators, training machine learning models, and developing correlations to acquire new insights into physical processes in porous media.

Sample names follow the convention:
    DigitalRocksPortalProjectNumber_SampleNumber_Size

Version 1.0
-------------
This version includes 256^3 and 480^3 volumes that were sampled from binary images hosted on the DRP. Slip flow (at 5 confinement pressures), single-phase LBM, and electrical simulations were performed on each sample. We also include ten features and four Minkowski functionals to characterize the geometry of the void space.

All data is hosted on the Digital Rocks Portal:
    https://www.digitalrocksportal.org/projects/372

----------------------------
Load data in Python:
----------------------------
```
from hdf5storage import loadmat
from pandas import read_csv

# Load binary, simulation results, and features (.mat) as 3D Numpy array
mat_data = loadmat('<FILENAME>.mat')['<KEY>']

# Load Minkowski Functionals (.csv) as Pandas dataframe
mf = read_csv('<FILENAME>.csv', delimiter=’ ’)
```
----------------------------
Load data in Matlab:
----------------------------
```
% Load binary, simulation results, and features (.mat)
load('<FILENAME>.mat')

% Load Minkowski Functionals (.csv) as table (access variables with mf.<KEY>)
mf = readtable ('minkowski.csv')
```
 
----------------------------
Filenames and Keys
----------------------------
| Filename  |   Key |   Description |
|-----------|-------|---------------|
|LBM.mat    |   ux  |   x-component of flow velocity|
|           |   uy  |   y-component of flow velocity|
|           |   uz  |   z-component of flow velocity|
|           |   rho |   pressure field|
|LBM.csv    |   -   |   convergence, # iterations, # cores used, hours of run time, permeability|
|Vel_Z.png	|   -	|   flow velocity magnitude in the direction of flow
|Vel_Streamlines.png|	-	|   streamlines calculated from flow velocity
|P_x_MPa.mat    | 	MFP	    |normalized mean free path
|   	    |   ux  |  	x-component of flow velocity|
|           |   uy	|   y-component of flow velocity|
|           |	uz	|   z-component of flow velocity|
|           |	rho	|   pressure field|
|P_x_MPa.csv|	-	|   convergence, # iterations, # cores used, hours of run time, permeability|
|\*elec.mat |	Ix	|   x-component of electric current|
|           |	Iy	|   y-component of electric current|
|           |	Iz	|   z-component of electric current|
|           |   phi	|   electric potential|
|Elec_Potential.png|	-	|   electric potential magnitude|
|Elec_Streamlines.png|	-	|   streamlines of the electric current|
|features.mat   |	chords_x|	inscribed chords inside the pore space in the x-direction|
|               |   chords_y|	inscribed chords inside the pore space in the y-direction|
|               |	e_domain|	Euclidean distance of the pore space in all three coordinate directions|
|               |   e_full  |  	signed distance function with positive labels inside the pore and negative labels inside the solid|
|               |   e_z	    |   Euclidean distance in the X-Y plane (orthogonal to the flow direction)|
|               |	MIS_3D	|   maximum inscribed sphere|
|               |	MIS_z	|   maximum inscribed sphere in the direction of flow (drainage experiment)|
|	            |porosity_z |  	slice-wise porosity in the z-direction|
|               |	tOf_L   |	time of flight from the left boundary (inlet)|
|               |	tOf_R   |	time of flight from the right boundary (outlet)|
|features.png   |	-	    |   cross-sections of five features: e_domain, tOf_L, MIS_3D, MIS_z, chords_y|
|minkowski.csv  |	Vn      |	volume|
|               |	An	    |   surface area|
|               |	Jn	    |   mean curvature|
|               |	Xn      |	Euler characteristic|




For comments/inquiries/suggestions use the issues tab of our repo:
https://github.com/je-santos/Large-simulation-dataset
