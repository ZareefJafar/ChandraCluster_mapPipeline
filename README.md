-----------------------
### Introduction
------------------

Pipeline to create x-ray temeprature maps, pressure maps, surface brightness maps, and density maps of  galaxy clusters from [Chandra Data Archive.](https://cda.harvard.edu/chaser/)


This pipeline is based on a [pipeline](https://github.com/jpbreuer/Chandra_pipeline) created by Jean-Paul Breuer

Special thanks to,

[Dr. Khan M B Asad](http://phy.iub.edu.bd/people/asad/)\
Assistant Professor
Independent University, Bangladesh

[Jean-Paul Breuer](http://jpbreuer.com/index.html)\
Masaryk University, Czech Republic

-----------------------
### Environment setup
-----------------------


System requirements:\
Platform Support: Tested on Ubuntu 20.04.5 lts,  Ubuntu 20.04.4 LTS.\
Any multicore CPU, minimum 8 GB RAM, 70 GB storage for software packages. 

**1. Install Anaconda distribution.**

Follow the [Anaconda Installation page](https://docs.anaconda.com/anaconda/install/linux/) for installation.

**2. Installing CIAO with conda.**

- Run the following command in the terminal to install ciao, caldb and some associated software in a conda environment named “ciao-4.14” or anything you like.
```
conda create -n ciao-4.15 -c https://cxc.cfa.harvard.edu/conda/ciao -c conda-forge ciao sherpa ds9 ciao-contrib caldb marx jupyter jupyterlab numpy matplotlib astropy scipy scikit-learn pandas seaborn
```
- CALDB, acis_bkgrnd and hrc_bkgrnd file download might fail because of  ```CondaHTTPError: HTTP 000 CONNECTION FAILED for url``` error or slow internet connection. If this happens remove caldb from CIAO installation command and follow the [Alternative download instructions](https://cxc.cfa.harvard.edu/ciao/threads/ciao_install_conda/index.html#alt_download). There are multiple approches under ```CALDB alternatives```. Recommended and tested alternative: ```Install individual conda tar files``` .


- Reference: [Installing CIAO with conda page](https://cxc.cfa.harvard.edu/ciao/threads/ciao_install_conda/)


**3. Download and install HEASOFT Software.**

- Go to the [HEASOFT installation page](https://heasarc.gsfc.nasa.gov/lheasoft/download.html)

- Select "Source Code" and select "PC - Linux - Ubuntu" from checkbox in STEP 1.

- Select all in STEP 2 and click submit.

- unzip or extract the .tar.gz file ```(using e.g. "tar zxf [tar file]")``` and follow the [INSTALLATION](https://heasarc.gsfc.nasa.gov/lheasoft/ubuntu.html) process to install HEASOFT. For user without sudo access see the [OPTIONAL] steps at the end. 


- To make HEASOFT initialization easy I have created the following alias:

  Get the PLATFORM name:\
    Go inside the heasoft directory and run:
    ```
    cd /home/[user_name]/[heasoft_saved_directory]/heasoft-6.31.1/BUILD_DIR
    ```
    ```
    nano config.txt
    ```
    see  line number 4 which will look something like this: ``` modified Linux system type is x86_64-pc-linux-gnu-libc2.31```\
    So, machine's architecture/PLATFORM is ```x86_64-pc-linux-gnu-libc2.31```\
  In the terminal type and run the following:
  ```
  nano ~/.bashrc
  ```
  
  Paste the following command (replace the "heasoft-6.31.1" with your downloaded heasoft version and replace "PLATFORM" with machine's architecture):

  ```
  alias heainit='export HEADAS=/path/to/your/installed/heasoft-6.31.1/(PLATFORM); . $HEADAS/headas-init.sh'
  ```
  For example I created following alias in the ```.bashrc``` script of my system:
  ```
  alias heainit='export HEADAS=/home/zareef/software/heasoft-6.31.1/x86_64-pc-linux-gnu-libc2.31; . $HEADAS/headas-init.sh'
  ```
  save the ~/.bashrc.\
  run ```source ~/.bashrc```\
  Type ```heainit``` to initiate HEASOFT whenever needed.


***[OPTIONAL]For users without sudo access***

During the [INSTALLATION](https://heasarc.gsfc.nasa.gov/lheasoft/ubuntu.html) process check gcc, g++, gfortran, perl, python3 by running ```which gcc```, ```which python3``` etc in the terminal. Use these locations in the ```export``` of ```Building the software``` step.


**4. Install CFITSIO**

- Download CFITSIO from [here](https://heasarc.gsfc.nasa.gov/docs/software/fitsio/fitsio.html)

- Follow [this](https://www.gnu.org/software/gnuastro/manual/html_node/CFITSIO.html) instructions.

***[OPTIONAL]For users without sudo access***\
In the ```./configure``` part of the instructions replace the ```--prefix=/usr/local``` with ```--prefix=[home]/[usr_name]/local/bin```. Create ```mkdir -p [home]/[usr_name]/local/bin``` if it is not created before.

In my case I used ```/home/zareef/anaconda3/bin```(automatically created with anaconda installation) as the location of ```[home]/[usr_name]/local/bin``` in the server user account. 

**5. Download and install Contour binning and accumulative smoothing software.**

- Open terminal and run the following:
```
git clone https://github.com/jeremysanders/contbin
```
- Go to the downloaded folder directory.
```
cd home/[user_name]/[dowload_location]/contbin
```
- Build:
```
make
```
- Copy the built program:
```
sudo make install 
```


***[OPTIONAL]For users without sudo access***
- Open terminal and run the following:
```
git clone https://github.com/jeremysanders/contbin
```

- Go to the ```contbin``` folder

- Open Makefile
```
nano Makefile
```
- Edit following parameters:

You need to change the line in the Makefile that says linkflags=... to have -L/path/of/library  at the start. Change the line which says CXXFLAGS=... to have -I/path/of/include/directory  at the start.

e.g (for /usr/local/lib and /usr/local/include)

...
```
# add -lsocket to below for Solaris
# add -Ldirname to add directory to link path to look for cfitsio
linkflags=-L/usr/local/lib -lcfitsio -Lparammm -lparammm -lpthread 

# where to install (not very well tested)
bindir=/usr/local/bin

# sensible compiler flags
export CXXFLAGS=-I/usr/local/include -O2 -g -Wall -std=c++11
export CXX=g++
...
```
This is the part of the ```Makefile``` for my server account. I used my ```anaconda3``` folder location as the lib, include and bin path which was created after anaconda installtion:

...
```
# add -lsocket to below for Solaris
# add -Ldirname to add directory to link path to look for cfitsio
linkflags=-L/home/zareef/anaconda3/lib -lcfitsio -Lparammm -lparammm -lpthread 

# where to install (not very well tested)
bindir=/home/zareef/anaconda3/bin

# sensible compiler flags
export CXXFLAGS=-I/home/zareef/anaconda3/include -O2 -g -Wall -std=c++11
export CXX=g++
...
```

- Build:
```
make
```
- Copy the built program:
```
make install 
```

To learn more about [contbin](https://github.com/jeremysanders/contbin)


The tools in step 6 and 7 are not implemented yet in this pipeline. They may be added as an option in future updates.\
**6. OPTIONAL: Installing GNU parallel shell tool.(Not used)**

Run the following:
```
conda install -c conda-forge parallel
```

Reference:

[GNU parallel official page](https://www.gnu.org/software/parallel/)

[Anaconda parallel package link](https://anaconda.org/conda-forge/parallel) 




**7. OPTIONAL: Install SPEX software package.(Not used)**

Follow the SPEX installation guide from [here](https://spex-xray.github.io/spex-help/getstarted/install.html).

-----------------------
### Generating maps.
-----------------------
To download ChandraCluster_mapPipeline, simply run ```git clone https://github.com/ZareefJafar/ChandraCluster_mapPipeline.git```

Go to the folder ```cd ~/ChandraCluster_mapPipeline```.

There are several python scripts (.py files). Running each script will generate a bash script (.sh file). 

Let's start!!!

**Step 0: Creating directories**
- Everything will run on ```conda``` environment. So, activate it first.
```
conda activate ciao-4.14
```
- Run ```directory.py```. Enter the instructed informations. 
```
python directory.py
```

**Step 1: Run PreProcessing_download_data.py**
```
python PreProcessing_download_data.py
```
```
bash preprocessing.sh
```

**Step 2: Run PreProcessing_reprocess_data.py**
```
python PreProcessing_reprocess_data.py
```
```
bash preprocessing.sh
```

Bug List and solution:\
[pget_error](https://cxc.cfa.harvard.edu/ciao/faq/pget_error.html)\
solution: go to the link\
[cannot import name 'object' from 'numpy': Problems with NumPy 1.24](https://cxc.cfa.harvard.edu/ciao/watchout.html)\
solution: enter ciao environment and run ```conda install -c anaconda numpy=1.23.5```

**Step 3: Run PreProcessing_flare_filter.py**

```
python PreProcessing_flare_filter.py
```
```
bash preprocessing.sh
```

**Step 4: Run PreProcessing_merge_data.py**
```
python PreProcessing_merge_data.py
```
```
bash preprocessing.sh
```

**Step 5: Run PreProcessing_merge_data_flux.py**
```
python PreProcessing_merge_data_flux.py
```

**Step 6: Removing point source from merged image**

- Open ```broad_thresh.img``` with ds9. This file should be located inside ```merged``` folder inside cluster data folder.

```
ds9 ~/[data_dir]/[cluster_name]/merged/broad_thresh.img
```
- We need to create 3 region files from ```broad_thresh.img``` file.\
```src_0.5-7-nps-noem.reg```:\
A region file that contains all cluster emission (eg. a large circle around the cluster that includes the extended emission, 
which will be removed and used for the deflaring/high energy rescaling). This would include areas such as the peak of cluster                             emission as these regions may contain high energy events you want to consider in this analysis.\
```broad_src_0.5-7-pointsources.reg```:\
A region file that contains all of the pointsources. These are typically foreground point sources one does not want                                       to consider when analyzing the cluster.\
```square.reg```:   
This will eventually crop out all things outside of the region of interest. 

Region file format:```Region - ciao```,```Coordinate System - wcs```\
Save location: ```~/[data_dir]/[cluster_name]/regionfiles```.


- Run ```PreProcessing_source_crop.py```
```
python PreProcessing_source_crop.py
```
- Run generated ```preprocessing.sh```
```
bash preprocessing.sh
```

**Step 7: Run Preliminary_Products_contourbin.py**

For system without sudo access go to the base environment: ```conda deactivate``` before running the following commands. 
```
python Preliminary_Products_contourbin.py
```
```
bash preliminary_products.sh
```
Go to ciao environment ```conda activate ciao-4.15``` and continue from step 8.


**Step 8: Converting region file coordinate system syntax**

- Convert region file coordinate system syntax
```
python RegCoordChange.py
```
```
bash regcoordchange.sh
```

- ***[OPTIONAL]For users without sudo access***\
You may see following problem while converting region file coordinate system syntax in a remote server. Better to do it in a local system. Update is coming soon.

![RegCoordChange_error](images/RegCoordChange_error.png)




**Step 9: Pre fitting**\
Running this will take a long time depending on the data. To run this in a remote server or another computer system follow the instruction ```FOR REMOTE MACHINE```. Future works includes adding CPU/GPU parallel processing.
- ***[OPTIONAL]:FOR REMOTE MACHINE.***\
Transfer the data file and script file to the remote server. Make sure the remote server has ciao and heasoft installed. Then run ```change_machine.py```.
```
python change_machine.py
```
input: /....../[new_data_dir]\
- ***[OPTIONAL]For users without sudo access***\
first go to the script/code directory
```
cd ~/.../ChandraCluster_mapPipeline
```
make ```tmp``` folder
```
mkdir tmp
```
```
chmod 777 tmp
```
set the ASCDS_WORK_PATH environment variable. See [Bugs: wavdetect](https://cxc.harvard.edu/ciao/bugs/wavdetect.html#parallel) and [specextract tmpdir](https://cxc.cfa.harvard.edu/ciao/ahelp/specextract.html#plist.tmpdir) on the CIAO website for details information.

see ASCDS_WORK_PATH value.
```
printenv ASCDS_WORK_PATH
```
Now change it to your created tmp folder path.
```
export ASCDS_WORK_PATH=$PWD/tmp
```
Continue running remaining steps from the remote server.

- Run Processing_pre_fitting.py
```
python Processing_pre_fitting.py
```
- Initialize ```heasoft``` using alias we created previously.

```
heainit
```

- Run generated ```pre-fitting.sh```
```
bash pre-fitting.sh
```
- While running ```pre-fitting``` you may see following Warnings related to ```OBS_ID and background files```. Ignore it.
![pre_fitting_error](images/pre_fitting_error.png)

- May encounter ```specextract zero count error```. Ignore it for now.
![zerocount_error_specextract](images/zerocount_error_specextract_obs16129.png)

***[OPTIONAL]Bug for users without sudo access***
- If you see this ```specextract tmp file missing error``` run ```pre-fitting.sh``` in local machine with sudo access to avoid it. Fix is coming soon.
![specextract tmp folder error](images/Pre_fitting_tmp_folder_error.png)


**Step 10: Processing_xspecfitting.py**
- Run Processing_xspecfitting.py
```
python Processing_xspecfitting.py
```
- Go to ```specfile_output``` folder. You will find a file named```xspecfitting.sh```. 
```
cd ~/[data_dir]/[cluster_name]/specfile_output
```
- run ```xspecfitting.sh```
```
bash xspecfitting.sh
```
- If you face following error just type ```exit``` and press Enter.

![xspecfitting_error_1](images/xspecfitting_error_1.png)

- This particular error will run endlessly. Just press ```Ctrl+C``` to stop it and type ```exit``` to continue.   

![xspecfitting_error_2](images/xspecfitting_error_2.png)

- Return to the python script folder and start following from step 11.
```
cd ~/ChandraCluster_mapPipeline
```

**Step 11: Run ParseOutput_xspec.py**
```
python ParseOutput_xspec.py
```
**Step 12: Run cleanup.py**
```
python cleanup.py
```
**Step 13: Finale step, creating maps**

- Run ```pipeline_maps.py```
```
python pipeline_maps.py
```
All the maps will be saved in the maps folder of the data folder. ```~/[data_dir]/[cluster_name]/maps```

DONE!!!!!!!!

-----------------------
### Sample data, bash scripts and paper.
-----------------------

- All the generated data products including generated bash script and maps of some galaxy clusters using the pipeline: [drive](https://drive.google.com/drive/folders/16Sxy-VS4MbmElKVLhYDZdtxcmunzIFm1?usp=share_link)

- This [paper](https://arxiv.org/pdf/2005.10263.pdf) by J. P. Breuer discusses about image analysis of a2256 cluster.

-----------------------
### Additional Resources: 
-----------------------

Some resources which helped me to work with this pipeline and also my ongoing work on detecting cold fronts from galaxy clusters with potential minihalo.  
- [Galaxy Clusters, ARGI](http://abekta.iub.edu.bd/rs/gc)
- [Contour binning: a new technique for spatially resolved X-ray spectroscopy applied to Cassiopeia A
](https://ui.adsabs.harvard.edu/abs/2006MNRAS.371..829S/abstract)
- [The Galaxy Cluster 'Pypeline' for X-ray Temperature Maps: ClusterPyXT](https://github.com/bcalden/ClusterPyXT), [arXiv](https://arxiv.org/abs/1903.08215)
- [Study of the formation of Cold Fronts and Radio Mini-halos induced by the
Intergalactic Gas Sloshing in the Cores of Galaxy Clusters](https://drive.google.com/file/d/1RyDp2HOEMch7D02P2CQ9kiDz8j-O6hpf/view)
- [The Mergers in Abell 2256: Displaced Gas and its Connection to the Radio-emitting Plasma](https://arxiv.org/abs/2005.10263)
- [X-ray spectroscopy of galaxy clusters: studying astrophysical processes in the largest celestial laboratories](https://link.springer.com/content/pdf/10.1007/s00159-009-0023-3.pdf)
- [A Brief Intro to the Chandra Mission by Jonathan McDowell](https://cxc.harvard.edu/ciao/workshop/jan21/jcm.ws21.pdf)
- [An X-ray Data Primer](https://cxc.harvard.edu/cdo/xray_primer.pdf)
- [X-ray spectroscopy of galaxy clusters: studying astrophysical processes in the largest celestial laboratories](https://link.springer.com/article/10.1007/s00159-009-0023-3)
- [Occurrence of Radio Minihalos in a Mass-limited Sample of Galaxy Clusters](https://iopscience.iop.org/article/10.3847/1538-4357/aa7069/meta)
- [Expanding the Sample of Radio Minihalos in Galaxy Clusters](https://iopscience.iop.org/article/10.3847/1538-4357/ab29f1/meta)
- [Diffuse Radio Emission from Galaxy Clusters](https://link.springer.com/article/10.1007/s11214-019-0584-z)
- [Different binning approaches](https://cxc.cfa.harvard.edu/ciao/gallery/binning.html)

