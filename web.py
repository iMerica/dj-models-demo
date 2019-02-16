from flask import Flask, request
import djmodels

djmodels.setup()
from project.base.models import Person

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        count = Person.objects.count()
        return (
            f"{count} objects in the DB for this model. "
            f"Send a POST request to add more!"
        )

    if request.method == 'POST':
        Person.objects.create(name='XXX', age=23)
        return "Successfully Added!"


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
