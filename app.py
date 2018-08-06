"""
Example loading all specs from JSON template
"""
from flask import Flask, jsonify

from flasgger import Swagger

app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'Eshipz API',
    "headers": [
        ('Access-Control-Allow-Origin', '*'),
        ('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS"),
        ('Access-Control-Allow-Credentials', "true"),
]
}
swag = Swagger(app, template_file='schema.yaml')


@app.route('/hello')
def colors(palette):
    """
    Example using a dictionary as specification
    Hello workd
    """

    return jsonify({"hello":"world"})

if __name__ == "__main__":
    app.run(debug=True)
