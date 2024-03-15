from flask import Flask

app = Flask("OBPS")

@app.route('/')
def hello():
    return 'Hi everyone'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
