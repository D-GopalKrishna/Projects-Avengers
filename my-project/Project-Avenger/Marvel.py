from flask import Flask
from flask import render_template
app = Flask(__name__)




@app.route('/')
def main():
    return render_template("mainpage.html")
    


@app.route('/IronMan')
def IronMan():
    return render_template("Ironman.html")



@app.route('/BlackWidow')
def BlackWidow():
    return render_template("Blackwidow.html")



@app.route('/DoctorStrange')
def DoctorStrange():
    return render_template("Doctorstrange.html")






if __name__=="__main__":
    app.run(debug=True)