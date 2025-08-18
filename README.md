# Minecraft Server Web Page
Simple web page to minecraft server on Crafty Controller

[GitHub](https://github.com/zicstardust/mcserver-web-page)

[Docker Hub](https://hub.docker.com/r/zicstardust/mcserver-web-page)


## Supported Architectures

| Architecture | Available | Tag |
| :----: | :----: | ---- |
| 386 | ✅ | latest |
| amd64 | ✅ | latest |
| arm/v6 | ✅ | latest |
| arm/v7 | ✅ | latest |
| arm64 | ✅ | latest |
| ppc64le | ✅ | latest |
| s390x | ✅ | latest |

## Tags

| Tag | Available | Description |
| :----: | :----: |--- |
| [`latest`](https://github.com/zicstardust/mcserver-web-page/blob/main/Dockerfile) | ✅ | Default tag |


## Usage
### API permission required
- Access
- Logs

**No use "full access" API permission**

### Default credentials
- **User:** admin
- **Password:** admin

### docker-compose
```
services:
  mcserver-web-page:
    image: zicstardust/mcserver-web-page:latest
    restart: unless-stopped
    container_name: mcserver-web-page
    environment:
      PUID: 1000
      PGID: 1000
    ports:
      - "5000:5000"
    volumes:
      - /path/to/data/:/data/
```
### docker cli
```
docker run -d \
  --name=mcserver-web-page \
  -e PUID=1000 \
  -e PGID=1000 \
  -p 5000:5000 \
  -v /path/to/data/:/data/ \
  --restart unless-stopped \
  zicstardust/mcserver-web-page:latest
```
## Environment variables

| variables | Function | Default |
| :----: | --- | --- |
| `PUID` | Set User ID | 1000 |
| `PGID` | Set Group ID | 1000 |
| `BACKGROUND_IMAGE_URL` | Set background image | |


## Dev environment
[Dev environment here](https://github.com/zicstardust/mcserver-web-page/blob/main/README-dev.md)