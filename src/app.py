from flask import Flask,jsonify,request
app = Flask(__name__)
todos = [
  { "label": "My first task", "done": False },
  { "label": "My second task", "done": False }
]
@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)

    # Agregar el nuevo todo a la lista
    todos.append(request_body)

    # Devolver la lista actualizada
    return jsonify(todos)
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
  if 0 <= position < len(todos):
      del todos[position]  # o todos.pop(position)
      return jsonify(todos)
  else:
      return jsonify({"error": "Position out of range"}), 400
   
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)