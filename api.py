#Importações de frameworks
from flask import Flask, jsonify, request
from flask_cors import CORS

#Criar nosso app
app = Flask(__name__)
#Habilitar o CORS
CORS(app)

#Criar
produtos = [
    {"id":1,
      "nome":"Notebook Gamer",
      "preco": 4000},
      {"id":2,
       "nome":"Cadeira Gamer",
       "preco":300},
       {"id":3,
        "nome":"Monitor",
        "preco":800
        }
]

#Criar uma rota e p metodo GET(visualizar os dados)
@app.route("/listar", methods=['GET'])
def exbirProdutos():
    return jsonify(produtos)

#Criar uma rota e o metodo post
@app.route("/criar",methods=['POST'])
def criarProdutos():
    produtoNovo= request.get_json()
    produtos.append(produtoNovo)
    return jsonify(produtoNovo),201


#Criar uma rota e o metodo PUT(Atualizar)
@app.route("/atualizar/<int:id>", methods=['PUT'])
def atualizarProdutos(id):
    dados= request.get_json()
    for produto in produtos:
        if produto['id']==id:
            produto['preco']= dados['preco']
            return jsonify(dados)
        return jsonify({"mensagem":"ID não encontrado"}),404
    
    #Criar uma rota e o metedo de DELETE(apagar)
@app.route("/apagar/<int:id>", methods=['DELETE'])
def apagarProduto(id):
        for produto in produtos:
            if produto['id']== id:
                produtos.remove(produto)
                return jsonify({"mensagem":"Produto removido!"})
            return jsonify({"mensagem":"ID não encontrado"}),404
#Rodar o progama
if __name__ == "__main__":
    app.run(port=8000,host="0.0.0.0")

    