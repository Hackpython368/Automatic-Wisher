from flask import Flask, render_template
from modules.readData import read_json_file

app = Flask(__name__)

# Dummy data for now
birthdays = read_json_file('Database/dataset.json')

@app.route('/')
def index():
    return render_template('render.html', data = birthdays)

@app.route('/add')
def add_birthday():
    # Future: Show form to add birthday
    return "<h2>Add Birthday Page (Coming Soon)</h2>"

if __name__ == '__main__':
    app.run(debug=True)
