# DjModels Demo App using Flask

This app demonstrates how you can DjModels together with Flask.


### Setup

- Clone this repo
- Install Docker & Docker Compose
- Start the stack `docker-compose up -d`
- Create migrations, if any: `docker-compose run app python3 manage.py makemigrations`
- Run migrations, if any: `docker-compose run app python3 manage.py migrate`

## Demo
- Visit http://0.0.0.0:5000/ to view a count of objects in the database.
- Send a POST request to add more `curl -X POST http://0.0.0.0:5000/`
 
 
## Licence

MIT