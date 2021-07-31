import os, subprocess
from Arrays import *
from tabulate import tabulate
from time import sleep

class Encoder:
	__HBcmd = ["HandBrakeCLI", "-i", "", "-o", "", "--preset-import-file", ""]
	__presets = ["C:\Program Files\HandBrakeCLI-1.4.0\Fast_1080p30.json", "C:\Program Files\HandBrakeCLI-1.4.0\Web_Fast_1080p30.json"]
	__basePath = ""
	__dstPath = ""
	files = list()
	__preset = ""

	def init(self):
		print("\nWelcome to the BatchEncodeScript! \nDescription: This is a Batch Video Encoder based on HandBrakeCLI.\nAuthor: s3_jarvis\n");

	def setBasePath(self, path):
		self.__basePath = path
		self.files = os.listdir(self.__basePath);

	def setDstPath(self, path):
		self.__dstPath = path

	def fileTable(self):
		k = 1
		dataList = list()

		for i in range (0, len(self.files)):
			size = round(os.path.getsize(os.path.join(self.__basePath, self.files[i]))/(1024**3),2)

			if(size < 1):
				size *= 1024;
				dataList.insert(i, [k, self.files[i], "{} MB".format(size)])

			else :
				dataList.insert(i, [k, self.files[i], "{} GB".format(size)])

			k += 1

		table = tabulate(dataList, headers = ["#", "File Name", "Size"])

		print("Files found in the {} Directory, \n".format(self.__basePath[23:]))
		print(table)

	def setPreset(self, index):
		self.__preset = self.__presets[index-1]

	def encodeVideo(self):
		print()

		for file in self.files:
			fullPath = os.path.join(self.__basePath, file)
			fileSize = round(os.path.getsize(fullPath)/(1024**3), 2)
			self.__HBcmd[2] = r"{}".format(fullPath)
			self.__HBcmd[4] = r"{}".format(os.path.join(self.__dstPath, file)[:-3] + "mp4")
			self.__HBcmd[6] = r"{}".format(self.__preset)
			
			subprocess.run(self.__HBcmd, shell = True)
			#print(self.__HBcmd)

			self.__SystemCoolDown(fileSize)
	
	def __SystemCoolDown(self, fileSize):
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


class ArgumentException(RuntimeError):
	def __init__(self, args):
		self.__args = args

		if(self.__args < 2):
			print("\nNo arguments! \nUsage: python BatchEncodeScript.py -i <source folder> -o <destination folder>")

		elif(self.__args < 5):
			print("\nIncorrect arguments! \nUsage: python BatchEncodeScript.py -i <source folder> -o <destination folder>")			


class DirectoryNotFoundException(RuntimeError):
	def __init__(self, directoryType):
		self.__directoryType = directoryType

		print("\nError: {} Directory not found!".format(self.__directoryType))


class FileNotFoundException(RuntimeError):
	def __init__(self):	
		print("\nError: No files found!")				