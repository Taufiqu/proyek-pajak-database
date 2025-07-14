# backend/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Konfigurasi utama aplikasi Flask."""
    USER = os.getenv("user")
    PASSWORD = os.getenv("password")
    HOST = os.getenv("host")
    PORT = os.getenv("port")
    DBNAME = os.getenv("dbname")
    POPPLER_PATH = os.getenv("POPPLER_PATH")
    UPLOAD_FOLDER = "uploads"

    @staticmethod
    def init_app():
        """Buat folder upload jika belum ada."""
        if not os.path.exists(Config.UPLOAD_FOLDER):
            os.makedirs(Config.UPLOAD_FOLDER)
