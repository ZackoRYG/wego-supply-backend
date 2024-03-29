# WeGo Demand Backend

A guide to the WeGo demand Flask backend

## Table of Contents

- [Installation](#installation)
- [Set Up](#set-up)
- [Usage](#usage)
- [Contributing](#contributing)

## Installation

1. Clone the repository:
    1. Navigate to /SWETeam21/WeGo Demand/demand_backend in BitBucket
    2. Click Clone in the upper right
    3. Clone the repo by whatever method you prefer

2. Install dependencies:
    1. Navigate to the folder you cloned the repo to in a cli of your choosing
    2. Follow [this guide](https://docs.python.org/3/library/venv.html) to create and activate your virtual environment
    3. Run the following to install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
## Setup
Establish ``config.py`` and ``.env``

### Config
config.py is for all of your system-nonspecific constants. That is, what database you are using, what secret keys you might have, etc.
1. Create a new file named config.py with the following:
    ```py
    DB_NAME = 'test21-supply'
    DB_URI = f'sqlite://{DB_NAME}.db'
    SECRET_KEY = 'FILL ME IN'
    WEGO_SUPPLY = 'FILL ME IN'
    DEBUG = True
    ```
    - DB_URI specifies the URI for the DBMS and DB name you will be using
    - SECRET_KEY specifies the secret key for flask
    - WEGO_SUPPLY specifies the supply server backend we are hitting. Make this your own computer or the real URL for whaterver test you need
    - DEBUG specifies whether the flask app is being run in debug mode or not. We DO NOT run the app in debug on production
### Env
The .env file is for all of our system-specific variables. That is, things that might matter on a windows environment vs various \*nix environments

## Usage
1. Activate your virtual environment, if not already active
2. Run the following:
| OS   | Command |
| -------- | ------- |
| Windows  | ```python app.py```|
| Mac/Linux | ```python3 app.py```|
3. Navitage to whatever location the CLI says when you run the app plus the route of any GET
    - if your route is 'example/get-data', you would go to something like http://127.0.0.1:8080/example/get-data
4. If you see a page showing you a json return, you did everything correctly

## Contributing
### Project Structure
```
+---api
|   +---model
|   +---object
|   +---route
|   |   +---cs
|   |   \---plugins
|   \---service
+---app.py
\---test
```
- *model* contains all of the database construction
- *object* contains all of the logic specific to the code representation of an object
- *route* contains all the blueprint initialization and route control
- *service* contains any helper function that formats anything or manipulates data

If you wanted to make a 'foo' endpoint, there would be:
- a foo table defined in /model/db_models.py
- a foo_service.py that has functions for fetching and manipulating data from the database
- a foo_route.py in route defines the blueprint that has all of the route endpoints for a foo
- a foo object that handles all of the logic specific to a foo representation

### Naming endpoints
Follow the beginning of [this guide](https://auth0.com/blog/best-practices-for-flask-api-development/) for a description of endpoint naming best practices