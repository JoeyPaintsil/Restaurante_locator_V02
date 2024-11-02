# #!/bin/bash

# # Install pip if it's not available
# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# python3 get-pip.py

# # Install dependencies
# pip3 install -r requirements.txt

# # Collect static files
# python3 manage.py collectstatic --noinput

# # Apply migrations
# python3 manage.py migrate

#!/bin/bash

echo "Creating projects packages..."
python3 -m pip install -r requirements.txt

echo "Moving databases..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collecting static files..."
python3 manage.py collectstatic --noinput
