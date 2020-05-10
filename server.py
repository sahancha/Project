from flask import jsonify
import connexion
import gridfs

# http://0.0.0.0:8080/cloudmesh_ai/ui

#from cloudmesh_abstract import *

#cmdb = CmDatabase()
#db = cmdb.client["ai_services"]

#data = db["files"]
#data.insert_one({"AI Services": "Logistic regression and Image Classification"})

# Create the application instance
app = connexion.App(__name__, specification_dir="./")
app.add_api("knn.yaml")

# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"msg": "It's working!"}
    return jsonify(msg)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
