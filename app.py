from flask import Flask, request, jsonify, render_template

# Criando a aplicação Flask
app = Flask(__name__)

# Dicionário inicial de municípios do Nordeste
municipios_nordeste_dataset = {
    "metadados": {
        "regiao": "Nordeste",
        "pais": "Brasil",
        "total_municipios": 30,
        "fonte_dados_populacao": "IBGE"
    },

    "municipios": {
        "Fortaleza": {
            "id_ibge": 2304400,
            "estado": "Ceará",
            "sigla_uf": "CE",
            "capital": True,
            "populacao_estimada": 2582360
        },

        "Salvador": {
            "id_ibge": 2927408,
            "estado": "Bahia",
            "sigla_uf": "BA",
            "capital": True,
            "populacao_estimada": 2559945
        },
         "São Luís": {
            "id_ibge": 2111300,
            "estado": "Maranhão",
            "sigla_uf": "MA",
            "capital": True,
            "populacao_estimada": 1037775
        },

        "Imperatriz": {
            "id_ibge": 2105302,
            "estado": "Maranhão",
            "sigla_uf": "MA",
            "capital": False,
            "populacao_estimada": 273110
        },

        "Timon": {
            "id_ibge": 2112209,
            "estado": "Maranhão",
            "sigla_uf": "MA",
            "capital": False,
            "populacao_estimada": 174465
        },

        "Caxias": {
            "id_ibge": 2103000,
            "estado": "Maranhão",
            "sigla_uf": "MA",
            "capital": False,
            "populacao_estimada": 156973
        },

        "Teresina": {
            "id_ibge": 2211001,
            "estado": "Piauí",
            "sigla_uf": "PI",
            "capital": True,
            "populacao_estimada": 866300
        },

        "Parnaíba": {
            "id_ibge": 2207702,
            "estado": "Piauí",
            "sigla_uf": "PI",
            "capital": False,
            "populacao_estimada": 162159
        },

        "Picos": {
            "id_ibge": 2208007,
            "estado": "Piauí",
            "sigla_uf": "PI",
            "capital": False,
            "populacao_estimada": 83090
        },

        "Floriano": {
            "id_ibge": 2203909,
            "estado": "Piauí",
            "sigla_uf": "PI",
            "capital": False,
            "populacao_estimada": 62036
        },

        "Caucaia": {
            "id_ibge": 2303709,
            "estado": "Ceará",
            "sigla_uf": "CE",
            "capital": False,
            "populacao_estimada": 355679
        },

        "Juazeiro do Norte": {
            "id_ibge": 2307304,
            "estado": "Ceará",
            "sigla_uf": "CE",
            "capital": False,
            "populacao_estimada": 286120
        },

        "Sobral": {
            "id_ibge": 2312908,
            "estado": "Ceará",
            "sigla_uf": "CE",
            "capital": False,
            "populacao_estimada": 203023
        },

        "Natal": {
            "id_ibge": 2408102,
            "estado": "Rio Grande do Norte",
            "sigla_uf": "RN",
            "capital": True,
            "populacao_estimada": 751300
        },

        "Mossoró": {
            "id_ibge": 2408003,
            "estado": "Rio Grande do Norte",
            "sigla_uf": "RN",
            "capital": False,
            "populacao_estimada": 264577
        },

        "Parnamirim": {
            "id_ibge": 2403251,
            "estado": "Rio Grande do Norte",
            "sigla_uf": "RN",
            "capital": False,
            "populacao_estimada": 252716
        },

        "João Pessoa": {
            "id_ibge": 2507507,
            "estado": "Paraíba",
            "sigla_uf": "PB",
            "capital": True,
            "populacao_estimada": 833932
        },

        "Campina Grande": {
            "id_ibge": 2504009,
            "estado": "Paraíba",
            "sigla_uf": "PB",
            "capital": False,
            "populacao_estimada": 419379
        },

        "Santa Rita": {
            "id_ibge": 2513703,
            "estado": "Paraíba",
            "sigla_uf": "PB",
            "capital": False,
            "populacao_estimada": 149910
        },

        "Recife": {
            "id_ibge": 2611606,
            "estado": "Pernambuco",
            "sigla_uf": "PE",
            "capital": True,
            "populacao_estimada": 1488920
        },

        "Jaboatão dos Guararapes": {
            "id_ibge": 2607901,
            "estado": "Pernambuco",
            "sigla_uf": "PE",
            "capital": False,
            "populacao_estimada": 643759
        },

        "Olinda": {
            "id_ibge": 2609600,
            "estado": "Pernambuco",
            "sigla_uf": "PE",
            "capital": False,
            "populacao_estimada": 349976
        },

        "Caruaru": {
            "id_ibge": 2604106,
            "estado": "Pernambuco",
            "sigla_uf": "PE",
            "capital": False,
            "populacao_estimada": 378052
        },

        "Maceió": {
            "id_ibge": 2704302,
            "estado": "Alagoas",
            "sigla_uf": "AL",
            "capital": True,
            "populacao_estimada": 957916
        },

        "Arapiraca": {
            "id_ibge": 2700300,
            "estado": "Alagoas",
            "sigla_uf": "AL",
            "capital": False,
            "populacao_estimada": 234696
        },

        "Aracaju": {
            "id_ibge": 2800308,
            "estado": "Sergipe",
            "sigla_uf": "SE",
            "capital": True,
            "populacao_estimada": 602757
        },

        "Nossa Senhora do Socorro": {
            "id_ibge": 2804805,
            "estado": "Sergipe",
            "sigla_uf": "SE",
            "capital": False,
            "populacao_estimada": 192330
        },

        "Feira de Santana": {
            "id_ibge": 2910800,
            "estado": "Bahia",
            "sigla_uf": "BA",
            "capital": False,
            "populacao_estimada": 616272
        },

        "Vitória da Conquista": {
            "id_ibge": 2933307,
            "estado": "Bahia",
            "sigla_uf": "BA",
            "capital": False,
            "populacao_estimada": 370879
        },

        "Camaçari": {
            "id_ibge": 2905701,
            "estado": "Bahia",
            "sigla_uf": "BA",
            "capital": False,
            "populacao_estimada": 300372
        }
    }
}


# ROTA INICIAL - abre a página principal
@app.route('/')
def inicio():
    return render_template('index.html')


# GET - listar todos os municípios ou filtrar por nome, UF ou estado
@app.route('/municipios', methods=['GET'])
def listar_municipios():

    busca = request.args.get('busca', '').strip()

    municipios = municipios_nordeste_dataset["municipios"]

    if busca:
        import unicodedata

        def normalizar(texto):
            texto = unicodedata.normalize('NFD', texto)
            return ''.join(
                caractere for caractere in texto
                if unicodedata.category(caractere) != 'Mn'
            ).casefold()

        termo = normalizar(busca)

        filtrados = {}

        for nome, dados in municipios.items():

            if (
                termo in normalizar(nome)
                or termo == normalizar(dados["sigla_uf"])
                or termo in normalizar(dados["estado"])
            ):
                filtrados[nome] = dados

        return jsonify(filtrados)

    return jsonify(municipios)


# GET - consultar município pelo nome
@app.route('/municipios/<nome>', methods=['GET'])
def consultar_municipio(nome):

    municipios = municipios_nordeste_dataset["municipios"]

    municipio = municipios.get(nome)

    if municipio is None:
        return jsonify({"erro": "Município não encontrado"}), 404

    return jsonify(municipio)


# POST - cadastrar novo município
@app.route('/municipios', methods=['POST'])
def cadastrar_municipio():

    dados = request.get_json()

    if not isinstance(dados, dict):
        return jsonify({"erro": "Envie os dados em formato JSON"}), 400

    nome = dados.get("nome")

    if not isinstance(nome, str) or not nome.strip():
        return jsonify({"erro": "O nome do município é obrigatório"}), 400

    nome = nome.strip()

    campos_obrigatorios = [
        "id_ibge",
        "estado",
        "sigla_uf",
        "capital",
        "populacao_estimada"
    ]

    for campo in campos_obrigatorios:
        if campo not in dados:
            return jsonify({"erro": f"O campo {campo} é obrigatório"}), 400

    municipios = municipios_nordeste_dataset["municipios"]

    if nome in municipios:
        return jsonify({"erro": "Município já cadastrado"}), 409

    # Criando uma cópia dos dados sem o campo nome
    novos_dados = dados.copy()
    novos_dados.pop("nome", None)

    municipios[nome] = novos_dados

    # Atualizando a quantidade de municípios
    municipios_nordeste_dataset["metadados"]["total_municipios"] = len(municipios)

    return jsonify({
        "mensagem": "Município cadastrado com sucesso",
        "municipio": municipios[nome]
    }), 201


# PATCH - atualizar município
@app.route('/municipios/<nome>', methods=['PATCH'])
def atualizar_municipio(nome):

    dados = request.get_json()

    if not isinstance(dados, dict) or not dados:
        return jsonify({"erro": "Envie os dados que deseja atualizar"}), 400

    municipios = municipios_nordeste_dataset["municipios"]

    if nome not in municipios:
        return jsonify({"erro": "Município não encontrado"}), 404

    # Não permite alterar o nome pela atualização dos dados
    dados.pop("nome", None)

    municipios[nome].update(dados)

    return jsonify({
        "mensagem": "Município atualizado com sucesso",
        "municipio": municipios[nome]
    })


# DELETE - excluir município
@app.route('/municipios/<nome>', methods=['DELETE'])
def excluir_municipio(nome):

    municipios = municipios_nordeste_dataset["municipios"]

    if nome not in municipios:
        return jsonify({"erro": "Município não encontrado"}), 404

    del municipios[nome]

    # Atualizando a quantidade de municípios
    municipios_nordeste_dataset["metadados"]["total_municipios"] = len(municipios)

    return jsonify({
        "mensagem": "Município excluído com sucesso"
    })


# Executando a aplicação
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

