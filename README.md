# Installation steps:
1. Create the virtual environment and activate it.
```
virtualenv mypython
source mypython/bin/activate
```
2. Install the dependencies from "requirements.txt":
```
pip install -r requirements.txt
```
4. Migrate the database.
```
python3 manage.py migrate
```
6. Start the server.
```
python3 manage.py runserver 0.0.0.0:8000
```

# Endpoint Description

You should be able to access the endpoints:

1. GET      /      --> To get all the bookmarks saved in the DB.
2. GET      /\<id\>/  --> To retrive specific bookmark.
3. POST     /  --> To create the bookmark. Header content-type: json, JSON with fields "title" and "text" 
4. PUT      /\<id\>/ To update the bookmark of the given id. Header content-type: json, JSON with fields "title" and "text"
4. Delete   /\<id\>/  --> To delete the bookmark for the given ID.

# Testing
