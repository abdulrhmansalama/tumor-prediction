from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__, static_folder="../static", template_folder="../templates")
app.config['UPLOAD_FOLDER'] = 'uploads/'

# إنشاء مجلد uploads إذا لم يكن موجودًا
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    
    return render_template('result.html', filename=file.filename)

# هذا السطر مطلوب لتشغيل Flask كـ Serverless Function
def handler(request):
    return app(request)
