CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay"
    }
]

ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4,
        "status": "Admitted"
    },
    {
        "id": 2,
        "name": "Roman",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2,
        "status": "Admitted"
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1,
        "status": "Admitted"
    }
]

EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    }
]

LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
]


def all(resource, id):
    """For GET requests to collection"""
    pass


def retrieve(id):
    """For GET requests to a single resource"""
    pass


def create(resource, id):
    """For POST requests to a collection"""
    pass


def update(id):
    """For PUT requests to a single resource"""
    pass


def delete(id):
    """For DELETE requests to a single resource"""
    pass