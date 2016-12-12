create database peliculas;
use peliculas 
CREATE TABLE `peliculas`.`resumen` (
  `id_resumen` INT NOT NULL AUTO_INCREMENT,
  `pelicula` VARCHAR(45) NULL,
  `formato` VARCHAR(45) NULL,
  `cliente` VARCHAR(45) NULL,
  `tiempo` VARCHAR(45) NOT NULL,
  `total` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_resumen`, `total`, `tiempo`));
