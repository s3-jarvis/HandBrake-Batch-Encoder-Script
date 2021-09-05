## Batch Video Encoding Script using HandBrakeCLI

### Introduction
Let's say that you have recorded your Video Lectures/Meetings and now they're taking up large amounts of space on your hard drive (or SSD), what do you do?
The answer to that problem is Video Encoding. HandBrake is a popular open-source software that does this job for you. In this Python Script, I'll be making use of their CLI Tool for Batch Video Encoding.

### Why this Script?
By default, HandBrake supports encoding multiple video files by adding them to the queue. But where's the fun in that?
By using my script, you can encode an entire directory of video files with just a single command!

### Features
This script has the following features, (more features coming soon!)
- [x] Single Command for getting your job done!
- [x] System Cool Down Time after each Video Encoding
- [x] File System View of the Input Directory
- [x] OOPs for Code Reuse
- [x] Exception Handling for Smooth Code Execution

### Prerequisites
- [Download](https://handbrake.fr/rotation.php?file=HandBrakeCLI-1.4.1-win-x86_64.zip) HandBrakeCLI and extract its contents into a directory (preferably Program Files in C Drive) and copy the path of this directory. 
- Now, Edit the Environment PATH variable and add the path of this directory. 
- [Download](https://www.python.org/downloads/) and Install Python (if you don't have it already).
- Download the .zip of this repo (or) Clone it into your system by running the command,
    ```
    git clone https://github.com/s3-jarvis/HandBrake-Batch-Encoder-Script.git
    ```
- Now, install the necessary packages required for this script by, 
    ```
    pip install -r Requirements.txt
    ```
    >NOTE: You should be inside the directory for running this command! 

### Usage
How to run this script

### Acknowledgements
Thanks to HandBrake

### Future Thoughts
Upgrades to this script!