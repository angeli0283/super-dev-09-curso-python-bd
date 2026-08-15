-- Criar banco de dados
CREATE DATABASE restau_calabresa;

-- Definir qual banco de dados que utilizaremos
USE restau_calabresa;

-- Criar tabela
CREATE TABLE funcionarios(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50)
);

-- APRESENTAR AS TABELAS
SHOW TABLES;

-- Visualizar a tabela como ela é
DESCRIBE funcionarios;

-- Cadastrar um registro
-- INSERT INTO <nome-tabela> (colunas) VALUE (valores);
INSERT INTO funcionarios (nome) VALUE ("Justin Bieber");

-- Consultar os registros
-- SELECT <colunas> FROM <tabela>;
SELECT id, nome FROM funcionarios;

-- Adicionar uma coluna em uma tabela existente
-- ALTER TABLE <nome_tabela> ADD COLUMN <nome_coluna> <TIPO_COLUNA>;
ALTER TABLE funcionarios ADD COLUMN cargo VARCHAR(30);

-- Consultar os registros
SELECT id, nome, cargo FROM funcionarios;

-- Adicionar coluna data de nascimento
ALTER TABLE funcionarios ADD COLUMN data_nascimento DATE;
-- Adicionar coluna salario
ALTER TABLE funcionarios ADD COLUMN salario DOUBLE;

-- Consultar todas as colunas da tabela funcionarios
SELECT id, nome, cargo, data_nascimento, salario FROM funcionarios;

-- Atualizar dados de um registro
-- UPDATE <nome_tabela> SET <coluna> = <valor>
UPDATE funcionarios SET cargo = "Garçom" WHERE id = 1;

-- Atualizar mais de uma coluna por vez
UPDATE funcionarios SET
    data_nascimento = "1998-01-09",
    salario = 2500.20
    WHERE id = 1;

INSERT INTO funcionarios (nome, cargo, data_nascimento, salario) 
    VALUE ("Elias da Silva", "Caixa", "2000-07-12", 1996.50);
INSERT INTO funcionarios (nome, cargo, data_nascimento, salario) 
    VALUE ("Victor sem C", "Manobrista", "2012-09-29", 300.00);
INSERT INTO funcionarios (nome, cargo, data_nascimento, salario) 
    VALUE ("Peter Souza", "Cozinheiro Junior", "1995-02-28", 6795.30);

-- Consultar todas as colunas da tabela funcionarios
SELECT id, nome, cargo, data_nascimento, salario FROM funcionarios;



USE restau_calabresa;

CREATE TABLE pratos_feitos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    custo DOUBLE NOT NULL
);

INSERT INTO pratos_feitos (nome, custo) VALUE ("X-Calabresa sem carne", 60.9);
INSERT INTO pratos_feitos (nome, custo) VALUE ("Pizza de Calabresa de 10cm", 25);
INSERT INTO pratos_feitos (nome, custo) VALUES 
("Folhado de Calabresa", 17.28),
("Kalzone de Calabresa", 86.45),
("Calabresa Cheddar e Batata Frita", 9.75),
("Calabresa no Pão de queijo", 133.35),
("Pirão banco com calabresa e ovo", 17.55),
("Pão de alho e calabresa", 67.77),
("Sopa de cala com lingua de boi", 100.6),
("Fondue de Chocolate", 823.4);

CREATE TABLE clientes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    documento VARCHAR(18) NOT NULL,
    telefone VARCHAR(15) NOT NULL
);

INSERT INTO clientes (nome, documento, telefone) VALUES 
("Luquita da galera", "24.740.464/0001-00", "(96) 3741-5005"),
("Leandro Antonio Melo", "834.931.626-85", "(71) 2929-9455"),
("Isis Rebeca Vanessa Sales", "936.423.500-20", "(11) 98693-3252");


CREATE TABLE bebidas(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    valor DOUBLE NOT NULL,
    tipo VARCHAR(255) NOT NULL
);

INSERT INTO bebidas (nome, valor, tipo) VALUES
("Laranjinha", 18.00, "Refrigerante"),
("Fruki", 10.00, "Refrigerante"),
("Corote", 27.00, "Vodka"),
("Vinho Campo Largo 750ml", 74.43, "Vinho"),
("Del Valle 100% Laranja 1L", 66.50, "Suco");

DROP TABLE IF EXISTS mesas;

CREATE TABLE mesas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    numero CHAR(3) NOT NULL,
    lugares INT NOT NULL
);

INSERT INTO mesas (numero, lugares) VALUES
("002", 12),
("003", 4),
("004", 8),
("005", 5),
("006", 9),
("007", 5),
("008", 3),
("009", 2),
("010", 1),
("001", 7);

DROP TABLE IF EXISTS comandas_pratos_feitos;
DROP TABLE IF EXISTS comandas;

CREATE TABLE comandas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes (id),
    total DOUBLE DEFAULT(0.0),
    data_criacao DATETIME DEFAULT NOW()
);

INSERT INTO clientes (nome, documento, telefone) VALUES
("Samuca", "04.422.160/0001-80", "(47) 99277-1029");

INSERT INTO comandas (id_cliente) VALUES (1);
INSERT INTO comandas (id_cliente) VALUES (3);
INSERT INTO comandas (id_cliente) VALUES (4);

-- Consultar as comandas
SELECT id, id_cliente FROM comandas;

-- Consultar as comandas com o nome do cliente
SELECT 
    comandas.id, 
    comandas.id_cliente,
    clientes.nome
FROM comandas
INNER JOIN clientes ON (comandas.id = clientes.id);




/*
comandas_pratos_feitos			
id	id_comanda	id_prato_feito	quantidade
20	10	Pirão branco com calabresa e ovo	2
21	11	X-Calabresa sem carne	4
22	12	Calabresa no Pão de queijo	3
23	12	Fondue de Chocolate	2
*/

CREATE TABLE comandas_pratos_feitos (
    id INT PRIMARY KEY AUTO_INCREMENT,

    id_comanda INT NOT NULL,
    id_prato_feito INT NOT NULL,
    quantidade INT NOT NULL,

    FOREIGN KEY(id_comanda) REFERENCES comandas(id),
    FOREIGN KEY(id_prato_feito) REFERENCES pratos_feitos(id)
);

INSERT INTO comandas_pratos_feitos (id_comanda, id_prato_feito, quantidade) VALUES
(1, 7, 2);

INSERT INTO comandas_pratos_feitos (id_comanda, id_prato_feito, quantidade) VALUES
(2, 1, 4);

INSERT INTO comandas_pratos_feitos (id_comanda, id_prato_feito, quantidade) VALUES
(3, 6, 3),
(3, 10, 2);

SELECT 
    comandas_pratos_feitos.id_comanda,
    comandas_pratos_feitos.id_prato_feito,
    comandas_pratos_feitos.quantidade,
    pratos_feitos.nome,
    comandas.total,
    clientes.nome
FROM comandas_pratos_feitos
INNER JOIN pratos_feitos ON (comandas_pratos_feitos.id_prato_feito = pratos_feitos.id)
INNER JOIN comandas ON (comandas_pratos_feitos.id_comanda = comandas.id)
INNER JOIN clientes ON (comandas.id_cliente = clientes.id);

-- Consultar nome do cliente e nome do prato feito
SELECT 
    clientes.nome AS "Cliente",
    pratos_feitos.nome AS "Prato",
    comandas_pratos_feitos.quantidade AS "Quantidade",
    pratos_feitos.custo AS "Preço Unitário",
    FORMAT(comandas_pratos_feitos.quantidade * pratos_feitos.custo, 2) AS "Total"
FROM comandas_pratos_feitos
INNER JOIN pratos_feitos ON (comandas_pratos_feitos.id_prato_feito = pratos_feitos.id)
INNER JOIN comandas ON (comandas_pratos_feitos.id_comanda = comandas.id)
INNER JOIN clientes ON (comandas.id_cliente = clientes.id);

-- Ordenar os clientes por nome de crescente
SELECT nome FROM clientes ORDER BY nome ASC;

-- Ordenar os clientes por nome decrescente
SELECT nome FROM clientes ORDER BY nome DESC;

-- Consultar a quantidade de caracteres
SELECT nome, LENGTH(nome) FROM clientes;

-- Consultar a quantidade de caracteres ordenando pelo que tem menos caracteres
SELECT nome, LENGTH(nome) FROM clientes ORDER BY LENGTH(nome) ASC;

-- Concatenar nome e documento do cliente
SELECT CONCAT(RPAD(nome, 30, " "), " => ", documento) AS "Clientes e documentos" FROM clientes;

-- Consultar os nomes em caixa alta
SELECT UPPER(nome) FROM clientes;
-- Consultar os nomes em caixa baixa
SELECT LOWER(nome) FROM clientes;

-- Consutlar nome prato e seu custo ordenando custo mais caro
-- filtrando os pratos com preço menor que 100 e acima de 60
SELECT 
    pratos_feitos.nome,
    pratos_feitos.custo
FROM pratos_feitos
WHERE custo > 60 AND custo < 100
ORDER BY custo DESC;



-- Adicionar coluna na tabela
ALTER TABLE bebidas ADD COLUMN data_vencimento DATE;

/*

1	Laranjinha	R$ 18,00	Refrigerante	10/08/2027
2	Fruki	R$ 10,00	Refrigerante	10/12/2030
3	Corote	R$ 27,00	Vodka	10/01/2025
4	Vinho Campo Largo 750ml	R$ 74,43	Vinho	NULL
5	Del Valle 100% Laranja 1L	R$ 66,50	Suco	09/08/2026
*/

UPDATE bebidas SET data_vencimento = "2027-08-10" WHERE id = 1;
UPDATE bebidas SET data_vencimento = "2030-12-10" WHERE id = 2;
UPDATE bebidas SET data_vencimento = "2026-08-09" WHERE id = 5;
UPDATE bebidas SET data_vencimento = "2025-01-10" WHERE id = 3;

-- Usuário sem querer definiu a data de vencimento do vinho
UPDATE bebidas SET data_vencimento = "2027-02-01" WHERE id = 4;
-- Limpar a data de vencimento do vinho
UPDATE bebidas SET data_vencimento = NULL WHERE id = 4;

-- Consultar as bebidas que não tem data de vencimento
SELECT id, nome, data_vencimento FROM bebidas WHERE data_vencimento IS NULL;
-- Consultar as bebidas que tem data de vencimento
SELECT id, nome, data_vencimento FROM bebidas WHERE data_vencimento IS NOT NULL;

-- Consultar as bebidas que tem data de vencimento ordenar da data mais antiga para a mais nova
SELECT 
    id, 
    nome, 
    data_vencimento 
FROM bebidas 
WHERE data_vencimento IS NOT NULL 
ORDER BY data_vencimento ASC;

-- Apresentar o nome da bebida e o ano de vencimento
SELECT nome, YEAR(data_vencimento) FROM bebidas;


-- Apresentar o nome da bebida e mês de vencimento
SELECT nome, MONTH(data_vencimento) FROM bebidas;

-- Apresentar o nome da bebida e dia de vencimento
SELECT nome, DAY(data_vencimento) FROM bebidas;

-- Apresentar nome, mês junto com ano de vencimento
SELECT nome, CONCAT(LPAD(MONTH(data_vencimento), 2, "0"), "/", YEAR(data_vencimento)) AS 'Mês Ano' FROM bebidas;

-- Apresentar nome, mês junto com ano de vencimento (FORMA SIMPLIFICADA)
-- https://dev.mysql.com/doc/refman/9.7/en/date-and-time-functions.html#function_date-format
SELECT nome, DATE_FORMAT(data_vencimento, "%m/%Y") AS 'Mês Ano' FROM bebidas;

-- Consultar as bebidas que vencem em 2027
SELECT nome, data_vencimento FROM bebidas WHERE YEAR(data_vencimento) = 2027;

-- Consultar a data e hora atual
SELECT NOW();
-- Consultar a data atual
SELECT CURDATE();
-- Consultar a hora atual
SELECT CURTIME();

-- Consultar os produtos vencidos
SELECT nome, data_vencimento FROM bebidas WHERE data_vencimento < CURDATE();

SELECT
    nome,
    IF(
        data_vencimento IS NULL, 
        "Sem data de vencimento", 
        DATE_FORMAT(data_vencimento, "%d/%m/%y")
    ) AS 'Data de vencimento'
FROM bebidas;

-- Alterar o nome da coluna de 'data_criacao' para 'data_hora_criacao'
ALTER TABLE comandas RENAME COLUMN data_criacao TO data_hora_criacao;

-- Nome do cliente, id da comanda, data e hora de criação daquela comanda
SELECT
    clientes.nome,
    comandas.id,
    comandas.data_hora_criacao
FROM comandas
INNER JOIN clientes ON (comandas.id_cliente = clientes.id);


/*

Criar tabela de estados (com 2 estados)
- id
- nome
- sigla
Criar tabela de cidades (com 2 cidades por estado)
- id
- nome
- quantidade habitantes
Criar tabela de bairros (com 2 bairros por cidade)
- id
- nome
Criar endereço por bairro (com 1 endereços por bairro)
- id 
- cep
- logradouro
- numero
- complemento

*/