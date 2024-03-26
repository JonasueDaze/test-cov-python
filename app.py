import usecases.person as usecase
from flask import Flask, jsonify, render_template, request
from flask_bootstrap import Bootstrap
from marshmallow_generic import fields, GenericSchema
from models.person import Person


# Auxiliary classes


class PersonSchema(GenericSchema[Person]):
    id = fields.Int(load_default=None)
    name = fields.Str()
    age = fields.Int()


def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    # API routes

    api_people_url = "/api/people"
    api_people_url_id = api_people_url + "/<int:id>"

    @app.post(api_people_url)
    def create_person():
        person = PersonSchema().load(request.get_json())
        id = usecase.create(person)
        return str(id), 201

    @app.get(api_people_url)
    def get_all_persons():
        people = usecase.get_all()
        data = PersonSchema().dump(people, many=True)
        return jsonify(data)

    @app.get(api_people_url_id)
    def get_person(id: int):
        person = usecase.get(id)
        if person is None:
            return "", 404

        data = PersonSchema().dump(person)
        return jsonify(data), 200

    @app.put(api_people_url_id)
    def update_person(id: int):
        person = PersonSchema().load(request.get_json())
        person.id = id
        usecase.update(person)
        return "", 200

    @app.delete(api_people_url_id)
    def delete_person(id: int):
        usecase.delete(id)
        return "", 200

    # View routes

    @app.route("/")
    def index():
        people = usecase.get_all()
        return render_template("index.html", people=people)

    @app.route("/form")
    def form():
        id = request.args.get("id", type=int)

        person: Person | None = None
        if id is not None:
            person = usecase.get(id)
        return render_template("form.html", person=person)

    return app
