## Setting up your Development Environment for the RMS application

1. In your Terminal or Command Prompt, go to a location where you would like the github repository to live. Since cloning the repo will use the repository's name for its folder name, a location like Documents will work. E.g. ```cd ~/Documents/```.

2. Install Python if you don't already own it. For Mac users, your default will be 2.7 which won't work with this project. Specifically, we want Python 3.5+ which can be found [here](https://www.python.org/downloads/). Since Mac comes with a pre-installed 2.7 that is necessary for some other applications, you'll need to run commands like ```python3 manage.py runserver``` until step 6. This also applies to pip (pip3).

3. Clone the repo with ```git clone https://github.com/ip2176/RMS.git```.

4. Next use pip to install virtualenv. ```pip3 install virtualenv```. You may not need the 3 in pip3 depending on your python setup explained in step 2. Once installed, create a new virtualenv by running the following command: ```virtualenv venv --no-site-packages```.  Make sure to run this command at the root of the project (right inside the RMS folder).

5. Whenever you're about to begin developing code, you need to jump into your virtualenv which can be activated as follows for mac: ```source venv/bin/activate```. For windows, use this command: ```venv\Scripts\activate```. Both operating systems can deactivate it with the command ```deactivate```. You no longer need to use commands like python3 or pip3; from now on just use the original python or pip.

6. Start your virtual environment for your operating system according to the instructions in step 5.

7. For windows, inside the virtual environment, run ```pip install -r Packages.txt``` to install all the needed packages.

8. Start the Tornado app by running ```python main.py``` on a console.  Please change directory into the root folder of the RMS application to accomplish this.

9. Visit the following to access the website: [http://127.0.0.1:8888/](http://127.0.0.1:8888/)

10. To stop the application use CTRL+C.

## Testing the Heartbeat

To see the heartbeat and fault recovery of the system working, please follow the following steps.

1. With the server started, navigate to the financial aid portion of the website: [http://127.0.0.1:8888/financial-aid/](http://127.0.0.1:8888/financial-aid/)

2. Watch the terminal the server was started in.  It should periodically get "Financial Aid Heartbeat" (one per second).

3. There is a 1/10 chance per second that the financial aid app will crash.  When the system does crash, the terminal will display "Financial aid quit unexpectedly".

4. You will notice the page reloads at this point.  This happens because the backup httpserver is switched in for the main httpserver.  The main httpserver is restarted and positioned as the backup httpserver for the next time the application crashes.

5. You will see that the heartbeat messages continue on as normal after the page reloads.

## Frameworks

1. Python 3.5 +
2. Tornado 4.4.3
3. wtforms-tornado 0.0.2

All packages and their required versions are included in the Packages.txt file.

## Other Notes

If you want to use an IDE like PyCharm, then to get it to recognize Tornado is installed you need to follow the instructions [here](http://stackoverflow.com/questions/34520291/pycharm-cannot-find-the-packages-in-virtualenv) and add the virtual environment interpreter to the list of interpreters.  That should allow PyCharm to see all your packages installed in venv. 
