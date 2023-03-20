# python-django

This is a production-ready setup for running Django on Docker. It has sensible defaults for security.

## Table of Contents
1. Requirements
2. Setup
3. What does the project do?
4. Usage
5. Contribute

## 1. Requirements
- Python 3.7 or later versions
- Docker

## 2. Setup

Firstly install [Docker](https://docs.docker.com/get-docker/) on your computer.
Now launch pycharm and configure a project on this working directory.
All following commands must be run only once at project installation.

The first clone of the repository:

```bash
$ git clone https://github.com/D-derinalp/python-django.git
$ cd python-django
```

Then install the all dependencies:
```bash
$ pip install -r requirements.txt
```

Once pip has finished downloading the dependencies, make migrations:
```bash
(env)$ python manage.py migrate
```

After that create superuser(admin), enter your name, email and password:
```bash
(env)$ python manage.py createsuperuser
```

Finally enter below code to display the app on your web browser with url: http://127.0.0.1:8000/
:
```bash
(env)$ python manage.py runserver
```

### Docker Image
Run the following command to create docker image:

```bash
docker build --tag python-django .
```

To create docker container you should run the image with following command:

```bash
docker run --publish 8000:8000 python-django
```

To shut down your container by first getting its ID from this command:
```bash
docker ps
```

And then use only the first three characters of its ID to shut down the container :
```bash
docker stop [ID]
```

## 3. What does the project do?

This project is used Django frame make a survey about climate change awareness and get vote from the users only logged in and show the results the users who voted.
Servey questions and choices are as following:

1. Do you eat food that has been produced only in your country?
- Yes
- No
- It doesn't matter

2. Do you buy clothes from charity or second-hand shop?
- Yes
- No
- Rarely

3. Would you consider switching your vehicle to an electric one?
- Yes
- No
- Not Sure

4. Do you separate your domestic waste?
- Yes
- No
- Not Regularly

5. Do you think climate change could be prevented?
- Yes
- No
- I have no idea

6. Which of the following vehicles do you use to go to school or work?
- On foot
- Bicycle
- Your own car
- Public transportation


## 4. Usage

Open http://127.0.0.1:8000/admin/ on your browser after running app and enter website as an admin to add survey questions and choices given above.

## 5. Contribute

Contributions are always welcome! 
