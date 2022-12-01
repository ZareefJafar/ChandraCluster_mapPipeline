

import bin_region_directories as brd
import directory as d
import PreProcessing_download_data as pdd

def Processing(inputdir):
    #    obsids, obsids_padded, obsids_fullstr = _FindData(cluster)
    file = open('pre-fitting.sh', 'w')
    file.write('mkdir ' + brd.compresseddir + '\nmkdir ' + brd.resultsdir + '\n')
    file.write('rm ' + d.specfile_outputdir + '/*.res ' + d.specfile_outputdir + '/*.spo\n')
    file.write('rm *.arf *.rmf *.pi *.grp\n\n')

    x = 0
    # Loops for taking the relevant Chandra files for grouping and eventually making spectral fits out of them
    for ii in list(range(brd.sexnum)): #len(obsids)
        for jj in list(range(len(pdd.obsids))): #regnum
            file.write("echo 'Observation " + pdd.obsids[jj] + " (" + str(jj+1) + "/" + str(len(pdd.obsids)) + ") Region " + str(ii) + " (" + str(ii+1) + "/" + str(brd.sexnum) + ")'\n")
            file.write("echo 'Extract region of interest, spectra, rmf, arf, background spectra'\n")

            file.write('cd ' + d.specfile_outputdir + '\n\n')
            file.write('punlearn specextract\n')
            infile = 'infile="' + d.parentdir + '/' + pdd.obsids[jj] + '/repro/acisf' + pdd.obsids_padded[jj] + '_clean_evt.fits[sky=region(' + inputdir +'/xaf_' + str(ii) + '_sex.reg)]" '
            bkgfile = 'bkgfile="' + d.parentdir + '/' + pdd.obsids[jj] + '/repro/' + pdd.obsids[jj] + '_background_clean.evt[sky=region(' + inputdir +'/xaf_' + str(ii) + '_sex.reg)]" '
            outroot = 'outroot=' + d.specfile_outputdir + '/xaf_' + pdd.obsids[jj] + '_' + str(ii) + ' '
            bkgresp = 'bkgresp=no ' #no = subtract background; yes = model background using arf and rmf
            weight_rmf = 'weight_rmf=yes '
            binspec = 'binspec=1 '
            
            file.write('specextract ' + infile + outroot + bkgfile + bkgresp + weight_rmf + binspec + 'verbose=1 clobber=yes\n\n')

            file.write('grppha xaf_' + pdd.obsids[jj] + '_' + str(ii) + '.pi xaf_' + pdd.obsids[jj] + '_' + str(ii) + '.grp "chkey RESPFILE xaf_' + pdd.obsids[jj] + '_' + str(ii) + '.rmf & chkey ANCRFILE xaf_' + pdd.obsids[jj] + '_' + str(ii) + '.arf & chkey BACKFILE xaf_' + pdd.obsids[jj] + '_' + str(ii) + '_bkg.pi & group min 1 & exit"\n\n')#chkey backfile ' + backfile + ' exit"\n\n')
    #            file.write("echo 'STOP HERE TO MAKE SURE TRAFO IS CONFIGURED PROPERLY'\n\n\n\n")
            if d.SPEX:
                file.write("echo 'Converting files into SPEX format using trafo.sh'\n\n")
                file.write('if [ -e xaf_' + pdd.obsids[jj] + '_' + str(ii) + '.grp ]; then\ntrafo << EOF\n1\n1\n10000\n1\nxaf_' + pdd.obsids[jj] + '_' + str(ii) + '.grp\ny\ny\n0\nxaf_' + pdd.obsids[jj] + '_' + str(ii) + '\nxaf_' + pdd.obsids[jj] + '_' + str(ii) + '\nEOF\nfi\n')
            
            file.write('tar -cf xaf_' + pdd.obsids[jj] + '_' + str(ii) + '.tar *' + pdd.obsids[jj] + '_' + str(ii) + '*\n')
            file.write('gzip xaf_' + pdd.obsids[jj] + '_' + str(ii) + '.tar\n')

            file.write('mv xaf_' + pdd.obsids[jj] + '_' + str(ii) + '.tar.gz ' + brd.compresseddir + '\n\n')
    #            file.write('cp *.res *.spo '+ specfile_outputdir + '\n')
    #            file.write('rm *.arf *.pi *.rmf\n')

            x = x+1
            file.write("echo 'Observation " + pdd.obsids[jj] + " (" + str(jj+1) + "/" + str(len(pdd.obsids)) + ") Region " + str(ii) + " (" + str(ii+1) + "/" + str(brd.sexnum) + ") [..." + str((x/(len(pdd.obsids)*brd.sexnum-1))*100) + "% Done!]'\n\n")
    file.close()

Processing(brd.sexdir)