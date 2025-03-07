from flask import Flask, render_template, request, redirect, url_for

# إنشاء تطبيق Flask
app = Flask(__name__, static_folder="../static", template_folder="../templates")

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
    
    # يمكنك هنا معالجة الملف دون حفظه
    filename = file.filename
    return render_template('result.html', filename=filename)

# هذا السطر مطلوب لتشغيل Flask كـ Serverless Function
def handler(request):
    return app(request)
