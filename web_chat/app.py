from flask import Flask, render_template, request
import pymongo


mongo = pymongo.MongoClient('mongodb://myUserAdmin:abc123@mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0')
db = mongo.test_database
messages = db.messages

app = Flask(__name__)

def whole_chat():
    chat_mes = []
    cursor = messages.find({})
    for document in cursor:
        # print(document)
        chat_mes.append({document['author']: document['text']})
    return chat_mes

@app.route('/', methods=['GET','POST'])
def hello_world():
    mess = whole_chat()
    if request.method == 'POST':
        author = request.form.get('author')
        text = request.form.get('text')
        messages.insert_one({"author": author, "text": text})

    return render_template("index.html", chat = mess)

@app.route('/add')
def add_test_message():
    mes_id = messages.insert_one({"author": "Admin", "text": "testing chat"})
    return "Added"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
