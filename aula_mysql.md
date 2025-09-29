# Python MySQL

## Configurar o ambiente
Instale o MySQL ou o XAMPP.

O XAMPP serve para criar um servidor web local no seu computador, permitindo o desenvolvimento e teste de aplicações web. Ele inclui o Apache (servidor web), MySQL (ou MariaDB) para bancos de dados, PHP e Perl (linguagens de programação) e outras ferramentas, sendo ideal para estudantes e desenvolvedores testarem projetos sem precisar de acesso à internet ou um servidor remoto.

Se você usa o XAMPP é necessário configurar o local do MySQL nas variáveis de ambiente do windows. Passo a passo:
1. Encontre o caminho do MySQL no XAMPP. Por padrão em C:\xampp\mysql\bin
2. Adicione o caminho às variáveis de ambiente
    1. Abra o menu Iniciar e digite "variáveis de ambiente". Clique no resultado que aparecer.
    2. Na nova janela, procure a seção "Variáveis do sistema". Encontre a variável chamada Path e clique nela para selecioná-la.
    3. Clique no botão Editar.
    4. Na janela de edição do Path, clique em Novo e cole o caminho que você encontrou no passo 1. No meu caso C:\xampp\mysql\bin.
    5. Clique em OK em todas as janelas para fechar e salvar as alterações.

Para verificar a versão do MySQL use: ``--mysql version``.

Atualizar o pip e instalar o driver MySQL Connector, (pip é o gerenciador de pacotes padrão da linguagem python):
|powershell|
|:-|
|``cd C:\Users\Your Name\AppData\Local\Programs\Python\Python313\Scripts``|
|``python.exe -m pip install --upgrade pip``|
|``python -m pip install mysql-connector-python``|

Para testar se a instalação foi bem-sucedida ou se você já possui o "MySQL Connector" instalado, crie um arquivo Python com o seguinte conteúdo:
| aula-mysql.py |
|:-|
|``import mysql.connector``|

## Criar uma conexão
conexao_mysql.py
```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

print(mydb)
```