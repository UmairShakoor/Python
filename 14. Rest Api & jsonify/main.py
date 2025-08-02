from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    
@app.route("/even/<int:n>")
def even(n):
    if (n%2) == 0:
        result = {
            'Number': n,
            'Even': True
        }
    else:
        result = {
            'Number': n,
            'Even': False
        }
    return jsonify(result)
        
if __name__ == '__main__':
    app.run(debug=True)
