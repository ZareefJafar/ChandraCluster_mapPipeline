
import PreProcessing_source_crop as psc
import directory as d
from astropy.io import fits
import re




'''
For getting the value of minx and miny create the following region file
- min_xy.reg: opnen broad_thresh.img in ds9 and open square.reg. Save this as min_xy.reg. Region : ciao, Coordinate System: physical

if value inside min_xy.reg is box(3871.7065,3939.0178,1733.5429,1135.1521,0)

x = 3871.7065-(1733.5429/2) = 3004.93505
y = 3939.0178-(1135.1521/2) = 3371.44175


save these three region files to    /home/zareef/minihalo/data/a2256/regionfiles
'''

hdul = fits.open(d.parentdir+'/merged/scaled_broad_flux_fov_sps.fits')
region=hdul[0].header['DSVAL1']
numbers = [float(x) for x in re.findall(r'-?\d+\.?\d*',region)]
print(numbers)
x1 = float(numbers[0])
x2 = float(numbers[1])
y1 = float(numbers[2])
y2 = float(numbers[3]) 

minx = x1-(y1/2)
miny = x2-(y2/2)

print("Region: "+region+"\nminx: "+str(minx)+"\nminy: "+str(miny))

file = open('preliminary_products.sh', 'w')
file.write('cd ' + d.parentdir +'/merged\n')
file.write("echo 'step 7. Contour Binning'\n")
contbin = 'contbin --sn=' + str(5) + ' --smoothsn=' + str(15) + ' --constrainfill --constrainval=3. scaled_broad_flux_fov_sps.fits\nmkdir contbin_sn' + str(d.sn_per_region) + '_smooth' + str(d.reg_smoothness) + '\nmkdir contbin_sn' + str(d.sn_per_region) + '_smooth' + str(d.reg_smoothness) + '/outreg\nmv bin_signal_stats.qdp bin_sn_stats.qdp contbin_binmap.fits contbin_mask.fits contbin_out.fits contbin_sn.fits contbin_sn' + str(d.sn_per_region) + '_smooth' + str(d.reg_smoothness) + '\ncd contbin_sn' + str(d.sn_per_region) + '_smooth' + str(d.reg_smoothness) + '\n'
mkregions = 'make_region_files --minx=' + str(minx) + ' --miny=' + str(miny) + ' --bin=1 --outdir=outreg contbin_binmap.fits\n'
file.write(contbin)
file.write(mkregions)
#_RegCoordChange(parentdir + '/merged/contbin_sn' + str(sn_per_region) + '_smooth' + str(reg_smoothness) + '/outreg')
file.write('cd ' + d.parentdir +'/merged/\n')
file.write("echo 'step 7. Contour Binning... Done!'\n\n")
file.close()

#sn=70, smoothsn=100