#!/usr/bin/env python
import os, time,sys, os.path
import multiprocessing


def get_accesstime(dirname, files,result ) :
    value = 0 
    for infile in files :
        file_full_path = os.path.join(dirname,infile)
        if (not os.path.islink(file_full_path)) :
            new_value =  os.path.getatime(file_full_path) 
        else:
            new_value = os.path.getatime( os.readlink(file_full_path))
        if new_value > value : value = new_value
    result[dirname] = time.strftime("%Y%m%d",time.localtime(value))
    #print(result) 



if __name__ == '__main__':
    result = {}
    procs= []
    if ( len(sys.argv) != 2 or not os.path.isdir( sys.argv[1]) ) : sys.exit(-1)
    rootdir = sys.argv[1]

    #ncpus = int(multiprocessing.cpu_count()*0.75)   ## only 75% cores will be used.

    manager = multiprocessing.Manager()
    result = manager.dict()
    
    for subdir, dirs, files in os.walk(rootdir):
        #result[subdir] = get_accesstime(subdir,files)
        p = multiprocessing.Process(target=get_accesstime, args=( subdir,files, result))
        procs.append(p)
        p.start()

    for proc in procs :
        proc.join()


    for keys in result.keys() :
        if ( result[keys] == "19700101" ) : 
            continue
        print keys,result[keys]
