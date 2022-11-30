Pipeline to create x-ray temeprature maps, pressure maps, surface brightness maps, and density maps of from [Chandra Data Archive](https://cda.harvard.edu/chaser/) of galaxy clusters.

This pipeline is based on a [pipeline](https://github.com/jpbreuer/Chandra_pipeline) created by [Jean-Paul Breuer](http://jpbreuer.com/aboutme.html)



### Environment setup

Platform Support: Tested on Ubuntu 20.04.5 lts, Ubuntu 20.04.3 LTS server.


**1. Install Anaconda distribution.**

Follow the [Anaconda Installation page](https://docs.anaconda.com/anaconda/install/linux/) for installation.

**2. Installing CIAO with conda.**

Run the following command in the terminal to install ciao, caldb and some associated software in a conda environment named “ciao-4.14” or anything you like.
```
conda create -n ciao-4.14 -c https://cxc.cfa.harvard.edu/conda/ciao -c conda-forge ciao sherpa ds9 ciao-contrib caldb marx jupyter jupyterlab numpy matplotlib astropy scipy scikit-learn pandas seaborn
```
CALDB, acis_bkgrnd and hrc_bkgrnd file download might fail because of  ```CondaHTTPError: HTTP 000 CONNECTION FAILED for url``` error or slow internet connection. If this happens remove caldb from CIAO installation command and follow the [Alternative download instructions](https://cxc.cfa.harvard.edu/ciao/threads/ciao_install_conda/index.html#alt_download)

See the [Installing CIAO with conda page](https://cxc.cfa.harvard.edu/ciao/threads/ciao_install_conda/) to know more.


**3. Download and install HEASOFT Software.**

-Go to the [HEASOFT installation page](https://heasarc.gsfc.nasa.gov/lheasoft/download.html)

-Select "Source Code" and select "PC - Linux - Ubuntu" from checkbox in STEP 1.

-Select all in STEP 2 and click submit.

-unzip or extract the .tar.gz file and follow the [INSTALLATION](https://heasarc.gsfc.nasa.gov/lheasoft/ubuntu.html) process to install HEASOFT.

-To make initialization easy I have created the following alias:

  In the terminal type the following:
  ```
  nano ~/.bashrc
  ```
  Paste the following command (replace the "heasoft-6.30.1" with downloaded heasoft folder name and "PLATFORM" with machine's architecture):

  ```
  alias heainit="export HEADAS=/path/to/your/installed/heasoft-6.30.1/(PLATFORM); . $HEADAS/headas-init.sh"
  ```
  To get the PLATFORM name:\
  -Go inside the heasoft directory\
  -Will see a folder named like "x86_64-pc-linux-gnu-libc2.31"\
  -Copy the folder name\
  -Replace PLATFORM placeholder with "x86_64-pc-linux-gnu-libc2.31"\



  Finale Initialization alias will look something like this:
  ```
  alias heainit="export HEADAS=/home/usr/software/heasoft-6.30.1/x86_64-pc-linux-gnu-libc2.31; . $HEADAS/headas-init.sh"
  ```
  save the ~/.bashrc.\
  run ```source ~/.bashrc```\
  Type ```heainit``` to initiate HEASOFT whenever needed.







**4.Install CFITSIO**

-Download CFITSIO from [here](https://heasarc.gsfc.nasa.gov/docs/software/fitsio/fitsio.html)

-Follow [this](https://www.gnu.org/software/gnuastro/manual/html_node/CFITSIO.html) instructions.


**5. Download and install Contour binning and accumulative smoothing software.**

-Open terminal and run the following:
```
git clone https://github.com/jeremysanders/contbin
```
-Go to the downloaded folder directory.
```
cd ~/Downloads/contbin
```
-Build:
```
make
```
-Copy the built program:
```
sudo make install 
```


**For server**\
-Open terminal and run the following:
```
git clone https://github.com/jeremysanders/contbin
```

-Create a ```local/bin``` directory in home directory:
```
mkdir -p local/bin
```

-Go to the ```contbin``` folder\
-Open MakeFile
```
nano MakeFile
```
-Set the ```bindir``` varaible path as the created local/bin path (e.g ```/home/usr/local/bin```)

-Build:
```
make
```
-Copy the built program:
```
sudo make install 
```

Learn more about [contbin](https://github.com/jeremysanders/contbin)

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

1. directory.py

- Open directory.py.
- Edit and create following directories:

```
cluster = '"a2256"'                              #replace 'a2256' with your cluster name
parentdir = '/home/zareef/minihalo/data/a2256'   #path where all the data will be stored   
specfile_outputdir = parentdir + '/specfile_output'  # create specfile_output folder 
```

Use the following command to run the Spectral Fitting (e.g. pre-fitting.sh file) in parallel
```
parallel -a ./pre-fitting.sh 
```

See the tutorial by [freeCodeCamp](https://www.freecodecamp.org/news/how-to-supercharge-your-bash-workflows-with-gnu-parallel-53aab0aea141/) for details.


