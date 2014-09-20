"""
REST endpoints for Simplixity
"""

from simplixity import app


@app.route('/')
def test():
    return "Making sure flask works."
