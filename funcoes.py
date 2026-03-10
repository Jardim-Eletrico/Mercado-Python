
import csv
import os

def criar_csv():
  
    cliente_csv = "Clientes.csv"
    produtos_csv = "Produtos.csv"
    ordem_vendas = "OrdemDeVendas.csv"

    if not os.path.exists(cliente_csv):    
        with open(cliente_csv, mode='w', newline='', encoding='utf-8') as file:
            data = [
                ["ID", "NOME", "SOBRENOME", "DATA DE NASCIMENTO", "CPF"]
            ]
            writer = csv.writer(file)
            writer.writerows(data)
    else:
        print('O arquivo já existe!')

    if not os.path.exists(produtos_csv):    
        with open(produtos_csv, mode='w', newline='', encoding='utf-8') as file:
            data = [
                ["ID", "NOME", "FORNECEDOR", "QUANTIDADE"]
            ]
            writer = csv.writer(file)
            writer.writerows(data)
    else:
        print('O arquivo já existe!')

    if not os.path.exists(ordem_vendas):    
        with open(ordem_vendas, mode='w', newline='', encoding='utf-8') as file:
            data = [
                ["ID", "ID-Cliente", "ID-Produto"]
            ]
            writer = csv.writer(file)
            writer.writerows(data)
    else:
        print('O arquivo já existe!')