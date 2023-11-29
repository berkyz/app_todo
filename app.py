from flask import Flask,render_template,request,redirect,url_for
import veri

app = Flask(__name__)

@app.route("/")
def indexQ():
    return render_template("extra.html")
@app.route("/kayitla")
def index3():
    return render_template("yeni2.html")
@app.route("/kayit",methods=['GET','POST'])
def indexW():
    if request.method=='POST':
        bir=request.form.get("bir")
        iki=request.form.get("iki")
        veri.tabloya_veri_ekle(str(bir),str(iki))
        return render_template("kayıt.html",abc=bir,efg=iki)
    else:
        return redirect(url_for("indexQ"))
@app.route("/giris")
def index():
    return render_template("index.html")
@app.route("/yeni",methods=["GET","POST"])
def index2():
    if request.method=="POST":
        ilk=request.form.get("ilk")
        ikinci=request.form.get("ikinci")
        if veri.tablo_veri_yazma_kullanici(ilk,ikinci)==None or veri.tablo_veri_yazma_sifre(ilk,ikinci)==None:
            return redirect(url_for("index"))
        else:
            return render_template("yeni.html",ilk=ilk)



if __name__=="__main__":
    app.run(debug=True)