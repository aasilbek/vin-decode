# VIN-decoder Project

## Outline
- Prerequisites
- Setup
    - Development
- Documentation


## Prerequisites
This project has the following prerequisites
- python 3.8.5
- docker 19.03.12
- docker-compose 1.25.0


## Setup

### Development

- Install virtual environment:
```
git clone git@github.com:aasilbek/vin-decode.git
cd clyqe-backend
python3.8 -m venv --prompt="v" .env
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

- If *postgresql database* has not started please start it by following command:
```
docker-compose -f deployments/development/docker-compose.yml up -d
```

- If *development packages* has not been installed please install by running following commit:
```
pip install -r requirements/development.txt
```

- If *migration* has not been applied please apply it first:
```
cd src
python manage.py migrate
```

- Start development server:
```
python runserver 0.0.0.0:8080
```
