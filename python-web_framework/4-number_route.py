"""
4-number_route.py - Flask web application with multiple routes.

This script creates a Flask web application with five routes:
1. Root ("/"): Displays "Hello HBNB!"
2. /hbnb: Displays "HBNB"
3. /c/<text>: Displays "C " followed by the value of the text variable 
   (replace underscore _ symbols with a space)
4. /python/<text>: Displays "Python " followed by the value of the text variable 
   (replace underscore _ symbols with a space). Default value of text is "is cool".
5. /number/<n>: Displays "n is a number" only if n is an integer.

Usage:
    - Start the server: Run the script using 'python3 4-number_route.py'.
    - Stop the server: Press 'CTRL+C' to quit the server.

Routes:
    - /: Displays "Hello HBNB!"
    - /hbnb: Displays "HBNB"
    - /c/<text>: Displays "C " followed by the value of the text variable.
    - /python/<text>: Displays "Python " followed by the value of the text variable.
    - /number/<n>: Displays "n is a number" only if n is an integer.

Example:
    - Correct output: curl 0.0.0.0:5000/number/89
       
        $ curl 0.0.0.0:5000/number/89
        89 is a number
        
    - Incorrect output (404): curl 0.0.0.0:5000/number/8.9
       
        $ curl 0.0.0.0:5000/number/8.9
        404 Not Found
        
    - Incorrect output (404): curl 0.0.0.0:5000/number/python
       
        $ curl 0.0.0.0:5000/number/python
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

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Route function for the "/number/<n>" route.

    Args:
        n (int): The number variable in the route.

    Returns:
        str: The string "n is a number" only if n is an integer.
    """
    return '{} is a number'.format(n)

if name == '__main__':
    app.run(host='0.0.0.0', port=5000)



    