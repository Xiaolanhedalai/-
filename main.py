from api.expression_api import app as expression_app
from api.emotion_detect_api import app as emotion_app
from api.error_report_api import app as error_app
from api.plugin_api import app as plugin_app
from api.ws_notify import socketio, ws_app
from api.action_manager_api import app as action_app

if __name__ == "__main__":
    from werkzeug.middleware.dispatcher import DispatcherMiddleware
    from flask import Flask
    print("数字人后端服务启动中，请访问 http://localhost:5000")
    master_app = Flask(__name__)
    master_app.wsgi_app = DispatcherMiddleware(
        master_app.wsgi_app,
        {
            "/api/expression": expression_app,
            "/api/emotion": emotion_app,
            "/api/error": error_app,
            "/api/plugin": plugin_app,
            "/api/action": action_app,
        }
    )
    socketio.init_app(master_app)
    socketio.run(master_app, port=5000)