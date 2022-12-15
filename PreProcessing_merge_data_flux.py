
import directory as d


from astropy.io import fits
import numpy as np






def _mkmap(input,output,head):
    #hdu = fits.PrimaryHDU(input)
    fits.writeto(output,input,head,overwrite=True)

fluxim = fits.open(d.parentdir + '/merged/broad_flux.img')
fluxhdr = fluxim[0].header
fluximdata = fluxim[0].data
threshim = fits.open(d.parentdir + '/merged/broad_thresh.img')
#        threshhdr = threshim[0].header
threshimdata = threshim[0].data
expoim = fits.open(d.parentdir + '/merged/broad_thresh.expmap')
expohd = expoim[0].header
expoimdata = expoim[0].data

threshsum = np.sum(threshimdata)
fluxsum = np.sum(fluximdata)
threshav = threshsum/len(threshimdata)
#        fluxav = fluxsum/len(fluximdata)
#        scaledflux = (fluximdata*(threshav/fluxav))#(threshav/fluxav)
#        _mkmap(scaledflux*28*(np.amax(threshimdata)/np.amax(scaledflux)),parentdir + '/merged/scaled_broad_flux.fits',fluxhdr)
fluxav = fluxsum/len(fluximdata)
scaledflux = (2.5*fluximdata*(threshav/fluxav))#(threshav/fluxav)
_mkmap(scaledflux,d.parentdir + '/merged/scaled_broad_flux.fits',fluxhdr)

print("step5. Merged X-ray surface brightness map created.\nNow run following command to create region files\nds9 "+ d.parentdir+"/merged/broad_thresh.img")