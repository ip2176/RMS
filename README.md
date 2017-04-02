## Setting up your Development Environment for the RMS application

1. In your Terminal or Command Prompt, go to a location where you would like the github repository to live. Since cloning the repo will use the repository's name for its folder name, a location like Documents will work. E.g. ```cd ~/Documents/```.

2. Install Python if you don't already own it. For Mac users, your default will be 2.7 which won't work with this project. Specifically, we want Python 3.5+ which can be found [here](https://www.python.org/downloads/). Since Mac comes with a pre-installed 2.7 that is necessary for some other applications, you'll need to run commands like ```python3 manage.py runserver``` until step 6. This also applies to pip (pip3).

3. Clone the repo with ```git clone https://github.com/ip2176/RMS.git```.

4. Next use pip to install virtualenv. ```pip3 install virtualenv```. You may not need the 3 in pip3 depending on your python setup explained in step 2. Once installed, create a new virtualenv by running the following command: ```virtualenv venv --no-site-packages```.  Make sure to run this command at the root of the project (right inside the RMS folder).

5. Whenever you're about to begin developing code, you need to jump into your virtualenv which can be activated as follows for mac: ```source venv/bin/activate```. For windows, use this command: ```venv\Scripts\activate```. Both operating systems can deactivate it with the command ```deactivate```. You no longer need to use commands like python3 or pip3; from now on just use the original python or pip.

6. Start your virtual environment for your operating system according to the instructions in step 5.

7. For windows, inside the virtual environment, run ```pip install tornado``` to install Tornado.

8. Start the Tornado app by running ```python main.py```.

9. Visit the following to access the website: [http://127.0.0.1:8888/](http://127.0.0.1:8888/)

10. To stop the application use CTRL+C.
