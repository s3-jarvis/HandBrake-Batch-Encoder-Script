#!/usr/bin/env python

import os, sys, subprocess
from Arrays import *
from tabulate import tabulate
from time import sleep

n = len(sys.argv)

HBcmd = ["HandBrakeCLI", "-i", "", "-o", "", "--preset-import-file", ""]
presets = ["C:\Program Files\HandBrakeCLI-1.4.0\Fast_1080p30.json", "C:\Program Files\HandBrakeCLI-1.4.0\Web_Fast_1080p30.json"]


if(n < 2):
    print("No arguments! \nUsage: python script.py -i <source folder> -o <destination folder>")

elif(n < 5):
    print("Incorrect arguments! \nUsage: python BatchEncodeScript.py -i <source folder> -o <destination folder>")

else :
    if(sys.argv[1] == "-i"):
        basePath = sys.argv[2]
    
    else : 
        print("Error: Input Directory not found!")

    if(sys.argv[3] == "-o"):
        dstPath = sys.argv[4]
    
    else :
        print("Error: Ouptut Directory not found!")
    
    print("Welcome to the BatchEncodeScript! \nDescription: This is a Batch Video Encoder based on HandBrakeCLI.\nAuthor: s3_jarvis\n")
    
    files = os.listdir(basePath)

    if(len(files) > 0):
        print("Files found in the {} Directory, \n".format(basePath[23:]))

        k = 1
        dataList = list()
        #print("#   File Name\t\t\tSize")
        for i in range (0, len(files)):
            size = round(os.path.getsize(os.path.join(basePath, files[i]))/(1024**3),2)
            
            if(size < 1):
                size *= 1024;
                dataList.insert(i, [k, files[i], "{} MB".format(size)])
                
            else :
                dataList.insert(i, [k, files[i], "{} GB".format(size)])
                
            k += 1
        
        table = tabulate(dataList, headers = ["#", "File Name", "Size"])
        print(table);

        print("\nAvailable Presets: \n1. Fast 1080p30 \n2. Web Fast 1080p30")
        j = int(input("\nPlease Select Preset for encoding: "))        
        finalPreset = presets[j-1]

        print()
        for file in files:
            fullPath = os.path.join(basePath, file)
            fileSize = round(os.path.getsize(fullPath)/(1024**3), 2)
            HBcmd[2] = r"{}".format(fullPath)
            HBcmd[4] = r"{}".format(os.path.join(dstPath, file)[:-3] + "mp4")
            HBcmd[6] = r"{}".format(finalPreset)
            subprocess.run(HBcmd, shell = True)
            #print(HBcmd)

            if(fileSize > 5):
                counter = 180
                print("\nFile encoded is greater than 5GB. \nSystem Cool Down Time: 2mins\n")

            else :
                counter = 30
                print("\nSystem Cool Down Time: 30sec\n")

            while(counter > 0):
                print("Count Down Timer: {} sec".format(counter), end = "\r")
                counter -= 1
                sleep(1)
                print("                         ", end = "\r")

    else :
        print("Error: No files found!")

