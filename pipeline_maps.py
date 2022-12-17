



import directory as d
import pandas as pd
from astropy.io import fits
import numpy as np


binmap = d.parentdir + '/merged/contbin_sn' + str(d.sn_per_region) + '_smooth' + str(d.reg_smoothness) + '/contbin_binmap.fits'



XSPEC= True










def _mkmap(input,output,head):
    #hdu = fits.PrimaryHDU(input)
    output = d.mapDirec+'/'+output
    fits.writeto(output,input,head,overwrite=True)


def MakeBasicMaps(inputdata,binmap):
       
    if XSPEC:
        data = pd.read_csv(inputdata, delimiter=' ', index_col=0)
#        mapdata = data[0:168]
        mapdata = data
        region = [];nh = [];temp=[];temp_low=[];temp_high=[];temp_error_low=[];temp_error_high=[];temp_error_diff=[]
        abund=[];abund_low=[];abund_high=[];abund_error_low=[];abund_error_high=[];abund_error_diff=[];redshift=[]
        norm=[];norm_low=[];norm_high=[];norm_error_low=[];norm_error_high=[];norm_error_diff=[]
        chi=[];dof=[];chi2=[]
        for index,row in mapdata.iterrows():
            region.append(index)
            nh.append(round(row['nH'],4))
            temp.append(round(row['temperature'],4))
            temp_low.append(round(row['temp_low'],4))
            temp_high.append(round(row['temp_high'],4))
            temp_error_low.append(round(row['temp_error_low'],4))
            temp_error_high.append(round(row['temp_error_high'],4))
            temp_error_diff.append(round(row['temp_error_diff'],4))
            abund.append(round(row['abundance'],4))
            abund_low.append(round(row['abund_low'],4))
            abund_high.append(round(row['abund_high'],4))
            abund_error_low.append(round(row['abund_error_low'],4))
            abund_error_high.append(round(row['abund_error_high'],4))
            abund_error_diff.append(round(row['abund_error_diff'],4))
            redshift.append(round(row['redshift'],4))
            norm.append(round(row['norm'],4))
            norm_low.append(round(row['norm_low'],4))
            norm_high.append(round(row['norm_high'],4))
            norm_error_low.append(round(row['norm_error_low'],4))
            norm_error_high.append(round(row['norm_error_high'],4))
            norm_error_diff.append(round(row['norm_error_diff'],4))
            chi.append(round(row['chi'],4))
            dof.append(round(row['dof'],4))
            chi2.append(round(row['chi2'],4))
            
#    LoadData(inputdata)
    #IMAGE DATA
    im = fits.open(binmap)
    hdr = im[0].header
    imdata = im[0].data
    #we = wcs.WCS(hdr)
    
    
    def _printmap2(input,output):
        f = plt.figure()
        plt.subplot(111, projection=wcs)
        plt.imshow(input, origin='lower', cmap=plt.cm.viridis)
        ax = plt.subplot(projection=wcs)
        ax.imshow(input, origin='lower', cmap=plt.cm.viridis)
        ax.coords.grid(True, color='white', ls='solid')
        ax.coords[0].set_axislabel('Galactic Longitude')
        ax.coords[1].set_axislabel('Galactic Latitude')
        overlay = ax.get_coords_overlay('fk5')
        overlay.grid(color='white', ls='dotted')
        overlay[0].set_axislabel('Right Ascension (J2000)')
        overlay[1].set_axislabel('Declination (J2000)')
        f.savefig(output, bbox_inches='tight')
    
    ## NORM MAPS
    boolmask = [];region_pixsum = []
    for ii in region:
        imreg = imdata == ii
        region_pixsum.append(np.count_nonzero(imreg.astype(np.int)))
        boolmask.append(((imreg.astype(np.int))*norm[ii]/region_pixsum[ii]))
#        boolmask.append(((621.5*621.5*1000*(3.086*10**(21))*1.18*(1.67*10**(-27))*(imreg.astype(np.int))*norm[ii]/region_pixsum[ii])))
        #621.5*621.5*1000: volume kpc to cm, 621.5*621.5*1000*(3.086*10**(21)): particle number density*mean molecular weight in proton mass units 
#        boolmask.append(n_e*(imreg.astype(np.int)))
        
    normmap = sum(boolmask)
    _mkmap(normmap,"norm_map.fits",hdr)
    #_printmap(normmap,"norm_map.pdf")
    
    boolmask = [];region_pixsum = []
    for ii in region:
        imreg = imdata == ii
        region_pixsum.append(np.count_nonzero(imreg.astype(np.int)))
        boolmask.append(((imreg.astype(np.int))*norm_error_low[ii]/region_pixsum[ii]))
#        boolmask.append(((621.5*621.5*1000*(3.086*10**(21))*1.18*(1.67*10**(-27))*(imreg.astype(np.int))*norm[ii]/region_pixsum[ii])))
        #621.5*621.5*1000: volume kpc to cm, 621.5*621.5*1000*(3.086*10**(21)): particle number density*mean molecular weight in proton mass units 
#        boolmask.append(n_e*(imreg.astype(np.int)))
        
    normelowmap = sum(boolmask)
    _mkmap(normelowmap,"norm_error_low_map.fits",hdr)

    boolmask = [];region_pixsum = []
    for ii in region:
        imreg = imdata == ii
        region_pixsum.append(np.count_nonzero(imreg.astype(np.int)))
        boolmask.append(((imreg.astype(np.int))*norm_error_high[ii]/region_pixsum[ii]))
#        boolmask.append(((621.5*621.5*1000*(3.086*10**(21))*1.18*(1.67*10**(-27))*(imreg.astype(np.int))*norm[ii]/region_pixsum[ii])))
        #621.5*621.5*1000: volume kpc to cm, 621.5*621.5*1000*(3.086*10**(21)): particle number density*mean molecular weight in proton mass units 
#        boolmask.append(n_e*(imreg.astype(np.int)))
        
    normehighmap = sum(boolmask)
    _mkmap(normehighmap,"norm_error_high_map.fits",hdr)

    
    boolmask = [];region_pixsum = []
    for ii in region:
        imreg = imdata == ii
        region_pixsum.append(np.count_nonzero(imreg.astype(np.int)))
        boolmask.append(((imreg.astype(np.int))*norm_error_diff[ii]/region_pixsum[ii]))
    
    normerrordepthmap = sum(boolmask)
    _mkmap(normerrordepthmap,"norm_error_range_map.fits",hdr)
    #_printmap(normerrordepthmap,"norm_errordepthmap.pdf")
    
    
    ## Density MAPS 
    boolmask = [];region_pixsum = []
    for ii in region:
        imreg = imdata == ii
        region_pixsum.append(np.count_nonzero(imreg.astype(np.int)))
        K = norm[ii]; z = 0.058100; d_A = 233.5*(3.08568*10**24)#cm 
        EI = (K * 4 * np.pi * ((d_A * (z+1))**2))/(10**(-14))
        V = 0.6215*0.6215*1000*(2.938*10**(64)) # kpc to cm^3 
        n_e = np.sqrt(1.18 * EI/(V*region_pixsum[ii]))
#        boolmask.append(((imreg.astype(np.int))*norm[ii]/region_pixsum[ii]))
#        boolmask.append(((621.5*621.5*1000*(3.086*10**(21))*1.18*(1.67*10**(-27))*(imreg.astype(np.int))*norm[ii]/region_pixsum[ii])))
        #621.5*621.5*1000: volume kpc to cm, 621.5*621.5*1000*(3.086*10**(21)): particle number density*mean molecular weight in proton mass units 
        boolmask.append(n_e*(imreg.astype(np.int)))
    
    densmap = sum(boolmask)
    _mkmap(densmap,"density_map.fits",hdr)
    #_printmap(normmap,"norm_map.pdf")
    
    boolmask = [];region_pixsum = []
    for ii in region:
        imreg = imdata == ii
        region_pixsum.append(np.count_nonzero(imreg.astype(np.int)))
        Kerr = norm_error_diff[ii]; z = 0.058100; d_A = 233.5*(3.08568*10**24)#cm 
        EIerr = (Kerr * 4 * np.pi * ((d_A * (z+1))**2))/(10**(-14))
        V = 0.6215*0.6215*1000*(2.938*10**(64)) # kpc to cm^3 
        n_e_err = np.sqrt(1.18 * EIerr/(V*region_pixsum[ii]))
        boolmask.append(n_e_err*(imreg.astype(np.int)))
    
    denserrordepthmap = sum(boolmask)
    _mkmap(denserrordepthmap/2,"density_error_range_map.fits",hdr)
    #_printmap(normerrordepthmap,"norm_errordepthmap.pdf")
    
    boolmask = [];region_pixsum = []
    for ii in region:
        imreg = imdata == ii
        region_pixsum.append(np.count_nonzero(imreg.astype(np.int)))
        K = norm_error_low[ii]; z = 0.058100; d_A = 233.5*(3.08568*10**24)#cm 
        EI = (K * 4 * np.pi * ((d_A * (z+1))**2))/(10**(-14))
        V = 0.6215*0.6215*1000*(2.938*10**(64)) # kpc to cm^3 
        n_e = np.sqrt(1.18 * EI/(V*region_pixsum[ii]))
#        boolmask.append(((imreg.astype(np.int))*norm[ii]/region_pixsum[ii]))
#        boolmask.append(((621.5*621.5*1000*(3.086*10**(21))*1.18*(1.67*10**(-27))*(imreg.astype(np.int))*norm[ii]/region_pixsum[ii])))
        #621.5*621.5*1000: volume kpc to cm, 621.5*621.5*1000*(3.086*10**(21)): particle number density*mean molecular weight in proton mass units 
        boolmask.append(n_e*(imreg.astype(np.int)))
    
    denselowmap = sum(boolmask)
    _mkmap(denselowmap,"density_error_low_map.fits",hdr)

    boolmask = [];region_pixsum = []
    for ii in region:
        imreg = imdata == ii
        region_pixsum.append(np.count_nonzero(imreg.astype(np.int)))
        K = norm_error_high[ii]; z = 0.058100; d_A = 233.5*(3.08568*10**24)#cm 
        EI = (K * 4 * np.pi * ((d_A * (z+1))**2))/(10**(-14))
        V = 0.6215*0.6215*1000*(2.938*10**(64)) # kpc to cm^3 
        n_e = np.sqrt(1.18 * EI/(V*region_pixsum[ii]))
#        boolmask.append(((imreg.astype(np.int))*norm[ii]/region_pixsum[ii]))
#        boolmask.append(((621.5*621.5*1000*(3.086*10**(21))*1.18*(1.67*10**(-27))*(imreg.astype(np.int))*norm[ii]/region_pixsum[ii])))
        #621.5*621.5*1000: volume kpc to cm, 621.5*621.5*1000*(3.086*10**(21)): particle number density*mean molecular weight in proton mass units 
        boolmask.append(n_e*(imreg.astype(np.int)))
    
    densehighmap = sum(boolmask)
    _mkmap(densehighmap,"density_error_high_map.fits",hdr)

    
    ## TEMP MAPS
    boolmask = []
    for ii in region:
        imreg = imdata == ii
        boolmask.append((imreg.astype(np.int))*temp[ii])
    
    tempmap = sum(boolmask)
    #tempmap[tempmap >= 18] = np.nan
    _mkmap(tempmap,"temp_map.fits",hdr)
    #_printmap(tempmap,"temp_map.pdf")
    
    boolmask = []
    for ii in region:
        imreg = imdata == ii
        boolmask.append((imreg.astype(np.int))*temp_error_diff[ii])
    
    temperrordepthmap = sum(boolmask)
    _mkmap((temperrordepthmap/2),"temp_error_range_map.fits",hdr)
    #_printmap(temperrordepthmap,"temp_errordepthmap.pdf")
    
    boolmask = []
    for ii in region:
        imreg = imdata == ii
        boolmask.append((imreg.astype(np.int))*temp_error_low[ii])
    
    tempelowmap = sum(boolmask)
    #tempmap[tempmap >= 18] = np.nan
    _mkmap(tempelowmap,"temp_error_low_map.fits",hdr)
    
    boolmask = []
    for ii in region:
        imreg = imdata == ii
        boolmask.append((imreg.astype(np.int))*temp_error_high[ii])
    
    tempehighmap = sum(boolmask)
    #tempmap[tempmap >= 18] = np.nan
    _mkmap(tempehighmap,"temp_error_high_map.fits",hdr)
    
    ## ABUND MAPS
    boolmask = []
    for ii in region:
        imreg = imdata == ii
        boolmask.append((imreg.astype(np.int))*abund[ii])
    
    abundmap = sum(boolmask)
    #tempmap[tempmap >= 18] = np.nan
    _mkmap(abundmap,"abund_map.fits",hdr)
    #_printmap(tempmap,"temp_map.pdf")
    
    boolmask = []
    for ii in region:
        imreg = imdata == ii
        boolmask.append((imreg.astype(np.int))*abund_error_diff[ii])
    
    abunderrordepthmap = sum(boolmask)
    _mkmap((abunderrordepthmap/2),"abund_error_range_map.fits",hdr)
    #_printmap(temperrordepthmap,"temp_errordepthmap.pdf")
    
    boolmask = []
    for ii in region:
        imreg = imdata == ii
        boolmask.append((imreg.astype(np.int))*abund_error_low[ii])
    
    abundelowmap = sum(boolmask)
    #tempmap[tempmap >= 18] = np.nan
    _mkmap(abundelowmap,"abund_error_low_map.fits",hdr)
    
    boolmask = []
    for ii in region:
        imreg = imdata == ii
        boolmask.append((imreg.astype(np.int))*abund_error_high[ii])
    
    abundehighmap = sum(boolmask)
    #tempmap[tempmap >= 18] = np.nan
    _mkmap(abundehighmap,"abund_error_high_map.fits",hdr)
    
    ##ENTROPY/PRESSURE MAPS
    entropymap = tempmap/(densmap**(2/3))
    pressuremap = densmap*tempmap
    entroerrordepthmap = np.abs(entropymap)*np.sqrt((((denserrordepthmap/2)/densmap)**2) + (((temperrordepthmap/2)/tempmap)**2) + ((2*(denserrordepthmap/2)*(temperrordepthmap/2))/(densmap*tempmap)))
    presserrordepthmap = pressuremap*np.sqrt((((temperrordepthmap/2)/tempmap)**2) + (((2/3)*(denserrordepthmap/2)/densmap)**2) - ((2*(denserrordepthmap/2)*(temperrordepthmap/2))/(densmap*tempmap)))
    sigmat = 6.65245*10**-25
    pseudocompy = (sigmat*pressuremap*(3.086*10**24))/511.0
    _mkmap(pseudocompy, "pseudocomptony_map.fits",hdr)

    _mkmap(entropymap,"entropy_map.fits",hdr)
    _mkmap(pressuremap,"pressure_map.fits",hdr)
    _mkmap(entroerrordepthmap,"entropy_error_range_map.fits",hdr)
    _mkmap(presserrordepthmap,"pressure_error_range_map.fits",hdr)
    
    _mkmap((presserrordepthmap/2)/pressuremap,"pressure_error_range_percent_map.fits",hdr)
    
    
    entropyelow = tempelowmap/(denselowmap**(2/3))
    entropyehigh = tempehighmap/(densehighmap**(2/3))
    pressureelow = denselowmap*tempelowmap
    pressureehigh = densehighmap*tempehighmap
    
    _mkmap(entropyelow,"entropy_error_low_map.fits",hdr)
    _mkmap(entropyehigh,"entropy_error_high_map.fits",hdr)
    _mkmap(pressureelow,"pressure_error_low_map.fits",hdr)
    _mkmap(pressureehigh,"pressure_error_high_map.fits",hdr)
    
    




MakeBasicMaps('./regions-info-xspec-sn' + str(d.sn_per_region) + '.data',binmap) #temperature, density, abundance, pressure, entropy

#%%