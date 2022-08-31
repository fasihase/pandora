# Pandora Challenge
Pandora is a mysterious planet. Those types of planets can support human life, for that reason the president of the Handsome Jack decides to send some people to colonise this new planet and reduce the number of people in their own country. After 10 years, the new president wants to know how the new colony is growing, and wants some information about his citizens. Hence he hired you to build a rest API to provide the desired information.

- - -

## Getting Started
   This Pandora API Code is developed and verified on **mac OS** using **Python** and **Django**.

#### Download or clone the project


Download(and Unzip) or Clone the project from https://github.com/fasihase/pandora.git on your hard drive.


#### Setup environment

    1. Run below commands to install dependencies and activate virtiual environment:

        $ cd pandora
        $ pipenv shell
        $ pipenv install


    2. Run management command migrate to create all the necessary tables:
    
        $ python manage.py migrate

    3. Load the data in database(make sure below commands are executed in specified order):

        $ python scripts/load_companies.py
        $ python scripts/load_people.py

    4. Run server on your local computer:
    
        $ python manage.py runserver

    Then navigate to http://127.0.0.1:8000/api/


### Usage

* To run tests, Run below command:

        $ python manage.py test

* Eager to use different companies.json or people.json files:

    1. Copy companies.json and/or people.json file in resource folder availabe under project directory
    2. Run below command:

        $ python manage.py flush
    
    3. Make sure you have already activated the virtual environemnt
    4. Navigate to the project directory(pandora) 
    5. Run below command
    
        $ python scripts/load_companies.py     
        $ python scripts/load_people.py


## REST API Endpoints:
    
#### 1. Given a company (**_index_** or **_name_**), returns all its employees. Where `1` is index of the company as specified in source data.

#### http://127.0.0.1:8000/api/employees/1/

#### http://127.0.0.1:8000/api/employees/?company=PERMADYNE

JSON:

    {
        "index": 1,
        "company": "PERMADYNE",
        "employees": [
            {
                "index": 289,
                "name": "Frost Foley",
                "age": 22,
                "address": "824 Clark Street, Utting, New Mexico, 3994",
                "phone": "+1 (987) 436-3916"
            },
            {
                "index": 580,
                "name": "Luna Rodgers",
                "age": 56,
                "address": "430 Frank Court, Camino, American Samoa, 2134",
                "phone": "+1 (889) 544-3275"
            },
            {
                "index": 670,
                "name": "Boyer Raymond",
                "age": 20,
                "address": "326 Times Placez, Cumminsville, Montana, 2703",
                "phone": "+1 (867) 458-3241"
            },
            {
                "index": 714,
                "name": "Solomon Cooke",
                "age": 51,
                "address": "340 Granite Street, Cazadero, Colorado, 1597",
                "phone": "+1 (844) 460-3877"
            },
            {
                "index": 828,
                "name": "Walter Avery",
                "age": 35,
                "address": "797 Vandervoort Place, Wheaton, Kentucky, 1051",
                "phone": "+1 (992) 532-3748"
            },
            {
                "index": 928,
                "name": "Hester Malone",
                "age": 38,
                "address": "928 Seaview Court, Jacksonburg, American Samoa, 4161",
                "phone": "+1 (847) 435-3662"
            },
            {
                "index": 985,
                "name": "Arlene Erickson",
                "age": 46,
                "address": "821 Coventry Road, Manchester, New Mexico, 2751",
                "phone": "+1 (878) 521-3781"
            }
        ]
    }
    


#### 2. Given 2 people, provides their information (Name, Age, Address, phone) and the list of their friends in common which have brown eyes and are still alive. Where `15` and `36` are indexes of people as specified in source data.

#### http://127.0.0.1:8000/api/twopeople/15/36/

JSON:

    {
        "person1": {
            "index": 15,
            "name": "Morris Logan",
            "age": 25,
            "address": "776 Thatford Avenue, Wattsville, New York, 8981",
            "phone": "+1 (830) 441-2767"
        },
        "person2": {
            "index": 36,
            "name": "Tammy Lowery",
            "age": 61,
            "address": "856 Macon Street, Tolu, Massachusetts, 6888",
            "phone": "+1 (910) 566-2351"
        },
        "common_friends": [
            {
                "index": 1,
                "name": "Decker Mckenzie",
                "age": 60,
                "address": "492 Stockton Street, Lawrence, Guam, 4854",
                "phone": "+1 (893) 587-3311"
            },
            {
                "index": 4,
                "name": "Mindy Beasley",
                "age": 62,
                "address": "628 Brevoort Place, Bellamy, Kansas, 2696",
                "phone": "+1 (862) 503-2197"
            }
        ]
    }


#### 3. Given 1 person, provides a list of fruits and vegetables they like. This endpoint respects this interface for the output:

#### http://127.0.0.1:8000/api/fruits_and_vegetables/15/

JSON:

    {
        "username": "Morris Logan",
        "age": 25,
        "fruits": [
            "orange",
            "apple",
            "banana"
        ],
        "vegetables": [
            "celery"
        ]
    }
