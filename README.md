# Pipeline de Dados com Python e POO

## Sobre o Projeto

Desenvolvido no curso **"Pipeline de dados: combinando Python e orientação a objeto"** da Alura, este projeto cria um pipeline de dados para processar e combinar informações de duas empresas (Empresa A e Empresa B) a partir de arquivos JSON e CSV. Usando programação orientada a objetos (POO), o pipeline carrega, transforma e carrega os dados, gerando análises exploratórias e relatórios.

## Estrutura

```
pipeline_dados/
├── data_raw/
│   ├── dados_empresaA.json  # Dados da Empresa A (JSON)
│   └── dados_empresaB.csv   # Dados da Empresa B (CSV)
├── notebooks/
│   └── exploracao.ipynb     # Análise exploratória dos dados
└── scripts/
    ├── fusao_mercado.py  # Pipeline ETL
    └── process_dados.py   # Criação de clases
```

## Instalação

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd pipeline_dados
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/WSL
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. **Explorar os dados**:
   - Abra o notebook `exploracao.ipynb`:
     ```bash
     jupyter notebook notebooks/exploracao.ipynb
     ```

2. **Executar o pipeline**:
   - Rode o script principal `fusao_mercado_fev.py`:
     ```bash
     python scripts/fusao_mercado_fev.py
     ```
   - O pipeline:
     - Lê `dados_empresaA.json` e `dados_empresaB.csv`.
     - Aplica transformações (limpeza, normalização).
     - Combina os dados.
     - Salva resultados (verifique `data_processed/` ou configure a saída).
