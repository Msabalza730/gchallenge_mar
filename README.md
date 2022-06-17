# Challenge consume API Jokes

In this repository you will find my proposed solution to the challenge, the main objective was:

  - Consume Chucknorris Api Jokes from: https://api.chucknorris.io using the param Chuck
  - Consume Dad Api Jokes from: https://icanhazdadjoke.com/api using the param Dad
  - Return error if no param is received
  - Create a C.R.U.D
  
# Tools and Technologies

  - Django Rest Framework
  - Python

# Commands to run my solution:

  - docker-compose run web python manage.py createsuperuser
  - docker-compose run web python manage.py makemigrations
  - docker-compose run web python manage.py migrate
  - docker-compose up --build
