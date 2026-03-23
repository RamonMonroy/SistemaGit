from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Lista de usuarios
Usuario = [
    { 'id': 1, 'nombre': 'Juan Pérez',  'correo': 'juan@gmail.com',  'estado': 'Activo'    },
    { 'id': 2, 'nombre': 'Ana Gómez',   'correo': 'ana@hotmail.com', 'estado': 'Pendiente' },
    { 'id': 3, 'nombre': 'Luis Torres', 'correo': 'luis@gmail.com',  'estado': 'Activo'    },
    { 'id': 4, 'nombre': 'Jose Monroy',  'correo': 'Jose@gmail.com', 'estado': 'Activo'  }
]

@app.route('/')
def inicio():
    # Ordenar la lista por el campo 'id' usando una función lambda
    lista_usuarios = sorted(Usuario, key=lambda x: x['id'])

    # Los pasamos al template
    return render_template('index.html', usuarios=lista_usuarios)

@app.route('/acerca')
def acerca():
    return render_template('acerca.html')

# API usuarios
@app.route('/api/usuarios')
def api_usuarios():
    return jsonify(Usuario)

# Reto: API usuarios activos
@app.route('/api/usuarios/activos')
def usuarios_activos():
    activos = [u for u in Usuario if u['estado'] == 'Activo']
    return jsonify(activos)

if __name__ == '__main__':
    app.run(debug=True)