from flask import Flask, request, jsonify
import os
from ArbolAVL import ArbolAVL, Registro, arbol_registros, cargar_registros_desde_csv, encontrar_registro_por_id

app = Flask(__name__)

@app.route('/cargar_registros_desde_csv', methods=['POST'])
def cargar_registros():
    datos = request.json
    ruta_archivo = datos.get('ruta_archivo')
    if not ruta_archivo:
        return jsonify({'error': 'Ruta del archivo CSV requerida'}), 400

    if not os.path.isfile(ruta_archivo):
        return jsonify({'error': 'El archivo CSV no existe en la ruta proporcionada'}), 400

    cargar_registros_desde_csv(ruta_archivo)
    return jsonify({'mensaje': 'Registros cargados exitosamente'}), 200

@app.route('/insertar_registro', methods=['POST'])
def insertar_registro():
    datos = request.json
    id = datos.get('id')
    if not id:
        return jsonify({'error': 'id'}), 400
    arbol_registros.insertar(id, Registro(id))
    return jsonify({'mensaje': 'Registro insertado exitosamente'}), 201

@app.route('/buscar_registro', methods=['GET'])
def buscar_registro():
    id = request.args.get('id')
    if not id:
        return jsonify({'error': 'id es requerido'}), 400
    
    registro = encontrar_registro_por_id(id, arbol_registros.raiz)
    if registro:
        return jsonify({'registro': registro.id}), 200
    else:
        return jsonify({'error': 'Registro no encontrado'}), 404


@app.route('/informacion', methods=['GET'])
def mostrar_informacion_grupo():
    informacion = {
        'Datos': [
            {'nombre': 'Jeremi', 'carnet': '9490-22-11282', 'contribucion': '100%'},
        ]
    }
    return jsonify(informacion), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)
