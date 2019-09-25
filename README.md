## REP Git Workshop Part 2. (Singapore PSI Level)

**1. Clone this repository to your local file directory.**

``git clone https://github.com/loichiilek/flask_psi.git``

**2. Set up your python virtual environment in the root directory.**

``python -m virtualenv venv``

**3. Install the required dependencies.**

``pip install -r requirements.txt``

**4. Run the Flask server locally.**
``python run.py``

**5. Visit localhost:5000 to view the Flask application**

**6. Complete the function located in**
- api.py (you have to understand how array and dict work in python)


**7. Create an API endpoint locally, to serve the same content, but for PM2.5** (Requires some knowledge of Javascript)
- Add a new route in routes.py
- Make another call to the same API
- Edit weather.js in static/js folder to display pm2.5 instead of psi
