from flask import Flask, render_template

# just serve all the static files under root
app = Flask(__name__, static_folder='html', static_url_path='')


# for / root, return Hello Word
@app.route("/")
def root():
    return render_template("index.html")


@app.route("/html")
def index():
    return render_template("index.html")


@app.route("/cv")
def cv():
    return render_template("cv.html")


@app.route("/motivation")
def motivation():
    return render_template("motivation.html")


@app.route("/fremtidsplaner")
def fremtidsplaner():
    return render_template("fremtidsplaner.html")


@app.route("/kontakt")
def kontakt():
    return render_template("kontakt.html")


# start listening
if __name__ == "__main__":
    app.run(debug=True, port='8080', host='0.0.0.0')

