export PYTHONDONTWRITEBYTECODE=1

sudo apt install -y python3 python3-venv python3-pip

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
pip install gunicorn

# Check if port 8000 is in use and kill the process if necessary
if lsof -i:8000 -t >/dev/null; then
    echo "Port 8000 is in use. Stopping the process using it."
    kill -9 $(lsof -i:8000 -t)
fi

gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app