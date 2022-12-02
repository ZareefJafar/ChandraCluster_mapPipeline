Pipeline to create x-ray temeprature maps, pressure maps, surface brightness maps, and density maps of  galaxy clusters from [Chandra Data Archive.](https://cda.harvard.edu/chaser/)

This pipeline is based on a [pipeline](https://github.com/jpbreuer/Chandra_pipeline) created by [Jean-Paul Breuer](http://jpbreuer.com/aboutme.html)

Specail thanks to,\

Dr. Khan M B Asad\
Assistant Professor
Independent University, Bangladesh

Jean-Paul Breuer\
Masaryk University, Czech Republic

### Environment setup

Platform Support: Tested on Ubuntu 20.04.5 lts, Ubuntu 20.04.3 LTS server.


**1. Install Anaconda distribution.**

Follow the [Anaconda Installation page](https://docs.anaconda.com/anaconda/install/linux/) for installation.

**2. Installing CIAO with conda.**

- Run the following command in the terminal to install ciao, caldb and some associated software in a conda environment named “ciao-4.14” or anything you like.
```
conda create -n ciao-4.14 -c https://cxc.cfa.harvard.edu/conda/ciao -c conda-forge ciao sherpa ds9 ciao-contrib caldb marx jupyter jupyterlab numpy matplotlib astropy scipy scikit-learn pandas seaborn
```
- CALDB, acis_bkgrnd and hrc_bkgrnd file download might fail because of  ```CondaHTTPError: HTTP 000 CONNECTION FAILED for url``` error or slow internet connection. If this happens remove caldb from CIAO installation command and follow the [Alternative download instructions](https://cxc.cfa.harvard.edu/ciao/threads/ciao_install_conda/index.html#alt_download)

- Reference: [Installing CIAO with conda page](https://cxc.cfa.harvard.edu/ciao/threads/ciao_install_conda/)


**3. Download and install HEASOFT Software.**

- Go to the [HEASOFT installation page](https://heasarc.gsfc.nasa.gov/lheasoft/download.html)

- Select "Source Code" and select "PC - Linux - Ubuntu" from checkbox in STEP 1.

- Select all in STEP 2 and click submit.

- unzip or extract the .tar.gz file and follow the [INSTALLATION](https://heasarc.gsfc.nasa.gov/lheasoft/ubuntu.html) process to install HEASOFT.

- To make HEASOFT initialization easy I have created the following alias:

  In the terminal type the following:
  ```
  nano ~/.bashrc
  ```
  Paste the following command (replace the "heasoft-6.30.1" with downloaded heasoft folder name and "PLATFORM" with machine's architecture):

  ```
  alias heainit="export HEADAS=/path/to/your/installed/heasoft-6.30.1/(PLATFORM); . $HEADAS/headas-init.sh"
  ```
  To get the PLATFORM name:\
      Go inside the heasoft directory\
      Will see a folder named like "x86_64-pc-linux-gnu-libc2.31"\
      Copy the folder name\
      Replace PLATFORM placeholder with "x86_64-pc-linux-gnu-libc2.31"\



  Finale Initialization alias will look something like this:
  ```
  alias heainit="export HEADAS=/home/usr/software/heasoft-6.30.1/x86_64-pc-linux-gnu-libc2.31; . $HEADAS/headas-init.sh"
  ```
  save the ~/.bashrc.\
  run ```source ~/.bashrc```\
  Type ```heainit``` to initiate HEASOFT whenever needed.







**4. Install CFITSIO**

- Download CFITSIO from [here](https://heasarc.gsfc.nasa.gov/docs/software/fitsio/fitsio.html)

- Follow [this](https://www.gnu.org/software/gnuastro/manual/html_node/CFITSIO.html) instructions.


**5. Download and install Contour binning and accumulative smoothing software.**

- Open terminal and run the following:
```
git clone https://github.com/jeremysanders/contbin
```
- Go to the downloaded folder directory.
```
cd ~/Downloads/contbin
```
- Build:
```
make
```
- Copy the built program:
```
sudo make install 
```


**For server**\
- Open terminal and run the following:
```
git clone https://github.com/jeremysanders/contbin
```

- Create a ```local/bin``` directory in home directory:
```
mkdir -p local/bin
```

- Go to the ```contbin``` folder\
- Open MakeFile
```
nano MakeFile
```
- Set the ```bindir``` varaible path as the created local/bin path (e.g ```/home/usr/local/bin```)

- Build:
```
make
```
- Copy the built program:
```
sudo make install 
```

To learn more about [contbin](https://github.com/jeremysanders/contbin)

**6. Installing GNU parallel shell tool.(Not yet implemented)**

Run the following:
```
conda install -c conda-forge parallel
```

Reference:

[GNU parallel official page](https://www.gnu.org/software/parallel/)

[Anaconda parallel package link](https://anaconda.org/conda-forge/parallel) 




**7. Install SPEX software package.(Not yet implemented)**

Follow the SPEX installation guide from [here](https://spex-xray.github.io/spex-help/getstarted/install.html).


### Generating maps.

There are several python scripts (.py files). Running each script will generate a bash script (.sh file). 

**Step 0: Creating directories**

- Open directory.py.
- Edit following variables and create these directories manually. Replace the ```/home/zareef/minihalo/data/a2256``` path with yours.

```
cluster = '"a2256"'                              #replace 'a2256' with your cluster name
parentdir = '/home/zareef/minihalo/data/a2256'   #path where all the data will be stored   
```
- create additional directories inside data directory. Replace the ```/home/zareef/minihalo/data/a2256``` path with yours.
```
mkdir -p /home/zareef/minihalo/data/a2256/merged 
```
```
mkdir -p /home/zareef/minihalo/data/a2256/specfile_output
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
```
bash preprocessing.sh
```

**Step 6: Removing point source from merged image**
- Create a ```regionfiles``` folder to save region files. (Replace "/home/zareef/minihalo/data/a2256" with your data path. )
```
mkdir -p /home/zareef/minihalo/data/a2256/regionfiles
```
- Open ```broad_thresh.img``` with ds9. This file should be located inside ```merged``` folder.\
Replace the "/home/zareef/minihalo/data/a2256" path with yours.
```
ds9 /home/zareef/minihalo/data/a2256/merged
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
Save location: ```/home/zareef/minihalo/data/a2256/regionfiles```. Replace ```/home/zareef/minihalo/data/a2256``` with your data path. 


- Again open ```broad_thresh.img``` with ds9. Open ```square.reg``` from ```regionfiles```. Save this as min_xy.reg. Region file format:```Region - ciao```,```Coordinate System - physical```\

- Open the ```min_xy.reg``` using any text editor. You will see a region value which will look something like this:\
```box(3871.7065,3939.0178,1733.5429,1135.1521,0)```. These values will be different for your cluster data.\
x1 = 3871.7065\
y1 = 1733.5429\
x2 = 3939.0178\
y2 = 1135.1521\
Now do the following calculation,\
minx = x1 -(y1/2)\
miny = x2 -(y2/2)

- Open ```directory.py``` and replace the value of minx and miny with our calculated value.

- Run ```PreProcessing_source_crop.py```
```
python PreProcessing_source_crop.py
```
- Run generated ```preprocessing.sh```
```
bash preprocessing.sh
```

**Step 7: Run Preliminary_Products_contourbin.py**
```
python Preliminary_Products_contourbin.py
```
```
bash preliminary_products.sh
```

**Step 8: Converting region file coordinate system syntax**

- Create ```/home/zareef/minihalo/data/a2256/merged/contbin_sn70_smooth100/outreg/sex``` directory. (Replace ```/home/zareef/minihalo/data/a2256``` with your data path.)
```
mkdir -p /home/zareef/minihalo/data/a2256/merged/contbin_sn70_smooth100/outreg/sex
```
- Convert region file coordinate system syntax

```
python RegCoordChange.py
```
```
bash regcoordchange.sh
```

**Step 9: Pre fitting**

Running this will take a long time depending on the data. Code for running it on server will come in the next update. Future works includes adding CPU/GPU parallel processing. 

- Run Processing_pre_fitting.py
```
python Processing_pre_fitting.py
```
- Initialize ```heasoft``` using alias we created previously
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

will fix both in the next update.

**Step 10: Processing_xspecfitting.py**
- Run Processing_xspecfitting.py
```
python Processing_xspecfitting.py
```
- Go to ```specfile_output``` folder. You will find a file named```xspecfitting.sh```. Replace ```/home/zareef/minihalo/data/a2256/``` with your data path.
```
cd /home/zareef/minihalo/data/a2256/specfile_output
```
- run ```xspecfitting.sh```
```
bash xspecfitting.sh
```
- If you face following error just type ```exit``` and press Enter.

![xspecfitting_error_1](images/xspecfitting_error_1.png)

- This particular error will run endlessly. Just press ```Ctrl+C``` to stop it and type ```exit``` to continue.   

![xspecfitting_error_2](images/xspecfitting_error_2.png)


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

DONE!!!!!!!!

### Sample data, bash scripts and paper.

- All the generated data products including generated bash script and maps of Abell 2256 galaxy cluster using the pipeline: [drive](https://drive.google.com/drive/folders/15_onfxHnGdudMGuqgs3AC5pItJadYI8D?usp=share_link)

- This [paper](https://arxiv.org/pdf/2005.10263.pdf) by J. P. Breuer discusses about image analysis of this cluster.


### Additional Resources: 

Some resources which hepled me to work with this pipeline and also my ongoing work on detecting cold frontfrom galaxy clusters with potentail minihalo. 

- [Galaxy Clusters, ARGI] (http://abekta.iub.edu.bd/rs/gc)
- [A Brief Intro to the Chandra Mission by Jonathan McDowell](https://cxc.harvard.edu/ciao/workshop/jan21/jcm.ws21.pdf)
- [An X-ray Data Primer](https://cxc.harvard.edu/cdo/xray_primer.pdf)
- [X-ray spectroscopy of galaxy clusters: studying astrophysical processes in the largest celestial laboratories(https://link.springer.com/article/10.1007/s00159-009-0023-3)
- [Occurrence of Radio Minihalos in a Mass-limited Sample of Galaxy Clusters] (https://iopscience.iop.org/article/10.3847/1538-4357/aa7069/meta)
- [Expanding the Sample of Radio Minihalos in Galaxy Clusters] (https://iopscience.iop.org/article/10.3847/1538-4357/ab29f1/meta)
- [Diffuse Radio Emission from Galaxy Clusters] (https://link.springer.com/article/10.1007/s11214-019-0584-z)
- 

