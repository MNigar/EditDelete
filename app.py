from flask import Flask,render_template,request,redirect,url_for
from data import Xeber
from flask_modus import Modus
app = Flask(__name__)
modus=Modus(app)
news=[]
news.append(Xeber(1,"Xeber 01","Xeber 01 Detal"))
#  index page
@app.route('/')
def index():
    return render_template("index.html")

#  news page
@app.route('/xeberler')
def xeberler():
    return render_template("xeberler.html",data=news)

#  single news page
def find(id):
#   return [new for new in news if new.id==id][0]
    for i in news:
         if (int(id)==i.id):
             obj=i
    return obj
@app.route('/xeber/<id>',methods=["GET","PATCH"])
def xeber(id):
    """Renders the contact page."""
    fnews=find(id)
    if request.method==b'PATCH':
        fnews.title=request.form['title']
        fnews.body=request.form['body']
        return redirect(url_for('xeberler'))
    return render_template(
        "xeber.html",
       data=fnews)

@app.route('/delete/<id>')
def delete(id):
    for i in news:
            if(int(id)==i.id):
             news.remove(i)           
    return redirect(url_for('xeberler'))


x_id=1
@app.route('/yeni',methods=["GET","POST"])
def yeni():
    if request.method=="POST":
        global x_id
        x_id+=1
        t=request.form['title']
        d=request.form['body']
        yeniXeber=Xeber(x_id,t,d)
        news.append(yeniXeber)
        return render_template("yeni.html",message="Yeni xeber elave olundu")
    else:
        return render_template("yeni.html",message="Xeber elave olunmayib")

# @app.route('/edit/<int:id>',methods=["GET,POST"] )
# def edit(id):
    #  if request.method=="POST":
    #     for i in news:
    #         if(int(id)==i.id):                     
    #          i.title=request.form['title']
    #          i.body=request.form['detail']
    #          obj=i
    #          news.session.commit()
    #     return render_template("edit.html",message="Deyisdi")
    
    #  if request.method=="GET":
    #     for i in news:
    #         if(int(id)==i.id):                     
    #           obj=i
    #     return render_template("edit.html",message="Get",b=obj)
   
@app.route('/edit/<int:id>')
def edit(id):
    
    new1=find(id)
    return render_template("edit.html",data=new1)




if __name__ == '__main__':
    app.run(debug=True)