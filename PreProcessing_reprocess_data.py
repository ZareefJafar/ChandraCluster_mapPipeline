
import directory as d
import PreProcessing_download_data as pdd
import os



file = open('preprocessing.sh', 'w')
file.write("echo 'step2. Reprocess Data'\n")
file.write('cd ' + d.parentdir + '\n')
mode_obsid = []
for ii in list(range(len(pdd.obsids))):
    file.write('rm -rf ' + pdd.obsids[ii] + '/repro\n')
    mode_obsid.append(os.popen('dmkeypar ' + d.parentdir + '/' + pdd.obsids[ii] + '/primary/*evt2.fits.gz DATAMODE echo+').read().split()[0])
    #file.write('dmkeypar ' + obsids[ii] + '/primary/*evt2.fits.gz DATAMODE echo+')
    #mode_obsid = mode_obsid.split()
    #file.write(str(mode_obsid))
    if mode_obsid[ii] == 'VFAINT':
        reprodata = 'chandra_repro ' + pdd.obsids[ii] + ' outdir= check_vf_pha=yes verbose=1 clobber=yes'
    else:
        reprodata = 'chandra_repro ' + pdd.obsids[ii] + ' outdir= verbose=1 clobber=yes'
    file.write('punlearn ardlib\n')
    file.write(reprodata + '\n')
file.write("echo 'step2. Reprocess Data... Done!'\n\n")
file.close()