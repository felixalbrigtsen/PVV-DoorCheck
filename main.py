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