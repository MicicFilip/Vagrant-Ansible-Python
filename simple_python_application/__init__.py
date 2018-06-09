from flask import Flask

application = Flask(__name__)
application.config.from_object('simple_python_application.config')

import simple_python_application.controller