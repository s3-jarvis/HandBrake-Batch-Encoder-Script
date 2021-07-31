# File handling test

import os, sys, time

class FileData:
	__fileDate = ""
	__fileTime = ""
	__filePath = r""
	__fileContents = list()
	__basePath = r""

	def __init__(self, filePath, basePath):
		self.__filePath = filePath
		self.__basePath = basePath
		self.__fileContents = os.listdir(self.__basePath)

	def isFileEmpty(self):
		return os.path.getsize(self.__filePath) == 0

	def doesFileExist(self):
		return os.path.exists(self.__filePath)

	def getTimestamp(self, path):
		self.__fileDate = time.strftime('%d-%m-%Y', time.localtime(os.path.getmtime(path)))
		self.__fileTime = time.strftime('%H:%M', time.localtime(os.path.getmtime(path))) 
		return [self.__fileDate, self.__fileTime]

	def writeContent(self):
		fd.__setWriteMode()

		for i in self.__fileContents:
			data = os.path.join(self.__basePath, i) + "\n"
			self.__file.write(data)

	def writeContentIndex(self, index):
		fd.__setWriteMode()

		for i in self.__fileContents[index:]:
			data = os.path.join(self.__basePath, i) + "\n"
			self.__file.write(data)

	def readData(self):
		self.__setReadMode()
		return self.__file.readline()

	def fileClose(self):
		self.__file.close()

	def getFile(self):
		self.__setReadMode()
		return self.__file

	def __setReadMode(self):
		self.__file = open(self.__filePath, 'r')

	def __setWriteMode(self):
		self.__file = open(self.__filePath, 'w')

basePath = r"C:\Users\shash\Desktop\Exports"

#folderContents = os.listdir(basePath)

folderContentPath = r"C:\Users\shash\Desktop\Batch Encoder Repo\Testing\DirectoryContents.txt"

fd = FileData(folderContentPath, basePath)

if(fd.doesFileExist() or fd.isFileEmpty()):	
	fd.writeContent()
	fd.fileClose()

k = 1
for i in fd.getFile():
	print(i, fd.getTimestamp(r"{}".format(i)))
	if(input() == 'T'):
		fd.writeContentIndex(k)
		k+=1

fd.fileClose()