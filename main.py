from flask import Flask, jsonify, request

app = Flask (__name__)

lista_professores = [
    {
        'Escola': 'Professor Daniel Neri Da Silva',
        'id':1,
        'Descrição': 'lista De Professores',
        'Professores': [ 
            {
                'Nome': 'Flávia Vitória Neves De Matos',
                'Inscrição': 1,
                'Idade': 21,
                'Matéria': 'Matemática'
            }
        ]
    }
]



@app.route('/')
def home():
    return "Hello World!!"

#GET na lista de professores
@app.route('/lista_professores')
def get_lista_de_professores():
    return jsonify(lista_professores)


@app.route('/lista_professores/<int:inscricao>')
def get_professor_by_inscricao(inscricao):
    for escola in lista_professores:
        for professor in escola['Professores']:
            if professor['Inscrição'] == inscricao:
                return jsonify(professor)
    return jsonify({'message': 'Número de inscrição {} não encontrado'.format(inscricao)}), 404


@app.route('/lista_professores', methods= ['POST'])
def create_escola():
    request_data = request.get_json()
    nova_escola = {
        'Escola': request_data['Escola'],
        'Descrição': request_data['Descrição'],
        'Professores':[]
    }
    lista_professores.append(nova_escola)
    return jsonify(nova_escola)



@app.route('/lista_professores/<int:id>/professores', methods= ['POST'])
def create_professore(id):
    req_data = request.get_json()

    for escola in lista_professores:
        if escola['id'] == id:
            novo_professor = {
                'Nome':req_data['Nome'],
                'Inscrição':req_data['Inscrição'],
                'Idade':req_data['Idade'],
                'Matéria':req_data['Matéria']
            }
            escola['Professores'].append(novo_professor)
            return jsonify(novo_professor)
        
        
    
    return jsonify({'message':'Nao foi possivel encontrar a escola {}'.format(id)})


app.run(port= 5000)
DEBUG = True