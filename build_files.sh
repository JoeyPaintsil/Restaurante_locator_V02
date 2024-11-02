curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
#!/bin/bash
echo "Building project packageS..."
python3 -m pip install -r requirements.txt

echo "Moving Database..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collecting all static files..."
python3 manage.py collectstatic --noinput