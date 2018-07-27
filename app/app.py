from flask import Flask
from flask_restplus import Resource, Api
import os

app = Flask(__name__)
api = Api(app)

@api.route('/shutdown')
class Shutdown(Resource):
    def get(self):
        os.system('/sbin/shutdown -h +2')
        return {'shutdown_in': 2 }

@api.route('/cancel')
class CancelShutdown(Resource):
    def get(self):
        os.system('/sbin/shutdown -c')
        return {'shutdown_in': -1 }

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')