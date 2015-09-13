from base import app
from controllers import *

app.register_blueprint(data_controller)
app.register_blueprint(index_controller)
