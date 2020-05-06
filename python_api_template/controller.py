
from flask import Blueprint, Flask, jsonify


dummy = Blueprint('dummy', __name__)
api = Blueprint('api', __name__)


@dummy.route('/', methods=["GET"])
def dummy_home():
    return jsonify({
        "msg": "hello {}".format(dummy.name)
    })


@api.route('/', methods=["GET"])
def api_home():
    return jsonify({
        "msg": "hey {}".format(api.name)
    })


def create_app(env=None):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.register_blueprint(dummy, url_prefix='/dummy')
    app.register_blueprint(api, url_prefix='/api')

    @app.route("/health")
    def health():
        return jsonify({
            "msg": "I'm healthy"
        })

    return app
