
import bin_region_directories as brd
import directory as d
import subprocess


def CleanUp(output):
    subprocess.run('mkdir ' + output, shell=True)
#    subprocess.run('cp *.fits *.data *.png ' + output, shell=True)
    subprocess.run('cp regions-info-xspec.data regions-info-xspec-sn' + str(d.sn_per_region) + '.data', shell=True)
    subprocess.run('cp regions-info-xspec-sn' + str(d.sn_per_region) + '.data ' + output, shell=True)


CleanUp(brd.mapsdir)