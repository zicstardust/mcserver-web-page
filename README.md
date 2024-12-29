# minecraft-server-web-page
Simple web page to display the status of the minecraft server

## Run Docker Compose
```
services:
  mcserver-web-page:
    image: zicstardust/mcserver-web-page:latest
    restart: unless-stopped
    environment:
      SERVER_NAME: "Server name"
      SERVER_URI_JAVA: "play.exemple.com"
      #PORT: 5000 #Default: 5000
      #SERVER_URI_BEDROCK: "bedrock.exemple.com:19132" #Opcional
      #SERVER_MAP_URL: "https://dynmap.exemple.com"  #Opcional
      #DISCORD_LINK: "https://discord.gg/exemple"  #Opcional
      #BACKGROUND_IMAGE_URL: "https://exemple.com/image" #Opcional
      #CRAFTY_URL: #Opcional
      #CRAFTY_API_KEY: #Opcional
      #CRAFTY_SERVER_ID: #Opcional
    ports:
      - "5000:5000"
```