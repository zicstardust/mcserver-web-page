from lib.background_image import define_background_image
from lib.app import *

def before_start_app():
    define_background_image()
    api_status = check_api(crafty_url, crafty_api_key, crafty_server_id)
    if api_status != 'Ok':
        print('Error in Crafty environment variables: {}'.format(check_api(crafty_url, crafty_api_key, crafty_server_id)))

def production():
    before_start_app()
    return app


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    before_start_app()
    app.run(debug=True)
