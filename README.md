# daily-diet-api
API for creating, deleting, updating and listing meals.

### Creating the database
1 - On terminal (linux), enter `flask shell`
2 - enter `db.create_all()`
3 - enter `db.session.commit()`
4 - enter `exit()`
Now you'll be able to see the database and table created.

### Using the API
In the **resources** folder there is a collection generated by the Postman application. Import it and use it to test the API. Remember to replace the environment variable `{{baseFlaskUrl}}` with your **URL**.

