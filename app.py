from flask import Flask
import logging as logger

logger.basicConfig(level="DEBUG")


# created a flask app instance
flaskAppInstance = Flask(__name__)

if __name__ == '__main__':
    logger.debug("Starting the application")

    from api import *
    # creating flask app server
    flaskAppInstance.run(host="localhost", port=5000, debug=True, use_reloader=True)
