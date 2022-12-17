









import re
import sys
import os
import subprocess

import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from matplotlib import rc
rc('text', usetex=True)
matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)
from astropy.io import fits
from astropy import wcs

#from scipy import ndimage
#from scipy.stats import multivariate_normal

#os.mkdir('/home/zareef/minihalo/data/a2256')





















if __name__ == "__main__":
	file_name = 'directory_list.txt'

	with open(file_name, 'w', encoding='utf-8') as f:
		clusterName = input("Enter cluster name for downloading data from Chandra Data Archive.\ne.g. aco3444 for aco3444 galaxy cluster.\nCluster name: ")
		obsids_search = os.popen('find_chandra_obsid ' + clusterName).read()
		f.write(clusterName+'\n')
		print("Following observations will be downloaded.\nIf you want to use only selected observations please manually edit the PreProcessing_download_data.py file before running STEP 2.\n\n"+obsids_search)

		clusterDirec = input("\nEnter the path where all the data files will be downloaded.\ne.g. [data_dir]/[sub_data_dir]/...\ndata path: ")
		f.write(clusterDirec)
		f.close()



		
		content=[]
		with open ('directory_list.txt', 'rt') as myfile:  
		    for line in myfile:                   
		        content.append(line)  
		myfile.close()
		cluster = content[0].strip()    ##'"07 17 31.20" "+37 45 35.4"'#
		MyDir = os.path.expanduser('~')
		parentdir = MyDir+'/'+content[1]+'/'+cluster # + cluster + '/'
		specfile_outputdir = parentdir + '/specfile_output'
		regionDirec = parentdir + '/regionfiles'
		mapDirec = parentdir + '/maps'
		os.makedirs(parentdir)
		merged_path = os.path.join(parentdir, 'merged/contbin_sn70_smooth100/outreg/sex')
		os.makedirs(merged_path)
		os.makedirs(specfile_outputdir)
		os.makedirs(regionDirec)
		os.makedirs(mapDirec)

		print("\nCreated directories\n"+parentdir+"\n"+merged_path+"\n"+specfile_outputdir+"\n"+regionDirec+"\n"+mapDirec)




#clusterNameVarify = input(f"{val}for{val} is a portal for {val}.")

###--- Required ---> Make these directories if they do not exist 

content=[]
with open ('directory_list.txt', 'rt') as myfile:  
    for line in myfile:                   
        content.append(line)  
myfile.close()
cluster = content[0].strip()    ##'"07 17 31.20" "+37 45 35.4"'#
MyDir = os.path.expanduser('~')
parentdir = MyDir+'/'+content[1]+'/'+cluster # + cluster + '/'
specfile_outputdir = parentdir + '/specfile_output'
regionDirec = parentdir + '/regionfiles'
mapDirec = parentdir + '/maps'
XSPEC = True #keep one True and one False, not both True, else issues parsing + making maps
SPEX = False


def create_path():
	os.makedirs(parentdir)
	merged_path = os.path.join(parentdir, 'merged/contbin_sn70_smooth100/outreg/sex')
	os.makedirs(merged_path)
	os.makedirs(specfile_outputdir)
	os.makedirs(regionDirec)

	print("\nCreated paths\n"+parentdir+"\n"+merged_path+"\n"+specfile_outputdir+"\n"+regionDirec)



#%%
###--- PreProcessing Flags ---> # Output from these flags results in a different code inside the prelim_products.sh 
download_reprocess_data = True
flare_filter = True # True to check for flaring in individual observations and to automate partial removal of pointsources
merge_data = True
#!! After merge_data, pointsources must be excised and confirmed manually. See broad_thresh_sps.fits with regionfile pointsources_combo.fits
no_emission = parentdir + '/regionfiles/src_0.5-7-nps-noem.reg'
no_pointsources = parentdir + '/regionfiles/broad_src_0.5-7-pointsources.reg'
fov_name = parentdir + '/regionfiles/square.reg' # or False

###--- Image Analysis Algorithm Flags --->
simple_hardnessmap = False
# From this point it's assumed that merged observation has been reduced with square_fov
#!! Check that broad_thresh_square_sps.fits exists in merged observation directory 
adaptivebin = False
contourbin = True

sn_per_region = 70; reg_smoothness = 100



#!! Need to manually find dimensions (minx and miny) of broad_thresh_square_sps.fits for producing the regions
# sn approx sqrt number of counts: 40k = 200, 20k = 141.42, 10k = 100, 5k = 70.71
# keep reg_smoothness at 100 or high

circle_mincounts = False; mincount = 5000
unsharp_mask = False
ggm = False
directional_ggm = False #'Sobel' #'Laplace', 'Sobel', 'Roberts', 'Prewitt', 'Robinson', 'Kirsch'
skeleton = False




