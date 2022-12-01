
import PreProcessing_source_crop as psc
import directory as d




file = open('preliminary_products.sh', 'w')
file.write('cd ' + d.parentdir +'/merged\n')
file.write("echo 'step 7. Contour Binning'\n")
contbin = 'contbin --sn=' + str(d.sn_per_region) + ' --smoothsn=' + str(d.reg_smoothness) + ' --constrainfill --constrainval=3. scaled_broad_flux_fov_sps.fits\nmkdir contbin_sn' + str(d.sn_per_region) + '_smooth' + str(d.reg_smoothness) + '\nmkdir contbin_sn' + str(d.sn_per_region) + '_smooth' + str(d.reg_smoothness) + '/outreg\nmv bin_signal_stats.qdp bin_sn_stats.qdp contbin_binmap.fits contbin_mask.fits contbin_out.fits contbin_sn.fits contbin_sn' + str(d.sn_per_region) + '_smooth' + str(d.reg_smoothness) + '\ncd contbin_sn' + str(d.sn_per_region) + '_smooth' + str(d.reg_smoothness) + '\n'
mkregions = 'make_region_files --minx=' + str(psc.minx) + ' --miny=' + str(psc.miny) + ' --bin=1 --outdir=outreg contbin_binmap.fits\n'
file.write(contbin)
file.write(mkregions)
#_RegCoordChange(parentdir + '/merged/contbin_sn' + str(sn_per_region) + '_smooth' + str(reg_smoothness) + '/outreg')
file.write('cd ' + d.parentdir +'/merged/\n')
file.write("echo 'step 7. Contour Binning... Done!'\n\n")
file.close()