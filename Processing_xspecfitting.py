
import bin_region_directories as brd
import directory as d
import PreProcessing_download_data as pdd
import subprocess




file2 = open('xspecfitting.sh', 'w')
file2.write('mkdir ' + brd.resultsdir + '/xspec\n')
#    file2.write('cp xspecfitting.sh ' + specfile_outputdir + '\n')
for ii in list(range(brd.sexnum)):#len(obsids)
    file3 = open(d.specfile_outputdir + '/reg_' + str(ii) + '_xspec_fit.script','w')
#        file3.write('xspec << EOF\n')
    file3.write('statistic cstat\nsetplot energy\ncpd ' + brd.resultsdir + '/xspec/reg_' + str(ii) + '_xspec_fit.ps/cps\n\n')
    for jj in list(range(len(pdd.obsids))): #regnum
        file3.write('data ' + str(jj+1) + ':' + str(jj+1) + ' ' + d.specfile_outputdir + '/xaf_' + pdd.obsids[jj] + '_' + str(ii) + '.grp\n/*\n')
        file3.write('ig ' + str(jj+1) + ':' + str(jj+1) + ' bad\nig ' + str(jj+1) + ':' + str(jj+1) + ' **-0.5 7.5-**\n')
    file3.write('\nmo phabs(apec)\n/*\nnewpar 1 0.041 -1\nnewpar 2 5.\nnewpar 3 0.3\nnewpar 4 0.058100 -1\nquery yes\nfit\nsetplot back\nfit\npl ld res\n\n')
    file3.write('set fileall [open ' + brd.resultsdir + '/xspec/reg_' + str(ii) + '_data.xcm w 0600]\n')
    file3.write('tclout param 1\nscan $xspec_tclout "%f" nh\ntclout param 2\nscan $xspec_tclout "%f" temp\nerror 1. 2\ntclout error 2\nscan $xspec_tclout "%f %f" temp_low temp_high\ntclout param 3\nscan $xspec_tclout "%f" abundance\nerror 1. 3\ntclout error 3\nscan $xspec_tclout "%f %f" abundance_low abundance_high\ntclout param 4\nscan $xspec_tclout "%f" redshift\ntclout param 5\nscan $xspec_tclout "%f" norm1\nerror 1. 5\ntclout error 5\nscan $xspec_tclout "%f %f" norm1_low norm1_high\ntclout stat\nscan $xspec_tclout "%f" chi\ntclout dof\nscan $xspec_tclout "%f" dof\n')
    file3.write('puts $fileall "$nh $temp $temp_low $temp_high $abundance $abundance_low $abundance_high $redshift $norm1 $norm1_low $norm1_high $chi $dof"\nclose $fileall\n\n')
    file3.write('cpd none\nsave all ' + brd.resultsdir + '/xspec/reg_' + str(ii) + '_savestate.tcl\nquit y\n')
#        file3.write('EOF\n\n')
    file3.close()
    file2.write('xspec - reg_' + str(ii) + '_xspec_fit.script\n')
file2.close()

#file.write('cp spexfitting.sh ' + specfile_outputdir + '/\n')
#file.write('cp spexoutparsing.py ' + specfile_outputdir + '/results\n')
#file.write('cp mkmaps.py ' + specfile_outputdir + '/results\n')
#file.write('cd ' + specfile_outputdir + '/\n')

subprocess.run('cp xspecfitting.sh ' + d.specfile_outputdir, shell=True)