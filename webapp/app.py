import predict as p
from net import Net
import os
from io import BytesIO
from flask import Flask
import flask
from PIL import Image
from flask import render_template

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(app.root_path, "static", "img")

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["POST", "GET"])
def prediction():
    name = "placeholder.png"
    title = "upload image"
    result = {"success": False}
    result["predictions"] = []
    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            image1 = flask.request.files["image"]
            # save the image to the upload folder, for display on the webpage.
            image = image1.save(
                os.path.join(app.config["UPLOAD_FOLDER"], image1.filename)
            )

            result["success"] = "Uploaded"
            
            output = p.predict(image1)
            result["predictions"].append(output)
            
            title = "predict"
            result["success"] = "Predicted Result"
            
            return render_template("index.html", result = result, title=title, name=image1.filename)
       
    return render_template("index.html", result = result, title=title, name=name)

if __name__ == "__main__":
    print("* Flask starting server... please wait until the server has fully started (60sec)")
    app.run(debug=True)
    