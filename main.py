import random

import discord

intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)

retos = [
    "usa hoy una botella reutilizable",
    "separa la basura organica de la reciclable",
    "evita usar bolsas plasticas durante todo el dia",
    "recicla una lata y dejala limpia",
    "usa bicicleta o camina para un trayecto corto",
    "apaga las luces que no estes usando",
    "cierra el grifo mientras te cepillas los dientes",
    "reutiliza una caja o un frasco vacio",
    "recoge cinco residuos de la calle y tiralos correctamente",
    "no uses vasos desechables durante todo el dia",
]

reto = random.choice(retos)
puntos = {}

canecas = {
    "plastico": "amarillo",
    "papel": "azul",
    "carton": "azul",
    "vidrio": "verde",
}

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!reto":
        await message.channel.send(f"Reto: {reto}. Escribe !reto cumplido al terminarlo.")

    elif message.content == "!reto cumplido":
        usuario = message.author.id
        puntos[usuario] = puntos.get(usuario, 0) + 10
        await message.channel.send(f"Bien hecho! Ganaste 10 puntos verdes. Llevas {puntos[usuario]} en total.")

    elif message.content == "!puntos":
        usuario = message.author.id
        await message.channel.send(f"Tienes {puntos.get(usuario, 0)} puntos verdes.")

    elif message.content.startswith("!reciclar "):
        material = message.content[10:].lower()

        if material in canecas:
            await message.channel.send(f"Ese material va en la caneca de color {canecas[material]}.")
        else:
            await message.channel.send("Prueba con: vidrio, carton, papel o plastico.")

    else:
        await message.channel.send("No le entiendo 😡")

client.run("TOKEN DE DISCORD")
