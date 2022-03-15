# django-react

1. In terminal, run "docker-compose up" (The docker should be installed in this case)
This should startup React app, postgres, and redis

2. Open a new Terminal and cd into "django-api" and run "pip3 install -r requirements.txt"

3. run "python3 manage.py makemigrations"

4. run "python3 manage.py migrate"

5. run "python3 manage.py startserver"

This will startup the django-api and open "http://localhost:3000" in browser

Click on Map on sidebar , it'll show login screen, click on signup and create a user..

Now you'll be redirected to homepage.. click on map again .. you can see the map.. but no pointers will be there since we don't have any records in db
