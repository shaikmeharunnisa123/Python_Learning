from flask import Flask,jsonify  # Flask -web framework class

app = Flask(__name__)

my_custom_data = {
    "status" : "Success",
    "user" : "Developer",
    "items" : ["apple","banana","cherry"]
    "designation" : "Developer"
}

@app.route('/api/data',methods=['GET'])

def get_custom_data():
    return jsonify(my_custom_data)

if __name__ == '__main__':
    app.run(debug=True, port= 5000)