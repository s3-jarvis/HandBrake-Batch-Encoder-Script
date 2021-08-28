""" Utility Library for Batch Video Encoding Script based on HandBrakeCLI

Imports
-------
os
	Required for obtaining Files and Folder Stats and Properties

subprocess
	Required for running the HandBrakeCLI 

tabulate
	For printing a formatted table of Folder Contents

time
	For SystemCoolDown Timer method implemented in Encoder Class

Requirements
------------
tabulate (v0.8.9)
	Required for displaying table of folder contents

Author
------
s3_jarvis

"""

import os, subprocess
from tabulate import tabulate
import time

class Encoder:
	"""
	A class for handling batch video encoding using HandBrakeCLI.

	...

	Attributes
	----------
	__HBcmd: list(str)
		a list containing the HandBrakeCLI commands for video encoding
	__presets: list(str) **
		a list containing the preset file paths
	__basePath: str **
		a string containing the input directory path
	__dstPath: str **
		a string containing the output directory path
	__preset: str **
		a string containing selected preset file path
	files: list(str) **
		a list containing the files in the input directory
	__fileDateTime: str
		a string containing current file last modified date and time stamp

	NOTE
	----
	** - means the str is a path;
		 Eg.: location = r"{}".format(path)

	"""

	__HBcmd = ["HandBrakeCLI", "-i", "", "-o", "", "--preset-import-file", ""]
	__presets = ["C:\Program Files\HandBrakeCLI-1.4.0\Fast_1080p30.json", "C:\Program Files\HandBrakeCLI-1.4.0\Web_Fast_1080p30.json"]
	files = list()

	def __str__(self):
		"""
		Greeting Function; invoked upon printing class object.

		Returns
		-------
		str
			A string containing the appropriate print message

		"""

		return "\nWelcome to the BatchEncodeScript! \nDescription: This is a Batch Video Encoder based on HandBrakeCLI.\nAuthor: s3_jarvis\n"

	def setBasePath(self, path):
		"""
		Set the input directory path for video encoding.
		Contents of this directory is also populated in the files attribute. 

		Parameters
		----------
		path: str **
			input directory file path
		
		"""

		if(self.__doesDirectoryExist(path)):
			self.__basePath = path
			self.files = os.listdir(self.__basePath);
		else:
			raise DirectoryNotFoundException("Input")

	def setDstPath(self, path):
		"""
		Set the output directory path for storing the encoded video files.

		Parameters
		----------
		path: str **
			Output directory file path

		"""

		if(self.__doesDirectoryExist(path)):
			self.__dstPath = path
		else:
			raise DirectoryNotFoundException("Output")

	def setPreset(self, index):
		"""
		Set the preset to be used for video encoding, based on the index passed.

		Parameters
		----------
		index: int
			An integer for setting the preset from __presets list

		"""

		self.__preset = self.__presets[index-1]

	def fileTable(self):
		"""
		Print a formatted Table containing the contents of the input directory.

		"""

		k = 1
		dataList = list()

		for i in range (0, len(self.files)):
			size = round(os.path.getsize(os.path.join(self.__basePath, self.files[i]))/(1024**3),2)
			fullPath = os.path.join(self.__basePath, self.files[i])

			if(size < 1):
				size *= 1024;
				dataList.insert(i, [k, self.files[i], "{} MB".format(size), self.__getLastModified(fullPath)])

			else :
				dataList.insert(i, [k, self.files[i], "{} GB".format(size), self.__getLastModified(fullPath)])

			k += 1

		table = tabulate(dataList, headers = ["#", "File Name", "Size", "Last Modified"])

		print("Files found in the {} Directory, \n".format(self.__basePath[23:]))
		print(table)

	def encodeVideo(self):
		"""
		Encode the video file paths present in the files attribute sequentially and store the same in the output directory.

		"""

		print()

		for file in self.files:
			fullPath = os.path.join(self.__basePath, file)
			fileSize = round(os.path.getsize(fullPath)/(1024**3), 2)
			self.__HBcmd[2] = r"{}".format(fullPath)
			self.__HBcmd[4] = r"{}".format(os.path.join(self.__dstPath, file)[:-3] + "mp4")
			self.__HBcmd[6] = r"{}".format(self.__preset)
			
			status = subprocess.run(self.__HBcmd, shell = True)

			if(status.returncode):
				raise EncodeFailureException()

			self.__SystemCoolDown(fileSize)
	
	def __SystemCoolDown(self, fileSize):
		"""
		This function stalls the iterative encoding process by using a time counter.

		Parameters
		----------
		fileSize: int
			This integer contains the video file size in GB;
			if this > 5GB
				stall for 2 mins
			else
				stall for 30 sec

		"""
		if(fileSize > 5):
			counter = 180
			print("\nFile encoded is greater than 5GB. \nSystem Cool Down Time: 2mins\n")

		else :
			counter = 30
			print("\nSystem Cool Down Time: 30sec\n")

		while(counter > 0):
			print("Count Down Timer: {} sec".format(counter), end = "\r")
			counter -= 1
			time.sleep(1)
			print("                         ", end = "\r")	

	def __getLastModified(self, path):
		"""
		This function returns the last modified date and time of the file path parameter.

		Parameters
		----------
		path: str **
			File path for which last modified date and time is required

		Returns
		-------
		str
			A string containing the last modified date and time stamp

		"""

		self.__fileDateTime = time.strftime('%d-%m-%Y  %H:%M:%S', time.localtime(os.path.getmtime(r"{}".format(path))))
		return self.__fileDateTime

	def __doesDirectoryExist(self, path):
		"""
		This function returns true if the file path exists.

		Parameters
		----------
		path: str **
			File path whose existence is to be checked

		Returns
		-------
		bool
			Existence of file path

		"""

		return os.path.exists(path)


class ArgumentException(RuntimeError):
	"""
	User-defined Exception Handling Function which inherits RuntimeError. 

	"""

	def __init__(self, args):
		"""
		Init Function for ArgumentException Handling.
		
		Parameters
		----------
		args
			Number of arguments passed via the command line to the main.py script

		"""

		self.__args = args

	def __str__(self):
		"""
		Print a message to the stdout when incorrect arguments are passed via command line.

		Returns
		-------
		str
			A string containing the appropriate print message

		"""

		if(self.__args < 2):
			str = "\nNo arguments found! \nUsage: python main.py -i <source folder> -o <destination folder>"

		elif(self.__args < 5):
			str = "\nIncorrect arguments! \nUsage: python main.py -i <source folder> -o <destination folder>"

		return str


class DirectoryNotFoundException(RuntimeError):
	"""
	User-defined Exception Handling Function which inherits RuntimeError. 
	
	"""

	def __init__(self, directoryType):
		"""
		Init Function for DirectoryNotFoundException Handling.

		Parameters
		----------
		directoryType
			Specify input/output directory

		"""

		self.__directoryType = directoryType

	def __str__(self):
		"""
		Print a message to the stdout when Directory Path passed via command line doesn't exist.

		Returns
		-------
		str
			A string containing the appropriate print message

		"""

		return "\nError: {} Directory not found!".format(self.__directoryType)


class FileNotFoundException(RuntimeError):
	"""
	User-defined Exception Handling Function which inherits RuntimeError. 
	
	"""

	def __str__(self):	
		"""
		Print a message to the stdout when no files are found in the input directory.

		Returns
		-------
		str
			A string containing the appropriate print message

		"""
		
		return "\nError: No files found!"


class EncodeFailureException(RuntimeError):
	"""
	User-defined Exception Handling Function which inherits RuntimeError. 
	
	"""

	def __str__(self):	
		"""
		Print a message to the stdout when HandBrakeCLI fails in encoding a video file.

		Returns
		-------
		str
			A string containing the appropriate print message

		"""
		
		return "\nError: Encoding Failed!"
