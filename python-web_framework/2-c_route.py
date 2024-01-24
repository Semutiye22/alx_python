"""
2-c_route.py - Flask web application with multiple routes.

This script creates a Flask web application with three routes:
1. Root ("/"): Displays "Hello HBNB!"
2. /hbnb: Displays "HBNB"
3. /c/<text>: Displays "C " followed by the value of the text variable 
   (replace underscore _ symbols with a space)

Usage:
    - Start the server: Run the script using 'python3 2-c_route.py'.
    - Stop the server: Press 'CTRL+C' to quit the server.

Routes:
    - /: Displays "Hello HBNB!"
    - /hbnb: Displays "HBNB"
    - /c/<text>: Displays "C " followed by the value of the text variable.

Example:
    - Correct output: curl 0.0.0.0:5000/c/is_fun
       
        $ curl 0.0.0.0:5000/c/is_fun
        C is fun
        
    - Correct output: curl 0.0.0.0:5000/c/cool
       
        $ curl 0.0.0.0:5000/c/cool
        C cool
        
    - Incorrect output (404): curl 0.0.0.0:5000/c
       
        $ curl 0.0.0.0:5000/c
        404 Not Found
        
Requirements:
    - Python 3.x
    - Flask: Install using 'pip install Flask'.

"""

from flask import Flask, escape

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

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Route function for the "/c/<text>" route.

    Args:
        text (str): The text variable in the route.

    Returns:
        str: The string "C " followed by the value of the text variable.
    """
    return 'C {}'.format(escape(text.replace('_', ' ')))

if name == '__main__':
    app.run(host='0.0.0.0', port=5000)