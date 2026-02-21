CLIENTE
---------
id_cliente (PK)
nombre
telefono
email
direccion

PRODUCTO
---------
id_producto (PK)
nombre
marca
precio
stock

EMPLEADO
---------
id_empleado (PK)
nombre
cargo

VENTA
---------
id_venta (PK)
fecha
id_cliente (FK)
id_empleado (FK)

DETALLE_VENTA
---------
id_detalle (PK)
id_venta (FK)
id_producto (FK)
cantidad
precio_unitario


-- CLIENTES
CREATE TABLE clientes (
    id_cliente SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    telefono VARCHAR(20),
    email VARCHAR(100),
    direccion TEXT
);

-- PRODUCTOS
CREATE TABLE productos (
    id_producto SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    marca VARCHAR(50),
    precio NUMERIC(10,2),
    stock INT
);

-- EMPLEADOS
CREATE TABLE empleados (
    id_empleado SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    cargo VARCHAR(50)
);

-- VENTAS
CREATE TABLE ventas (
    id_venta SERIAL PRIMARY KEY,
    fecha DATE,
    id_cliente INT,
    id_empleado INT,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado)
);

-- DETALLE VENTA
CREATE TABLE detalle_venta (
    id_detalle SERIAL PRIMARY KEY,
    id_venta INT,
    id_producto INT,
    cantidad INT,
    precio_unitario NUMERIC(10,2),
    FOREIGN KEY (id_venta) REFERENCES ventas(id_venta),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);





-- CLIENTES
INSERT INTO clientes(nombre, telefono, email, direccion)
VALUES
('Andres Narvaez', '3001234567', 'andres@mail.com', 'Cali'),
('Maria Lopez', '3015557777', 'maria@mail.com', 'Bogota');

-- PRODUCTOS
INSERT INTO productos(nombre, marca, precio, stock)
VALUES
('iPhone 14', 'Apple', 4500000, 10),
('Galaxy S23', 'Samsung', 3500000, 8),
('Xiaomi Redmi Note 12', 'Xiaomi', 1200000, 20);

-- EMPLEADOS
INSERT INTO empleados(nombre, cargo)
VALUES
('Carlos Perez', 'Vendedor'),
('Laura Gomez', 'Cajera');

-- VENTAS
INSERT INTO ventas(fecha, id_cliente, id_empleado)
VALUES
('2026-02-20', 1, 1),
('2026-02-21', 2, 2);

-- DETALLE VENTA
INSERT INTO detalle_venta(id_venta, id_producto, cantidad, precio_unitario)
VALUES
(1, 1, 1, 4500000),
(1, 3, 2, 1200000),
(2, 2, 1, 3500000);

--CONSULTA SENCILLA
SELECT * FROM clientes;

--INNER JOIN
SELECT c.nombre, v.id_venta, v.fecha
FROM clientes c
INNER JOIN ventas v ON c.id_cliente = v.id_cliente;

--LEFT JOIN
SELECT c.nombre, v.id_venta
FROM clientes c
LEFT JOIN ventas v ON c.id_cliente = v.id_cliente;
--Muestra todos los clientes aunque no compren.

--RIGHT JOIN
SELECT c.nombre, v.id_venta
FROM clientes c
RIGHT JOIN ventas v ON c.id_cliente = v.id_cliente;
--Muestra todas las ventas aunque no haya cliente.

--FULL JOIN
SELECT c.nombre, v.id_venta
FROM clientes c
FULL JOIN ventas v ON c.id_cliente = v.id_cliente;
--MUESTRA TODOS LOS CLIENTES Y TODAS LAS VENTAS, INCLUYENDO LOS QUE NO TIENEN RELACION.

--Agregar un Nuevo Campo

--Ejemplo: agregar fecha_nacimiento a clientes.

ALTER TABLE clientes
ADD COLUMN fecha_nacimiento DATE;

--Agregar Nueva Relación

--Ejemplo: Crear tabla metodo_pago y relacionar con ventas.
CREATE TABLE metodo_pago (
    id_pago SERIAL PRIMARY KEY,
    tipo VARCHAR(50)
);

ALTER TABLE ventas
ADD COLUMN id_pago INT;

ALTER TABLE ventas
ADD CONSTRAINT fk_pago
FOREIGN KEY (id_pago)
REFERENCES metodo_pago(id_pago);

--INSERTAR METODOS DE PAGO
INSERT INTO metodo_pago(tipo)
VALUES ('Efectivo'), ('Tarjeta');

UPDATE ventas SET id_pago = 1 WHERE id_venta = 1;

--Ejemplo ALTER Extra

C--ambiar tipo de dato:

--Renombrar columna:
ALTER TABLE clientes
RENAME COLUMN telefono TO celular;

--Eliminar columna:
ALTER TABLE clientes
DROP COLUMN direccion;