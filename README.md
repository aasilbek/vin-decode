# VIN-decoder Project

## Outline
- Prerequisites
- Setup
    - Development
- Documentation


## Prerequisites
This project has the following prerequisites
- docker 19.03.12
- docker-compose 1.25.0


## Setup

### Development

- Install virtual environment:
```
git clone git@github.com:aasilbek/vin-decode.git
cd vin-decode

```

- Load *local environment variables* to virtual environment:
```
cp ./deployments/development/env_example ./deployments/development/.env
change .env variable according to your settings
source ./deployments/development/.env
```

- If *pre commit* has not been installed please install by running following command:
```
pip install pre-commit
pre-commit install
```

- If *migration* has not been applied please apply it first:
```
docker-compose run app python src/manage.py migrate 
OR use
source manager migrate
```

 - If There is no user in database:
```
  docker-compose run app python src/manage.py createsuperuser
 OR use
 source manager createuser
```

 - Start development server:
```
docker-compose up
OR use 
source manager runserver
```

 - Documentation to API in :
```
  http://0.0.0.0:8000/decode/{vin_number}/
```