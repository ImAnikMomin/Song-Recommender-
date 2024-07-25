from dotenv import load_dotenv  # Importing load_dotenv to load environment variables from .env file
import os  # Importing os to access environment variables


load_dotenv()


SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')


SCOPE = 'user-library-read playlist-read-private'