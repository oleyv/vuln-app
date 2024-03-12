from flask import Flask, render_template, request
import os, subprocess

app = Flask(__name__)

@app.route('/up_me')
def up_me():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        from_web = request.files['file']
        from_web.save(os.path.join('/opt/app/files', from_web.filename))
        # pwnd portion; it is very unlikely that someone could do it,but for demo purposes is good 
        # app.logger.debug(f"============ls {from_web.filename}============")
        command = [f'cd /opt/app/files && {from_web.filename}']
        get_pwnd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
        lst =  get_pwnd.read()
        return lst.decode()
    return 'No file uploaded'

@app.route('/')
def home():
    return '<h1>This is not the droids that you are looking for, so live long and prosper!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
