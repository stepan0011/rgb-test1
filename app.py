#from crypt import methods
from flask import Flask,render_template
from flask import request
from flask import send_from_directory
#from flask_sqlalchemy import SQLAlchemy as sql1010
from os import path
import os
#import game
#print(game.tt1)
#f=open('1.score','w')
#f.write('helllo\n')
#f.write('dg')
#exit()
all=['tt1','tt2']
'''a=['1',2,3]
print(a[-1])
a=tuple('hello')
a='hhg'
exit()'''
app=Flask(__name__)

@app.route('/покупка/download/<filename>', methods=['GET', 'POST'])
def download(filename):
     #directory = path.join(app.root_path, app.config['FOLDER_WIT_FILE'])
     return send_from_directory(path=filename,directory=os.getcwd())
@app.route('/')
def home():
     return render_template("home.html")
     #return send_from_directory(path=filename,directory=os.getcwd())
@app.route('/home/<num>')
def zadanie(num):
     return render_template("home-"+num+".html")

#@app.route('/')
#@app.route('/')
if __name__ == '__main__':
     app.run()
