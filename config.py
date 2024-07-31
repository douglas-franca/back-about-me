import os

class Config:
  DEBUG = False
  GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

class DevelopmentConfig(Config):
  DEBUG = True
  GOOGLE_API_KEY = Config.GOOGLE_API_KEY
  HOST = '127.0.0.1'
  PORT = 5000
  CORS_ORIGINS = os.getenv('CORS_ORIGINS') or 'http://localhost:5173'

class ProductionConfig(Config):
  DEBUG = False
  GOOGLE_API_KEY = Config.GOOGLE_API_KEY
  CORS_ORIGINS = os.getenv('CORS_ORIGINS')