from flask import Flask, request


app = Flask(__name__)


@app.route('/todos', methods=['GET','POST'])
def todos():
    response_body = {}
    if request.method == 'GET':
        response_body['message'] = "Listado de Todos"
        response_body['results'] = todos_list
        return response_body
    if request.method == 'POST':
        data = request.json
        todos_list.append(data)
        response_body['message'] = "Todo agregado exitosamente"
        response_body['results'] = todos_list
        return response_body, 201


@app.route('/todos/<int:position>', methods=['GET','PUT','DELETE'])
def todo(position):
    response_body = {}
    if request.method == 'GET':
        response_body['message'] = "Todo requested"
        response_body['results'] = todos_list[position]
        return response_body
    if request.method == 'PUT':
        data = request.get_json()
        if not data:
            response_body['message'] = "Missing JSON body"
            return response_body
        if "label" in data:
            todos_list[position]["label"] = data["label"]
        if "done" in data:
            todos_list[position]["done"] = bool(data["done"])
        response_body['message'] = "Todo updated"
        response_body['results'] = todos_list[position]
        return response_body
    if request.method == 'DELETE':
        if position <= len(todos):
            del todos[position]
            response_body['message'] = "todo borrado ok"
            response_body['results'] = todos
            return response_body
    

todos_list = [{ "label": "My first task", "done": False },
         { "label": "My second task", "done": False } ]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)