#!/usr/bin/env python

import sys
from Utils import Encoder, FileNotFoundException, DirectoryNotFoundException, ArgumentException

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

	except (ArgumentException, DirectoryNotFoundException, FileNotFoundException, KeyboardInterrupt) as e:
		print(e, "\nExiting ...")
		sys.exit(0)


if __name__ == '__main__':
	main()