"""
1-hbnb_route.py - Flask web application with multiple routes.

This script creates a Flask web application with two routes:
1. Root ("/"): Displays "Hello HBNB!"
2. /hbnb: Displays "HBNB"

Usage:
    - Start the server: Run the script using 'python3 1-hbnb_route.py'.
    - Stop the server: Press 'CTRL+C' to quit the server.

Routes:
    - /: Displays "Hello HBNB!"
    - /hbnb: Displays "HBNB"

Example:
    - Correct output: curl 0.0.0.0:5000
       
        $ curl 0.0.0.0:5000
        Hello HBNB!
        
    - Correct output: curl 0.0.0.0:5000/hbnb
       
        $ curl 0.0.0.0:5000/hbnb
        HBNB
        
Requirements:
    - Python 3.x
    - Flask: Install using 'pip install Flask'.

"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route function for the root ("/") route.

    Returns:
        str: The string "Hello HBNB!" as the response.
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route function for the "/hbnb" route.

    Returns:
        str: The string "HBNB" as the response.
    """
    return 'HBNB'

if name == '__main__':
    app.run(host='0.0.0.0', port=5000)