import streamlit as st
import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv 
# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Função para conectar ao banco de dados PostgreSQL
def connect_db():
    return psycopg2.connect(
        dbname=os.getenv('DBNAME'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        host=os.getenv('HOST'),
        port=os.getenv('PORT')
    )

# Função para obter tabelas do banco de dados
def get_tables(conn):
    query = "SELECT table_name FROM information_schema.tables WHERE table_schema='public';"
    return pd.read_sql(query, conn)

# Função para executar uma consulta SQL
def execute_query(conn, query):
    return pd.read_sql(query, conn)

# Interface do Streamlit
st.title("Conexão Python com PostgreSQL")

# Verificar a conexão
if st.button("Verificar Conexão"):
    try:
        conn = connect_db()
        conn.close()
        st.success("Conexão bem-sucedida ao banco de dados!")

        # Listar tabelas apenas após a conexão bem-sucedida
        conn = connect_db()
        tables = get_tables(conn)['table_name'].tolist()
        conn.close()
        
        # Armazenar a lista de tabelas no estado da aplicação
        st.session_state.tables = tables  

    except Exception as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")

with st.expander("Tabelas disponíveis:", expanded=True):
    if 'tables' in st.session_state and st.session_state.tables:
        st.write(st.session_state.tables)

        # Seleção de tabela
        selected_table = st.selectbox("Escolha uma tabela para visualizar:", st.session_state.tables)

        # Campo para editar a consulta SQL
        default_query = f"SELECT * FROM public.{selected_table};"
        query = st.text_area("Edite sua consulta SQL:", value=default_query, height=80)

        # Executar a consulta
        if st.button("Executar Consulta"):
            if query:
                try:
                    conn = connect_db()
                    data = execute_query(conn, query)
                    conn.close()
                    
                    if not data.empty:
                        st.write(data)
                        
                        # Habilitar download se houver dados
                        csv = data.to_csv(index=False)
                        st.download_button(
                            label="Baixar dados como CSV",
                            data=csv,
                            file_name="resultado_query.csv",
                            mime='text/csv'
                        )
                    else:
                        st.warning("A consulta retornou resultados vazios.")
                except Exception as e:
                    st.error(f"Erro ao executar a consulta: {e}")
            else:
                st.warning("Por favor, insira uma consulta SQL.")
    else:
        st.warning("Nenhuma tabela disponível para selecionar.")
