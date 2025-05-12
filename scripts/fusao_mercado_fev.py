from process_dados import Dados


path_json = '\\root\\Documentos\\pipeline_dados\\data_raw\\dados_empresaA.json'
path_csv = '\\root\\Documentos\\pipeline_dados\\data_raw\\dados_empresaB.csv'

# Extract

dados_empresaA = Dados(path_json, 'json')
print(f"Nome colunas dados empresa A: {dados_empresaA.nome_colunas}")
print(f"Quantindade de linhas dados empresa A: {dados_empresaA.qtd_linhas}")

dados_empresaB = Dados(path_csv, 'csv')
print(f"Nome colunas dados empresa B: {dados_empresaB.nome_colunas}")
print(f"Quantindade de linhas dados empresa B: {dados_empresaB.qtd_linhas}")

# Transform

key_mapping = {'Nome do Item': 'Nome do Produto',
               'ClassificaÃ§Ã£o do Produto': 'Categoria do Produto',
               'Valor em Reais (R$)': 'Preço do Produto (R$)',
               'Quantidade em Estoque': 'Quantidade em Estoque',
               'Nome da Loja': 'Filial',
               'Data da Venda': 'Data da Venda'}

dados_empresaB.rename_columns(key_mapping)
print(f"Colunas padronizadas: {dados_empresaB.nome_colunas}")

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(f"Nome colunas fusão: {dados_fusao.nome_colunas}")
print(f"Quantidade de linhas fusão: {dados_fusao.qtd_linhas}")

# Load

path_dados_combinados = '\\root\\Documentos\\pipeline_dados\\data_processed\\dados_combinados.json'
dados_fusao.salvando_dados(path_dados_combinados)
print(f"Caminho dados fusão{path_dados_combinados}")
