import os, sys
from dream_team_app import create_app

config_name = os.getenv('FLASK_CONFIG', 'production')
app = create_app(config_name)


if __name__ == '__main__':
    app.run()
