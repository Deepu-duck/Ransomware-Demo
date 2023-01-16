# Ransomware
This program is a command line-based ransomware which will encrypts the file also it is written in python.

# This Repositary contains 4 files: - 

Readme.md: This file is what you are reading. This file has all Instructions related to how to Execute this code.
ransom.py: - It is a file that contains our main code which encrypts the files important.txt and key.txt using public_key.asc and ask for ransom to the victim
important.txt: - The file which contains all the confidential data which we will encrypts later
public_key.asc: - Contains the key of an attacker.

# Requirements

To run this project, we need to install the following Software’s.
Python3 : Python3 Programming Language that is used to develop/write the programs.
Pycharm IDE : Pycharm Integrated Development Environment is used to develop the Code.
Ubuntu(any linux Distribution) : Any distribution of Linux is fine, however this time we are using Ubuntu

# Steps to Use the Files.

Unzip the zip file.

Unzip program.zip -d destination_folder

Change the directory to the Unzipped Folder

cd /Ransomware

Give permissions to the Python Files which makes them Executable

chmod +x *.py

We Run this Python file on victims’ machine by using the Terminal

Python ransom.py

Now the program encrypts the files and delete the previous files.

Now our program ask for ransom to the victim
