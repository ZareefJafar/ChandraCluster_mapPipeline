
import directory as d
import PreProcessing_download_data as pdd
import PreProcessing_reprocess_data as prd

import os


file = open('preprocessing.sh', 'w')
file.write("echo 'step3. Extract Light Curves for Deflaring'\n")
file.write('cd ' + d.parentdir + '\n')
for ii in list(range(len(pdd.obsids))):
    file.write('cd '+ d.parentdir + '/' + pdd.obsids[ii] + '\n')
    bpix = os.popen('ls ' + d.parentdir + '/' + pdd.obsids[ii] + '/repro/*repro_bpix1*').read()
    file.write('punlearn ardlib\nacis_set_ardlib ' + bpix + '\n')
    file.write('punlearn fluximage\nfluximage repro/ repro/' + pdd.obsids[ii] + ' binsize=1 bands=0.5:7:2.3 clobber=yes\n')
    file.write('cd repro\n')
    file.write('punlearn mkpsfmap\nmkpsfmap ' + pdd.obsids[ii] + '_0.5-7_thresh.img outfile=' + pdd.obsids[ii] + '_0.5-7.psf energy=2.3 ecf=0.9 clobber=yes\n')
    file.write('punlearn wavdetect\nwavdetect infile=' + pdd.obsids[ii] + '_0.5-7_thresh.img psffile=' + pdd.obsids[ii] + '_0.5-7.psf expfile=' + pdd.obsids[ii] + '_0.5-7_thresh.expmap outfile=src_0.5-7.fits scellfile=scell_0.5-7.fits imagefile=imgfile_0.5-7.fits defnbkgfile=nbkg_0.5-7.fits regfile=' + pdd.obsids[ii] + '_src_0.5-7-noem.reg scales="1 2 4 8 16 32" maxiter=3 sigthresh=5e-6 ellsigma=5.0 clobber=yes\n\n')
    file.write("echo 'Made regions... Done!'\n")
    file.write("echo 'CHECK REGLIST AND REMOVE ALL POINT SOURCES AS WELL AS CLUSTER EMISSION'\n\n")
    
    file.write("echo 'Make GTI for deflaring observations'\n\n")
#            file.write('punlearn dmcopy\ndmcopy "acisf' + obsids_padded[ii] + '_repro_evt2.fits[exclude sky=region(' + no_emission_reg + ')]" ' + obsids[ii] + '_nosources.evt option=all clobber=yes\n')
    file.write('punlearn dmcopy\ndmcopy "acisf' + pdd.obsids_padded[ii] + '_repro_evt2.fits[exclude sky=region(' + pdd.obsids[ii] + '_src_0.5-7-noem.reg)]" ' + pdd.obsids[ii] + '_nosources.evt option=all clobber=yes\n')
    file.write('punlearn dmcopy\ndmcopy "' + pdd.obsids[ii] + '_nosources.evt[energy=500:7000]" ' + pdd.obsids[ii] + '_0.5-7_nosources.evt option=all clobber=yes\n')
    file.write('punlearn dmextract\ndmextract "' + pdd.obsids[ii] + '_0.5-7_nosources.evt[bin time=::259.28]" ' + pdd.obsids[ii] + '_0.5-7.lc opt=ltc1 clobber=yes\n')
    file.write('punlearn deflare\ndeflare ' + pdd.obsids[ii] + '_0.5-7.lc ' + pdd.obsids[ii] + '_0.5-7.gti method=clean\n')
    file.write('punlearn dmcopy\ndmcopy "acisf' + pdd.obsids_padded[ii] + '_repro_evt2.fits[@' + pdd.obsids[ii] + '_0.5-7.gti]" acisf' + pdd.obsids_padded[ii] + '_clean_evt.fits opt=all clobber=yes\n\n')
    file.write("echo 'Make background with GTI'\n\n")
    #prd.mode_obsid.append(os.popen('dmkeypar ' + d.parentdir + '/' + pdd.obsids[ii] + '/primary/*evt2.fits.gz DATAMODE echo+').read().split())
    if prd.mode_obsid[ii] == 'VFAINT':
        file.write('punlearn blanksky\nblanksky evtfile="acisf' + pdd.obsids_padded[ii] + '_repro_evt2.fits[@' + pdd.obsids[ii] + '_0.5-7.gti]" outfile=' + pdd.obsids[ii] + '_vfbackground_clean.evt tmpdir=./ clobber=yes\n')
        file.write('punlearn dmcopy\ndmcopy "' + pdd.obsids[ii] + '_vfbackground_clean.evt[status=0]" ' + pdd.obsids[ii] + '_background_clean.evt clobber=yes\n\n')
    else:
        file.write('punlearn blanksky\nblanksky evtfile="acisf' + pdd.obsids_padded[ii] + '_repro_evt2.fits[@' + pdd.obsids[ii] + '_0.5-7.gti]" outfile=' + pdd.obsids[ii] + '_background_clean.evt tmpdir=./ clobber=yes\n')
#                os.popen('dmkeypar(infile="acisf' + obsids_padded[ii] + '_repro_evt2.fits" key="OBS_ID" echo=yes)').read()
    file.write('dmhedit infile="' + pdd.obsids[ii] + '_background_clean.evt" filelist=none key="OBS_ID" value="' + pdd.obsids[ii] + '" operation="add"\n')
    file.write('blanksky_image bkgfile=' + pdd.obsids[ii] + '_background_clean.evt outroot=' + pdd.obsids[ii] + '_blank imgfile=' + pdd.obsids[ii] + '_0.5-7_thresh.img tmpdir=./ clobber=yes\n\n')
file.close()