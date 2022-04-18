import sys
import os
from threads import main
from flask import Flask, request, render_template

from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'some secret key'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    render_template('upload.html')
    if request.method == 'POST':
        if 'file' in request.files:

            f = request.files['file']  #getting uploaded video 
            basepath = os.path.dirname(__file__)
            file_path = os.path.join(basepath, 'input', secure_filename(f.filename))
            f.save(file_path)  #saving uploaded video

            output = main(file_path) #running vidframe with the uploaded video
            os.remove(file_path)  #removing the video as we dont need it anymore
        else:
            print("Not working")
        print(output['video'])
        print(output['text'])
        print(output['speech'])
    return None


if __name__ == '__main__':
    app.run(debug=False)
    app.secret_key = 'some secret key'