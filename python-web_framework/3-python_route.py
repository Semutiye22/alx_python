"""
3-python_route.py - Flask web application with multiple routes.

This script creates a Flask web application with four routes:
1. Root ("/"): Displays "Hello HBNB!"
2. /hbnb: Displays "HBNB"
3. /c/<text>: Displays "C " followed by the value of the text variable 
   (replace underscore _ symbols with a space)
4. /python/<text>: Displays "Python " followed by the value of the text variable 
   (replace underscore _ symbols with a space). Default value of text is "is cool".

Usage:
    - Start the server: Run the script using 'python3 3-python_route.py'.
    - Stop the server: Press 'CTRL+C' to quit the server.

Routes:
    - /: Displays "Hello HBNB!"
    - /hbnb: Displays "HBNB"
    - /c/<text>: Displays "C " followed by the value of the text variable.
    - /python/<text>: Displays "Python " followed by the value of the text variable.

Example:
    - Correct output: curl -Ls 0.0.0.0:5000/python/is_magic
       
        $ curl -Ls 0.0.0.0:5000/python/is_magic
        Python is magic
        
    - Correct output: curl -Ls 0.0.0.0:5000/python
       
        $ curl -Ls 0.0.0.0:5000/python
        Python is cool
        
    - Correct output: curl -Ls 0.0.0.0:5000/python/
       
        $ curl -Ls 0.0.0.0:5000/python/
        Python is cool
        
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

@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is_cool'):
    """
    Route function for the "/python/<text>" route.

    Args:
        text (str): The text variable in the route. Default is "is_cool".

    Returns:
        str: The string "Python " followed by the value of the text variable.
    """
    return 'Python {}'.format(escape(text.replace('_', ' ')))

if name == '__main__':
    app.run(host='0.0.0.0', port=5000)