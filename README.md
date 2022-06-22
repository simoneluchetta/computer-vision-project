# Computer Vision project a.y. 2021/2022: A-NeRF: application to videos

Computer Vision project at University of Trento for a.y. 2021/2022

Authors:
1. Simone Luchetta (simone.luchetta@studenti.unitn.it)
2. Diego Planchenstainer (d.planchenstainer@studenti.unitn.it)

## Overview

A-NeRF makes it possible to animate a trained body model (Surreal, Mixamo-Archer). The motion of the character will follow a sequence of poses extracted from an user-specified video. The extraction of these poses is done through OpenPose and SPIN.

Link to the original codes:
1. A-NeRF: https://github.com/LemonATsu/A-NeRF
2. SPIN: https://github.com/nkolot/SPIN

One example of the possibility of the model is shown below:

<!-- ![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif) -->

https://user-images.githubusercontent.com/56063432/175058259-02cc04f7-0196-40a5-ba19-26c4c08c6c16.mp4



Install all the components as described below.  
To run the project simply type in the command shell:
```bash
python run_pipeline.py
```

## Installation instructions
This guide will list all the action needed to run this project.  
**Important: Linux-based system is required**

First run:
```bash
sudo apt get update
```

Create project folder:
```bash
mkdir project_name
```
Navigate to the folder :
```bash
cd project_name
```

**Make sure that all the files are created within the project_name folder**

### A-NeRF's virtual environment

1. Make sure to have the of file `A-NeRF/requirements.txt` in the A-NeRF folder.
2. Create a new virtual environment for A-NeRF: 
```bash
virtualenv -p /usr/bin/python3.8 anerf
```
3. Activate the environment: 
```bash
source anerf/bin/activate
```
4. Check if the environment is active: the following string should appear in the terminal, before the usual path: `(anerf)`.
5. Run the command 
```bash
pip install -r /A-NeRF/requirements.txt
```

### SPIN's virtual environment

1. Make sure to have the of file `requirements.txt` in the SPIN folder.
2. Create a new virtual environment for SPIN : 
```bash
virtualenv spin -p python3
```
3. Activate the environment: 
```bash
source spin/bin/activate
```
4. Check if the environment is active: the following string should appear in the terminal, before the usual path: `(spin)`.
5. Run the command
```bash
pip install -r /SPIN/requirements.txt
```

### Clone the project
```bash
git clone https://github.com/simoneluchetta/computer-vision-project
```


### Build OpenPose
https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation/0_index.md#compiling-and-running-openpose-from-source

We provide two ways to install OpenPose, either build the code (better, as `run_pipeline.py` assumes this) or download on another machine the precompiled binary for Windows.

#### Linux
Make sure Anaconda's protobuf package is not installed, because it is incompatible with Caffe's protobuf version that is needed in order to run OpenPose. So, either deactivate Anaconda, or uninstall it completely.

Make sure that the below packages are installed in your machine, else install them:
```bash
sudo apt install libsdl2-dev
sudo apt install cmake
sudo apt install protobuf-compiler
```
Make sure by running `cmake --help` that the selected option for the generator is for UNIX Files. Hereby we report only the commands for Ubuntu 20, as older versions are much less straightforward:
```bash
git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose
cd openpose
git submodule update --init --recursive --remote
mkdir build
cd build
cmake ..
```

#### Windows

If the above commands won't work, the other option is to install the precompiled version on a Windows machine.
If this step is chosen, then the file `run_pipeline.py` must be modified since it requires OpenPose to run on the Linux machine. To do so, just comment the lines of code providing the command to the bash executor. Obviously, the output files of OpenPose have to be sent to the linux machine and put inside `output_json_folder`, also the frames have to be put in `temp`.


### Install FFmpeg
If OpenPose was successfully installed on a Linux machine run this command.
```bash
sudo apt install ffmpeg
```  

If not, download it on your Windows machine. Informations can be found at:
https://ffmpeg.org/download.html#build-windows

### Folder structure
Inside `project_name` folder there should be:
1. anerf venv
2. A-NeRF source code folder
3. spin venv
4. SPIN source code folder
5. Openpose folder
6. *videofile*
7. `run_pipeline.py`

The output of A-NeRF will be stored in ```A-NeRF/render_output```

Please make sure that the **video is of the right length** as if it is too long, the process will require several hours.

If you didn't manage to install openpose on Linux the folder has to be as below:
1. anerf venv
2. A-NeRF source code folder
3. spin venv
4. SPIN source code folder
5. temp *(image folder)*
6. output_json_folder *(OpenPose output folder)*
7. `run_pipeline.py`

To run ffmpeg on Windows, open the FFmpeg folder (where the precompiled binary was downloaded) in terminal, then:
```bash
mkdir temp
.\ffmpeg.exe -i .\videoname.mp4 -vsync 0 temp\temp%d.png
```

### Last Info

Note that when running with `run_pipeline.py`, if it is necessary to stop the process this commands need to be done:
```bash
top
```

Take note of the PROCESS_ID referring to "Python" of your User.

```bash
kill -9 PROCESS_ID
```
