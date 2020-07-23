from flask import Flask

app =Flask(__name__)


@app.route('/test')
def helloworld():
    return '<h1>hellow world</h1>'

app.run()