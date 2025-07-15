import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Konfigurasi utama aplikasi Flask."""

    USER = os.getenv("USER")
    PASSWORD = os.getenv("PASSWORD")
    HOST = os.getenv("HOST")
    PORT = os.getenv("PORT")
    DBNAME = os.getenv("DBNAME")
    POPPLER_PATH = os.getenv("POPPLER_PATH")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")  # fallback default

    @staticmethod
    def init_app():
        """Buat folder upload jika belum ada."""
        if not os.path.exists(Config.UPLOAD_FOLDER):
            os.makedirs(Config.UPLOAD_FOLDER)
