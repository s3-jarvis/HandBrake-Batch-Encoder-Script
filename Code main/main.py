#!/usr/bin/env python

""" Batch Video Encoding Script based on HandBrakeCLI

This script allows the user to encode multiple video files present in the input directory using the HandBrakeCLI sequentially.  
It is assumed that HandBrakeCLI and Preset files are already installed/added in the system. Refer to the README.md. 

Arguments
---------
This tool must be execute in the following format,

	python main.py -i <InputDirectoryPath> -o <OutputDirectoryPath>

-i : Required to define the directory as input
<InputDirectoryPath> : Complete path of the Input Directory which contains the video files that are to be encoded
-o : Required to define the directory as output
<OutputDirectoryPath> : Complete path of the Output Directory where the encoded files will be stored

Classes Implemented 
-------------------
(imported from Utils.py)

ArgumentException 
	Raises RuntimeError if incorrect arguments are passed to the tool

DirectoryNotFoundException
	Raises RuntimeError if either the Input or Output Directory is not found

FileNotFoundException
	Raises RuntimeError if no files are found in the Input Directory

Encoder
	Used for encoding the video files using HandBrakCLI sequentially 

EncodeFailureException 
	Raises RuntimeError if HandbrakeCLI Tool fails in encoding a video file

(python builtIns)

KeyboardInterrupt
	Stop the execution of this Tool in case of encountering an error

Preset Configurations
---------------------
At the time of writing, only two presets were being used. Hence these are directly hardcoded into the Encoder class. 

Future versions of this tool will include an optional "-p <PresetPath>" argument which will allow the user to add the preset file as well.

Functions Defined
-----------------
main
	The main function for this script execution

Author
------
s3_jarvis

"""

import sys
from Utils import Encoder, FileNotFoundException, DirectoryNotFoundException, ArgumentException, EncodeFailureException

def main():
	n = len(sys.argv)
	encoder = Encoder()

	try:
		if(n < 5):
			raise ArgumentException(n)
		else:
			if(sys.argv[1] == "-i"):
				encoder.setBasePath(sys.argv[2])
			else:
				raise DirectoryNotFoundException("Input")

			if(sys.argv[3] == "-o"):
				encoder.setDstPath(sys.argv[4])
			else:
				raise DirectoryNotFoundException("Output")

			print(encoder)

			if(len(encoder.files) > 0):
				encoder.fileTable()

				print("\nAvailable Presets: \n1. Fast 1080p30 \n2. Web Fast 1080p30")
				index = int(input("\nPlease Select Preset for encoding: "))   

				encoder.setPreset(index)

				encoder.encodeVideo()

			else:
				raise FileNotFoundException()

	except (ArgumentException, DirectoryNotFoundException, FileNotFoundException, EncodeFailureException, KeyboardInterrupt) as e:
		print(e)
		print("\nExiting ...")
		sys.exit(0)


if __name__ == '__main__':
	main()