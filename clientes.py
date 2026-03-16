from fastapi import FastAPI
import os
import csv
from pydantic import BaseModel
from datetime import date

app = FastAPI()
file_path = 'clientes.csv'

if not os.path.exists(file_path):    
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        data = [
            ["ID", "NOME", "SOBRENOME", "BIRTH", "CPF"]
        ]
        writer = csv.writer(file)
        writer.writerows(data)

# ========================================== Classe do Cliente

class Cliente(BaseModel):
    id: int #0
    nome: str #1
    sobrenome: str #2
    birth: date #3
    cpf: str #4

# ========================================== Funções (CRUD)

@app.get("/clientes") # ==================== Listar cientes
def get_Clientes():
    clientes = {} #Dicionário que vai usar pra retornar os nomes

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file) #Criando interpretador pra ler o arquivo csv
        for row in reader: #Para cada linha no arquivo csv
            if row[0] == "ID":
                continue
            else:
                clientes[row[0]] = { #A chave do dicionário (linha do csv) se torna o ID que está na linha do cliente. Daí vai ficar "id": {"nome", "sobrenome", etc}
                    "nome": row[1],
                    "sobrenome": row[2],
                    "data de nascimento": row[3],
                    "cpf": row[4]
                } 
        return clientes
    

@app.post("/add_clientes")
def add_Clientes(cliente: Cliente):

    all_IDs = []
    data = [
        ["ID", "NOME", "SOBRENOME", "BIRTH", "CPF"]
    ]
    cliente_dados = [cliente.id, cliente.nome, cliente.sobrenome, cliente.birth, cliente.cpf] #Dados que serão passados pro cadastro do cliente
    clientes = {}

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == "ID":
                continue
            else:
                data.append(row)
                all_IDs.append(int(row[0])) #Adicionar todos os IDs já usados
            
            if row[4] == cliente.cpf: #Se algum ID ou CPF que já tá na lista do arquivo CSV forem iguais aos que foram passado pra adicionar um novo cliente
                return {"Status": "Erro. CPF já cadastrado."}
            
    if not all_IDs:
        cliente_dados[0]= "1"
    else:
        novo_id = max(all_IDs) + 1 #Vai pegar o maior número de ID registrado e adicionar +1 pra ser o próximo
        cliente_dados[0] = str(novo_id) 
        all_IDs.append(novo_id)
            
    data.append(cliente_dados)
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        
        writer = csv.writer(file)
        writer.writerows(data)

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file) #Criando interpretador pra ler o arquivo csv
        for row in reader: #Para cada linha no arquivo csv
            if row[0] == "ID":
                continue
            else:
                clientes[row[0]] = { #A chave do dicionário (linha do csv) se torna o ID que está na linha do cliente. Daí vai ficar "id": {"nome", "sobrenome", etc}
                    "nome": row[1],
                    "sobrenome": row[2],
                    "data de nascimento": row[3],
                    "cpf": row[4]
                } 
        return clientes


@app.put("/update_clientes")
def update_Clientes(cliente: Cliente):
    cliente_dados = [cliente.id, cliente.nome, cliente.sobrenome, cliente.birth, cliente.cpf]
    data = [
        ["ID", "NOME", "SOBRENOME", "BIRTH", "CPF"]
    ]

    clientes = {}

    with open(file_path, mode='r', newline='', encoding='utf-8') as file: #Adicionando informações do arquivo csv ao "dicionário" data (na verdade é uma lista dentro de uma lista)
        reader = csv.reader(file)
        for row in reader: #For para armazenar os dados do csv em variável local
            if row[0] == "ID":
                continue
            else:
                data.append(row)

        cont = False
        for row in data: #For para verificar a existência da pessoa e atualizar as informações dela
            if row[0] == str(cliente.id): #Serve pra verificar se existe esse ID
                cont = True
                for i, column in enumerate(row):#Isso vai estar devolvendo o vetor no i (0, 1, 2, etc...) e o valor dele no column ("id", "nome", etc...). Só que aqui não usa o column
                    row[i] = str(cliente_dados[i])
        
        if cont == False:
            return {"ERRO":"ID informado não existe ou foi excluído."}
        if row[4] == cliente.cpf and row[0] != str(cliente.id):
            return {"Status": "Erro. CPF já cadastrado."}
            
        
            
    with open(file_path, mode='w', newline='', encoding='utf-8') as file: #Sobrescrevendo o arquivo
        writer = csv.writer(file)
        writer.writerows(data)

    with open(file_path, mode='r', newline='', encoding='utf-8') as file: #Retornando todos os nomes com a alteração
        reader = csv.reader(file) 
        for row in reader: 
            if row[0] == "ID":
                continue
            else:
                clientes[row[0]] = { 
                    "nome": row[1],
                    "sobrenome": row[2],
                    "data de nascimento": row[3],
                    "cpf": row[4]
                } 
        return clientes


@app.delete("/delete_clientes/{id}")
def delete_Clientes(id: str):
    data = [
        ["ID", "NOME", "SOBRENOME", "BIRTH", "CPF"]
    ]

    clientes = {}

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
                clientes[row[0]] = { 
                    "nome": row[1],
                    "sobrenome": row[2],
                    "data de nascimento": row[3],
                    "cpf": row[4]
                } 
        return clientes

    
        

    