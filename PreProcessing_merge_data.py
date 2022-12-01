

import directory as d



file = open('preprocessing.sh', 'w')
file.write("echo 'step4. Merge all Observations'\n")
file.write('cd ' + d.parentdir + '\n')
file.write('find "$(pwd)" -name "acisf*clean*" > cleanevt2.list\n')
file.write('punlearn merge_obs\nmerge_obs @cleanevt2.list ' + d.parentdir + '/merged/ bin=1 bands=broad,csc clobber=yes\n')
file.write("echo 'Merge all Observations... Done!'\n\n")
#file.write("echo 'Combining all observation pointsource region files'\n")
#file.write('ds9 ' + parentdir +'/merged/broad_thresh.img &\nsleep 10\nxpaset -p ds9 lower\n')
#for ii in list(range(len(obsids))): 
#    file.write('xpaset -p ds9 regions load ' + parentdir + '/' + obsids[ii] + '/repro/pointsources.fits\n')
#file.write('xpaset -p ds9 regions format ciao\nxpaset -p ds9 regions system wcs\nxpaset -p ds9 regions skyformat sexagesimal\nxpaset -p ds9 regions save ' + parentdir + '/merged/pointsources_combo.fits\nxpaset -p ds9 exit\n')
#file.write("echo 'Combining all observation pointsource regionfiles... Done!'\n\n")
file.close()


