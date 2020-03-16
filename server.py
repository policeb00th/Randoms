from flask import Flask, redirect, url_for, request,jsonify
import cm
app = Flask(__name__)

@app.route('/success/Checkmate')
def success(name):
   return cm.abc(name)

@app.route('/Checkmate',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      a=cm.abc(user)
      b={1:a}
      return jsonify(b)
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
if __name__ == '__main__':
   app.run(debug = True,port=8080)