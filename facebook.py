import ariel

from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)

VERIFY_TOKEN = ""
DYTOMIC_ACCESS_TOKEN = ""
PRO_ACCESS_TOKEN = ""

bots = {}
bots["FACEBOOK_APP_ID_DYTOMIC"] = Bot(DYTOMIC_ACCESS_TOKEN)
bots["FACEBOOK_APP_ID_DYTOMIC"] = Bot(PRO_ACCESS_TOKEN)

bots["FACEBOOK_APP_ID_PRO"].set_get_started({ "get_started": { "payload": "Get Started" } })
bots["FACEBOOK_APP_ID_PRO"].set_get_started({ "get_started": { "payload": "Get Started" } })

def process_response(recipient_id, sender_id, response):
    if response.get("buttons"):
        bots[recipient_id].send_button_message(sender_id, response["text"][0], response["buttons"])
    elif response.get("quick_replies"):
        bots[recipient_id].send_message(sender_id, { "text": response["text"][0], "quick_replies": response["quick_replies"] })
    else:
        bots[recipient_id].send_text_message(sender_id, response["text"][0])

def process_message(recipient_id, sender_id, text):
    response = ariel.receive_message(recipient_id, text)
    if response:
        process_response(recipient_id, sender_id, response)
        if response.get("connect"):
            response = ariel.receive_message(recipient_id, response["connect"])
            process_response(recipient_id, sender_id, response)
    return "Success"

def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
       output = request.get_json()
       
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            sender_id = message['sender']['id']
            recipient_id = message['recipient']['id']

            text = None
            if message.get("postback"):
                text = message["postback"].get("payload")
            elif message.get('message'):
                if message['message'].get("quick_reply"):
                    text = message['message']["quick_reply"].get("payload")
                else:
                    text = message['message'].get("text")

            if text:
                process_message(recipient_id, sender_id, text)
                
    return "Message processed"

if __name__ == "__main__":
    app.run()

