# d-drive

type following commands to run this project

1 ) First, clone the repository to your local machine:

	git clone https://github.com/shalinsirwani/d-drive.git

2 ) Get inside the downloaded folder

	cd ddrive


3 ) Install the requirements:

	pip install -r requirements.txt

4 ) Apply the migrations:

	python manage.py makemigrations
        
	python manage.py makemigrations files

	python manage.py migrate

	python manage.py migrate files

5 ) Finally, run the development server:

	python manage.py runserver

	type this address on your browser :-  127.0.0.1:8000
