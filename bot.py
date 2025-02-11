from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
import time
api_id = input('API id:')
api_hash = input('API hash:')
phone_number = input('Phone number (with country code, ex: +90...):')

client = TelegramClient('session_name', api_id, api_hash)
check_valid_users=0
nr_to_check=input('Number of users to add: ')
# Connect to Telegram
client.connect()

# If not authorized, send code and log in
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code (you should receive it in the Telegram app): '))

# Get usernames from file
usernames_file = 'users.txt'
with open(usernames_file, 'r') as file:
    usernames = file.readlines()
    usernames = [username.strip() for username in usernames]

# Assume `channel_entity` is the entity of your channel
channel_username = input('Your channel/group: (t.me/channel): ')
try:
    for username in usernames:
        try:
            # Add each user to the channel
            client(InviteToChannelRequest(channel=channel_username, users=[username]))
            print(f'Successfully added user with username {username} to the channel.')
            check_valid_users+=1;
            if(check_valid_users==nr_to_check):
                exit()
            time.sleep(0.5) 
        except Exception as e:
            print(f'Error adding user {username} to the channel: {e}')
            time.sleep(0.5) 
except Exception as e:
    print(f'Error adding users to the channel: {e}')
    time.sleep(0.5) 

# Disconnect from Telegram
client.disconnect()
