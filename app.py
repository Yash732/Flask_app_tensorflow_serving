from flask import Flask,render_template,url_for,request,redirect
from flask_bootstrap import Bootstrap

import os
import inference
#app instance
app = Flask(__name__)
Bootstrap(app)

@app.route('/',methods= ['GET','POST'])
def index():
    if request.method == 'POST':
        uploaded_file =request.files['file']
        #using the next condition as sometimes only the button gets clicked and no file is uploaded. In that case, nothing needs to be done.
        if uploaded_file.filename != '':
            #saving the image on the server as well using static folder. All the copied image files will be uploaded in this folder
            image_path = os.path.join('static',uploaded_file.filename)
            uploaded_file.save(image_path)

            #now creating an inference
            class_name = inference.get_prediction(image_path)
            print('CLASS NAME=',class_name,"\n")
            result = {
                'class_name ': class_name,
                'image_path':image_path,
            }
            #another html page for showing the resutl
            return render_template("show.html", result= result)

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug = True)
