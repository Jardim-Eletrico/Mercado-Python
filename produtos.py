from fastapi import FastAPI
import os
import csv
from pydantic import BaseModel
from datetime import date

app = FastAPI()
file_path = 'produtos.csv'

if not os.path.exists(file_path):    
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        data = [
            ["ID", "NOME", "FORNECEDOR", "QUANTIDADE"]
        ]
        writer = csv.writer(file)
        writer.writerows(data)
        

# ========================================== Classe do Cliente

class Produto(BaseModel):
    id: int #0
    nome: str #1
    fornecedor: str #2
    quantidade: int #3

# ========================================== Funções (CRUD)

@app.get("/produtos") # ==================== Listar cientes
def get_Produtos():
    produtos = {} #Dicionário que vai usar pra retornar os nomes

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file) #Criando interpretador pra ler o arquivo csv
        for row in reader: #Para cada linha no arquivo csv
            if row[0] == "ID":
                continue
            else:
                produtos[row[0]] = { #A chave do dicionário (linha do csv) se torna o ID que está na linha do cliente. Daí vai ficar "id": {"nome", "sobrenome", etc}
                    "nome": row[1],
                    "fornecedor": row[2],
                    "quantidade": row[3],
                } 
        return produtos
    

@app.post("/add_produto")
def add_Produto(produto: Produto):

    all_IDs = []
    data = [
        ["ID", "NOME", "FORNECEDOR", "QUANTIDADE"]
    ]
    produto_dados = [produto.id, produto.nome, produto.fornecedor, produto.quantidade] #Dados que serão passados pro cadastro do cliente
    produtos = {}

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == "ID":
                continue
            else:
                data.append(row)
                all_IDs.append(int(row[0])) #Adicionar todos os IDs já usados
            
            
    if not all_IDs:
        produto_dados[0]= "1"
    else:
        novo_id = max(all_IDs) + 1 #Vai pegar o maior número de ID registrado e adicionar +1 pra ser o próximo
        produto_dados[0] = str(novo_id) 
        all_IDs.append(novo_id)
            
    produto_dados[3] = str(produto_dados[3]) #Transformar a quantidade em string pra poder passar pro csv
    data.append(produto_dados)
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        
        writer = csv.writer(file)
        writer.writerows(data)

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file) #Criando interpretador pra ler o arquivo csv
        for row in reader: #Para cada linha no arquivo csv
            if row[0] == "ID":
                continue
            else:
                produtos[row[0]] = { #A chave do dicionário (linha do csv) se torna o ID que está na linha do cliente. Daí vai ficar "id": {"nome", "sobrenome", etc}
                    "nome": row[1],
                    "fornecedor": row[2],
                    "quantidade": row[3],
                } 
        return produtos


@app.put("/update_produtos")
def update_Produtos(produto: Produto):
    produto_dados = [produto.id, produto.nome, produto.fornecedor, produto.quantidade]
    data = [
        ["ID", "NOME", "FORNECEDOR", "QUANTIDADE"]
    ]

    produtos = {}

    with open(file_path, mode='r', newline='', encoding='utf-8') as file: #Adicionando informações do arquivo csv ao "dicionário" data (na verdade é uma lista dentro de uma lista)
        reader = csv.reader(file)
        for row in reader: #For para armazenar os dados do csv em variável local
            if row[0] == "ID":
                continue
            else:
                data.append(row)

        cont = False
        for row in data: #For para verificar a existência da pessoa e atualizar as informações dela
            if row[0] == str(produto.id): #Serve pra verificar se existe esse ID
                cont = True
                for i, column in enumerate(row):#Isso vai estar devolvendo o vetor no i (0, 1, 2, etc...) e o valor dele no column ("id", "nome", etc...). Só que aqui não usa o column
                    row[i] = str(produto_dados[i])
        
        if cont == False:
            return {"ERRO":"ID informado não existe ou foi excluído."}
            
        
            
    with open(file_path, mode='w', newline='', encoding='utf-8') as file: #Sobrescrevendo o arquivo
        writer = csv.writer(file)
        writer.writerows(data)

    with open(file_path, mode='r', newline='', encoding='utf-8') as file: #Retornando todos os nomes com a alteração
        reader = csv.reader(file) 
        for row in reader: 
            if row[0] == "ID":
                continue
            else:
                produtos[row[0]] = { 
                    "nome": row[1],
                    "fornecedor": row[2],
                    "quantidade": row[3],
                } 
        return produtos


@app.delete("/delete_produtos/{id}")
def delete_Produtos(id: str):
    data = [
        ["ID", "NOME", "FORNECEDOR", "QUANTIDADE"]
    ]

    produtos = {}

    with open(file_path, mode='r', newline='', encoding='utf-8') as file: #Adicionando informações do arquivo csv ao "dicionário" data (na verdade é uma lista dentro de uma lista)
        reader = csv.reader(file)
        for row in reader: #For para armazenar os dados do csv em variável local
            if row[0] == "ID":
                continue
            else:
                data.append(row)

        cont = False
        for i, row in enumerate(data): 
            if row[0] == id: 
                cont = True
                data.pop(i)
        
        if cont == False:
            return {"ERRO":"ID informado não existe ou já foi excluído."}
        
    with open(file_path, mode='w', newline='', encoding='utf-8') as file: #Sobrescrevendo o arquivo
        writer = csv.writer(file)
        writer.writerows(data)

    with open(file_path, mode='r', newline='', encoding='utf-8') as file: #Retornando todos os nomes com a alteração
        reader = csv.reader(file) 
        for row in reader: 
            if row[0] == "ID":
                continue
            else:
                produtos[row[0]] = { 
                    "nome": row[1],
                    "fornecedor": row[2],
                    "quantidade": row[3],
                } 
        return produtos

    
        

    