from flask import Flask, render_template, url_for, request
import calc
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == "POST":
      if request.form.get('credit') == 'a':
        s = request.form.get('summ')
        p = request.form.get('percent')
        y = request.form.get('years')
        result = calc.anyitent(s,p,y)
        #вычисляем разницу и что выгоднее
        moneyD = calc.deff(s,p,y)
        moneyA = calc.anyitent(s,p,y)
        for i in range(len(moneyD)):
           moneyA -= moneyD[i]
        what = ''
        if moneyA < 0:
           what = 'Ануитентный'
        else: what = 'Дифференцированный'
        return render_template("index.html",result=result, s=s, p=p, y=y,what=what,money=abs(moneyA))
      
      elif request.form.get('credit') == 'd':
        result = []
        s = request.form.get('summ')
        p = request.form.get('percent')
        y = request.form.get('years')
        result = calc.deff(s,p,y)
        #вычисляем разницу и что выгоднее
        moneyD = calc.deff(s,p,y)
        moneyA = calc.anyitent(s,p,y)
        for i in range(len(moneyD)):
           moneyA -= moneyD[i]
        what = ''
        if moneyA < 0:
           what = 'Ануитентный'
        else: what = 'Дифференцированный'
        result = ' '.join(str(result))
        return render_template("index.html",result=result, s=s, p=p, y=y,what=what,money=abs(moneyA))
      
    else:
      return render_template("index.html")


@app.route('/a/<int:summ>/<int:percent_year>/<int:period>')
def anuitent_url(summ,percent_year,period):
    return str(calc.anyitent(summ,percent_year,period))


@app.route('/d/<int:summ>/<int:percent_year>/<int:period>')
def deff_url(summ,percent_year,period):
    return str(calc.deff(summ,percent_year,period))


if __name__ == '__main__':
    app.run(debug=True)