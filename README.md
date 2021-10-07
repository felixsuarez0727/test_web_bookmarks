Installation steps:
1. Create the virtual environment and activate it.
2. Install the dependencies from "requirements.txt" file using command - pip install -r requirements.txt
3. Migrate the database. 
4. Start the server.

Now, you should be able to access the endpoints. 
Base url: localhost:8000/bookmark
Endpoints:
1. GET      /      --> To get all the bookmarks saved in the DB.
2. GET      /\<id\>/  --> To retrive specific bookmark.
3. POST     /  --> To create the bookmark. Header content-type: json, JSON with fields "title" and "text" 
4. PUT      /\<id\>/ To update the bookmark of the given id. Header content-type: json, JSON with fields "title" and "text"
4. Delete   /\<id\>/  --> To delete the bookmark for the given ID.
