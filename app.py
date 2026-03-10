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