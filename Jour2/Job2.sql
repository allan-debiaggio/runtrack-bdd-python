CREATE TABLE etage (
    id int NOT NULL AUTO_INCREMENT,
    nom varchar (255) NOT NULL,
    numero int NOT NULL,
    superficie int NOT NULL,
    primary key (id)
);

CREATE TABLE salle (
    id int NOT NULL AUTO_INCREMENT,
    nom varchar (255) NOT NULL,
    id_etage int NOT NULL,
    capacite int NOT NULL,
    primary key (id)
);