from flask import Flask, jsonify,request
import json
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False }
]
@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    objetodecodificado = json.loads(request_body)
    print(objetodecodificado, request_body)
    if isinstance(objetodecodificado, list):
        for tarea in objetodecodificado:
            todos.append(tarea)
    elif isinstance(objetodecodificado, dict):
        todos.append(objetodecodificado)
    else: 
        return "error400"
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position)
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)