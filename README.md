# 🤖 Discord Voice Channel Notification Bot

Bot de Discord que envía notificaciones por mensaje privado cuando alguien entra a un canal de voz del servidor.

## 📋 Requisitos

- Python 3.8 o superior
- Una cuenta de Discord
- Permisos de administrador en el servidor de Discord donde se usará el bot

## 🚀 Instalación

### 1. Clonar o descargar el proyecto

Descarga todos los archivos en una carpeta local.

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Crear el bot en Discord Developer Portal

1. Ve a [Discord Developer Portal](https://discord.com/developers/applications)
2. Haz clic en **"New Application"**
3. Dale un nombre a tu aplicación y acepta los términos
4. En el menú lateral, ve a **"Bot"**
5. Haz clic en **"Add Bot"** y confirma
6. **Importante**: En la sección de **Privileged Gateway Intents**, activa:
   - ✅ **PRESENCE INTENT**
   - ✅ **SERVER MEMBERS INTENT**
   - ✅ **MESSAGE CONTENT INTENT**
7. Haz clic en **"Reset Token"** y copia el token (lo necesitarás después)

### 4. Invitar el bot a tu servidor

1. En el Developer Portal, ve a **"OAuth2"** > **"URL Generator"**
2. En **SCOPES**, selecciona:
   - ✅ `bot`
3. En **BOT PERMISSIONS**, selecciona:
   - ✅ `View Channels`
   - ✅ `Send Messages`
   - ✅ `Connect` (para canales de voz)
4. Copia la URL generada al final de la página
5. Pega la URL en tu navegador y selecciona el servidor donde quieres añadir el bot
6. Autoriza el bot

### 5. Configurar el archivo .env

1. Copia el archivo `.env.example` y renómbralo a `.env`:
   ```bash
   copy .env.example .env
   ```

2. Edita el archivo `.env` con tus valores:
   ```
   DISCORD_TOKEN=tu_token_del_bot_aqui
   NOTIFY_USER_ID=tu_id_de_usuario_aqui
   ```

#### ¿Cómo obtener tu ID de usuario?

1. Abre Discord
2. Ve a **Configuración de Usuario** > **Avanzado**
3. Activa el **Modo desarrollador**
4. Haz clic derecho en tu nombre de usuario en cualquier parte
5. Selecciona **"Copiar ID"**
6. Pega ese ID en `NOTIFY_USER_ID`

## ▶️ Ejecutar el bot

```bash
python bot.py
```

Si todo está configurado correctamente, verás:

```
✅ Bot conectado como TuBot (ID: xxxxxxxxxx)
📢 Notificando a usuario con ID: xxxxxxxxxx
🔊 Monitoreando 1 servidor(es)
   - Nombre del Servidor (ID: xxxxxxxxxx)
```

## 🎯 Cómo funciona

1. El bot monitorea todos los canales de voz del servidor
2. Cuando alguien **entra** a un canal de voz, el bot detecta el evento
3. El bot envía un mensaje privado al usuario configurado en `NOTIFY_USER_ID`
4. El mensaje incluye:
   - Nombre del usuario que entró
   - Canal de voz al que entró
   - Servidor donde ocurrió
   - Avatar del usuario

## 🛠️ Solución de problemas

### El bot no se conecta
- Verifica que el token en `.env` sea correcto
- Asegúrate de que no haya espacios extra en el archivo `.env`

### No recibo notificaciones
- Verifica que tu `NOTIFY_USER_ID` sea correcto
- Asegúrate de tener los mensajes privados habilitados
- Verifica que el bot tenga los permisos correctos en el servidor
- Revisa que los **Privileged Gateway Intents** estén activados en el Developer Portal

### Error de permisos
- Verifica que el bot tenga permisos para ver canales de voz
- Asegúrate de haber activado los intents en el Developer Portal

## 📝 Notas

- El bot **NO** notifica cuando alguien sale de un canal de voz, solo cuando entra
- El bot ignora a otros bots para evitar spam
- Los mensajes se envían como embeds (mensajes enriquecidos) con formato bonito

## 🔒 Seguridad

- **NUNCA** compartas tu token del bot
- **NUNCA** subas el archivo `.env` a repositorios públicos
- El archivo `.gitignore` ya está configurado para proteger tu `.env`

## 🚀 Deploy en Railway.app (24/7)

Para mantener tu bot activo 24/7 sin tener que dejar tu PC encendida:

### 1. Preparar el repositorio

El proyecto ya está configurado con los archivos necesarios:
- ✅ `Procfile` - Define cómo ejecutar el bot
- ✅ `runtime.txt` - Especifica la versión de Python
- ✅ `.gitignore` - Protege tu archivo `.env`

### 2. Subir a GitHub

```bash
git init
git add .
git commit -m "Initial commit: Discord voice notification bot"
git branch -M main
git remote add origin https://github.com/tu-usuario/discord-voice-bot.git
git push -u origin main
```

### 3. Deploy en Railway

1. Ve a [Railway.app](https://railway.app/) y crea una cuenta (puedes usar GitHub)
2. Haz clic en **"New Project"**
3. Selecciona **"Deploy from GitHub repo"**
4. Autoriza Railway para acceder a tu repositorio
5. Selecciona el repositorio `discord-voice-bot`
6. Railway detectará automáticamente que es un proyecto Python

### 4. Configurar Variables de Entorno

En Railway, ve a tu proyecto y:
1. Haz clic en la pestaña **"Variables"**
2. Añade las siguientes variables:
   - `DISCORD_TOKEN` = tu_token_del_bot
   - `NOTIFY_USER_ID` = tu_id_de_usuario

### 5. Deploy

Railway desplegará automáticamente tu bot. Verás los logs en tiempo real y el bot estará activo 24/7.

### Actualizar el bot

Cada vez que hagas `git push` a tu repositorio, Railway redesplegará automáticamente.

---

## 📄 Licencia

Este proyecto es de código abierto y puede ser usado libremente.
