import os.path
import os

# must remove __pycache__ files
# find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf

# run converter
# /home/shoumitro/Documents/FR/social_backend/venv/bin/python converter.py

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
# os.environ.setdefault("PYTHON_BIN", "/usr/bin/")
# PYTHON_BIN = '/home/shoumitro/Documents/FR/test/movie-database-assessment/venv/bin/'


def pyc_converter(dir_list, working_dir):
    for fd in dir_list:
        path = os.path.join(working_dir, fd)
        if fd.endswith("__pycache__") and os.path.isdir(path):
            for f in os.listdir(path):
                if f.endswith(".pyc"):
                    src_file_path = os.path.join(path, f)
                    st = f.split(".")
                    new_file = st[0] + "." + st[2]
                    dest_file_path = os.path.join(working_dir, new_file)
                    os.rename(src_file_path, dest_file_path)
            os.rmdir(path)
        elif fd.endswith(".py") and os.path.isfile(path):
            os.remove(path)
        elif os.path.isdir(path):
            os.chdir(path)
            os.system(PYTHON_BIN+'python -m compileall')
            pyc_converter([d for d in os.listdir(path) if d not in exclude_file_dir], path)


os.system(PYTHON_BIN+'python -m compileall')
pyc_converter([d for d in os.listdir('.') if d not in exclude_file_dir], os.getcwd())
