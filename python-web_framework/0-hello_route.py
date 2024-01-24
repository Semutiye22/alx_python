#0-hello_route
"""
0-hello_route.py - Simple Flask web application.

This script creates a basic Flask web application with a single route that
responds with "Hello HBNB!" when accessed at the root ("/") route.

Usage:
    - Start the server: Run the script using 'python3 0-hello_route.py'.
    - Stop the server: Press 'CTRL+C' to quit the server.

Routes:
    - /: Displays "Hello HBNB!"

Example:
    - Correct output: curl 0.0.0.0:5000
       
        $ curl 0.0.0.0:5000
        Hello HBNB!
        
    - Correct output (404): curl 0.0.0.0:5000/noroute
       
        $ curl 0.0.0.0:5000/noroute
        Not Found
        
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