

content=[]
with open ('directory_list.txt', 'rt') as myfile:  
    for line in myfile:                   
        content.append(line.strip())  
myfile.close()



file_name = 'directory_list.txt'

with open(file_name, 'w', encoding='utf-8') as f:
	clusterName = content[0].strip()
	#obsids_search = os.popen('find_chandra_obsid ' + clusterName).read()
	f.write(clusterName+'\n')
	#print("Following observations will be downloaded.\nIf you want to use only selected observations please manually edit the PreProcessing_download_data.py file before running STEP 2.\n\n"+obsids_search)

	clusterDirec = input("\nEnter the new data path.\ne.g. /home/[user_name]/[data_dir]/[sub_data_dir]/...\ndata path: ")
	f.write(clusterDirec+'\n')


	f.write(content[2]+'\n')
	f.write(content[3])
	f.close()