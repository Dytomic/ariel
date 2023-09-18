
import json

intents = {}
responses = {}

with open('dytomic.json') as f:
    json_file = json.load(f)
    intents["FACEBOOK_APP_ID_DYTOMIC"] = json_file["intents"]
    responses["FACEBOOK_APP_ID_DYTOMIC"] = json_file["responses"]

with open('PRO.json') as f:
    json_file = json.load(f)
    intents["FACEBOOK_APP_ID_PRO"] = json_file["intents"]
    responses["FACEBOOK_APP_ID_PRO"] = json_file["responses"]

def resolve_intent(recipient_id, message):
    for intent in intents[recipient_id].items():
        if message.lower() in map(lambda example: example.lower(), intent[1]["examples"]):
            return intent[0]
    return None

def receive_message(recipient_id, message):
    response = responses[recipient_id].get(message)
    if not response:
        intent = resolve_intent(recipient_id, message)
        response = responses[recipient_id].get(intent)
    return response
