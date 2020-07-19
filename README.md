# ItMovies

A website about movies to provide its customers and users an API to query their database, as well as provide the trusted company users the ability to update or create new records.

## List of available endpoints and supported methods
- localhost/swagger
- localhost/redoc
Note: you should be authenticated to use the unsafe methods

## List of libraries/framework (requirements.txt)
```sh
  Django==3.0.8                 <- Django version
  djangorestframework==3.11.0   <- DRF version
  django-heroku==0.3.1          <- Heroku CLI
  ipython==7.16.1               <- A powerful interactive Python shell
  django-extensions==3.0.3      <- To enable ./manage.py shell_plus --ipython
  drf-yasg==1.17.1              <- Swagger with Django
  gunicorn==20.0.4              <- To deploy the project on Heroku
```
