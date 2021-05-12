from pathlib import Path
import platform

# the os running
OS = platform.platform()

BASE_DIR = Path(__file__).resolve().parent

if "Windows" in OS:
    DB_PATH = "sqlite:///"+str(BASE_DIR)+"\db" + "\database.db"
    DB_PATH = DB_PATH.replace('\\', '\\\\')
else:
    DB_PATH = "sqlite:////"+str(BASE_DIR)+"/db"+"/database.db"

# configurations
SECRET_KEY = '79fd2ac64c35e4fd2c4ae04452925c31fd92a97a84ab647d0a4f260744e66639'
SQLALCHEMY_DATABASE_URI = DB_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = False
BCRYPT_LOG_ROUNDS = 12

if __name__ == '__main__':
    print(DB_PATH)
