from flask import Flask,render_template
from modules.readData import read_json_file

app = Flask(__name__)

@app.route("/")
def hello_world():
    data = read_json_file('Database/dataset.json')
    print(data)
    return render_template('home.html',data=data)


if __name__=="__main__":
    app.run(debug=True)