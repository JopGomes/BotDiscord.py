import discord
import requests
import json
import random

client = discord.Client()
discussion_words = ["tchau", "assim", "termino", "tudo bem"]
peace_words = ["Vocês se amam","E o eu te amo?","Vocês vao dar certo juntos","Calma gente"]
sad_words =["triste","poxa","chorando","chorei"]
hello_words=["oi","ola","iai"]
bye_words=["boa noite","ate","durma bem"]
response_bye_words=["vou ficar com saudade","ate a proxima","voltem logo"]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print('Estamos logados como {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content.lower()
    canal= message.channel
    if any(word in msg for word in sad_words):
        quote = get_quote()
        await canal.send(quote)
    if any(word in msg for word in discussion_words):
        await canal.send(random.choice(peace_words))
    if any(word in msg for word in bye_words):
        await canal.send(random.choice(response_bye_words))


client.run('OTU1MDU4NTQzODIyNzcwMTc2.YjcJlA._fc7jwRENu9dV6wSxqeNcqO4zgc')