
import directory as d
import os



def FindData(input):
    obsids_search = os.popen('find_chandra_obsid ' + input).read().split('\n')
    obsids = []; obsids_padded = [];
    for ii in list(range(len(obsids_search)-2)):
        obsids.append(obsids_search[ii+1].split()[0])
        obsids_padded.append(format(int(obsids_search[ii+1].split()[0]), '05d'))
    obsids_fullstr = ','.join(map(str, obsids)) 
    return obsids, obsids_padded, obsids_fullstr

obsids, obsids_padded, obsids_fullstr = FindData(d.cluster)


# could not deflare 965
# 1386 missing background for ccd8 - removed
#######################
obsids = obsids[3:]
obsids_padded = obsids_padded[3:]
obsids_fullstr = ','.join(map(str, obsids)) 
#######################
###--- OPTIONAL --->
#obsids = ['2419','16129','16514','16515','16516']
#obsids_padded = ['02419','16129','16514','16515','16516']
#obsid_fullstr = '02419 16129 16514 16515 16516'
#######################





file = open('preprocessing.sh', 'w')
file.write("echo 'step1. Download Data'\n")
file.write('cd ' + d.parentdir + '\n')
dldata = 'download_chandra_obsid ' + obsids_fullstr
file.write(dldata + '\n')
file.write("echo 'step1. Download Data... Done!'\n\n")
file.close()