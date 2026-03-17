from fastapi import FastAPI
import os
import csv
from pydantic import BaseModel
from datetime import date

app = FastAPI()
file_path = 'ordemdevendas.csv'
file_path_clientes = 'clientes.csv'
file_path_produtos = 'produtos.csv'

if not os.path.exists(file_path):    
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        data = [
            ["ID", "CLIENTE_ID", "PRODUTO_ID"]
        ]
        writer = csv.writer(file)
        writer.writerows(data)

if not os.path.exists(file_path_clientes):    
    with open(file_path_clientes, mode='w', newline='', encoding='utf-8') as file:
        data = [
            ["ID", "NOME", "SOBRENOME", "BIRTH", "CPF"]
        ]
        writer = csv.writer(file)
        writer.writerows(data)

if not os.path.exists(file_path_produtos):    
    with open(file_path_produtos, mode='w', newline='', encoding='utf-8') as file:
        data = [
            ["ID", "NOME", "FORNECEDOR", "QUANTIDADE"]
        ]
        writer = csv.writer(file)
        writer.writerows(data)
        

# ========================================== Classe Vendas

class Vendas(BaseModel):
    id: int
    cliente_id: int
    produto_id: int

# ========================================== Funções (CRUD)

@app.get("/vendas")
def get_vendas():
    vendas = {}

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == "ID":
                continue
            else:
                vendas[row[0]] = {
                    "cliente_id": row[1],
                    "produto_id": row[2]
                } 
    return vendas
    

@app.post("/add_vendas")
def add_vendas(venda: Vendas):

    all_IDs = []
    data = [
        ["ID", "CLIENTE_ID", "PRODUTO_ID"]
    ]

    venda_dados = [venda.id, venda.cliente_id, venda.produto_id]
    vendas = {}

    cont1 = False #Para verificar existência do ID do cliente
    cont2 = False #Para verificar existência do ID do produto

    # Cont1/2 são variáveis pra saber se o ID do produto e do cliente existe. Se um dos dois não existir, não vai ser possível registrar a venda.

    with open(file_path_clientes, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == "ID":
                continue
            elif row[0] == str(venda.cliente_id):
                cont1 = True

    with open(file_path_produtos, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == "ID":
                continue
            elif row[0] == str(venda.produto_id):
                cont2 = True
    
    if cont1 and cont2:

        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == "ID":
                    continue
                else:
                    data.append(row)
                    all_IDs.append(int(row[0]))
                
        if not all_IDs:
            venda_dados[0] = "1"
        else:
            novo_id = max(all_IDs) + 1
            venda_dados[0] = str(novo_id) 
            all_IDs.append(novo_id)
                
        data.append(venda_dados)

    elif not cont1:
        return {"Status": "Erro. ID do cliente não encontrado."}
    elif not cont2:
        return {"Status": "Erro. ID do produto não encontrado."}

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == "ID":
                continue
            else:
                vendas[row[0]] = {
                    "cliente_id": row[1],
                    "produto_id": row[2]
                } 
    return vendas


@app.put("/update_vendas")
def update_vendas(venda: Vendas):
    venda_dados = [venda.id, venda.cliente_id, venda.produto_id]

    data = [
        ["ID", "CLIENTE_ID", "PRODUTO_ID"]
    ]

    vendas = {}

    cont1 = False #Para verificar existência do ID do cliente
    cont2 = False #Para verificar existência do ID do produto

    # Cont1/2 são variáveis pra saber se o ID do produto e do cliente existe. Se um dos dois não existir, não vai ser possível registrar a venda.

    with open(file_path_clientes, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == "ID":
                continue
            elif row[0] == str(venda.cliente_id):
                cont1 = True

    with open(file_path_produtos, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == "ID":
                continue
            elif row[0] == str(venda.produto_id):
                cont2 = True

    if cont1 and cont2:

        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == "ID":
                    continue
                else:
                    data.append(row)

            cont = False
            for row in data:
                if row[0] == str(venda.id):
                    cont = True
                    for i, column in enumerate(row):
                        row[i] = str(venda_dados[i])
            
            if cont == False:
                return {"ERRO":"ID informado não existe."}
            
    elif not cont1:
        return {"Status": "Erro. ID do cliente não encontrado."}
    elif not cont2:
        return {"Status": "Erro. ID do produto não encontrado."}
    
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file) 
        for row in reader: 
            if row[0] == "ID":
                continue
            else:
                vendas[row[0]] = { 
                    "cliente_id": row[1],
                    "produto_id": row[2]
                } 
    return vendas


@app.delete("/delete_vendas/{id}")
def delete_vendas(id: str):

    data = [
        ["ID", "CLIENTE_ID", "PRODUTO_ID"]
    ]

    vendas = {}

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
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
        
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file) 
        for row in reader: 
            if row[0] == "ID":
                continue
            else:
                vendas[row[0]] = { 
                    "cliente_id": row[1],
                    "produto_id": row[2]
                } 
    return vendas