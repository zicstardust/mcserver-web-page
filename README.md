# Minecraft Server Web Page
Simple web page to minecraft server on Crafty Controller

## API permissions
- Access
- Logs

## Run with Docker Compose
```
services:
  mcserver-web-page:
    image: zicstardust/mcserver-web-page:latest
    restart: unless-stopped
    environment:
      CRAFTY_URL: "https://crafty.exemple.com"
      CRAFTY_API_KEY: "abcdefghijk"
      CRAFTY_SERVER_ID: "12345-12345-12345-12345-12345"
      SERVER_URI_JAVA: "play.exemple.com"
      #PORT: 5000 #Opcional
      #SERVER_URI_BEDROCK: "bedrock.exemple.com:19132" #Opcional
      #SERVER_MAP_URL: "https://dynmap.exemple.com"  #Opcional
      #DISCORD_LINK: "https://discord.gg/exemple"  #Opcional
      #BACKGROUND_IMAGE_URL: "https://exemple.com/image" #Opcional
    ports:
      - "5000:5000"
```