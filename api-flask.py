from crypt import methods
from flask import Flask, jsonify, request

app = Flask(__name__)

alumnos = []

@app.route('/')
def home():
    return 'Home'

@app.route('/alumno', methods=['GET','POST','PUT','DELETE'])
def alumno():

    if request.method == 'GET':
        return jsonify({'alumnos':alumnos})

    elif request.method == 'POST':
        if not alumnos:
            id_alumno = 1
        else:
            id_alumno = alumnos[-1]['id'] + 1
        alumno = {
            'id':id_alumno,
            'nombre':request.json['nombre'],
            'cursos':request.json['cursos'],
        }
        alumnos.append(alumno)
        return jsonify('Alumno añadido correctamente.')

    elif request.method == 'PUT':
        id_alumno = request.json['id']
        
        for alumno in alumnos:
            if id_alumno == alumno.get('id'):
                if request.json['nombre'] is not None:
                    alumno['nombre'] = request.json['nombre']
                if request.json['cursos'] is not None:
                    alumno['cursos'] = request.json['cursos']
                return jsonify('Datos modificados.')
        return jsonify(f"id {id_alumno} no hallado.")

    elif request.method == 'DELETE':
        id_alumno = request.json['id']
        
        for alumno in alumnos:
            if id_alumno == alumno.get('id'):
                alumnos.remove(alumno)
                return jsonify('Alumno borrado.')
        return jsonify('Alumno no hallado.')

@app.route('/alumno/<int:id>/')
def get_alumno(id):
    try:
        return jsonify({
            'alumno':alumnos[id-1]
        })
    except IndexError:
        return jsonify(f"No existe el alumno con el id {id}.")

@app.route('/instructor/')
def get_instructor():
    return 'En construccion.'

if __name__ == '__main__':
    app.run(debug=True)


#export FLASK_APP = webserver.py

#flask run