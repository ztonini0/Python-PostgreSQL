# Python-PostgreSQL

O que o código faz?
Conexão Segura: Utiliza variáveis de ambiente para armazenar credenciais sensíveis (como nome do banco, usuário e senha), garantindo que nossas informações estejam protegidas e fora do código-fonte.

Listagem de Tabelas: Após estabelecer a conexão, o aplicativo obtém uma lista das tabelas disponíveis no esquema público do banco de dados, permitindo ao usuário selecionar a tabela que deseja visualizar.

Execução de Consultas SQL: Os usuários podem editar consultas SQL diretamente na interface, facilitando a exploração dos dados. A consulta padrão seleciona todos os registros da tabela escolhida, mas pode ser modificada conforme necessário.

Download de Resultados: Se a consulta retornar dados, os usuários têm a opção de baixar os resultados em formato CSV.
