import json


def get_payload(payload: str, replaces: dict = {}) -> dict:
    filedata = ""
    with open("payloads/" + payload + ".json", "r") as file:
        filedata = file.read()

    # Replace the target string
    for key in replaces:
        filedata = filedata.replace("${" + key + "}", replaces[key])

    return json.loads(filedata)
