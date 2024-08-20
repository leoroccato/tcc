import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

# Credenciais

username = 'postgres'
password = 'cancer09'
host = 'localhost'
port = '5432'
database = 'Cronobox_DB'

# URL de conexão

conn = st.connection("postgresql", type="sql")

engine = create_engine(conn)

# Função para carregar os dados de uma tabela específica
def load_data(table_name):
    df = conn.query(f"SELECT * FROM {table_name}", ttl="10m")

    for col in df.columns:
        if df[col].dtype == 'object':  # Verifica se a coluna é lida como 'object', que pode conter strings
            df[col] = df[col].astype(str)

    return df


# Listas manuais de pilotos, corridas e categorias
nomes = ['aguiar20', 'alcaraz60', 'araujo33', 'arruda129', 'barbosa121', 'barros69', 'bassani72', 'bertucelli44',
         'brasil139', 'bufoni13', 'campos8', 'campos14', 'campos33', 'campos82', 'cardoso22', 'castro22',
         'chaves54', 'cifali74', 'costa1', 'cytrynbaum7', 'farah84', 'feldmann1', 'feldmanneto1', 'ferrao65',
         'ferrer121', 'ferter56', 'frangulis88', 'giaffone3', 'guedes9', 'hahn26', 'heil331', 'hermann23',
         'horta77', 'junior27', 'kim71', 'leite66', 'liber14', 'locatelli177', 'lucco777', 'malucelli100',
         'marcal544', 'marcondes199', 'mariotti21', 'marques77', 'marreiros992', 'martins911', 'mascarello22',
         'mello29', 'menossi85', 'mohr3', 'monteiro87', 'morestoni8', 'muller544', 'neto45', 'neugebauer8',
         'paludo7', 'pires888', 'pisani12', 'pontes99', 'posser266', 'raijan22', 'regadas17', 'reina9',
         'rios11', 'roque32', 'rosario2', 'salles70', 'salmen51', 'sanchez15', 'santos38', 'seiroz12',
         'simao58', 'sousa25', 'souza7', 'stallone61', 'totaro45', 'tulio55', 'vivacqua10', 'zanon24',
         'ziemkiewicz80', 'zylberman18']

corridas = ['corrida', 'corrida1', 'corrida2']
categorias = ['carrera', 'carrera1', 'carrera2', 'carrera3', 'carrera4', 'challenge', 'challenge1', 'challenge2', 'challenge3', 'challenge4',
              'trophy', 'trophy1', 'trophy2', 'trophy3']

# Título da aplicação
st.title("Visualização de Dados")

# Interface do Streamlit para selecionar piloto, categoria e corrida
piloto = st.selectbox('Selecione o Piloto', nomes)
categoria = st.selectbox('Selecione a Categoria', categorias)
corrida = st.selectbox('Selecione a Corrida', corridas)

# Construir o nome da tabela com base na seleção
table_name = f"dados_{piloto}_{categoria}_{corrida}"

# Tentar carregar e exibir os dados da tabela selecionada
try:
    df = load_data(table_name)
    print(df)
    st.write(f"Visualizando dados da tabela: {table_name}")
    st.markdown(df.to_html(index=False), unsafe_allow_html=True)
except Exception as e:
    st.write(f"Erro ao carregar a tabela {table_name}: {e}")
