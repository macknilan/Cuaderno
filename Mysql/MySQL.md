# MariaDB - MySql en Linux

```bash
                                                ▓   ▓▓░
                                                   ▓▒       ▓▓
                                                     ▓   ▓     ▓▒
                                                     ▓           ▓
                                                      ▓           ▓▓
                                                       ▓           ▒▓
                                                       ▓            ▓▓
                                                      ░   ▒          ▓▓
                                                       ▓ ▓▓▓          ▓▓
                                                       ▓░▓ ▓▓            ▓▓
                                                             ▓              ▓▓
                                                               ░         ▓▓▓░
  ▓▓▓          ▓▓▓                    ░▓▓▓▓▓▓▓▓    ░▓▓▓▓▓▓▓    ░▓▓        ▓▓▒
 ▓▓▓▓▓       ▓▓▓▓▓▓                 ▓▓▒          ▓▓▓▓      ▓▓▓ ░▓▓           ░▓
 ▓▓ ▓▓▓     ▓▓▓ ▓▓▓  ▓▓▓       ▓▓▒  ▓▓           ▓▓▓       ░▓▓ ░▓▓
 ▓▓  ▓▓▓   ▒▓▓  ▓▓▓  ▓▓▓       ▓▓▒  ▒▓▓▓▓▓▓▓▓▓   ▓▓▓       ░▓▓ ░▓▓
 ▓▓   ▓▓▓  ▓▓   ▓▓▓  ▓▓▓       ▓▓▓          ░▓▓  ▓▓▓       ░▓▓ ░▓▓
 ▓▓    ▓▓▒▓▓▓   ▓▓▓  ▓▓▓       ▓▓▓          ▓▓▓  ▓▓▓   ▒▓▓░▓▓▓  ▓▓░         ▓
 ▓▓     ▓▓▓░    ▓▓▓    ▒▓▓▓▓▓▓▓▓▓▒ ▓▓▓▓▓▓▓▓▓▓      ▓▓▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓▓  ▓░▒
                              ▓▓▓                           ▓▓▓

```

## Instalar MariaDB/MySQL Debian

- :link: [MariaDB Downloads](https://downloads.mariadb.org/mariadb/repositories/#mirror=globotech)
- :link: [MariaDB tutorials](https://mariadb.com/kb/en/library/training-tutorials/)
- :link: [How To Install the Latest MySQL on Debian 10](https://www.digitalocean.com/community/tutorials/how-to-install-the-latest-mysql-on-debian-10)
- :link: [How To Install the Latest MySQL on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-22-04)
- :link: [MySQL Lifecycle (EOL) 1](https://endoflife.software/applications/databases/mysql)
- :link: [MySQL Lifecycle (EOL) 2](http://www.oracle.com/us/support/library/lifetime-support-technology-069183.pdf)
- :link: [A Quick Guide to Using the MySQL APT Repository](https://dev.mysql.com/doc/mysql-apt-repo-quick-guide/en/)
- :link: [MySQL Community Downloads](https://dev.mysql.com/downloads/mysql/)
- :link: [Ubuntu / Debian (Architecture Independent), DEB Package ](https://dev.mysql.com/downloads/repo/apt/)

## Instalar MariaDB, crear en `source.list`

```bash
# MariaDB 10.2 repository list - created 2018-04-30 01:28 UTC
# http://downloads.mariadb.org/mariadb/repositories/
deb [arch=amd64,i386,ppc64el] http://sfo1.mirrors.digitalocean.com/mariadb/repo/10.2/debian stretch main
deb-src http://sfo1.mirrors.digitalocean.com/mariadb/repo/10.2/debian stretch main

```

Después

```bash
sudo apt-get install software-properties-common dirmngr
sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xF1656F24C74CD1D8
sudo apt-get update
sudo apt-get install mariadb-server
```

Para añadir password y configurar las opciones de MariaDB:

```sql

```

### Instalar MySql en Ubuntu 20.04

Instalar el paquete `mysql-server`

```bash
sudo apt install mysql-server
```

Iniciar el servicio usando `systemctl start`

```bash
sudo systemctl start mysql.service
```

Revisar el servicio si esta activo

```bash
sudo systemctl status mysql.service
```

#### Configurar MySql

Primero abrir en consola MySql

```bash
sudo mysql
```

Ejecutar el comando `ALTER USER` para cambiar el método de autenticación de la cuenta de usuario `root`

```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
```

Después salir de la linea de comando de MySQL

```sql
exit
```

Ejecutar el comando `mysql_secure_installation` para configurar la seguridad de la instalación de MySQL

```bash
sudo mysql_secure_installation
```

👇

```bash
➜ sudo mysql_secure_installation

Securing the MySQL server deployment.

Enter password for user root:

VALIDATE PASSWORD COMPONENT can be used to test passwords
and improve security. It checks the strength of password
and allows the users to set only those passwords which are
secure enough. Would you like to setup VALIDATE PASSWORD component?

Press y|Y for Yes, any other key for No: Y

There are three levels of password validation policy:

LOW    Length >= 8
MEDIUM Length >= 8, numeric, mixed case, and special characters
STRONG Length >= 8, numeric, mixed case, special characters and dictionary                  file

Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG: 2
Using existing password for root.

Estimated strength of the password: 100
Change the password for root ? ((Press y|Y for Yes, any other key for No) : n

 ... skipping.
By default, a MySQL installation has an anonymous user,
allowing anyone to log into MySQL without having to have
a user account created for them. This is intended only for
testing, and to make the installation go a bit smoother.
You should remove them before moving into a production
environment.

Remove anonymous users? (Press y|Y for Yes, any other key for No) : Y
Success.


Normally, root should only be allowed to connect from
'localhost'. This ensures that someone cannot guess at
the root password from the network.

Disallow root login remotely? (Press y|Y for Yes, any other key for No) : Y
Success.

By default, MySQL comes with a database named 'test' that
anyone can access. This is also intended only for testing,
and should be removed before moving into a production
environment.


Remove test database and access to it? (Press y|Y for Yes, any other key for No) : y
 - Dropping test database...
Success.

 - Removing privileges on test database...
Success.

Reloading the privilege tables will ensure that all changes
made so far will take effect immediately.

Reload privilege tables now? (Press y|Y for Yes, any other key for No) : Y
Success.

All done!
```

Cuando el script de seguridad acabe, se tiene que cambiar el método de autenticación del usuario `root` al por default `auth_socket`

```bash
mysql -u root -p
```

Luego vuelva a usar el método de autenticación predeterminado usando:

```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH auth_socket;
```

Realizado lo anterior se puede conectar a MySQL como `root` usando el comando `sudo mysql`

```sql
exit
```

> In Ubuntu systems running MySQL 5.7 (and later versions), the root MySQL user is set to authenticate using the auth_socket plugin by default rather than with a password. This plugin requires that the name of the operating system user that invokes the MySQL client matches the name of the MySQL user specified in the command, so you must invoke mysql with sudo privileges to gain access to the root MySQL user

```bash
sudo mysql
```

#### Crear usuario

> ES RECOMENDABLE NO USAR `root` para tareas administrativas, es mejor crear un usuario con permisos de administrador.
> El usuario administrativo se encarga la creación de los usuarios y de creación de las tablas.

> Un usuario o grupo de usuarios se les asigna una base de datos y se les otorgan permisos para realizar operaciones en esa base de datos.

```sql
CREATE USER 'admin_mack'@'localhost' IDENTIFIED WITH authentication_plugin BY 'AQUIVALACONTRASEÑA';
```

> In MySQL versions prior to 8.0, `sha256_password` might not be the default authentication plugin. You might need to explicitly specify it during user creation using the PASSWORD clause with the `sha256_password` plugin name.

> From MySQL 8.0 onwards, 👉 `caching_sha2_password` (a more advanced version with caching) is the default, while `sha256_password` _is deprecated and recommended to be migrated towards_ `caching_sha256_password`

**NOTA:** Otra forma puede ser usando `authentication_plugin` 👁️

Usando el siguiente comando se utiliza `caching_sha2_password` de forma predeterminada.

```sql
CREATE USER 'mi_usuario'@'localhost' IDENTIFIED BY 'mi_contraseña';
```

Para otorgarle privilegios _administrativos_ al usuario creado [privilegios de MySQL](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#privileges-provided-summary)

```sql
GRANT ALL PRIVILEGES ON *.* TO 'mi_usuario'@'localhost' WITH GRANT OPTION;
```

Es buena practica usar el comando `FLUSH PRIVILEGES`. Para liberar cualquier memoria en el cache como resultado de los cambios en los privilegios, usando `CREATE USER`y `GRANT`

```sql
FLUSH PRIVILEGES;
```

```sql
exit
```

Para ingresar con el nuevo **usuario administrativo** y no como `root`

```bash
mysql -u mi_usuario -p
```

### Instalar MySql Workbench en Debian buster 10

En [MySQL Community Downloads](https://dev.mysql.com/downloads/) descargar del 🔗 [MySQL Workbench](https://dev.mysql.com/downloads/workbench/)

1. Seleccionar **Ubuntu Linux**
2. Seleccionar la version **22.04**
3. Se descarga el archivo para **Ubuntu 22.04 (Architecture Independent), DEB Package**
4. Instalar en caso de no estar instalado `gdebi` `$ sudo apt install gdebi-core gdebi`
5. Instalar MySql Workbench `sudo gdebi ARCHI_DESCARGADO_amd64.deb`
6. Si se presenta que no esta instalada una dependencia `$ sudo apt-get install -f`

### Database Backups

Store mysql root password in `/root/.cnf` Como **root** se puede acceder. chmod 600

```bash
[client]
user=root
password=<CONTRASEÑA>
```

### Back Up una DB

```bash
mysql --add-drop-table --database nombredelabasededatos > /home/nombredeusuario/backups/db/$(bin/date '+\%Y-\%m-\%d').sql.bk
```

### Back Up todas las DB

```bash
mysql --all-databases --all-routines > /path/to/fulldump.sql
```

### Restaurar a DB de un Back Up

```bash
mysql -u root -p [nombredelabasededatos] < archivoDeBackup.sql
```

### Para restaurar dotas las DB

Primero necesitan existir o el archivo debe de contener **CREATE TABLE**

```bash
mysql -u root -p < archivoDeTodasLasDB.sql
```

### Login MySQL

```bash
mysql -u root -p -h localhost
```

### Howto's MySql

Mostrar lista de todos usuarios de MySql

```sql
SELECT user, host FROM mysql.user;
```

### Mostrar variables MySql/mariadb

```sql
SHOW VARIABLES LIKE "%version%";
```

### Cambiar contraseña de _root_

1. `mysql -u root -p`
2. `use mysql;`
3. `update user set password=PASSWORD('your_new_password') where User='root';`
4. `flush privileges;`
5. `quit`

#### Mostrar privilegios concedidos de un usuario

1. `mysql> show grants for 'root'@'%';`
2. `SHOW GRANTS FOR 'root'@'localhost';`

#### Muestra las BD

```sql
SHOW DATABASES;
```

#### Crea una BD

```sql
CREATE DATABASE nombredelabasededatos;
```

#### Borrar una BD

1. `mysql> DROP DATABASE nombredelabasededatos;`
2. `DROP DATABASE IF EXISTS tutorial_database;`

#### Para usar una BD

```sql
USE nombredelabasededatos;
```

#### Crear usuario con

:link: [Chapter 13 Creating User Accounts](https://dev.mysql.com/doc/mysql-secure-deployment-guide/8.0/en/secure-deployment-user-accounts.html)

Crear un usuario forma No.1

```sql
CREATE USER 'mi_usuario'@'localhost' IDENTIFIED BY 'Mi contrasena 2020';
```

Crear un usuario forma No.2

```sql
CREATE USER 'mi_usuario'@'localhost' IDENTIFIED WITH sha256_password BY 'Mi contrasena 2020'
       REQUIRE X509 WITH MAX_USER_CONNECTIONS 3 PASSWORD EXPIRE DEFAULT;
```

Mostrar los usuarios

```sql
SELECT user, authentication_string, host FROM mysql.user;
```

### Dar permisos a una DB a un usuario [privileges](https://dev.mysql.com/doc/refman/8.0/en/privileges-provided.html#privileges-provided-summary)

1. `GRANT permission ON DATABASENAME.* TO 'user'@'localhost';`
   - `ALL`: Allow complete access to a specific database. If a database is not specified, then allow complete access to the entirety of MySQL.
   - `CREATE`: Allow a user to create databases and tables.
   - `DELETE`: Allow a user to delete rows from a table.
   - `DROP`: Allow a user to drop databases and tables.
   - `EXECUTE`: Allow a user to execute stored routines.
   - `GRANT` OPTION: Allow a user to grant or remove another user’s privileges.
   - `INSERT`: Allow a user to insert rows from a table.
   - `SELECT`: Allow a user to select data from a database.
   - `SHOW DATABASES`: Allow a user to view a list of all databases.
   - `UPDATE`: Allow a user to update rows in a table.
   - `ALTER`: Allow a user to alter a table.
2. _Dar permisos a todas las DB_ para un suario -> `GRANT CREATE ON *.* TO 'test_user'@'localhost';`
3. Dar permiso de _borrar_ una DB a un usuario -> `GRANT DROP ON tutorial_database.* TO 'test_user'@'localhost';`
4. Cuando termine de hacer los cambios de permiso, _es una buena práctica volver a cargar todos los privilegios con el comando de descarga_ -> `FLUSH PRIVILEGES;`
5. Mostrar permisos otorgados para un usuario -> `SHOW GRANTS FOR 'test_user'@'localhost';`

### Quitar/revocar permisos de una DB a un usuario

1. `REVOKE permission ON database.table FROM 'user'@'localhost';`
   - `ALL`: Allow complete access to a specific database. If a database is not specified, then allow complete access to the entirety of MySQL.
   - `CREATE`: Allow a user to create databases and tables.
   - `DELETE`: Allow a user to delete rows from a table.
   - `DROP`: Allow a user to drop databases and tables.
   - `EXECUTE`: Allow a user to execute stored routines.
   - `GRANT` OPTION: Allow a user to grant or remove another user’s privileges.
   - `INSERT`: Allow a user to insert rows from a table.
   - `SELECT`: Allow a user to select data from a database.
   - `SHOW DATABASES`: Allow a user to view a list of all databases.
   - `UPDATE`: Allow a user to update rows in a table.
   - `ALTER`: Allow a user to alter a table.
2. _Quitar permisos para todas las DB_ a un usuario -> `REVOKE CREATE ON *.* FROM 'test_user'@'localhost';`
3. _Quitar el permiso de eliminar una DB_ -> `REVOKE DROP ON tutorial_database.* FROM 'test_user'@'localhost';`
4. Cuando termine de hacer los cambios de permiso, _es una buena práctica volver a cargar todos los privilegios con el comando de descarga_ -> `FLUSH PRIVILEGES;`
5. Mostrar permisos otorgados para un usuario -> `SHOW GRANTS FOR 'test_user'@'localhost';`

#### Para borrar un usuario

```sql
DROP USER 'usuario'@'localhost';
```

#### Para mostrar las tablas

```sql
SHOW TABLES;
```

#### Para dar permisos desde la consola sobre todas las tablas de una base de datos

```sql
GRANT ALL PRIVILEGES ON nombredelabasededatos.* TO 'nombre_usuario'@'localhost';
```

#### Después de dar o quitar permisos, siempre tendremos que ejecutar el siguiente comando para aplicarlos

```sql
FLUSH PRIVILEGES;
```

#### Para dar permisos desde la consola sobre una tabla concreta de la base de datos, el usuario se puede conectar desde cualquier host

```sql
GRANT CREATE, DELETE, EXECUTE, INSERT, SELECT, UPDATE, ALTER, REFERENCES, TRIGGER ON database_name.concrete_table TO 'nombre_usuario'@'%';
```

Opción No.2

```sql
GRANT CREATE, DELETE, EXECUTE, INSERT, SELECT, UPDATE, ALTER, REFERENCES, TRIGGER ON the_database.* TO 'nombre_usuario'@'localhost';
```

Option No.3

```sql
GRANT ALL PRIVILEGES ON the_database.*.* TO 'mi_usuario'@'localhost'
```

Para quitar permisos desde la consola de mysql, ejecutaremos el siguiente comando.

Si queremos afectar a una base de datos, tabla concreta, etc. lo haremos igual que para dar permisos.

En este ejemplo afectamos a todas las bases de datos `.` y quitaremos todos los permisos (`ALL PRIVILEGES`)

```sql
REVOKE ALL PRIVILEGES ON *.* FROM 'nombre_usuario'@'localhost';
```

#### Para saber que BD estoy usando

```sql
SELECT DATABASE(); -- \s
```

#### Para saber que usuario estoy parado

```sql
SELECT USER(); -- \s
mysql> SELECT CURRENT_USER;
```

#### Para saber los privilegios de un usuario

```sql
SHOW GRANTS FOR 'root'@'localhost';
```

#### Para ver los privilegios concedidos a una cuenta que se esta usando conectada al server

```sql
SHOW GRANTS;
SHOW GRANTS FOR CURRENT_USER;
SHOW GRANTS FOR CURRENT_USER();
```

#### Saber cuales son los triggers de una tabla

```sql
SHOW TRIGGERS;
```

#### How to Check which MySQL version I am running?

```sql
# mysqladmin -u root -p version
```

#### How to Find out current Status of MySQL server?

```sql
# mysqladmin -u root -ptmppassword status
```

#### How to check status of all MySQL Server Variable’s and value’s?

```sql
# mysqladmin -u root -p extended-status
```

#### How to see all MySQL server Variables and Values?

```sql
# mysqladmin  -u root -p variables
```

#### How to check all the running Process of MySQL server?

```sql
# mysqladmin -u root -p processlist
```

#### How to reload/refresh MySQL Privileges?

```sql
# mysqladmin -u root -p reload;
# mysqladmin -u root -p refresh
```

#### Como apagar el servidor de MySql dse forma segura

```sql
# mysqladmin -u root -p shutdown
    Ó
# /etc/init.d/mysqld stop
# /etc/init.d/mysqld start
```

#### Some useful MySQL Flush commands - Following are some useful flush commands with their description

```sql
flush-hosts: Flush all host information from host cache.
flush-tables: Flush all tables.
flush-threads: Flush all threads cache.
flush-logs: Flush all information logs.
flush-privileges: Reload the grant tables (same as reload).
flush-status: Clear status variables.

# mysqladmin -u root -p flush-hosts
# mysqladmin -u root -p flush-tables
# mysqladmin -u root -p flush-threads
# mysqladmin -u root -p flush-logs
# mysqladmin -u root -p flush-privileges
# mysqladmin -u root -p flush-status
```

#### How to kill Sleeping MySQL Client Process? - Use the following command to identify sleeping MySQL client process

```sql
# mysqladmin -u root -p processlist
```

#### Despues con el siguiente comando se mata el proceso, es el "Id"

```sql
# mysqladmin -u root -p kill 5
```

#### How to Connect remote mysql server - To connect remote MySQL server, use the -h (host) with IP Address of remote machine

```sql
# mysqladmin  -h 172.16.25.126 -u root -p
```

#### How to start/stop MySQL replication on a slave server? - To start/stop MySQL replication on salve server, use the following commands

```sql
# mysqladmin  -u root -p start-slave
# mysqladmin  -u root -p stop-slave
```

#### How to store MySQL server Debug Information to logs? - It tells the server to write debug information about locks in use, used memory and query usage to the MySQL log file including information about event scheduler

```sql
# mysqladmin  -u root -p debug
```
