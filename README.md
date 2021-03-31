# how to use csv-shit.py

## Index

1. requirements

2. Installation

3. How to run the program

## 1. requirements

1. Python 3 installed

2. pandas library installed

## 2. Installation

### 2.1 How to install Python 3

Python3 can be installed on 2 ways on mac os by installing the xcode developer tools by running `xcode-select --install` or by downloading the installer from the python website

### 2.2.1 How to install the pandas library on intel mac / windows machine

open a terminal and run the command `pip3 install pandas`

#### 2.2.2 How to install the pandas library on M1 macbook

##### 2.2.2.1 Native (prefered)

1. open a terminal session as a root by opening the terminal and running the command `sudo -s` and filling in the password of your useraccount

2. run the following sequence of commands and let them run until you can run a other command

```
    python3 -m pip install virtualenv 
    virtualenv -p python3.8 venv
    source venv/bin/activate
    pip install --upgrade pip   
    pip install numpy cython
    git clone https://github.com/pandas-dev/pandas.git
    cd pandas
    python3 setup.py install
```

##### 2.2.2.2 Rosseta 2 

1 . Close the Terminal Application

2. Find the Terminal App in Finder (usually located in Macintosh HD/Applications/Utilities)

3. Secondary Click the Terminal Icon >> Get Info
Check the checkbox labeled Open Using Rosetta

4. Now launch a Terminal window (The new Terminal window will be opened using Rosetta emulation)

5. Run the command from 2.2.1 then continue to step 3

## 3. How to run the program

go to the directory where the script is located in a terminal session en run `python3 matchAndCombineCsvFiles.py [filePath or cwd (current working directory)] [incidents filename] [incidents columnName] [assets filename] [assets columnname]` or if you are unsure what the arguments are just run `python3 matchAndCombineCsvFiles.py help`

