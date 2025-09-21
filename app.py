# from flask import Flask,render_template,request

# app=Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def feedback():
#     if request.method == "POST": #data submited or not
#         name=request.form.get("username")
#         message=request.form.get("message")

#         return render_template("thankyou.html", user=name, message=message)
    
#     return render_template("feedback.html")


from flask import Flask,request,flash,redirect,url_for,render_template

app=Flask(__name__)

app.secret_key="my_key"

@app.route("/",methods=["GET","POST"])
def form():
    if request.method == "POST":
        name=request.form.get("username")

        if not name:
            flash("name can't be empty")
            return redirect(url_for("form"))
        
        flash(f"thanks {name}, your feedback was saved")
        return redirect(url_for("thankyou")) # display in same page where you are becouse redirecting 
    
    return render_template("form.html")

    
@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")
    

if __name__=="__main__":
    app.run()
