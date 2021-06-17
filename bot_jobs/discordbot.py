import datetime
import json
import os
import random

import discord
import requests
from replit import db
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

API_ROOT = "https://api.github.com"
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
# GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')


def get_pull_requests(owner: str, repo: str):
    yesterday = datetime.datetime.now().date() - datetime.timedelta(days=1)
    yesterday_text = yesterday.strftime("%Y-%m-%d")

    endpoint = f"{API_ROOT}/repos/{owner}/{repo}/pulls"
    params = f"q=created:>={yesterday_text}"
    url = f"{endpoint}?{params}"

    response = requests.get(
        url,
        headers={
            # "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json",
        },
    )

    result = response.json()
    titles = [r["title"] for r in result]

    # return just for tests for now
    return titles


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith("$get-prs"):
        prs = get_pull_requests("pytorch", "pytorch")
        result = "\n".join(prs)
        await message.channel.send(result)


if __name__ == "__main__":
    client.run(DISCORD_TOKEN)
