import os.path
import os

# run converter
# /home/shoumitro/Documents/FR/social_backend/venv/bin/python py_converter.py

# for uncompile
# pip install uncompyle6
# uncompyle6 manage.pyc > manage.py


exclude_file_dir = set([
    'venv',
    '.gitignore',
    'db.sqlite3',
    'doc.txt',
    'converter.py',
    'README.md',
    'LICENSE',
    'py_code',
    '.idea',
    '.git'
])

PYTHON_BIN = os.environ.get('PYTHON_BIN', '/home/shoumitro/Documents/FR/social_backend/venv/bin/')


def pyc_converter(dir_list, working_dir):
    for fd in dir_list:
        path = os.path.join(working_dir, fd)
        if fd.endswith(".pyc") and os.path.isfile(path):
            new_path = os.path.join(working_dir, fd[:-1])
            os.system(PYTHON_BIN + 'uncompyle6 ' + path + ' > ' + new_path)
            os.remove(path)
        elif os.path.isdir(path):
            os.chdir(path)
            pyc_converter([d for d in os.listdir(path) if d not in exclude_file_dir], path)


pyc_converter([d for d in os.listdir('.') if d not in exclude_file_dir], os.getcwd())
