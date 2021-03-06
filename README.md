## Batch Video Encoding Script using HandBrakeCLI

### Introduction
Let's say that you have recorded your Video Lectures/Meetings and now they're taking up large amounts of space on your hard drive (or SSD), what do you do? <br />
The answer to that problem is Video Encoding. HandBrake is a popular open-source software that does this job for you. In this Python Script, I'll be making use of their CLI Tool for Batch Video Encoding.

### Why this Script?
By default, HandBrake supports encoding multiple video files by adding them to the queue. But where's the fun in that? <br />
By using my script, you can encode an entire directory of video files with just a single command!

### Features
This script has the following features, (more features coming soon!)
- [x] Single Command for getting your job done!
- [x] System Cool Down Time after each Video Encoding
- [x] File System View of the Input Directory
- [x] OOPs for Code Reuse
- [x] Exception Handling for Smooth Code Execution

### Prerequisites
- Download [HandBrakeCLI](https://handbrake.fr/rotation.php?file=HandBrakeCLI-1.4.1-win-x86_64.zip) and extract its contents into a directory (preferably Program Files in C Drive) and copy the path of this directory. 
- Now, Edit the Environment PATH variable and add the path of this directory. 
- Download and Install [Python](https://www.python.org/downloads/) (if you don't have it already).
- Download the .zip of this repo (or) Clone it into your system by running the command,
    ```sh
    git clone https://github.com/s3-jarvis/HandBrake-Batch-Encoder-Script.git
    ```
- Now, install the necessary packages required for this script by, 
    ```sh
    pip install -r Requirements.txt
    ```
    >**_NOTE:_** You should be inside the directory for running this command! 
- Don't forget to copy the Preset Files present in this repo to the HandBrakeCLI directory. (my directory is named ```HandBrakeCLI-1.4.0```, in case you name it differently, make the appropriate change in the code! /*Line 63 in __Utils.py__*/)

### Usage
This script must be execute in the following format,
```sh
python main.py -i <InputDirectoryPath> -o <OutputDirectoryPath>
```

| Argument                    | Description                                                                                |
|-----------------------------|--------------------------------------------------------------------------------------------|
| ```-i```                    | Required to define the directory as input                                                  |
| ```<InputDirectoryPath>```  | Complete path of the Input Directory which contains the video files that are to be encoded |
| ```-o```                    | Required to define the directory as output                                                 |
| ```<OutputDirectoryPath>``` | Complete path of the Output Directory where the encoded files will be stored               |

Refer to the Code DocString for more info.
```py
~$ python
Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import main, Utils
>>> help(main)
Help on module main:

NAME
    main - Batch Video Encoding Script based on HandBrakeCLI

--- More ---
>>>
>>> help(Utils)
Help on module Utils:

NAME
    Utils - Utility Library for Batch Video Encoding Script based on HandBrakeCLI

--- More ---
>>>
```
>**_NOTE:_** You should be inside the directory for running these command! 

### Acknowledgements
I would like to thank **_HandBrake_** for creating such an awesome software/CLI without which this script wouldn't be created. <br />
I would also thank the numerous _Python Resources_ on the Internet which provided me with the necessary knowledge to build this script.

### Future Thoughts
This script can be further upgraded with the addition of the following features,
- [ ] Include an optional ```-p <PresetPath>``` argument which will allow the User to add the Preset file
- [ ] Sorting Video Files based on size before beginning the Encode Process
