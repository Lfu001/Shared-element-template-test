from flask import *
import os

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.html")


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 9761))
    app.run(debug=True, port=port, host="0.0.0.0")
