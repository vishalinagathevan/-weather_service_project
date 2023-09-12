from flask import Flask, render_template
from flask_restful import Resource, Api
from weather_service import (
    get_current_location,
    get_default_location,
    get_current_weather,
)
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

  
app = Flask(__name__)
api = Api(app)

@app.route('/')
def info():
    return render_template('info.html')

class Weather(Resource):
  
    def get(self):
        location = get_current_location()
        if not location:
            location = get_default_location()
        app.logger.info("Location received as : {}".format(location))  
        return get_current_weather(location)

          
# adding the defined resources along with their corresponding urls
api.add_resource(Weather, '/api/v1/weather')

# driver function
if __name__ == '__main__':
    # app.run(debug = True)
    app.run(host='0.0.0.0', port = 5000, debug = True)