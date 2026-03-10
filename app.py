from fastapi import FastAPI
import os
import csv
from pydantic import BaseModel
from datetime import date
import funcoes

app = FastAPI()

funcoes.criar_csv()









class Cliente(BaseModel):
    id: int
    nome: str
    sobrenome: str
    data: date
    cpf: str

class Produtos(BaseModel):
    id: int
    nome: str
    fornecedor: str
    quantidade: int

class OrdemVendas(BaseModel):
    id: int
    cliente_id: int
    produto_id: int

clientes_id = []


@app.post("/add_cliente")
async def add_cliente(cliente:Cliente):
    data = [
        ["ID", "NOME", "SOBRENOME", "DATA", "CPF"]
    ]

    Clientes = {}
    ultimo_id = clientes_id[-1] + 1

    if not clientes_id:
        ultimo_id = 1
        clientes_id.append(ultimo_id)

    with open(funcoes.cliente_csv, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == 'ID':
                continue
            else:
                data.append(row)

    novo = [cliente.id, cliente.nome]
    data.append(novo)

    with open(funcoes.cliente_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    
    with open(funcoes.cliente_csv, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == 'ID':
                continue
            else:
                Clientes[row[0]] = row[1]

    return Clientes