CREATE SCHEMA db_quitanda;
USE db_quitanda;

CREATE TABLE tb_categorias(
	id bigint AUTO_INCREMENT,
	descricao varchar(255) NOT NULL,
	PRIMARY KEY (id)
);

INSERT INTO tb_categorias (descricao) VALUES
	("Frutas"),
    ("Verduras"),
    ("Legumes"),
    ("Temperos"),
    ("Ovos"),
    ("Outros");
    
SELECT * FROM tb_categorias;

CREATE TABLE tb_produtos(
	id bigint AUTO_INCREMENT,
	nome varchar(255) NOT NULL,
	quantidade int, 
	dtvalidade date NULL,
	preco decimal(6, 2),
	categoria_id bigint, 
	PRIMARY KEY (id),
	FOREIGN KEY (categoria_id) REFERENCES tb_categorias(id)
);

INSERT INTO tb_produtos (nome, quantidade, dtvalidade, preco, categoria_id)
VALUES 
    ("Maçã", 1000, "2022-03-07", 1.99, 1),
    ("Banana", 1300, "2022-03-08", 5.00, 1),
    ("Batata doce", 2000, "2022-03-09", 10.00, 3),
    ("Alface", 300, "2022-03-10", 7.00, 2),
    ("Cebola", 1020, "2022-03-08", 5.00, 3),
    ("Ovo Branco", 1000, "2022-03-07", 15.00, 5),
    ("Agrião", 1500, "2022-03-06", 3.00, 2),
    ("Cenoura", 1800, "2022-03-09", 3.50, 3),
    ("Pimenta", 1100, "2022-03-15", 10.00, 4),
    ("Alecrim", 130, "2022-03-10", 5.00, 4),
    ("Manga", 200, "2022-03-07", 5.49, 1),
    ("Laranja", 3000, "2022-03-13", 10.00, 1),
    ("Couve", 100, "2022-03-12", 1.50, 2),
    ("Tomate", 1105, "2022-03-15", 3.00, 3),
    ("Rabanete", 1200, "2022-03-15", 13.00, 3);

INSERT INTO tb_produtos (nome, quantidade, preco)
VALUES 
    ("Sacola Cinza", 1118, 0.50),
    ("Sacola Verde", 1118, 0.50);
    
SELECT * FROM tb_produtos;