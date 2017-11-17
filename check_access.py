import os, time
#import multiprocessing


def get_accesstime(dirname, files) :
    value = 0 
    for infile in files :
        file_full_path = os.path.join(dirname,infile)
        new_value =  os.path.getatime(file_full_path) 
        if new_value > value : value = new_value
    result = time.strftime("%Y%m%d",time.localtime(value))
    return( result)



rootdir = os.getcwd()
result = {}
print rootdir
for subdir, dirs, files in os.walk(rootdir):
    #if subdir.startswith(".") : continue
    result[subdir] = get_accesstime(subdir,files)

for keys in result.keys() :
    if ( result[keys] == "19700101" or result[keys]==0 ) : continue
    print keys,result[keys]
