from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import slack
import os
from dotenv import load_dotenv

load_dotenv()
user_id = 'U04SD2EFKM5'
SLACK_TOKEN = os.environ["SLACK_TOKEN"]
print("SLACK_TOKEN", SLACK_TOKEN)
client = WebClient(token=os.environ['SLACK_TOKEN'])

def message_instructor():
    try:
        result = client.chat_postMessage(
            channel= user_id,
            text= 'Hello World'
        )
        print(result)
    except SlackApiError as e:
        print(f"Error posting message: {e}")


message_instructor()

print('\n Running in script.py \n')
