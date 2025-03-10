# Runtrack Bases de Données / Python

### Job 1 :  
Installation MySQL Server  
  
### Job 2 :  
Commandes :  
CREATE DATABASE LaPlateforme; 
SHOW DATABASES;  
  
### Job 3 :  
Commandes :  
USE LaPlateforme  
CREATE TABLE etudiant (  
id int NOT NULL AUTO_INCREMENT,  
nom varchar (255) NOT NULL,  
prenom varchar (25) NOT NULL,  
age int NOT NULL,  
email varchar (255) NOT NULL,  
primary key (id)  
);  
SHOW TABLES;  
  
### Job 4 :  
Commandes :  
DESCRIBE etudiant;  
  
### Job 5 :  
INSERT INTO etudiant (nom, prenom, age, email)  
VALUES  
("Spaghetti", "Betty", 23, "betty.spaghetti@laplateforme.io"),  
("Steak", "Chuck", 45, "chuck.steak@laplateforme.io"),  
("Doe", "John", 18, "john.doe@laplateforme.io"),  
("Barnes", "Binkie", 16, "binkie.barnes@laplateforme.io"),  
("Dupuis", "Gertrude", 20, "gertrude.dupuis@laplateforme.io");  
  
### Job 6 :  
SELECT * FROM etudiant;  
  