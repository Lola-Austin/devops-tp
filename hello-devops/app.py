from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, CI/CD!"

@app.route('/status')
def status():
    return "Status: OK"

if __name__ == "__main__":
    app.run()
📝 Explanation:
Flask(__name__): Creates the web app.

@app.route('/'): Defines a URL endpoint ("/") that returns the message.

app.run(): Starts the server when the file is executed directly.

