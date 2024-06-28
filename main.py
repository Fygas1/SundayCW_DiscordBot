from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_responses

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
#print(TOKEN)

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')
    
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()