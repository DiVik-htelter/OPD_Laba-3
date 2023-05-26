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
        return render_template("index.html",result=result, s=s, p=p, y=y)
      elif request.form.get('credit') == 'd':
        result = []
        s = request.form.get('summ')
        p = request.form.get('percent')
        y = request.form.get('years')
        result = calc.deff(s,p,y)
        return render_template("index.html",result=result,s=s,p=p,y=y)
      else:
         return render_template("index.html")
    else:
      return render_template("index.html")


@app.route('/<int:summ>/<int:percent_year>/<int:period>')
def mortgage_calculator(summ,percent_year,period):
    return str(calc.anyitent(summ,percent_year,period))


if __name__ == '__main__':
    app.run(debug=True)