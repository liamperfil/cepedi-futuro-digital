CREATE DATABASE biblioteca

CREATE TABLE usuario(
	cpf CHAR(11) PRIMARY KEY,
	nome VARCHAR(50),
	email VARCHAR(100),
	bairro VARCHAR(50),
	data_nascimento DATE)

ALTER TABLE usuario ADD telefone CHAR(11)

CREATE TABLE livro(
	isbn CHAR(13) PRIMARY KEY,
	nome VARCHAR(50),
	ano YEAR,
	edicao VARCHAR(50))

ALTER TABLE livro MODIFY COLUMN nome VARCHAR(255) NOT NULL

CREATE TABLE emprestimo(
	id INT PRIMARY KEY AUTO_INCREMENT,
	cpf_usuario CHAR(11),
	isbn_fk CHAR(13),
	data_emprestimo DATE,
	data_devolucao DATE,
	FOREIGN KEY (cpf_usuario) REFERENCES usuario(cpf),
	FOREIGN KEY (isbn_fk) REFERENCES livro(isbn))

INSERT INTO `usuario` (`cpf`, `nome`, `email`, `bairro`, `data_nascimento`, `telefone`) 
VALUES
('11122233344','Joao Santos','abc@exemplo.com','Paralela','2000-12-22','00123456789'),
('21122233344','Maria Oliveira','maria@exemplo.com','Itapuã','1999-11-10','00223456789'),
('31122233344','Joana Dark','joana@exemplo.com','Lalala','1998-10-09','00323456789'),
('41122233344','Jean Lima','jeancarlos.ramos@live.com','Paralela','1999-12-22','71984018811'),
('51122233344','Joana Santana','joana@exemplo.com','Paralela','1999-05-20','00252425262')

SELECT cpf, nome FROM usuario WHERE bairro="PAralela" AND YEAR(data_nascimento)=1999

INSERT INTO livro (isbn, nome, ano, edicao) VALUES
('9780000000001', 'Programação Python', 2001, '1 edição'),
('9780000000002', 'Programação Python', 2002, '2 edição'),
('9780000000003', 'Programação Python', 2003, '3 edição'),
('9780000000004', 'Receitas da Terra', 1995, '1 edição'),
('9780000000005', 'Apredendo SQL', 2005, '1 edição'),
('9780000000006', 'HTML, CSS e JavaScript', 2006, '6 edição'),
('9780000000007', 'Java', 2007, '7 edição'),
('9780000000008', 'Estágios e Aprendizagem', 2008, '8 edição'),
('9780000000009', 'Power Plus', 2009, '9 edição'),
('9780000000010', 'Apredendo SQL', 2010, '2 edição')

INSERT INTO `emprestimo` (`id`, `cpf_usuario`, `isbn_fk`, `data_emprestimo`, `data_devolucao`) VALUES
('1','11122233344','9780000000001','2025-10-01','2025-10-03'),
('2','11122233344','9780000000002','2025-10-01','2025-10-03'),
('3','21122233344','9780000000003','2025-10-06','2025-10-08'),
('4','31122233344','9780000000006','2025-10-05','2025-10-08'),
('5','51122233344','9780000000006','2025-10-20','2025-10-22')

TRUNCATE emprestimo
TRUNCATE livro

SELECT nome, (2025 - YEAR(data_nascimento)) AS idade FROM usuario

-- A função CURDATE() é usada para buscar a data atual (sem a parte da hora)
-- A função TIMESTAMPDIFF() é usada para retornar a diferença entre duas datas
SELECT nome, TIMESTAMPDIFF(YEAR, data_nascimento, CURDATE()) AS idade
FROM usuario;

SELECT * FROM usuario WHERE nome LIKE 'Jo%'

SELECT * FROM `biblioteca`.`usuario` LIMIT 0,3