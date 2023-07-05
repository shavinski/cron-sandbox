import slack
import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
user_id = 'U04SD2EFKM5'

load_dotenv(dotenv_path=env_path)
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

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
