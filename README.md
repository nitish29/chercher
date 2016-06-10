# chercher

Chercher is a multi-lingual search system which allows users to search and browse multilingual data based on various topics like Paris attacks, Syrian refugee crisis etc. It uses content tagging and LDA topic modeling to improve a user's search experience. Other features supported by the system include pseudo-relevance feedback and query expansion, faceted search, semantic search.

Video Demo Link : https://drive.google.com/file/d/0B1zSNVaXoshRaWM3WUxpS29DN3M/view


# chercher Installation Steps

- Install Virtual Env and Virtual Env wrapper

- Make a new virtual env with python version as 3.5
	
	- mkvirtualenv --python=(*path to your python3.5 installation directory*) (*name of virtual enviornment*)
	- eg : **mkvirtualenv --python=/usr/local/bin/python3.5 ir_project**

- activate the virtual environment that you have made

- sudo pip install -r requirements.txt
	
	- in case you face problem installing psycopg2 , try installing it with this command instead _pip3.5_ _install_ _psycopg2_

- install postgres database and create a new database

- make a copy of local_settings.py.sample file from nongit folder and move it to lingualsearch folder

- rename this file copied file to **local_settings.py** 

- change all these database parameters: NAME,USER,PASSWORD,PORT,HOST as per your postgres database setup

- run the migrate command, to add/update database schema tables: python manage.py migrate 

- type the following command using command line - python manage.py runserver 0:8000 

- open browser and type localhost:8000, you should see the default django page
