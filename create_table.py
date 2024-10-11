import psycopg2

# Função para conectar ao banco de dados PostgreSQL
def connect_db():
    return psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='46073180',
        host='localhost',
        port='5433'
    )

# Função para criar as tabelas
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    
    create_cliente_table = """
    CREATE TABLE IF NOT EXISTS cliente (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        telefone VARCHAR(15),
        data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    
    create_produto_table = """
    CREATE TABLE IF NOT EXISTS produto (
        id SERIAL PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        descricao TEXT,
        preco NUMERIC(10, 2) NOT NULL,
        estoque INT DEFAULT 0
    );
    """
    
    try:
        cursor.execute(create_cliente_table)  # Cria a tabela cliente
        cursor.execute(create_produto_table)   # Cria a tabela produto
        conn.commit()                          # Confirma as mudanças
        print("Tabelas criadas com sucesso!")
    except Exception as e:
        print(f"Erro ao criar as tabelas: {e}")
    finally:
        cursor.close()                        # Fecha o cursor
        conn.close()                          # Fecha a conexão

# Função para adicionar dados
def insert_data():
    conn = connect_db()
    cursor = conn.cursor()

    # Dados de exemplo para a tabela cliente
    clientes = [
        ("Alice Silva", "alice@example.com", "123456789"),
        ("Bruno Santos", "bruno@example.com", "987654321"),
        ("Carla Oliveira", "carla@example.com", "123123123"),
    ]

    # Dados de exemplo para a tabela produto
    produtos = [
        ("Camiseta", "Camiseta 100% algodão", 49.90, 100),
        ("Calça Jeans", "Calça jeans feminina", 89.90, 50),
        ("Tênis Esportivo", "Tênis para corrida", 199.90, 30),
    ]

    try:
        # Inserindo dados na tabela cliente
        for cliente in clientes:
            cursor.execute(
                "INSERT INTO cliente (nome, email, telefone) VALUES (%s, %s, %s);", 
                cliente
            )
        
        # Inserindo dados na tabela produto
        for produto in produtos:
            cursor.execute(
                "INSERT INTO produto (nome, descricao, preco, estoque) VALUES (%s, %s, %s, %s);", 
                produto
            )
        
        conn.commit()  # Confirma as inserções
        print("Dados inseridos com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")
    finally:
        cursor.close()  # Fecha o cursor
        conn.close()    # Fecha a conexão

# Executa as funções
create_tables()
insert_data()
