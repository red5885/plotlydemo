from flask import Flask
import chart

def create_app():
    app = Flask(__name__)
    app.register_blueprint(chart.bp)
    return app

if (__name__ == '__main__'):
    app = create_app()

    app.run(host='0.0.0.0',port=5001,debug=True)