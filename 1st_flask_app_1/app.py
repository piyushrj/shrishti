from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #route decorator ( @app.route('/') ) to specify the URL that should
# trigger the execution of the index function
def index():
    return render_template('first_app.html')

if __name__ == '__main__':
    app.run()
