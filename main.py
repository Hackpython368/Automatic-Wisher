from flask import Flask, render_template
from modules.readData import read_json_file

app = Flask(__name__)

# Dummy data for now
birthdays = read_json_file('Database/dataset.json')

@app.route('/',methods=['POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        date = request.form.get('date')
        # Here you would typically add the new birthday to your data store
        birthdays[name] = [{"name": name, "date": date}]
    return render_template('render.html', data = birthdays)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/card-click', methods=['POST'])
def card_click():
    data = request.get_json()
    print(f"Card clicked: {data['name']} on {data['date']}")
    # You can log this, store in DB, etc.
    return jsonify({'status': 'success'})


@app.route('/add')
def add_birthday():
    # Future: Show form to add birthday
    return "<h2>Add Birthday Page (Coming Soon)</h2>"

if __name__ == '__main__':
    app.run(debug=True)
