REQUESTS = [
    {
        "id": 1,
        "parentName": "Brandon",
        "childName": "Nora",
        "numberOfChildren": 2,
        "address": "1234 Street",
        "dateOfReservation": 20221011,
        "lengthOfReservation": 5
    },
    {
        "id": 2,
        "parentName": "Nate",
        "childName": "Jermey",
        "numberOfChildren": 2,
        "address": "45678 Street",
        "dateOfReservation": 20221012,
        "lengthOfReservation": 4
    },
    {
        "id": 3,
        "parentName": "Shane",
        "childName": "Steve",
        "numberOfChildren": 2,
        "address": "1234 Street",
        "dateOfReservation": 20221013,
        "lengthOfReservation": 2
    }
]


def get_all_requests():
    return REQUESTS

def get_single_request(id):

    requested_request = None

    for request in REQUESTS:
        if request["id"] == id:
            requested_request= request

    return requested_request

def create_requests(request):

    max_id = REQUESTS[-1]["id"]

    new_id = max_id + 1

    request["id"] = new_id

    REQUESTS.append(request)

    return request

def update_request(id, new_request):

    for index, request in enumerate(REQUESTS):
        if request["id"] == id:
            REQUESTS[index] = new_request
            break 

def delete_request(id):
    # Initial -1 value for request index, in case one isn't found
    request_index = -1

    # Iterate the requestS list, but use enumerate() so that you
    # can access the index value of each item
    for index, request in enumerate(REQUESTS):
        if request["id"] == id:
            # Found the request. Store the current index.
            request_index = index

    # If the request was found, use pop(int) to remove it from list
    if request_index >= 0:
        REQUESTS.pop(request_index)
