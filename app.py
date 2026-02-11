from flask import Flask
app = Flask(__name__)

def log():
    print("Sample Docker Container................................")


log()

@app.route('/')
def hello_world():
    return  {'code': '00', 'message': 'We are live!!!!!!'}

@app.route("/health_check")
def health_check():
    return "ok"


@app.route("/readiness_check")
def readiness_check():
        return "ok"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5153"), debug=False)