# Mercado-Python
Atividade "PROJETO API FLASK SUPERMERCADO" do dia 10/3/2026

#Endpoints disponíveis:

## CLIENTES
- GET CLIENTES: http/127.0.0.1:8000/clientes
- POST CLIENTE: http/127.0.0.1:8000/add_clientes
- UPDATE CLIENTE: http/127.0.0.1:8000/update_clientes
- DELETE CLIENTE: http/127.0.0.1:8000/delete_clientes/{id}


## PRODUTOS
- GET PRODUTOS: http/127.0.0.1:8000/produtos
- POST PRODUTO: http/127.0.0.1:8000/add_produto
- UPDATE PRODUTOS: http/127.0.0.1:8000/update_produtos
- DELETE PRODUTOS: http/127.0.0.1:8000/delete_produtos/{id}

## ORDEM DE VENDAS
- GET VENDAS: http/127.0.0.1:8000/vendas
- POST VENDAS: http/127.0.0.1:8000/add_vendas
- UPDATE VENDAS: http/127.0.0.1:8000/update_vendas
- DELETE VENDAS: http://127.0.0.1:8000/delete_vendas/{id}

# COMO USAR?
## GET: 
Apenas selecione a função GET no postman e dê SEND.
## POST: 
Selecione a função POST no postman, e escreva a seguinte identação:
````JSON
// Estrutura para Clientes
  {
    "id": "0",
    "nome": "{Nome}",
    "sobrenome": "{Sobrenome}",
    "birth": "{xxxx-xx-xx}",
    "cpf": "{CPF}"
  }

// Estrutura para Produtos
{
    "id": "0",
    "nome": "{Nome}",
    "fornecedor": "{Fornecedor}",
    "quantidade": "{Quantidade}"
  }

// Estrutura para Vendas
{
    "id": "0",
    "cliente_id": "{Nome}",
    "produto_id": "{Fornecedor}"
  }
````

  Complete os espaços vazios com informações de sua preferência. Nota: Apesar de necessário, o campo do valor do ID inserido não será contado, pois este é configurado internamente de forma automática. Mantênha-o como valor "0" de preferência.

## UPDATE:
Insira o ID de um elemento existente e coloque as informações que você quer manter ou alterar nos demais valores.

## DELETE:
No POSTMAN coloque a URL do método delete e substitua {id} pelo ID de um elemento existente.
