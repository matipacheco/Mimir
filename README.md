# Mimir
The oracle. The dollar predictor.

_Note: This project was put on hold due my lazyness, as well as the project factibility.. Something's not right_ :thinking_face:

## Develepment environment setup
For the creation of the development environment that contains all the necessary dependencies to run the application, I used [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

### Installation
`sudo apt-get install python3-pip`

`pip3 install virtualenv`

### Dependencies
`virtualenv Mimir`

`virtualenv -p /usr/bin/python3.4 Mimir`

`source Mimir/bin/activate`

`pip install -r requirements.txt`

## Setup
1. For the database tables creation, run:

`python3 mimirs_well.py`

2. To populate those tables, run:

`python3 brokkr_the_blacksmith.py`
