#First draft for the door sensor server program.
#Flask API, the website server polls(http GET) this pi script for a JSON object
import flask

#Debug, replace with gpio read
def getDoorState():
    return True, ""

app = flask.Flask(__name__)

@app.route('/door', methods=['GET'])
def home():
    doorState, err = getDoorState()
    if(err):
        print(err)
        return
    retJSON = flask.jsonify({"doorIsOpen": doorState})
    return retJSON
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080