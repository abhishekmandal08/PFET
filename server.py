import os
from bottle import route, request, static_file, run

@route('/')
def root():
    return static_file('test.html', root='.')

@route('/upload', method='POST')
def do_upload():
    # category = request.forms.get('category')
    upload = request.files.get('original')
    name, ext = os.path.splitext(upload.filename)
    upload2 = request.files.get('mask')
    name2, ext2 = os.path.splitext(upload2.filename)
    upload3 = request.files.get('gt')
    name3, ext3 = os.path.splitext(upload3.filename)
    if ext not in ('.png', '.jpg', '.jpeg', '.JPG', '.gif', '.tif'):
        return "File extension not allowed."
    if ext2 not in ('.png', '.jpg', '.jpeg', '.JPG', '.gif', '.tif'):
        return "File extension not allowed."
    if ext3 not in ('.png', '.jpg', '.jpeg', '.JPG', '.gif', '.tif'):
        return "File extension not allowed."


    save_path = os.getcwd()+"/tmp/"
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    file_path = "{path}/{file}".format(path=save_path+"images/", file=upload.filename)
    upload.save(file_path)
    file_path2 = "{path}/{file}".format(path=save_path+"mask/", file=upload2.filename)
    upload2.save(file_path2)
    file_path3 = "{path}/{file}".format(path=save_path+"manual/", file=upload3.filename)
    upload3.save(file_path3)
    import subprocess
    proc = subprocess.Popen(['python', 'prepare_data_app.py'],
                                stdin = subprocess.PIPE,
                                stdout = subprocess.PIPE,
                                stderr = subprocess.PIPE
                            )

    (out, err) = proc.communicate()
    print out
    proc2 = subprocess.Popen(['python', 'run_testing_app.py'],
                                stdin = subprocess.PIPE,
                                stdout = subprocess.PIPE,
                                stderr = subprocess.PIPE
                            )

    (out2, err2) = proc2.communicate()
    print out2    
    return "File successfully saved to '{0}'.".format(save_path)

if __name__ == '__main__':
    run(host='localhost', port=8080)