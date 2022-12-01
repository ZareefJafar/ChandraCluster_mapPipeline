


# Zareef: added try, except block to handle missing values. 
# See "ParseOutput(inputdir)" of pipeline.py from Chandra_pipeline by jpbreuer for the original implementation


import bin_region_directories as brd
import numpy as np



def ParseOutput(inputdir):

	XSPEC= True

	if XSPEC:
		file = open('regions-info-xspec.data', 'w')
		file.write('region nH temperature temp_low temp_high temp_error_low temp_error_high temp_error_diff abundance abund_low abund_high abund_error_low abund_error_high abund_error_diff redshift norm norm_low norm_high norm_error_low norm_error_high norm_error_diff chi dof chi2\n')

		nh = ""
		temp = ""
		templow = ""
		temphigh = ""
		tempelow = ""
		tempehigh = ""
		temperange = ""

		abund = ""
		abundlow = ""
		abundhigh = ""
		abundelow = ""
		abundehigh = ""
		abunderange = ""

		redshift = ""

		norm = ""
		normlow = ""
		normhigh = ""
		normelow = ""
		normehigh = ""
		normerange = ""
		chi = ""
		dof = ""
		chi2= ""

		#loop over regions here
		for ii in list(range(brd.sexnum)):#regnum
			try: ##ZAREEF
			    regdata = open(inputdir + '/xspec/reg_' + str(ii) + '_data.xcm','r')
			    info = regdata.read().split()
			    
			    nh = str(info[0])
			    
			    temp = str(info[1])
			    templow = str(info[2])
			    temphigh = str(info[3])
			    tempelow = str(round(float(temp) - float(templow),5))
			    tempehigh = str(round(float(temphigh) - float(temp),5))
			    temperange = str(round(float(tempehigh) + np.abs(float(tempelow)),5))
			    
			    abund = str(info[4])
			    abundlow = str(info[5])
			    abundhigh = str(info[6])
			    abundelow = str(round(float(abund) - float(abundlow),5))
			    abundehigh = str(round(float(abundhigh) - float(abund),5))
			    abunderange = str(round(float(abundehigh) + np.abs(float(abundelow)),5))
			    
			    redshift = str(info[7])
			    
			    norm = str(info[8])
			    normlow = str(info[9])
			    normhigh = str(info[10])
			    normelow = str(float(norm) - float(normlow))
			    normehigh = str(float(normhigh) - float(norm))
			    normerange = str(round(float(normehigh) + np.abs(float(normelow)),5))
			    
			    chi = str(info[11])
			    dof = str(info[12])
			    try:
			        chi2 = str(round(float(chi)/float(dof),5))
			    except:
			        pass

			except: #ZAREEF

				nh=nh
	      
				temp = temp
				templow = templow
				temphigh = temphigh
				tempelow = tempelow
				tempehigh = tempehigh
				temperange = temperange

				abund = abund
				abundlow = abundlow
				abundhigh = abundhigh
				abundelow = abundelow
				abundehigh = abundehigh
				abunderange = abunderange

				redshift = redshift

				norm = norm
				normlow = normlow
				normhigh = normhigh
				normelow = normelow
				normehigh = normehigh
				normerange = normerange

				chi = chi
				dof = dof
				try:
				    chi2 = chi2
				except:
				    pass

			file.write(str(ii) + ' ' + nh + ' ' + temp + ' ' + templow + ' ' + temphigh + ' ' + tempelow + ' ' + tempehigh + ' ' + temperange + ' ' + abund + ' ' + abundlow + ' ' + abundhigh + ' ' + abundelow + ' ' + abundehigh + ' ' + abunderange + ' ' + redshift + ' ' + norm + ' ' + normlow + ' ' + normhigh + ' ' + normelow + ' ' + normehigh + ' ' + normerange + ' ' + chi + ' ' + dof + ' ' + chi2 + '\n')# + ' ' + press + ' ' + presselow + ' ' + pressehigh + ' ' + presslow + ' ' + presshigh + ' ' + presserange + ' ' + entropy + ' ' + entroelow + ' ' + entroehigh + ' ' + entrolow + ' ' + entrohigh + ' ' + entroerange + '\n')
		file.close()




ParseOutput(brd.resultsdir)#resultsdir