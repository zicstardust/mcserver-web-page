# Minecraft Server Web Page
Simple web page to minecraft server on Crafty Controller

## Infos

### API permission required
- Access
- Logs

**No use "full access" API permission**

### Default credentials
- **User:** admin
- **Password:** admin

## Dev environment
Recommended to use asdf to keep the same python version

Python version used in `.tool-versions` file

```
pip install -r requirements-dev.txt
python app/main.py
```

## Production - Docker Compose
```
services:
  mcserver-web-page:
    image: zicstardust/mcserver-web-page:latest
    restart: unless-stopped
    environment:
      #UID: 1000 #Permission /data
      #GID: 1000 #Permission /data
      #PORT: 5000 #App port
      #BACKGROUND_IMAGE_URL: "https://exemple.com/image" #Opcional
    ports:
      - "5000:5000"
    volumes:
      - /path/to/data/:/data/
```