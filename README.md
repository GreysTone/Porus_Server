# Porus Server

## Introduction

Porus server is the server-side application for Porus App. It accepts the uploaded images from the client and runs the prediction script for recognizing the type of road. 

The server application is based on `Django`. It can be deployed on local network for testing purposes. The prediction model applies a Inception V3 model. For more details, please refer to [this page](https://www.kaggle.com/google-brain/inception-v3).

## Setup

### Prequisites
1. `Python`, version `>= 3.3`
2. `Django`[1]

Django is a framework for Web Apps. You can use the following command to install `Django`. I recommend the latest version of `Django`.
~~~~
pip3 install django
~~~~
3. `Pillow`[2]

The image processing procedures in this project relies on `PIL`. You need to install the latest version of `Pillow`.
~~~~
pip3 install pillow
~~~~

4. `Keras`[3]

`Keras` contains a set of APIs for Neural Networks. The Deep Learning script in `Porus Server` is dependent on `Keras`. To install `Keras`, you also need the latest version of `NumPy` and `SciPy`.
~~~~
pip3 install numpy
pip3 install scipy
pip3 install keras
~~~~

### Deploy And Run
1. Make sure your computer is connected to local network and have a valid `IP address`. Check your firewall settings so that the incoming network traffic is not blocked.

2. In `settings.py`, add your IP address to `ALLOWED_HOSTS`. It should look like the following.

~~~~python
ALLOWED_HOSTS = ['192.168.xxx.xxx']
~~~~

3. **Migrate Database**

In `Django`, you need to migrate the database when you run this App for the first time. Open a command window, enter the project directory and run this command:
~~~~
python manage.py migrate
~~~~

4. **Server Configuration**

You need to specify the IP address to `0.0.0.0` when you run the server. This allows the server to listen to all addresses.
~~~~
python manage.py runserver 0.0.0.0:8080
~~~~
This command runs the server on port `8080`. You can also change another port, but please remember to change the port number on your client application.

## Reference

1. Django Website. [https://docs.djangoproject.com/zh-hans/2.0/topics/install/](https://docs.djangoproject.com/zh-hans/2.0/topics/install/)
2. Pillow Documentation. [https://pillow.readthedocs.io/en/latest/](https://pillow.readthedocs.io/en/latest/)
3. Keras Documentation. [https://keras.io](https://keras.io)

