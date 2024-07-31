sudo apt install -y python3 python3-venv python3-pip

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

pip install gunicorn

gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app