from pandas import read_excel
import numpy as np

xls = ExcelFile('geom_desciption.xlsx')
df = xls.parse(xls.sheet_names[0])

df = read_excel('geom_desciption.xlsx',
                0,)


info = df.loc[:,['sample name', 'origin', 'type', 'subtype', 'percolation','link']].to_dict()


info_dict = {}
for i in range(len(info['link'])):
    info_dict[info['sample name'][i]] = {}
    for field in ['origin', 'type', 'subtype', 'percolation','link']:
        info_dict[info['sample name'][i]][field] = info[field][i] 
    
    
    
## Example



sample = '10_01_256'
# calc porosity
phi = 0.2

print(f'Sample {sample} is a {info_dict[sample]["subtype"]} {info_dict[sample]["type"]}')
print(f'Created {info_dict[sample]["origin"]}')
print(f'with a porosity of ...')
print(f'can be found at  {info_dict[sample]["link"]}')
if np.isnan( info_dict[sample]["percolation"] ):
    pass
else:
    print('it doesnt percolate')
