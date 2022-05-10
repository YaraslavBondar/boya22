from core import create_app
from core.config import Config, DevConfig

app = create_app(DevConfig)

if __name__ == '__main__':
    app.run()
