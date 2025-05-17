from flask import *
import mysql.connector
from flask_mail import Mail, Message
from flask_session import Session
import random

app = Flask(__name__) 

app.secret_key = 'adsfadsfasddf'


mail = Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'wa6073318@gmail.com'
app.config['MAIL_PASSWORD'] = 'efvp vknl spvp gsgp'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/")
def index():
    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
  return render_template("login.html")

@app.route("/registration") 
def registration():
  return render_template("register.html")

@app.route("/show")
def show():
  con=mysql.connector.connect(host="localhost",user="root",password="",database="wasim")
  qry="select * from user "
  cur=con.cursor()
  cur.execute(qry)
  dt=cur.fetchall()                
  return render_template("show.html",data=dt)

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/forget")
def forget():
  return render_template("fotget.html")

@app.route("/reg", methods=['POST','GET'])
def reg():
  if request.method=="POST":
    nm=request.form['vnm']
    em=request.form['vem']
    ps=request.form['vpass']
    cnt=request.form['vcon']
    myfile=request.files['vfile']
    myfile.save("static/image/"+myfile.filename)

    con=mysql.connector.connect(host="localhost",user="root",password="",database="wasim")
    qry="select * from user where email ='" + em + "' "
    cur=con.cursor()
    cur.execute(qry)
    cur.fetchall()                
    if(cur.rowcount>=1):
      return render_template("register.html",err="email already hai!")
    else:
      con=mysql.connector.connect(host="localhost",user="root",password="",database="wasim")
      cur=con.cursor()
      qry="insert into user set username='"+nm+"',email='"+em+"',password='"+ps+"',contact='"+str(cnt)+"',image='"+myfile.filename+"' "
      cur.execute(qry)
      con.commit()
      return render_template("login.html")
  else:
    return render_template("page404.html")
  

@app.route("/sinup",methods=['GET','POST'])
def sinup():
  if request.method == "POST":
    em=request.form['vem']
    ps=request.form['vpass']

    con=mysql.connector.connect(host="localhost",user="root",password="",database="wasim")
    qry="select * from user where email ='" + em + "' "
    cur=con.cursor()
    cur.execute(qry)
    data=cur.fetchone()
    if cur.rowcount>=1:
      if data[3]==ps:
        return render_template("home.html",mes=data)
      else:
        return render_template("login.html",mes="password not match")
    else:
      return render_template("login.html",mes="Please register first")

@app.route("/delete/<id>")
def delete(id):
  con=mysql.connector.connect(host="localhost",user="root",password="",database="wasim")
  cur=con.cursor()
  cur.execute("delete from user where id = "+str(id))
  con.commit()
  return redirect("/show")

@app.route("/update/<id>")
def update(id):
  con=mysql.connector.connect(host="localhost",user="root",password="",database="wasim")
  cur=con.cursor()
  cur.execute("select * from user where id = "+str(id))
  updata=cur.fetchone()
  return render_template("update.html",dt=updata)

@app.route("/updatapage", methods=['POST','GET'])
def updatapage():
  if request.method=="POST":
    uid=request.form['userid']
    nm=request.form['vnm']
    em=request.form['vem']
    ps=request.form['vpass']
    cnt=request.form['vcon']
    myfile=request.files['vfile']
    myfile.save("static/image/"+myfile.filename)

    con=mysql.connector.connect(host="localhost",user="root",password="",database="wasim")
    cur=con.cursor()
    qry="update user set name='"+nm+"',email='"+em+"',password='"+ps+"',contact='"+str(cnt)+"',image='"+myfile.filename+"' where id='"+str(uid)+"' "
    cur.execute(qry)
    con.commit()
    return redirect("/show")

@app.route("/otp",methods=["GET","POST"])
def otp():
  if request.method == "POST":
    session['em']=em=request.form["fem"]  
    session['OTP']=OTP=random.randint(00000,99999)
    msg = Message('Hello', sender = 'wa6073318@gmail.com', recipients = [em])
    msg.body = "Your OTP is " +str(OTP )+ " Please do not share anyone OTP!"
    mail.send(msg)
  return render_template("updateotp.html")

@app.route("/changepass",methods=["GET","POST"])
def changepass():
  if request.method=="POST":
    motp=request.form["myotp"]
    ps=request.form["pass"]
    cps=request.form["cpass"]
    msotp=session['OTP']
    msem=session['em']
    if str(motp)==str(msotp):
      con=mysql.connector.connect(host="localhost",user="root",password="",database="wasim")
      cur=con.cursor()
      qry="update user set password='"+ps+"' where email='"+msem+"' "
      cur.execute(qry)
      con.commit()
      return redirect("/login")
  return redirect("/registration")


@app.route("/User-Page",methods=["GET","POST"])
def userpage():
  if request.method=="POST":
    name=request.form["name"]
    password=request.form["password"]
    
    con=mysql.connector.connect(host="127.0.0.1",user="root",password="",database="wasim")
    cur=con.cursor()
    
    qry="insert into userlogin set name='"+name+"',password='"+password+"' "
    cur.execute(qry)
    con.commit()
    return redirect("/User-Page")
    
  else:
    return render_template("userpage.html")



  
  
  
  
@app.route("/logout")
def logout():
  
  return render_template("login.html"  )
if __name__ == '__main__':
    app.run(debug=True)