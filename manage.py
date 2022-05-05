from core import create_app
from core.config import Config

app = create_app(Config)

if __name__ == '__main__':
    app.run()
