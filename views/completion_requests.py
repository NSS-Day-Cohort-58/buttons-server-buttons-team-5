
COMPLETIONS = [
    {
        "id": 1,
        "clownId": 1,
        "requestId": 3,
        "date_completion": 2,
    },
    {
        "id": 1,
        "clownId": 1,
        "requestId": 3,
        "date_completion": 2,
    }
]

# get all completions
def get_all_completions():
    return COMPLETIONS

# get single completion
def get_single_completion(id):
    requested_completion = None
    for completion in COMPLETIONS:
        if completion["id"] == id:
            requested_completion = completion
    #return completion according to id 
    return requested_completion

# create completions
def create_completion(completion):
    max_id = COMPLETIONS[-1]["id"]
    new_id = max_id + 1
    completion["id"] = new_id
    COMPLETIONS.append(completion)
    return completion

# delete completions by id
def delete_completion(id):
    completion_index = -1
    for index, completion in enumerate(COMPLETIONS):
        if completion["id"] == id:
            completion_index = index
    if completion_index >= 0:
        COMPLETIONS.pop(completion_index)

# update completion status
def update_completion(id, new_completion):
    for index, completion in enumerate(COMPLETIONS):
        if completion["id"] == id:
            COMPLETIONS[index] = new_completion
            break 