# Minecraft Server Web Page
Simple web page to minecraft server on Crafty Controller

## API permission required
- Access
- Logs

## Default credentials
in `/admin`
- **User:** admin
- **Password:** admin

## Run with Docker Compose
```
services:
  mcserver-web-page:
    image: zicstardust/mcserver-web-page:latest
    restart: unless-stopped
    environment:
      #PORT: 5000 #Opcional
      #BACKGROUND_IMAGE_URL: "https://exemple.com/image" #Opcional
    ports:
      - "5000:5000"
    volumes:
      -/path/to/data/:/data/
```