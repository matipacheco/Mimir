# Mimir
The oracle

## Preparación ambiente de desarrollo
Para la creación de un ambiente de desarrollo que contenga todas dependencias necesarias para levantar la aplicación, se utilizó [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).

### Instalación
sudo apt-get install python3-pip

pip3 install virtualenv

### Dependencias
virtualenv Mimir

virtualenv -p /usr/bin/python3.4 Mimir

source Mimir/bin/activate

pip install -r requirements.txt

## Setup
1. Para la creación de las tablas en la base de datos:

	python3 mimirs_well.py

2. Para poblar la base de datos:

	python3 brokkr_the_blacksmith.py