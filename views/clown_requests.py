CLOWNS =[
    {
        "id":1,
        "name":"Rob"
    },
    {
        "id":2,
        "name":"John"
    },
    {
        "id":3,
        "name":"Kate"
    }
]

def get_all_clowns():
    return CLOWNS

def get_single_clown(id):
    # Variable to hold the found metal, if it exists
    requested_clown = None

    # Iterate the METALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for clown in CLOWNS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if clown["id"] == id:
            requested_clown = clown

    return requested_clown


def create_clown(clown):
    # Get the id value of the last order in the list
    max_id = CLOWNS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the order dictionary
    clown["id"] = new_id

    # Add the order dictionary to the list
    CLOWNS.append(clown)

    # Return the dictionary with `id` property added
    return clown