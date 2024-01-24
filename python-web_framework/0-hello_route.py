"""
0-hello_route.py - Simple Flask web application.

This script creates a basic Flask web application with a single route that
responds with "Hello HBNB!" when accessed at the root ("/") route.

Usage:
    - Run the script using 'python3 0-hello_route.py'.
    - The web application will be accessible at http://0.0.0.0:5000/.

Routes:
    - /: Displays "Hello HBNB!"

Requirements:
    - Flask: Make sure to install Flask using 'pip install Flask'.

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

if name == '__main__':
    app.run(host='0.0.0.0', port=5000)