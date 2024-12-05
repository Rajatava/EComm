# create a virtual env and activate
python3 -m venv env
source env/bin/activate
# install packages
pip install -r requirements.txt
# run migrations
python manage.py migrate
# run server
python manage.py runserver
