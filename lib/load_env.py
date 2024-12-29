from os import environ

server_name=environ.get("SERVER_NAME","Minecraft Server")
server_uri_java=environ.get("SERVER_URI_JAVA","localhost")
server_uri_bedrock=environ.get("SERVER_URI_BEDROCK","")
server_map_url=environ.get("SERVER_MAP_URL","")
discord_link=environ.get("DISCORD_LINK","")
image_url=environ.get("BACKGROUND_IMAGE_URL", "")
crafty_url=environ.get("CRAFTY_URL","")
crafty_api_key=environ.get("CRAFTY_API_KEY","")
crafty_server_id=environ.get("CRAFTY_SERVER_ID","")