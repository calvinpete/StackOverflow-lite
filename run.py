from app import create_app
from instance.config import DevelopmentConfig

# The application initialization creates an instance to pass all client requests to it
app = create_app(DevelopmentConfig)

if __name__ == '__main__':
    app.run()
