DATABASE = {
    "customers": {
        "id": 1,
        "name": "Ryan Tanay"
    },
    "animals": [
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
    ],
    "employees": {
            "id": 1,
            "name": "Jenna Solis"
    },
    "locations": [
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
}


def all(resource):
    """For GET requests to collection"""
    return DATABASE[resource]


def retrieve(id, resource):
    """For GET requests to a single resource"""
    requested_data = None

    for resource in DATABASE[resource]:
        if resource["id"] == id:
            requested_data = resource

    return requested_data


def create(resource, post_body):
    """For POST requests to a collection"""
    max_id = DATABASE[resource][-1]["id"]

    new_id = max_id + 1
    post_body["id"] = new_id

    DATABASE[resource].append(post_body)

    return resource


def update(id, post_body, resource):
    """For PUT requests to a single resource"""
    for index, item in enumerate(DATABASE[resource]):
        if item["id"] == id:
            DATABASE[resource][index] = post_body
            break


def delete(id, resource):
    """For DELETE requests to a single resource"""
    resource_index = -1
    for index, item in enumerate(DATABASE[resource]):
        if item["id"] == id:
            resource_index = index

    if resource_index >= 0:
        DATABASE[resource].pop(resource_index)
