

import bin_region_directories as brd
import directory as d

def _RegCoordChange(inputdir):
    file2 = open('regcoordchange.sh', 'w')
    file2.write("echo 'step8. Converting region file coordinate system syntax'\n")
    #file2.write('mkdir ' + d.parentdir + '/merged/contbin_sn' + str(d.sn_per_region) + '_smooth' + str(d.reg_smoothness) + '/outreg/sex/\n')
    file2.write('ds9 ' + d.parentdir +'/merged/scaled_broad_flux_fov_sps.fits &\nsleep 10\nxpaset -p ds9 lower\n')
    for ii in list(range(brd.regnum)): 
        file2.write('xpaset -p ds9 regions load ' + inputdir + '/xaf_' + str(ii) + '.reg\nxpaset -p ds9 regions format ciao\nxpaset -p ds9 regions system wcs\nxpaset -p ds9 regions skyformat sexagesimal\nxpaset -p ds9 regions save ' + inputdir + '/sex/xaf_' + str(ii) + '_sex.reg\nxpaset -p ds9 regions delete all\n')
    file2.write('xpaset -p ds9 exit\n\n')
    file2.write("echo 'step8. Converting region file coordinate system syntax... Done!'\n\n")
    file2.close()


_RegCoordChange(d.parentdir + '/merged/contbin_sn' + str(d.sn_per_region) + '_smooth' + str(d.reg_smoothness) + '/outreg')