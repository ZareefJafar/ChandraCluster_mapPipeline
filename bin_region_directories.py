

import directory as d
import os

###--- Some New Variables---> should not need to touch
contbindir = d.parentdir +'/merged/contbin_sn' + str(d.sn_per_region) + '_smooth' + str(d.reg_smoothness) + ''
regdir = contbindir + '/outreg'
regnum = int(os.popen('ls -1 ' + regdir + '| grep -v / | wc -l').read())-1 # this gets the number of non directory files in the regdir folder
sexdir = regdir + '/sex'
sexnum = int(os.popen('ls -1 ' + sexdir + '| grep -v / | wc -l').read())
binmap = contbindir + '/contbin_binmap.fits'
resultsdir = d.specfile_outputdir + '/results_sn' + str(d.sn_per_region) + '_smooth' + str(d.reg_smoothness)
compresseddir = d.specfile_outputdir + '/compressed_sn' + str(d.sn_per_region) + '_smooth' + str(d.reg_smoothness)
mapsdir = resultsdir + '/maps'