from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # You can pass variables from Python to HTML like this:
    return render_template("index.html", my_variable="Hello from Python!")

if __name__ == "__main__":
    app.run(debug=True)
