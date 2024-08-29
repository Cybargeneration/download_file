from flask import Flask, render_template, send_from_directory, abort
import os

app = Flask(__name__)

# Directory where files are stored
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), 'downloads')

def is_safe_path(basedir, path, follow_symlinks=True):
    if follow_symlinks:
        return os.path.realpath(path).startswith(basedir)
    return os.path.abspath(path).startswith(basedir)

@app.route('/')
def download():
    files = os.listdir(DOWNLOAD_FOLDER)
    return render_template('download.html', files=files)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/download/<filename>')
def download_file(filename):
    filepath = os.path.join(DOWNLOAD_FOLDER, filename)
    if is_safe_path(DOWNLOAD_FOLDER, filepath) and os.path.exists(filepath):
        return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

