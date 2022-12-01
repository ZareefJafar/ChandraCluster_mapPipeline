
'''

Open broad_thresh.img inside merged folder using ds9  and create following region files:



- src_0.5-7-nps-noem.reg:   A region file that contains all cluster emission (eg. a large circle around the cluster that includes the extended emission, 
                            which will be removed and used for the deflaring/high energy rescaling). This would include areas such as the peak of cluster emission as these regions 
                            may contain high energy events you want to consider in this analysis.


- broad_src_0.5-7-pointsources.reg:   A region file that contains all of the pointsources.

- square.reg:   This will eventually crop out all things outside of the region of interest. 


for these three region files
Region : ciao 
Coordinate System: wcs



For getting the value of minx and miny create the following region file
- min_xy.reg: opnen broad_thresh.img in ds9 and open square.reg. Save this as min_xy.reg. Region : ciao, Coordinate System: physical

if value inside min_xy.reg is box(3871.7065,3939.0178,1733.5429,1135.1521,0)

x = 3871.7065-(1733.5429/2) = 3004.93505
y = 3939.0178-(1135.1521/2) = 3371.44175


save these three region files to    /home/zareef/minihalo/data/a2256/regionfiles

'''




import directory as d


minx = 3004.93505; miny = 3371.44175

def main():
    #input no emission region, pointsources region, desired fov subset region 
    PreProcessing_source_crop(d.no_emission,d.no_pointsources,d.fov_name)
    #run ./preprocessing.sh




def PreProcessing_source_crop(no_emission_reg,pointsources_reg,fov):
    file = open('preprocessing.sh', 'w')
    file.write("echo 'CHECK SCALING OF SCALED FLUX IMG WITH THRESHOLD'\n")
    file.write("echo 'Removing Point Sources'\n")
    file.write('cd ' + d.parentdir +'/merged\n')
    file.write('wavdetect infile=broad_thresh.img psffile=none expfile=broad_thresh.expmap outfile=src_0.5-7.fits scellfile=scell_0.5-7.fits imagefile=imgfile_0.5-7.fits defnbkgfile=nbkg_0.5-7.fits regfile=broad_src_0.5-7.reg scales="1 2 4 8 16 32" maxiter=3 sigthresh=5e-6 ellsigma=5.0 clobber=yes\n\n')
    file.write("echo 'CHECK AND CORRECT THE POINT SOURCE REGIONS'\n\n")
    #        file.write('dmcopy "broad_thresh.img[exclude sky=region(' + pointsources_reg + ')]" broad_thresh_sps.fits clobber=yes\n')
    file.write('dmcopy "scaled_broad_flux.fits[exclude sky=region(' + pointsources_reg + ')]" scaled_broad_flux_sps.fits clobber=yes\n')
    file.write("echo 'Removing Point Sources... Done!'\n\n")

    if fov:
        file.write("echo 'Reducing FOV to specific region'\n")
    #            file.write('dmcopy "broad_thresh_sps.fits[sky=region(' + fov + ')]" broad_thresh_square_sps.fits clobber=yes\n')
        file.write('dmcopy "scaled_broad_flux_sps.fits[sky=region(' + fov + ')]" scaled_broad_flux_fov_sps.fits clobber=yes\n')
        file.write("echo 'Reducing FOV to specific region... Done!'\n\n")
    else:
        file.write("echo 'Renaming broad_thresh'\n")
        file.write('mv broad_thresh_sps.fits broad_thresh_square_sps.fits\n')
        file.write("echo 'broad_thresh_sps now broad_thresh_square_sps'\n")  

    file.close()



if __name__ == '__main__':
    main()