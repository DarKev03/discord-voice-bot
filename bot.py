import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('discord_voice_bot')

# Cargar variables de entorno
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
NOTIFY_USER_ID = os.getenv('NOTIFY_USER_ID')

if not TOKEN:
    raise ValueError("❌ No se encontró DISCORD_TOKEN en el archivo .env")
if not NOTIFY_USER_ID:
    raise ValueError("❌ No se encontró NOTIFY_USER_ID en el archivo .env")

# Configurar intents necesarios
intents = discord.Intents.default()
intents.voice_states = True  # Necesario para detectar cambios en canales de voz
intents.members = True  # Necesario para obtener información de miembros
intents.guilds = True  # Necesario para información del servidor

# Crear cliente del bot
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    """Evento que se ejecuta cuando el bot se conecta exitosamente"""
    logger.info(f'✅ Bot conectado como {bot.user.name} (ID: {bot.user.id})')
    logger.info(f'📢 Notificando a usuario con ID: {NOTIFY_USER_ID}')
    logger.info(f'🔊 Monitoreando {len(bot.guilds)} servidor(es)')
    for guild in bot.guilds:
        logger.info(f'   - {guild.name} (ID: {guild.id})')

@bot.event
async def on_voice_state_update(member, before, after):
    """
    Evento que se ejecuta cuando hay cambios en el estado de voz de un usuario
    
    Args:
        member: El miembro que cambió su estado de voz
        before: Estado de voz anterior
        after: Estado de voz nuevo
    """
    # Ignorar si es el propio bot
    if member.bot:
        return
    
    # Detectar si el usuario entró a un canal de voz sin haber estado antes en uno 
    
    if before.channel is None and after.channel is not None:
        logger.info(f'🎤 {member.name} entró al canal de voz: {after.channel.name}')
        
        try:
            # Obtener el usuario que debe recibir la notificación
            notify_user = await bot.fetch_user(int(NOTIFY_USER_ID))
            
            # Crear el mensaje de notificación
            embed = discord.Embed(
                title="🔊 Alguien entró a un canal de voz",
                description=f"**{member.display_name}** ha entrado a un canal de voz",
                color=discord.Color.green()
            )
            embed.add_field(name="Usuario", value=f"{member.mention} ({member.name})", inline=True)
            embed.add_field(name="Canal de voz", value=after.channel.name, inline=True)
            embed.add_field(name="Servidor", value=member.guild.name, inline=False)
            embed.set_thumbnail(url=member.display_avatar.url)
            embed.set_footer(text=f"ID: {member.id}")
            
            # Enviar mensaje privado
            await notify_user.send(embed=embed)
            logger.info(f'✉️ Notificación enviada a {notify_user.name}')
            
        except discord.errors.Forbidden:
            logger.error(f'❌ No se pudo enviar DM a {NOTIFY_USER_ID} (DMs deshabilitados o bot bloqueado)')
        except discord.errors.NotFound:
            logger.error(f'❌ No se encontró el usuario con ID {NOTIFY_USER_ID}')
        except Exception as e:
            logger.error(f'❌ Error al enviar notificación: {e}')

@bot.event
async def on_error(event, *args, **kwargs):
    """Manejo de errores global"""
    logger.exception(f'❌ Error en evento {event}')

# Iniciar el bot
if __name__ == '__main__':
    try:
        logger.info('🚀 Iniciando bot...')
        bot.run(TOKEN)
    except discord.errors.LoginFailure:
        logger.error('❌ Token inválido. Verifica tu DISCORD_TOKEN en el archivo .env')
    except Exception as e:
        logger.error(f'❌ Error al iniciar el bot: {e}')
