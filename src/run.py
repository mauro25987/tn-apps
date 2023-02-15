from app import create_app, enviroment

app = create_app(enviroment)

if __name__ == '__main__':
    app.run()
