# Inventory Web App

This Inventory app was built in Django as required
It is just a basic inventory app that does the following.
* Gets and lists all the items in the inventory database
* Allows users to create a new item to the inventory
* Users can delete one item at a time ( when the number of such item available
 becomes zero, it is deleted from the database.)


### To Run the app, just do the following
* Navigate into the inventory folder after cloning or downloading this web app from github
* You need python 3.1 and above to run the app
* Run "pip install -r requirements.txt" to install the required python packages needed to run the web app.
* After that, run "python manage.py makemigrations" to create a model that gets populated to the database.
* Then run "python manage.py migrate" to actually populate the DB.
* Visit "http://127.0.0.1:8000/" on your browser to access the web app