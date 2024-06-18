import sys 
import os 

# Add the app directory to the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

from app import app, db

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)