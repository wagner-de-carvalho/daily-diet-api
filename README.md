# daily-diet-api
API for creating, deleting, updating and listing meals.

### Setting the application
- `git clone https://github.com/wagner-de-carvalho/daily-diet-api.git`
- `pip install -r requirements.txt`

### Creating the database
- On terminal (linux), enter `flask shell`
- enter `db.create_all()`
- enter `db.session.commit()`
- enter `exit()`

Now you'll be able to see the database and table created.

### Using the API
In the **resources** folder there is a collection generated by the Postman application. Import it and use it to test the API. Remember to replace the environment variable `{{baseFlaskUrl}}` with your **URL**.

