from flask import Flask, render_template, request

app = Flask(__name__)

#renders the form
@app.route('/', methods = ['GET','POST'])
def root():
    print request
    print request.headers
    #this is the method used, whether GET or POST--used in hello.html as
    #the {{method}} variable
    print request.method
    #creates a dictionary; request.args['name'] is the name that the
    #participant enters
    print request.args
    print request.form
    #the form, as rendered on the root
    print render_template('form.html')

#at the hello page: renders the hello message to the reader
@app.route('/hello/', methods = ['GET','POST'])
def hello():
    return render_template('hello.html', method = request.method, name = request.args['name'])

if __name__ == "__main__":
    app.debug = True
    app.run()
