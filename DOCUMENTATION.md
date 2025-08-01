Contenido
Cambios en esta versión ......................................................................................... 7
Presentación ....................................................................... 8
Introducción ............................................................................................................ 9
Disponibilidad de la API ......................................................................................... 10
Características de GAPI .......................................................................................... 11
Seguridad ............................................................................................................... 11
Solicitud del token .................................................................................................................. 13
Construcción de consultas .................................................................................... 15
Paso de parámetros ................................................................................................................ 15
Manejo del tipo de contenido ................................................................................................ 16
Mensajes de error................................................................................................................... 17
Formato de respuesta ........................................................................................... 17
Paginación ............................................................................................................. 18
Filtrado de consultas ............................................................................................. 22
Disminuyendo el peso de las consultas (el parámetro w) ..................................... 25
Consultas anidadas ................................................................................................ 28
Combinación de parámetros ................................................................................. 30
El atributo data{} ................................................................................................... 32
en productos ........................................................................................................................... 32
en certificados ........................................................................................................................ 33
Versión 3.7 (Nov-2024) Desarrollada por
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
El atributo values{} ................................................................................................ 34
en certificados ........................................................................................................................ 35
El atributo addresses{} .......................................................................................... 36
en certificados ........................................................................................................................ 37
Diagrama de estructura de datos .......................................................................... 40
Consultas ........................................................................... 41
Coberturas ............................................................................................................. 42
Cobertura según el id ............................................................................................ 44
Productos .............................................................................................................. 45
Productos según el id ............................................................................................ 47
Coberturas del producto ....................................................................................... 49
Países ..................................................................................................................... 51
Regiones ................................................................................................................ 53
Direcciones ............................................................................................................ 55
Usuarios ................................................................................................................. 57
Productores ........................................................................................................... 60
Consulta de vendedores ........................................................................................ 64
Certificado por número ......................................................................................... 65
Certificado con factura asociada ........................................................................... 67
Certificado con direcciones ................................................................................... 69
Certificado en formato .pdf ................................................................................... 71
Certificado con productos y coberturas ................................................................ 72
Certificados emitidos ............................................................................................. 75
Versión 3.7 (Nov-2024) Desarrollada por
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Certificados cancelados ......................................................................................... 78
Asegurados ............................................................................................................ 81
Certificados: consulta personalizada ..................................................................... 84
Exportar ............................................................................ 86
Enviar documentos por correo electrónico .......................................................... 87
Exportar certificado a formato de archivo .CSV .................................................... 88
Exportar consulta de reaseguro a formato de archivo .CSV ................................. 91
Exportar a formato de archivo .XML ..................................................................... 94
Transacciones .................................................................... 97
Introducción .......................................................................................................... 98
Reglas del Negocio en GAPI ................................................................................... 99
Políticas ................................................................................................................................... 99
Acerca de la cotización del seguro de viaje .......................................................................... 100
Acerca de los canales de venta ............................................................................................. 100
Acerca de la emisión del seguro de viaje .............................................................................. 101
Acerca de los productos y sus coberturas ............................................................................ 102
Acerca de las tarifas .............................................................................................................. 102
Acerca de la facturación ....................................................................................................... 103
Acerca del pago .................................................................................................................... 103
Flujo transaccional............................................................................................... 104
Cotización ............................................................................................................................. 104
Validaciones adicionales ....................................................................................................... 106
Pago ...................................................................................................................................... 110
Versión 3.7 (Nov-2024) Desarrollada por
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Emitir seguro de viaje: 1 asegurado, 1 producto base ........................................ 112
Emitir seguro de viaje: 2 asegurados, 1 producto base + 1 producto opcional o
complementario .................................................................................................. 115
Emitir seguro de viaje: varios asegurados, 1 producto base + varios productos
opcionales o complementarios ........................................................................... 118
Pago de una póliza con cargo a la línea de crédito del productor ...................... 122
Cambios a un seguro de viaje .............................................................................. 123
Mover la vigencia de un seguro de viaje............................................................................... 124
Cambiar el destino de un certificado de viaje emitido ......................................................... 125
Cambiar la dirección de un certificado de viaje emitido ....................................................... 126
Cambiar datos de los asegurados en un certificado emitido ................................................ 128
Anular seguro de viaje ......................................................................................... 129
Reportes .......................................................................... 130
Introducción ........................................................................................................ 131
Alcance de la consulta ......................................................................................... 131
Reporte Costos de Emisión ................................................................................. 132
Reporte Costos de Emisión por región ................................................................ 135
Reporte Valores de Emisión ................................................................................ 137
Reporte de pagos a través de la pasarela CARDNET ........................................... 139
Reporte de pagos a través de la pasarela CARDNET en formato de archivo csv 142
Reporte de facturas ............................................................................................. 145
Solución de problemas ................................................... 148
Preguntas frecuentes .......................................................................................... 149
Versión 3.7 (Nov-2024) Desarrollada por
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Mensaje: “Al menos una persona entre las indicadas posee un producto básico activo”
... 149
Mensaje: “Arreglo de asegurados es inválido”
..................................................................... 150
Mensaje: “Arreglo de direcciones es inválido”
..................................................................... 150
Mensaje: “Arreglo de productos es inválido”
....................................................................... 151
Mensaje: “from no corresponde al formato Y-m-d”
............................................................. 151
Mensaje: “El campo <campo> es obligatorio”
...................................................................... 152
Mensaje: “El certificado ya ha sido cancelado”
.................................................................... 153
Mensaje: “La agencia <productor> no tiene balance para emitir a crédito”
........................ 154
Mensaje: “El destino es inválido o no está disponible.”
....................................................... 154
Mensaje: “ncf_id es inválido”
............................................................................................... 155
Mensaje: “No existen tarifas disponibles para su selección”
............................................... 156
Mensaje: “No se encontraron datos usando sus criterios”
.................................................. 156
Mensaje: “No se pudo procesar su solicitud”
....................................................................... 157
Mensaje: “Method Not Allowed”
......................................................................................... 157
Mensaje: “Not Found”
.......................................................................................................... 158
Mensaje: “salesman id es inválido”
...................................................................................... 158
Mensaje: “Token expirado” .................................................................................................. 159
Mensaje: “Usted no tiene acceso a esta acción” .................................................................. 160
Glosario de Términos ...................................................... 161
Anexos ............................................................................. 165
Códigos de Respuesta CARDNET ......................................................................... 166
Códigos de Tipos de NCF ..................................................................................... 168
Tabla de diagnóstico ............................................................................................ 169
Versión 3.7 (Nov-2024) Desarrollada por
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Actualización de la sección
Disminuyendo el peso de las consultas
(el parámetro w)
Se detalla en mayor profundidad las premisas que son la
base de las consultas, así como el uso del parámetro w , su
uso en consultas que se apoyan en relaciones y las
implicaciones por limitaciones del RFC 1738.
Actualización de la sección
Certificados emitidos
Certificados cancelados
Se incorpora la funcionalidad de búsqueda por los últimos 4
dígitos del número de certificado, además de por el número
completo. A partir de esta versión, los certificados se
identifican mediante un identificador compuesto por tres
secciones de 4 dígitos cada uno, separados por guiones que
aseguran la unicidad y seguridad del certificado.
Actualización de la sección
Se elimina el atributo EXONERATED
En Certificados
Actualización de la sección
En Productores
Se agregan atributos adicionales para la creación de
consultas a productores.
Versión 3.7 (Nov-2024) Desarrollada por Página 7 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Presentación
Versión 3.7 (Nov-2024) Desarrollada por Página 8 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Llamamos API (del inglés Application Programming Interface – Interfaz de Programación de
Aplicación) al conjunto de rutinas, funciones y procedimientos (métodos) que permite utilizar
recursos de un software por otro, sirviendo como una capa de abstracción o intermediario, dicho
en otras palabras, las API se crean con el objetivo de que cualquier software pueda “consumir”
recursos de otro software, por lo general datos, sin importar en que lenguaje o plataforma hayan
sido creados.
La API de GOVAL-Web, a la que llamamos GAPI, pone a disposición de los equipos de desarrollo,
procesos internos de la aplicación que facilitan la emisión de certificados de seguros de viaje y
realizar cambios a estas desde su software propietario, en adición consultar las transacciones
registradas en el sistema. Esto simplifica el desarrollo de integraciones, permitiendo ahorrar
tiempo y dinero al otorgar flexibilidad, simplificación de diseño, administración y uso de las
funcionalidades de la aplicación desde su core comercial.
GAPI está implementada con base a la especificación “Transferencia de Estado Representacional
(REST)”, siendo en realidad una API de RESTful que cumple con las siguientes premisas:
▪ Arquitectura cliente-servidor: está compuesta por clientes, servidores y recursos que
administran las solicitudes con HTTP.
▪ Sin estado: el contenido de los clientes no se almacena en el servidor entre las solicitudes,
sino que la información sobre el estado de la sesión se queda en el cliente, es decir, está
en posesión del cliente.
▪ Sistema en capas: las interacciones cliente-servidor están mediadas por capas adicionales,
que pueden ofrecer otras funciones, como balanceo de carga, cachés compartidos o la
seguridad. Funcionalidades adicionales son posible que se puedan agregar de manera
opcional de acuerdo con el contrato del cliente.
Como es usual, al “consumir” la API se deben especificar parámetros de consulta para que el
servicio sepa lo que se desea consultar. Para ello hemos provisto una estructura previamente
definida, la cual se especifica en este documento.
Los procedimientos o métodos de comunicación son los mismos que HTTP, siendo los principales:
GET, POST, PUT y DELETE. El otro componente para destacar es el “HTTP Status Code”
, con el cual
se le informa al cliente o consumidor del API qué debe hacer con la respuesta recibida.
Versión 3.7 (Nov-2024) Desarrollada por Página 9 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Para futuras referencias, seguidamente se copian estos estados:
▪ 200 OK
▪ 201 Created (Creado)
▪ 304 Not Modified (No modificado)
▪ 400 Bad Request (Error de consulta)
▪ 401 Unauthorized (No autorizado)
▪ 403 Forbidden (Prohibido)
▪ 404 Not Found (No encontrado)
▪ 422 (Unprocessable Entity (Entidad no procesable)
▪ 500 Internal Server Error (Error Interno de Servidor)
El cuerpo (BODY) de la respuesta de la API ofrece una estructura en formato jSON que permite que
cualquier cliente pueda consumir el servicio. Para acceder a estos, debe contactar al ejecutivo de
GOVAL quien le proporcionará la ruta o método especifico vía URL, o en su defecto, le pondrá en
contacto con el Departamento de Tecnología.
La disponibilidad de algunos métodos de la API está sujeta a condiciones
contractuales particulares del cliente.
Se recomienda consultar a su ejecutivo de negocios.
Versión 3.7 (Nov-2024) Desarrollada por Página 10 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GAPI
GAPI es un servicio basado en REST/JSON, autentificado mediante web tokens que ofrece muchas
facilidades a los equipos de desarrollo que desean integrar en sus aplicaciones, los servicios de
emisión de seguro de viaje proporcionados por GOVAL, de esta manera acortan una larga ruta de
desarrollo tradicional y los desafíos que representa la incorporación de nuevas opciones, lenguajes,
arquitecturas, librerías o frameworks, que crecen semana tras semana.
AL usar GAPI se asegura que los servicios se puedan consumir desde cualquier sistema o cliente
debido a que esta no devuelve más que datos desacoplados a cualquier modo de visualización. Si
se desea implementar una web, se puede consumir el API desde cualquiera de los frameworks o
librerías JavaScript populares, como AngularJS, Polymer o ReactJS. También se puede consumir los
servicios de la API desde aplicaciones desarrolladas en Java para Android o Swift/Objective C para
iOS, por ejemplo.
Como muchas de las API REST, GAPI simplifica el funcionamiento, porque elimina todo lo
relacionado al estado de la aplicación. Aunque REST de por si no almacena ninguna información de
la sesión del usuario, esto lo resuelve mediante un token que el cliente debe enviar al servidor en
cada solicitud que realice.
El acceso a la API está basado en el uso de JSON Web Token (JWT). Un JSON Web Token es un
estándar abierto (RFC 7519) que define una forma compacta y autónoma de transmitir información
de forma segura entre las partes como un objeto JSON, confiable y verificable porque está firmado
digitalmente.
En el caso de GAPI, los JWT se firman con un par de claves pública/privada utilizando RSA o ECDSA
y son utilizados tanto para la autentificación como para la autorización.
Versión 3.7 (Nov-2024) Desarrollada por Página 11 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
La autorización es el escenario más común donde GAPI usa JWT. Una vez que el usuario inicia
sesión, cada solicitud posterior incluirá el JWT, lo que le permitirá acceder a las rutas, servicios y
recursos permitidos con ese token.
Como la autentificación se basa en proporcionar un conjunto de credenciales para que el servidor
o la aplicación pueda verificar que el usuario es quien dice ser y que la información que se
proporciona es válida, la autorización parte del proceso de autentificación y este garantiza que una
vez que se determine que las credenciales de usuario son correctas, se aplicará el control de acceso
para determinar a qué recursos se puede acceder en el sistema.
El intercambio de información es una buena manera de transmitir los datos de forma segura entre
las partes por la capacidad que ofrecen los JWT al poder ser firmados, no obstante, GAPI
actualmente no utiliza esta funcionalidad para entregar la información.
Aunque no es el propósito de este documento explicar en detalles lo que es un JWT, es importante
destacar que se compone de tres partes: el encabezado, la carga útil y la firma. Es precisamente
este último componente el que asegura la autenticación.
Diagrama de solicitud del token
El proceso inicia suministrando a la ruta proporcionada, las credenciales de acceso compuestas del
nombre de usuario y la contraseña asociada a este; una vez el servidor de autenticación valida esta
información, crea un token JWT con una carga útil que contiene el identificador técnico del usuario
y una marca de tiempo de vencimiento determinada por los acuerdos de servicio.
El servidor de autenticación toma una clave secreta y la usa para firmar el encabezado más la carga
útil y lo envía de vuelta al navegador del usuario. El navegador toma el JWT firmado y lo envía con
cada solicitud HTTP al servidor de aplicaciones GAPI.
Versión 3.7 (Nov-2024) Desarrollada por Página 12 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Esquema de consulta
El JWT firmado actúa efectivamente como una credencial de usuario temporal, que reemplaza la
credencial permanente que es la combinación de nombre de usuario y contraseña. A partir de ahí,
el servidor de aplicaciones de GAPI verifica la firma JWT y confirma que, de hecho, alguien en
posesión de la clave secreta firmó esta carga útil en particular.
La carga útil identifica a un usuario en particular a través de un identificador técnico ya que el
servidor de autenticación solo entrega tokens a los usuarios que envían la contraseña correcta.
La firma JWT como la mayoría de las firmas, se basa en una función hash criptográfica con algunas
propiedades únicas tales como: irreversible, reproducible, sin colisiones e impredecible.
Para solicitar un token debe asegurarse de que la cuenta de usuario que utilizará en el servicio ha
sido habilitada en GOVAL-Web y que esta cuenta con los privilegios necesarios para acceder al
recurso. Este es uno de los aspectos que pueden generar llamadas de soporte, debido a que el
usuario considera que tiene acceso a todos los servicios de la aplicación.
En el siguiente ejemplo se utiliza curl para solicitar un token con el método POST. Nótese que por
razones de seguridad se ha indicado como ruta localhost y los valores login y password han
sido llenados con “*”.
Versión 3.7 (Nov-2024) Desarrollada por Página 13 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Petición
$ curl --location --request POST 'http://localhost/api/auth/token/jwt?acl=1' \
--form 'login=*****' \
--form 'password=*****'
Consulta con curl para obtener un token jwt
Respuesta
{"jwt":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJnb3ZhbC13ZWIiLCJhdWQiOlsiaHR0cHM6XC9cL2xhYnZpYW
phc2VndXJvLmxhY29sb25pYWwuY29tLmRvIl0sImlhdCI6MTY0MjQyNDg0MSwiZXhwIjoxNjQyNDI1MTQxLCJzdWIiOiIwMDEtODA5M
DAwMC0xIiwiYWNsIjpbImFkZHJlc3MudmlldyIsImFnZW5jeS5leHBvcnQiLCJhZ2VuY3kuZXhwb3J0IiwiYWdlbmN5LnZpZXciLCJh
Z2VuY3kudmlld19hbGwiLCJiZW5lZml0LmV4cG9ydCIsImJlbmVmaXQudmlldyIsImJlbmVmaXQudmlld19hbGwiLCJjbGllbnQuZXh
wb3J0IiwiY2xpZW50LnZpZXciLCJpbnZvaWNlLnByaW50IiwiaW52b2ljZS52aWV3Iiwib3BlcmF0aW9ucy52aWV3IiwicHJvZHVjdC
5leHBvcnQiLCJwcm9kdWN0LnZpZXciLCJwcm9kdWN0LnZpZXdfYWxsIiwicHJvZmlsZS52aWV3IiwicHJvbW8uZXhwb3J0IiwicHJvb
W8udmlldyIsInF1b3RlLmdlbmVyYXRlIiwicXVvdGUudmlldyIsInJlcG9ydC5hY2NvdW50aW5nLmV4cG9ydCIsInJlcG9ydC5hY2Nv
dW50aW5nLnZpZXciLCJyZXBV3IiwicmVwb3J0LmNvc3RzLmV4cG9ydCIsInJlcG9ydC5jcmVkaXQuZXhwb3J0IiwicmVwb3J0LmNyZW
RpdC52aWV3IiwicmVwb3J0LmN4Yy5leHBvcnQiLCJyZXBvcnQuY3hjLnZpZXciLCJyZXBvcnQuc2FsZXMuZXhwb3J0IiwicmVwb3J0L
nNhbGVzLnZpZXciLCJyZXBvcnQudGF4LmV4cG9ydCIsInJlcG9ydC50YXgudmlldyIsInRpY2tldC5jb25zdWx0LmNhbmNlbGxhdGlv
bi5leHBvcnQiLCJ0aWNrZXQuY29uc3VsdC5jYW5jZWxsYXRpb24udmlldyIsInRpY2tldC5jb25zdWx0LmNlcnRpZmljYXRlLmV4cG9
ydCIsInRpY2tldC5jb25zdWx0LmNlcnRpZmljYXRlLmV4cG9ydCIsInRpY2tldC5jb25zdWx0LmNlcnRpZmljYXRlLnZpZXciLCJ0aW
NrZXQuY29uc3VsdC5pbnN1cmVkLmV4cG9ydCIsInRpY2tldC5jb25zdWx0Lmluc3VyZWQudmlldyIsInRpY2tldC5pbnZvaWNlLnZpZ
XciLCJ0aWNrZXQucHJlcGFpZC5iYWxhbmNlLnZpZXciLCJ0aWNrZXQucHJlcGFpZC5pc3N1ZSIsInRpY2tldC5xdW90ZS52aWV3Iiwi
dGlja2V0LnZpZXdfYWxsIiwidGlja2V0LnZpZXcuYW1vdW50IiwidGlja2V0LnZpZXcuY2VydGlmaWNhdGUiLCJ0aWNrZXQudmlldy5
jZXJ0aWZpY2F0ZSIsInRpY2tldC52aWV3LmNvc3RzIiwidXNlci5leHBvcnQiLCJ1c2VyLnZpZXdfYWxsIiwid2VsY29tZV9sZXR0ZX
Iuc2VuZCIsIndlbGNvbWVfbGV0dGVyLnZpZXciXX0.Jjj6G83-qASo7_bcd-VN7opeDms3PrWoxn1d1FteLbwV7B-
F32v5t1dLKfsWw31RW_lLJrL7Vsi67JMoXKh20S-wcutl2geMzixD_HXgYA6iz2b-hXSFuGu4qMcFrDE-RzajyHP0IUQ4on-
FbHxYiFMScbcGzKcOp8S2yie0dJmULUS3BXUbHhiwydEJovdYSq_fG9UPMCXJOZTq2pcNijxAR_Wm92_FFGQ9spr4ErIN7QdpYbU1yk
svpNaEeB5iRFXYe6U2HtHvAUBbdhalFGXJto8EpmgS7oH2XJJEraYRY1mwvnRLfVfTFG3Me2cYjVzdlIYFn1MDamFqmSXqQw"}
Token JWT devuelto por GAPI
El token emitido por GAPI tiene una vigencia de 5
minutos por lo que es responsabilidad del usuario
asegurar su utilización en el tiempo previsto. Se pueden solicitar
tantos tokens como sean necesarios.
Versión 3.7 (Nov-2024) Desarrollada por Página 14 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Para realizar una consulta se debe incluir el token como encabezado. Por ejemplo:
Petición
$ curl --location --request GET 'http://localhost/api/ticket?ticket_id=00000002' \
--header 'Accept: application/json' \
--header 'x-goval-auth:
jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJnb3ZhbC13ZWIiLCJhdWQiOlsiaHR0cHM6XC9cL2xhYnZpYWphc2
VndXJvLmxhY29sb25pYWwuY29tLmRvIl0sImlhdCI6MTY2MjU1MjY2OSwiZXhwIjoxNjYyNTUyOTY5LCJzdWIiOiIyIn0.c-
Wx_WXxCk0tRO0lYb9lsTcL9gy5uYLSeESMGzhZIYSz-
HIXA2UTY0wMabXKuVvLeseA2slRchzlzkrQgT23NqiqgQagts8FKfbHq6umm5dgoNarxv1xHLK2b48WPMX7OoJ6PVNbazug7-
cqzXT69RuzKgmReBMMfvCGA9cWAw56O5DxhpOJ7OlOIusp5qC9GJg1uhqjYRWbbUVNs3Ae7VCnwFs-PzGYin0Q6fbHJHVfkHzb-
3cEcMQwvFpalNT58Cr8IFkI_ogHzJ-j8RISl-pULP-x2WnCnJ7hIL7RZ1TuHJkh1UfakRhb8v4YRANE_OrIGQ4JfcjFmdp4jWpkWA'
Consulta a GAPI utilizando el JWT obtenido
En el ejemplo se ha “recortado” el token que será
enviado a GAPI en la consulta por razones de espacio y
formato
Con la finalidad de aportar claridad en la construcción de consultas GAPI hay parámetros
obligatorios y parámetros opcionales. Los parámetros obligatorios se indican en esta guía en color
rojo y los opcionales en color azúl.
Versión 3.7 (Nov-2024) Desarrollada por Página 15 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Content-Type es la propiedad de cabecera (header) usada para indicar el media type del recurso.
Esta le dice al cliente que tipo de contenido se devuelve. En peticiones (tales como POST o PUT),
el cliente debe indicar al servidor que tipo de dato envía.
Para solicitudes HTTP POST/PUT, los encabezados Content-Type multipart/form-
data y aplication/x-www-form-urlencoded son dos: . El propósito de ambos es enviar una lista de pares de
clave/valor al servidor. Según el tipo y la cantidad de datos que se transmiten, uno de los métodos
será más eficiente que el otro.
aplication/x-www-form-urlencoded En , el cuerpo (body) del mensaje HTTP que se envía al servidor
es esencialmente una gran cadena de consulta: los pares de nombre/valor están separados por el
carácter ampersand (&), y los nombres están separados de los valores por el símbolo de igual (=).
Un ejemplo de esto sería:
VariableUno=ValorUno&VariableDos=ValorDos
Eso significa que por cada byte no alfanumérico que existe en uno de los valores, se necesitarán
tres bytes para representarlo.
En archivos binarios grandes, triplicar la carga útil sería muy ineficiente. Ahí es donde
interviene par se representa como una "parte" en un mensaje MIME. Las partes están separadas por un límite
de cadena particular (elegido específicamente para que esta cadena de límite no ocurra en ninguna
de las cargas útiles de "valor"). Cada parte tiene su propio conjunto de encabezados MIME
multipart/form-data . Con este método de transmisión de pares de nombre/valor, cada
como Content-Type y, en particular, Content-Disposition , que pueden dar a cada parte su
"nombre". La pieza de valor de cada par nombre/valor es la carga útil de cada parte del mensaje
MIME. La especificación MIME brinda así más opciones al representar el valor de la carga útil: lo
que permite elegir una codificación más eficiente de datos binarios para ahorrar ancho de banda
(por ejemplo, base 64 o incluso binario sin procesar).
Versión 3.7 (Nov-2024) Desarrollada por Página 16 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
¿Por qué no usar multipart/form-data todo el tiempo?
Para valores alfanuméricos cortos (como la petición de mover la vigencia de un certificado), la
sobrecarga de agregar todos los encabezados MIME superará significativamente cualquier ahorro
de una codificación binaria más eficiente.
En condiciones normales no se deberían recibir mensajes de error a menos que el token sea
manipulado y el servidor lo rechace, no obstante, a fin de ayudar en actividades de troubleshooting
seguidamente se indican los mensajes de error manejados por GAPI
▪ Algoritmo no permitido
▪ Algoritmo no soportado
▪ Algoritmo inválido
▪ Token expirado
▪ Llave incorrecta para este algoritmo
▪ Codificación de reclamaciones inválido
▪ Cabecera inválida
▪ Codificación de firma inválida
▪ Falló verificación de la firma
▪ Número de segmentos inválido
Las respuestas de GAPI tienen un formato común que se divide en dos secciones: records y
pagination.
{
"records": [
Versión 3.7 (Nov-2024) Desarrollada por Página 17 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
{
"id": 1,
"name": "Adelanto de fianzas",
"coverage": "USD10,000",
"description": "",
"status": 1
},
{
"id": 2,
"name": "Asistencia medica por accidente ",
"coverage": "USD 75.000",
"description": null,
"status": 1
},
{
...
}
],
"pagination": {
"total": 109,
"pages": 11,
"previous": false,
"next": true
}
}
Salida de una consulta GET de coberturas
La primera muestra un arreglo de registros con la información de la consulta, mientras que la
segunda, contiene metainformación de la respuesta. En esta sección se define pagination y en cada
servicio se detallará únicamente la información contenida en records.
• pagination.total: (entero) Cantidad de registros que contiene la consulta
• pagination.pages: (entero) Cantidad de páginas disponibles para consultar
• pagination.previous: (Lógico) Indica sí la consulta tiene página previa
• pagination.next: (Lógico) Indica sí la consulta tiene página siguiente
Con la finalidad de mejorar el rendimiento de las consultas y obtener solo la información que se
requiere GAPI implementa la paginación de resultados en las consultas.
Versión 3.7 (Nov-2024) Desarrollada por Página 18 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
De forma predeterminada, la página actual se detecta por el valor del argumento de cadena de
consulta page en la solicitud HTTP. Este valor es detectado automáticamente por GAPI y se inserta
en la metadata de pagination.
Por ejemplo, la consulta GET /api/benefit devuelve por defecto los primeros 10 registros de
coberturas de la primera página de resultados. Esto es así porque se ha establecido 10 registros
por página de forma predeterminada), es así entonces como la consulta se distribuye en 11 páginas
que totalizan 109 registros.
{
"records": [
{
"id": 1,
"name": "Adelanto de fianzas",
"coverage": "USD10,000",
"description": "",
"status": 1
},
{
...
},
{
"id": 10,
"name": "Garantia - Regreso en fecha diferente",
"coverage": "Costo Penalidad por cambio ",
"description": null,
"status": 1
},
],
"pagination": {
"total": 109,
"pages": 11,
"previous": false,
"next": true
}
}
Salida de una consulta GET de coberturas
(por razones de espacio se muestra solo los registros 1 y 10 de la primera página)
Existen argumentos que puede utilizar para navegar entre los resultados, como previous y next.
En el ejemplo, previous tiene la condición false debido a que la consulta predeterminada
devolvió la primera página y antes de ella no existe otra, sin embargo, next muestra la condición
true porque hay 11 páginas en total y la próxima página sería la página número 2.
Versión 3.7 (Nov-2024) Desarrollada por Página 19 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Conociendo los valores previous y next el usuario puede iterar el resultado de la consulta y
acceder a las páginas deseadas usando el estándar HTTP. De igual forma puede acceder de forma
directa a una página específica indicando el argumento page. Por ejemplo:
GET /api/benefit?page=2
{
"records": [
{
"id": 11,
"name": "Gastos de Desplazamiento Acompañante",
"coverage": "Boleto Aéreo ida/regreso",
"status": 1,
"description": null
},
{
"id": 12,
"name": "Gastos de Estadía Acompañante",
"coverage": "USD 1.000 (USD 100 por día)",
"status": 1,
"description": null
},
{
"id": 13,
"name": "Gastos de Hotel por Convalecencia",
"coverage": "USD 1.000 (USD 100 x día)",
"status": 1,
"description": null
},
{
...
},
{
"id": 20,
"name": "Medicamentos por Hospitalización",
"coverage": "Incluido en el Límite",
"status": 1,
"description": null
}
],
"pagination": {
"total": 139,
"pages": 14,
"previous": true,
"next": true
}
}
Salida de la consulta GET /api/benefit?page=2
(por razones de espacio se muestra solo los registros 11, 12, 13 y 20 de la segunda página)
Versión 3.7 (Nov-2024) Desarrollada por Página 20 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Existe otro argumento que permite redefinir la cantidad de registros que se desea obtener por
página de resultados, este es step. Como se observa en la imagen, el número de páginas aumenta
debido a que solo se piden 2 registros por página. Este argumento puede combinarse con page
para hacer más precisa la consulta.
GET /api/benefit?page=2&step=2
{
"records": [
{
"id": 3,
"name": "Asistencia Médica por Enfermedad ",
"coverage": "USD 15.000",
"status": 1,
"description": null
},
{
"id": 4,
"name": "Asistencia Mundial las 24 Horas",
"coverage": "Incluida",
"status": 1,
"description": null
}
]
"pagination": {
"total": 139,
"pages": 70,
"previous": true,
"next": true
}
}
Salida de la consulta GET /api/benefit?page=2&step=2
Versión 3.7 (Nov-2024) Desarrollada por Página 21 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Todos los métodos de consulta admiten “parámetros aceptados”, estos permiten el filtrado de la
consulta bajo los criterios indicados por el usuario, por ejemplo:
La consulta GET /api/benefit?id=1 devuelve la cobertura cuyo id es 1. Nótese que el control
de paginación muestra un total de 1 registro, 1 página y las propiedades previous y next son
falsas en ambos casos porque no hay más páginas que mostrar.
{
"records": [
{
"id": 1,
"name": "Adelanto de fianzas",
"coverage": "USD10,000",
"description": "",
"status": 1
},
],
"pagination": {
"total": 1,
"pages": 1,
"previous": false,
"next": false
}
}
Salida de la consulta de un registro específico usando GET /api/benefit?id=1
La consulta anterior también puede ser realizada de esta manera /api/benefit/1. La diferencia
de esta forma contra el primer ejemplo es que, mientras el primero devuelve una consulta
paginada, este devuelve la consulta sin paginación porque se indica claramente que solo es un
registro el que se mostrará (el 1 en este caso es el id del registro) .
{
"records": [
{
"id": 1,
"name": "Adelanto de fianzas",
"coverage": "USD10,000",
Versión 3.7 (Nov-2024) Desarrollada por Página 22 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
"description": "",
"status": 1
},
],
}
Salida de la consulta de un registro específico usando GET /api/benefit/1
Otro ejemplo de filtrado aplicando “parámetros aceptados” es la consulta usando una cadena de
búsqueda. Por ejemplo:
GET /api/benefit?name=MEDICA.
Devuelve todas las coberturas donde la palabra “MEDICA” aparece en el nombre, de manera
parcial o total, sin distinguir mayúsculas de minúsculas ni tomar en cuenta que comiencen o
terminen por dicha palabra.
Nótese que el control de paginación muestra un total de 14 registros, 2 página y la propiedad
previous es falsa mientras que next es verdadera porque hay una página más que mostrar.
{
"records": [
{
"id": 2,
"name": "Asistencia medica por accidente ",
"coverage": "USD 75.000",
"description": null,
"status": 1
},
{
"id": 3,
"name": "Asistencia medica por enfermedad ",
"coverage": "USD 15.000",
"description": null,
"status": 1
},
{
"id": 14,
"name": "Gastos de Medicamentos Ambulatorios",
"coverage": "Incluidos en el limite",
"description": null,
"status": 1
},
{
"id": 20,
Versión 3.7 (Nov-2024) Desarrollada por Página 23 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
"name": "Medicamentos por hospitalizacion",
"coverage": "Incluido en el limite",
"description": null,
"status": 1
},
{
"id": 29,
"name": "Asistencia Medica Telefonica 24 Horas",
"coverage": "Incluida",
"description": null,
"status": 1
},
{
"id": 32,
"name": "Visita Médica en centros vacacionales y/o Hoteles",
"coverage": "Incluido",
"description": null,
"status": 1
},
{
"id": 40,
"name": "ASISTENCIA MEDICA ",
"coverage": "LIMITES Y CONDICIONES",
"description": null,
"status": 0
},
{
"id": 47,
"name": "Medical Expenses coverage",
"coverage": "USD15,000",
"description": null,
"status": 1
},
{
"id": 51,
"name": "Emergency medical transportation",
"coverage": "Included",
"description": null,
"status": 1
}
],
"pagination": {
"total": 14,
"pages": 2,
"previous": false,
"next": true
}
}
Es importante destacar que el filtrado solo admite “parámetros aceptados”
, esos campos
implementan lo que se conoce como full Index y aplicarlos a otros tipos de campo tendría un
impacto significativo sobre el rendimiento de la consulta y la estabilidad del servicio.
Versión 3.7 (Nov-2024) Desarrollada por Página 24 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Para aligerar el rendimiento de las consultas y disminuir el volumen de datos transferidos, GAPI
implementa una interpretación simplificada de , lenguaje de consulta que brinda una
descripción completa y comprensible de los datos en la API, con este modelo otorga a los clientes
el poder de solicitar exactamente lo que necesitan y nada más, facilitando así la evolución de la API
con el tiempo, mientras habilita herramientas poderosas para los equipos de desarrollo.
Las consultas acceden no solo a las propiedades de un recurso, además siguen sin problemas las
referencias entre ellos. Mientras que una API REST típica requiere la carga desde varias URL, GAPI
obtiene todos los datos que su aplicación puede necesitar con una sola solicitud, brindando
rapidez, incluso en conexiones de red móvil lentas.
Las premisas que definen las consultas tienen como base el formato de la petición así:
• El atributo w define la consulta.
• Para filtrar columnas basta indicar su nombre. Ejemplo:
?w=col1,col2
• Las relaciones se agregan usando un formato recursivo. Ejemplo:
?w=relation{}
(Dentro de las llaves se puede definir como se comportará la relación)
• Al filtra columnas, la relación principal debe incluir el primary key de la tabla. Ejemplo:
?w=pk,col1,rel1{},rel2{}
Ejemplo recursivo
?w=rel1{w=rel1PK,col1,colN,rel2{}}
Ejemplo con query string recursivo
?foo=bar&w=rel1{key=value;w=col1,colN}
Versión 3.7 (Nov-2024) Desarrollada por Página 25 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
En aquellos casos que una relación interna necesite filtrar su contenido a través
del querystring, por limitaciones del RFC 1738 no podrá usar ampersand (&), por
ser este un carácter reservado. Para saltar estas limitaciones se debe usar punto
y coma (;) como reemplazo así:
?foo=bar&w=col1,col2,rel1{status=A;q=value;w=id,name}&q=criteria
En el siguiente ejemplo GAPI devuelve solo las columnas id y name en la consulta:
GET /api/benefit?w=id,name
{
"records": [
{
"id": 1,
"name": "Adelanto de fianzas"
},
{
"id": 2,
"name": "Asistencia medica por accidente "
},
{
"id": 3,
"name": "Asistencia medica por enfermedad "
},
{
"id": 4,
"name": "Asistencia mundial las 24 hs."
},
{
"id": 5,
"name": "Cancelación de viaje hasta edad 75 Años"
},
{
"id": 6,
"name": "Cobertura en Cruceros"
},
{
"id": 7,
"name": "Asistencia medica enfermedad o Accidente "
},
{
"id": 8,
"name": "Compensación por demora de equipaje"
},
{
"id": 9,
"name": "Compensacion perdida equipaje"
},
{
"id": 10,
Versión 3.7 (Nov-2024) Desarrollada por Página 26 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
"name": "Garantia - Regreso en fecha diferente"
}
],
"pagination": {
"total": 109,
"pages": 11,
"previous": false,
"next": true
}
}
Como se puede observar el parámetro w actúa como filtro de columnas y éstas pueden
especificarse separadas por coma.
Versión 3.7 (Nov-2024) Desarrollada por Página 27 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
En algunas circunstancias puede ser de utilidad incorporar a la consulta las relaciones que una tabla
tiene con otra. Por ejemplo, la consulta de productos que se muestra en la imagen de la página
siguiente, permite agregar el atributo data{} el cual contiene propiedades adicionales de los
productos.
En ese ejemplo, el parámetro w sirve para introducir el atributo data{}. No se debe olvidar incluir
las llaves como sufijo, ya que de lo contrario se asumiría un campo de nombre data en lugar del
atributo data{}.
Es importante tener presente que no hay forma de consultar de manera directa únicamente el
atributo data{} ya que esta información solo existe relacionada a un producto en particular. En
este caso, dichos valores proceden de una tabla clave->valor que incorpora informaciones
extendidas sobre los productos.
Se debe tener precaución al utilizar propiedades
basadas en data{}, estas informaciones son variables y
pueden romper su consulta en caso de cambios. Para más
detalles consulte a su ejecutivo de cuenta
Versión 3.7 (Nov-2024) Desarrollada por Página 28 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/product?w=data{}
{
"records": [
{
"id": 1,
"internal_code": "019",
"name": "LARIMAR",
"description": "PRODUCTO DE ASSISTENCIA LOCAL, CON COBERTURA NACIONAL",
"status": 1,
"created_at": "2022-01-01 06:00:00",
"updated_at": "2022-01-08 06:00:05",
"deleted_at": null,
"data": {
"cancellation": 0,
"certificate_email": {
"mode": "available",
"value": "api.ticket.pdf.client.672261"
},
"covid": 0,
"embassy": 0,
"exempt": 0,
"local": 1,
"nfree": 0,
"operation_commission": 0,
"optional": 0,
"physical": 0,
"prepaid": 0,
"start_from": 1,
"suggested_agency_commission": 0
}
},
{
...
}
]
}
De la misma manera como es posible filtrar columnas en una consulta, también es posible hacerlo
en una relación utilizando la misma técnica. Por ejemplo:
GET /api/product?w=data{w=cancellation}
Esta devolvería una consulta de productos anidada con el atributo data{} que incluye solo la
columna cancellation.
{
"records": [
{
"id": 1,
"internal_code": "019",
"name": "LARIMAR",
Versión 3.7 (Nov-2024) Desarrollada por Página 29 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
"description": "PRODUCTO DE ASSISTENCIA LOCAL, CON COBERTURA NACIONAL",
"status": 1,
"created_at": "2022-01-01 06:00:00",
"updated_at": "2022-01-08 06:00:05",
"deleted_at": null,
"data": {
"cancellation": 0
}
},
{
...
}
]
}
En este ejemplo se puede observar que el parámetro w se incluye dos veces, la primera vez para
introducir el atributo data{} y la segunda dentro de las llaves, para indicar que de dicho atributo
solo incluya la columna cancellation. Si se requirieran más columnas solo habría que separarlas
con comas.
Otros atributos están disponibles para su uso en la consulta, estos se detallan más adelante y son:
• values{}
• addresses{}
GAPI es sumamente versátil al permitir todos los elementos indicados en una consulta estándar
HTTP. Es posible hacer una consulta anidada, aplicando en adición filtros específicos, por ejemplo,
la siguiente consulta obtiene todos los productos de precompra incluyendo sus propiedades:
Versión 3.7 (Nov-2024) Desarrollada por Página 30 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/product?w=data{}&prepaid=1
{
"records": [
{
"id": "71",
"internal_code": "71",
"name": "PLAN ZAFIRO",
"description": null,
"status": "0",
"created_at": "2022-01-01 06:00:00",
"updated_at": "2022-01-08 06:00:05",
"deleted_at": null,
"data": {
"cancellation": 0,
"certificate_email": {
"mode": "default"
},
"covid": 0,
"embassy": 1,
"exempt": 1,
"local": 0,
"nfree": 0,
"operation_commission": 0,
"optional": 0,
"physical": 0,
"prepaid": 1,
"start_from": 1,
"suggested_agency_commission": 0
}
}
],
"pagination": {
"total": 1,
"pages": 1,
"previous": false,
"next": false
}
}
Versión 3.7 (Nov-2024) Desarrollada por Página 31 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
En el ejemplo anterior destacamos las propiedades del atributo data{} en una consulta de
productos, estas responden, como se dijo antes, a un modelo clave->valor.
Se debe tener precaución al utilizar propiedades
basadas en data{}, estas informaciones son variables y
pueden romper su consulta en caso de cambios. Para más
detalles consulte a su ejecutivo de cuenta
cancellation entero Indica si el producto es (1) o no (0) un
complemento de cancelación de viaje
certificate_email arreglo Indica el (los) certificado (s) que está (n)
asociado (s) al producto
covid entero Indica si el producto es (1) o no (0) un
complemento de COVID
covid.sample entero Especifica el número máximo de días desde
la realización de la prueba de COVID.
covid.result entero Define el número máximo de días desde que
se obtuvo el resultado de la prueba de
COVID.
embassy entero Indica si el producto es (1) o no (0) tiene un
certificado particular para consulados
(actualmente no habilitado)
Versión 3.7 (Nov-2024) Desarrollada por Página 32 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
exempt entero Indica si el producto está exento de
impuesto (1) o no (0) en la venta. Si la
operación no tiene impuesto el parámetro
no se utiliza.
local entero Indica si el producto es (1) o no (0) de venta
local (nacional)
nfree entero Indica si el producto aplica (1) para el
beneficio niños gratis o no (0)
operation_commission decimal Indica un porcentaje adicional que se aplica a
la operación por la venta del producto
optional entero Indica si el producto es BASE (0) o
COMPLEMENTARIO (1)
physical entero Indica si el producto aplica (1) o no (0) para el
beneficio complementario de perdida de
equipos electrónicos
prepaid entero Indica si el producto se utiliza para la venta
de seguros RETAIL (0) o de PRECOMPRA DE DÍAS
(1)
start_from fecha Indica desde que fecha está habilitado el
producto para su comercialización.
suggested_agency_commission decimal Indica la comisión sugerida que el producto
puede ofrecer a los productores o agencias.
certificate_email arreglo Indica el (los) certificado (s) que está (n)
asociado (s) al producto
PAID MODE Byte Indica el modo y medio de pago utilizado
para pagar la factura asociada a un
certificado.
TICKET_KIND entero Indica si el certificado vendido fue de venta
RETAIL (0) o por PRECOMPRA DE DÍAS (1)
Versión 3.7 (Nov-2024) Desarrollada por Página 33 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
VERSION entero Indica el número de versión del certificado
emitido.
agency_type entero Indica si el productor es (1) agencia o (2)
corredor
commission entero Indica la comisión global que aplica al
productor. Tenga presente que este valor
solo está presente si no se define la comisión
a nivel del producto de manera particular.
electronic entero Indica si el productor tiene (1) o (0) no, pago
con medios electrónicos habilitado.
invoice_mode entero Indica si el productor tiene (1) facturación
automática definida o (0) no.
limit entero Limite de la línea de crédito asignada al
productor.
ncf_default entero Tipo de Comprobante Fiscal
predeterminado. (1=Crédito Fiscal),
(2=Consumidor Final), (8=Regímenes
Especiales) y (9=Institución Gubernamental)
Al igual que el atributo data{}, GAPI ofrece un atributo que permite obtener todos los valores
relacionados con un certificado, este es el atributo values{}.
Versión 3.7 (Nov-2024) Desarrollada por Página 34 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Se debe tener precaución al utilizar propiedades
basadas en values{}, estas informaciones son variables
y pueden romper su consulta en caso de cambios. Para más
detalles consulte a su ejecutivo de cuenta
ticket arreglo Información de valores relacionados con el
certificado
amount decimal Monto del certificado o prima
discount decimal Monto del descuento aplicado al certificado
tax decimal Monto del impuesto aplicado al certificado
total decimal Monto total facturado por concepto de
prima. Este valor es igual a la suma de las
columnas: amount + discount + tax
GET /api/ticket?ticket_id=71&w=data{}&ticket_id=07056032
{
"records": [
{
"ticket_id": "07056032",
"date": "2022-01-05 15:43:16",
"agency_id": "00318",
"cancel": null,
"salesman_id": "001-0090290-1",
"days": "14",
"destiny_id": "840",
"from": "2022-01-15",
"insured_count": "1",
"to": "2022-01-29",
“values”: {
“ticket”: {
“amount": 113,
"discount": 0,
"tax": 0,
Versión 3.7 (Nov-2024) Desarrollada por Página 35 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
"total": 113
}
}
}
],
"pagination": {
"total": 1,
"pages": 1,
"previous": false,
"next": false
}
}
GAPI ofrece otro atributo que permite obtener las direcciones relacionadas con un certificado
emitido, este es el atributo addresses{}.
Aunque un certificado admite más de una dirección, las
direcciones están relacionados con el certificado y no
con los asegurados.
Tenga precaución al utilizar propiedades basadas en
addresses{}, estas informaciones son variables y pueden
romper su consulta en caso de cambios. Para más detalles
consulte a su ejecutivo de cuenta
Algo a considerar al utilizar este atributo es que solo una dirección es obligatoria al emitir un
certificado y que la propiedad kind admite cualquier etiqueta, en tal sentido pudiera definirse
como emergencia, oficina, etc.
Versión 3.7 (Nov-2024) Desarrollada por Página 36 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Para obtener solo las direcciones de correo electrónico asociadas a un certificado la consulta sería
así:
addresses arreglo Información de direcciones relacionadas con el
certificado
line1 Alfanumérico Primera línea de la dirección
line2 Alfanumérico Segunda línea de la dirección
city Alfanumérico Ciudad de la dirección
state Alfanumérico Estado de la dirección
country Alfanumérico País de la dirección
zip Alfanumérico Código postal de la dirección
phone arreglo Información de teléfonos relacionadas con la dirección
element 0 Alfanumérico Teléfono asociado a la dirección
Email arreglo Información de correos electrónicos relacionadas con
la dirección
element 0 Alfanumérico Dirección de correo electrónico asociado a la dirección
GET /api/ticket/00000002?w=addresses{}
{
"ticket_id": "00000002",
"date": "2021-10-01 00:00:01",
"cancel": null,
"agency_id": "12707",
"salesman_id": "999-7778017-7",
"days": "6",
"terms": null,
"tpainfo": null,
"coordinator_id": null,
"coordinator_commission": 0,
"destiny_id": "484",
"from": "2021-10-04",
"insured_count": "1",
"invoice_id": null,
"salesman_commission": 0,
"to": "2021-10-09",
"addresses": [
{
"line1": "SANTO DOMINGO",
"line2": "SANTO DOMINGO",
Versión 3.7 (Nov-2024) Desarrollada por Página 37 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
"city": "SANTO DOMINGO",
"state": "",
"country": "REPÚBLICA DOMINICANA",
"zip": "",
"id": "101",
"kind": "Por defecto",
"ticket_id": "00000002",
"phone": [
"809-326-0239"
],
"email": [
"elsie.guzman@micorreo.com.do"
]
},
{
"line1": "SANTO DOMINGO",
"line2": "",
"city": "SANTO DOMINGO",
"state": "",
"country": "REPÚBLICA DOMINICANA",
"zip": "",
"id": "102",
"kind": "Emergencia",
"ticket_id": "00000002",
"phone": [
"849-906-0531"
],
"email": [
"elsie.guzman@micorreo.com.do"
]
}
]
}
La siguiente consulta permitiría obtener solo las direcciones de correo electrónico relacionadas
con el certificado:
GET /api/ticket/00000002?w=addresses{w=email}
{
"ticket_id": "00000002",
"date": "2021-10-01 00:00:01",
"cancel": null,
"agency_id": "12707",
"salesman_id": "999-7778017-7",
"days": "6",
"terms": null,
"tpainfo": null,
"coordinator_id": null,
"coordinator_commission": 0,
"destiny_id": "484",
"from": "2021-10-04",
"insured_count": "1",
"invoice_id": null,
"salesman_commission": 0,
"to": "2021-10-09",
Versión 3.7 (Nov-2024) Desarrollada por Página 38 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
"addresses": [
{
"email": [
"elsie.guzman@micorreo.com.do"
]
},
{
"email": [
"elsie.guzman@micorreo.com.do"
]
}
]
}
Versión 3.7 (Nov-2024) Desarrollada por Página 39 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Con la finalidad de que el equipo de desarrollo conozca más sobre la forma en que los datos están
estructurados en GOVAL-Web, a continuación, se muestra el diagrama de estructura de datos
(DSD) que maneja GAPI, en este, los nombres de los métodos actúan como nombre de la entidad
referenciada.
Versión 3.7 (Nov-2024) Desarrollada por Página 40 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Consultas
Versión 3.7 (Nov-2024) Desarrollada por Página 41 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/benefit
Parámetros aceptados:
id entero Código de la cobertura
name alfanumérico Nombre de la cobertura
Respuesta:
Por cada elemento de records, se incluye:
id entero Código de la relación producto/cobertura
name alfanumérico Nombre de la cobertura
coverage alfanumérico Etiqueta / valor de la cobertura incluida
status entero Estado de la cobertura (1) activo (0) inactivo
description alfanumérico Descripción de la cobertura
Ejemplo
{
"records": [
{
"id": 1,
"name": "Adelanto de Fianzas",
"coverage": "USD 10.000",
"status": 1,
"description": null
},
{
"id": 2,
"name": "Asistencia Médica por Accidente ",
"coverage": "USD 75.000",
"status": 1,
"description": null
},
{
...
},
{
Versión 3.7 (Nov-2024) Desarrollada por Página 42 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
"id": 10,
"name": "Garantía - Regreso en Fecha Diferente",
"coverage": "Costo Penalidad por Cambio ",
"status": 1,
"description": null
}
],
"pagination": {
"total": 139,
"pages": 14,
"previous": false,
"next": true
}
}
Versión 3.7 (Nov-2024) Desarrollada por Página 43 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/benefit/id
Parámetros aceptados:
id entero Código de la cobertura
Respuesta:
La respuesta bajo este modelo no es paginada
id entero Código de la cobertura
name alfanumérico Nombre de la cobertura
coverage alfanumérico Etiqueta / valor de la cobertura incluida
description alfanumérico Descripción de la cobertura
status entero Estado de la cobertura (1) activo (0) inactivo
Ejemplo
{
"id": 1,
"name": "Adelanto de Fianzas",
"coverage": "USD 10.000",
"status": 1,
"description": null
}
Versión 3.7 (Nov-2024) Desarrollada por Página 44 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/product
Parámetros aceptados:
id entero Identificador del producto
internal_code alfanumérico Identificador alterno del producto (cliente)
name alfanumérico Nombre del producto
status lógico Valor activo (1) / inactivo (0) para la operación
Respuesta:
Por cada elemento de records, se incluye:
id entero Identificador del producto
internal_code alfanumérico Identificador alterno del producto (cliente)
name alfanumérico Nombre del producto
status entero Estado de la cobertura (1) activo (0) inactivo
created_at fecha/hora Meta data de fecha y hora en que el
producto fue creado
updated_at fecha/hora Meta data de fecha y hora en que el
producto fue actualizado por última vez
deleted_at fecha/hora Meta data de fecha y hora en que el
producto fue eliminado. Esta es una
eliminación lógica y no puede ser revertida.
description alfanumérico Descripción del producto
Versión 3.7 (Nov-2024) Desarrollada por Página 45 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Ejemplo
{
"records": [
{
"id": 2,
"internal_code": "501",
"name": "CANCELACIÓN BÁSICA ",
"status": 0,
"created_at": "2021-10-27 17:00:00",
"updated_at": "2023-03-15 08:49:24",
"deleted_at": null,
"description": "SERIE 2021-2022\nCANCELACIÓN BÁSICA "
},
{
"id": 3,
"internal_code": "90064",
"name": "EQUIPAJE ADICIONAL COMPLEMENTARIO",
"status": 0,
"created_at": "2021-10-27 17:00:00",
"updated_at": "2021-12-10 08:42:13",
"deleted_at": null,
"description": "SERIE 2021-2022\nEQUIPAJE ADICIONAL COMPLEMENTARIO"
},
{
"id": 5,
"internal_code": "136",
"name": "PRODUCTO 250 (ANUAL 45)",
"status": 1,
"created_at": "2021-10-27 17:00:00",
"updated_at": "2021-12-25 12:20:40",
"deleted_at": null,
"description": "SERIE 2021-2022\nPLAN F\n15,000"
},
],
"pagination": {
"total": 19,
"pages": 2,
"previous": false,
"next": true
}
}
(Por razones de espacio no se muestran todos los registros de la consulta)
Versión 3.7 (Nov-2024) Desarrollada por Página 46 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/product/id
Parámetros aceptados:
id entero Identificador del producto
internal_code alfanumérico Identificador alterno del producto (cliente)
name alfanumérico Nombre del producto
status lógico Valor activo (1) / inactivo (0) para la operación
Respuesta:
Por cada elemento de records, se incluye:
id entero Identificador del producto
internal_code alfanumérico Identificador alterno del producto (cliente)
name alfanumérico Nombre del producto
status entero Estado de la cobertura (1) activo (0) inactivo
created_at fecha/hora Meta data de fecha y hora en que el
producto fue creado
updated_at fecha/hora Meta data de fecha y hora en que el
producto fue actualizado por última vez
deleted_at fecha/hora Meta data de fecha y hora en que el
producto fue eliminado. Esta es una
eliminación lógica y no puede ser revertida.
description alfanumérico Descripción del producto
Ejemplo
{
"id": 3,
"internal_code": "90064",
"name": "EQUIPAJE ADICIONAL COMPLEMENTARIO",
"status": 0,
Versión 3.7 (Nov-2024) Desarrollada por Página 47 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
"created_at": "2021-10-27 17:00:00",
"updated_at": "2021-12-10 08:42:13",
"deleted_at": null,
"description": "SERIE 2021-2022\nEQUIPAJE ADICIONAL COMPLEMENTARIO"
}
Versión 3.7 (Nov-2024) Desarrollada por Página 48 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/product/product_id?w=id,name,benefits{w=benefit_id,coverage}
En el ejemplo se filtra la salida para obtener solo las propiedades id y name del
producto, así como las coberturas asociadas. En esta última propiedad se filtra
las propiedades benefit_id y coverage.
Parámetros aceptados:
product_id alfanumérico Código del producto
Respuesta:
Por cada elemento de records, se incluye:
id entero Identificador del producto
internal_code alfanumérico Identificador interno del producto
name alfanumérico Nombre del producto
description alfanumérico Descripción del producto
status entero Estado de la cobertura (1) activo (0) inactivo
created_at fecha/hora Meta data de fecha y hora en que el
producto fue creado
updated_at fecha/hora Meta data de fecha y hora en que el
producto fue actualizado por última vez
deleted_at fecha/hora Meta data de fecha y hora en que el
producto fue eliminado. Esta es una
eliminación lógica y no puede ser revertida.
benefits arreglo Coberturas asociadas al producto. Para
detalles de los elementos vea Consulta de
coberturas
Versión 3.7 (Nov-2024) Desarrollada por Página 49 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Ejemplo
{
"id": 5,
"name": " PRODUCTO 250 (ANUAL 45)",
"benefits": [
{
"id": 35,
"benefit_id": 7,
"coverage": "USD 60.000 "
},
{
"id": 47,
"benefit_id": 20,
"coverage": "Incluido en Límite Asistencia Médica"
},
{
...
},
{
"id": 66,
"benefit_id": 116,
"coverage": "Incluido en Límite De Gastos Médicos"
}
]
}
(Por razones de espacio no se muestran todos los registros de la consulta)
Versión 3.7 (Nov-2024) Desarrollada por Página 50 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/country
Parámetros aceptados:
id entero Identificador ISO 3166-1 del país
name alfanumérico Nombre del país
status entero Valor activo/inactivo para el destino
Respuesta:
Por cada elemento de records, se incluye:
id entero Identificador ISO 3166-1 del país
name alfanumérico Nombre del país
status entero Estado (1) activo (0) inactivo del destino
iso_31662 alfanumérico Identificador ISO 3166-2 de dos posiciones
del país
iso_31663 alfanumérico Identificador ISO 3166-3 de tres posiciones
del país
Versión 3.7 (Nov-2024) Desarrollada por Página 51 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Ejemplo
{
"records": [
{
"name": "ALBANIA",
"status": 1,
"id": 8,
"iso_31662": "AL",
"iso_31663": "ALB"
},
{
"name": "ANTÁRTIDA",
"status": 1,
"id": 10,
"iso_31662": "AQ",
"iso_31663": "ATA"
},
{
"name": "ARGELIA",
"status": 1,
"id": 12,
"iso_31662": "DZ",
"iso_31663": "DZA"
},
{
...
},
{
"name": "ARGENTINA",
"status": 1,
"id": 32,
"iso_31662": "AR",
"iso_31663": "ARG"
},
{
"name": "AUSTRALIA",
"status": 1,
"id": 36,
"iso_31662": "AU",
"iso_31663": "AUS"
}
],
"pagination": {
"total": 243,
"pages": 25,
"previous": false,
"next": true
}
}
(por razones de espacio se muestra solo algunos registros)
Versión 3.7 (Nov-2024) Desarrollada por Página 52 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/region
Parámetros aceptados:
id entero Identificador de la región
name alfanumérico Nombre del país
status entero Valor activo/inactivo para el destino
Respuesta:
Por cada elemento de records, se incluye:
id entero Identificador de la región
parent_id entero Identificador de la región padre
name alfanumérico Nombre de la región
status entero Estado (1) activo (0) inactivo de la región
deleted_at fecha/hora Meta data de fecha y hora en que la región
fue eliminada. Esta es una eliminación lógica
y no puede ser revertida.
Versión 3.7 (Nov-2024) Desarrollada por Página 53 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Ejemplo
{
"records": [
{
"id": 1,
"parent_id": null,
"name": "Global",
"status": 1,
"deleted_at": null
},
{
"id": 2,
"parent_id": 1,
"name": "COMERCIAL",
"status": 1,
"deleted_at": null
},
{
"id": 3,
"parent_id": 2,
"name": "OFICINA PRINCIPAL",
"status": 1,
"deleted_at": null
},
{
"id": 4,
"parent_id": 3,
"name": "CORREDORES OFICINA PRINCIPAL",
"status": 1,
"deleted_at": null
},
{
"id": 5,
"parent_id": 3,
"name": "AGENTES OFICINA PRINCIPAL",
"status": 1,
"deleted_at": null
},
],
"pagination": {
"total": 14,
"pages": 2,
"previous": false,
"next": true
}
}
(por razones de espacio se muestra solo algunos registros)
Versión 3.7 (Nov-2024) Desarrollada por Página 54 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/addresses
Parámetros aceptados:
id entero Identificador ISO 3166-1 del país
name alfanumérico Nombre del país
status entero Valor activo/inactivo para el destino
Respuesta:
Por cada elemento de records, se incluye:
id entero Identificador de la dirección
source alfanumérico Entidad referencia de la dirección: “Agencia”
o “Usuario”
source_id entero Identificador en la entidad referenciada
name alfanumérico Nombre de la dirección
line1 alfanumérico Primera línea de dirección
line2 alfanumérico Segunda línea de dirección
city alfanumérico Ciudad asociada a la dirección
state alfanumérico Estado o provincia asociada a la dirección
country_id entero Identificador ISO 3166-1 del país
zip alfanumérico Código postal de la dirección
Ejemplo
{
"records": [
{
"id": 1,
"source_id": 1,
"name": "Default",
"line1": "Av Winston Churchill #25",
"line2": "Ens. Piantini",
Versión 3.7 (Nov-2024) Desarrollada por Página 55 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
"city": "Santo Domingo",
"state": "DN",
"country_id": 214,
"zip": 11126l,
"source": "Agencia"
},
{
"id": 2,
"source_id": 2,
"name": "Default",
"line1": "Santo Domingo, Rep. Dom.",
"line2": "Santo Domingo de Guzman",
"city": "",
"state": "",
"country_id": 214,
"zip": null,
"source": "Agencia"
}
],
"pagination": {
"total": 2495,
"pages": 1248,
"previous": false,
"next": true
}
}
(por razones de espacio se muestra solo algunos registros)
Versión 3.7 (Nov-2024) Desarrollada por Página 56 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/users
Parámetros aceptados:
id entero id del usuario
firstname alfanumérico Nombres del vendedor
lastname entero Apellidos del vendedor
Respuesta:
Por cada elemento de records, se incluye:
id entero Id del usuario
internal_code alfanumérico Código del usuario (a nivel del cliente)
profile_id entero Id del usuario
firstname alfanumérico Nombres del usuario
lastname alfanumérico Apellidos del usuario
login alfanumérico Cuenta del usuario en el sistema
email alfanumérico Dirección de correo electrónico asociada
al usuario
from Fecha Inicio de vigencia de la cuenta del usuario
to Fecha Fin de vigencia de la cuenta del usuario
status entero Estado (1) activo (0) inactivo de la región
Ejemplo
{
"records": [
{
"id": 1,
"internal_code": "1",
"profile_id": 1,
"firstname": "GOVAL",
"lastname": "WSCLIENT",
Versión 3.7 (Nov-2024) Desarrollada por Página 57 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
"login": "abcdef",
"email": "abcdef@wxyz.com",
"from": null,
"to": null,
"status": 0,
"description": null,
},
{
"id": 2,
"internal_code": "2",
"profile_id": 1,
"firstname": "",
"lastname": "GOVAL 2DA LINEA",
"login": "ghlkgghh",
"email": "aaaaaa@wxyz.do",
"from": null,
"to": null,
"status": 1,
"description": null,
},
{
"id": 3,
"internal_code": "3",
"profile_id": 1,
"firstname": "",
"lastname": "GOVAL 1RA LINEA",
"login": "ssresr",
"email": "bbbbbbb@wxyz.do",
"from": "2023-05-01",
"to": null,
"status": 1,
"description": null,
},
],
"pagination": {
"total": 113,
"pages": 12,
"previous": false,
"next": true
}
}
(por razones de espacio se muestra solo algunos registros)
Las propiedades que se indican a continuación solo pueden obtenerse agregando el atributo
profile{} a la consulta:
GET /api/agency?w=profile{}
id entero Id del perfil asociado al usuario
name alfanumérico Nombre del perfil del usuario
from Fecha Inicio de vigencia del perfil del usuario
Versión 3.7 (Nov-2024) Desarrollada por Página 58 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
to Fecha Fin de vigencia del perfil del usuario
work_days alfanumérico Días de la semana permitidos para el
acceso del usuario
status entero Estado (1) activo (0) inactivo del perfil del
usuario
created_at Fecha/hora Meta data de fecha y hora en que el perfil
fue creado
updated_at Fecha/hora Meta data de fecha y hora en que el perfil
fue actualizado
Ejemplo
{
"records": [
{
"id": 1,
"internal_code": "1",
"profile_id": 1,
"firstname": "GOVAL",
"lastname": "WSCLIENT",
"login": "abcdef",
"email": "abcdef@wxyz.com",
"from": null,
"to": null,
"status": 0,
"description": null,
"profile": {
"id": 1,
"name": "Admin",
"from": null,
"to": null,
"work_days": null,
"status": 1,
"created_at": "2022-06-08 13:25:26",
"updated_at": "2022-06-08 13:25:26",
"description": null
}
},
{
...
},
],
"pagination": {
"total": 113,
"pages": 12,
"previous": false,
"next": true
}
}
(por razones de espacio se muestra solo algunos registros)
Versión 3.7 (Nov-2024) Desarrollada por Página 59 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/agency
Parámetros aceptados:
id entero Identificador del productor
name alfanumérico Nombre del productor
region_id entero Identificador de la región a la que pertenece el
productor
internal_code alfanumérico Código del productor (a nivel del cliente)
legal_id alfanumérico Identificador fiscal (RNC, RIF, RUC, etc.) asociado al
productor.
status entero Estado del productor (1) activo (0) inactivo
Respuesta:
Por cada elemento de records, se incluye:
id alfanumérico Identificador del productor
region_id entero Id de la región a la que pertenece el
productor
internal_code Código del productor (a nivel del cliente)
legal_id alfanumérico Identificador fiscal (RNC, RIF, RUC, etc.)
asociado al productor.
name alfanumérico Nombre del productor
legal_name alfanumérico Nombre comercial del productor
status entero Estado del productor (1) activo (0) inactivo
created_at fecha/hora Meta data de fecha y hora en que el
productor fue creado
updated_at fecha/hora Meta data de fecha y hora en que el
productor fue actualizado por última vez
Versión 3.7 (Nov-2024) Desarrollada por Página 60 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
deleted_at fecha/hora Meta data de fecha y hora en que el
productor fue inactivado. Esta es una
eliminación lógica y no puede ser revertida.
Las propiedades que se indican a continuación solo pueden obtenerse agregando el atributo data{}
a la consulta.:
GET /api/agency?w=data{}
address_default entero Id de la dirección predeterminada del
productor
commission decimal Comisión global asignada al productor por la
venta de certificados.
default_ncf entero Tipo de comprobante fiscal predeterminado
que usa el productor. (ver códigos de tipos
de NCF)
discount_max decimal Descuento máximo que puede aplicar el
productor a la venta de certificados
electronic lógico Indica si el productor está habilitado para
pagar con medios electrónicos
invoice_auto lógico Indica si el productor genera una factura con
cada emisión de póliza
invoice_mode alfanumérico Indica si el tipo de factura que genera el
productor, Valor predeterminado default
limit entero Límite de crédito en dólares asignado al
productor
Ejemplo
{
"records": [
{
"id": 1,
"region_id": 3,
"internal_code": "05621",
"legal_id": "1",
"name": "SOPORTE COMERCIAL",
"legal_name": "SOPORTE COMERCIAL",
"status": 0,
"created_at": "2021-04-27 11:25:30",
"updated_at": "2021-04-27 11:25:30",
Versión 3.7 (Nov-2024) Desarrollada por Página 61 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
"deleted_at": null,
"description": null,
"data": {
"address_default": 1,
"commission": 0,
"default_ncf": 2,
"discount_max": 0,
"electronic": true,
"invoice_auto": true,
"invoice_mode": "default",
"limit": 1500
}
},
{
"id": 2,
"region_id": 3,
"internal_code": "06907",
"legal_id": "0014226878",
"name": "Pedro Jimenez",
"legal_name": "Pedro Jimenez Corredores",
"status": 1,
"created_at": "2021-04-29 19:25:31",
"updated_at": "2021-04-29 19:25:31",
"deleted_at": null,
"description": null,
"data": {
"address_default": 2,
"commission": 20,
"default_ncf": 2,
"discount_max": 0,
"electronic": true,
"invoice_auto": true,
"invoice_mode": "default",
"limit": 0.1
}
},
],
"pagination": {
"total": 2293,
"pages": 230,
"previous": false,
"next": true
}
}
(por razones de espacio se muestra solo algunos registros)
Las propiedades que se indican a continuación solo pueden obtenerse agregando el atributo
middlemen{} a la consulta (el atributo data{} se indica como complemento, pero es opcional).
GET /api/agency?w=data{},middlemen{}
coordinator_id alfanumérico Cédula del coordinador asociado al
productor
Versión 3.7 (Nov-2024) Desarrollada por Página 62 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
coordinator_commission decimal Comisión para pagar al coordinador por las
ventas realizadas por el productor.
Las propiedades que se indican a continuación se obtienen agregando el atributo addresses{} a la
consulta (el atributo data{} se indica como complemento, pero es opcional). Ejemplo:
GET /api/agency?w=data{},addresses{}
id entero Identificador de la dirección
source alfanumérico Entidad referencia de la dirección: “Agencia”
o “Usuario”
source_id entero Identificador en la entidad referenciada
name alfanumérico Nombre de la dirección
line1 alfanumérico Primera línea de dirección
line2 alfanumérico Segunda línea de dirección
city alfanumérico Ciudad asociada a la dirección
state alfanumérico Estado o provincia asociada a la dirección
country_id entero Identificador ISO 3166-1 del país
zip alfanumérico Código postal de la dirección
Versión 3.7 (Nov-2024) Desarrollada por Página 63 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/salesman
Parámetros aceptados:
id alfanumérico Código del vendedor
firstname alfanumérico Nombres del vendedor
lastname entero Apellidos del vendedor
Respuesta:
Por cada elemento de records, se incluye:
id alfanumérico Código del vendedor
firstname alfanumérico Nombres del vendedor
lastname entero Apellidos del vendedor
Ejemplo
{
"records": [
{
"firstname": "PEDRO",
"lastname": "MARTINEZ VALDEZ",
"id": "001-1241241-2"
},
{
"firstname": "NICOLE PATRIA",
"lastname": "AYBAR HERRERA",
"id": "999-7777777-7"
}
],
"pagination": {
"total": 122,
"pages": 13,
"previous": false,
"next": true
}
}
(por razones de espacio se muestra solo algunos registros)
Versión 3.7 (Nov-2024) Desarrollada por Página 64 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/ticket/ticket/ticket_id
Parámetros aceptados:
ticket_id alfanumérico Número del certificado
invoice_id entero Número de factura asociada al certificado
Respuesta:
Por cada elemento de records, se incluye:
ticket_id alfanumérico Número del certificado
invoice_id Entero Número de factura
date fecha/hora ANSI Fecha y hora de emisión
cancel fecha/hora ANSI Fecha y hora de cancelación
agency_id entero Id de agencia que emitió el certificado
salesman_id entero Id del usuario vendedor que emitió el
certificado
from fecha ANSI Fecha de inicio de vigencia
to fecha ANSI Fecha de fin de vigencia
days alfanumérico Días de cobertura incluyendo días de salida y
regreso
destiny_id entero Código ISO-3361 de país destino
terms alfanumérico Condiciones particulares del certificado
tpainfo alfanumérico Información complementaria de T.P.A.
insured_count entero Cantidad de asegurados en el certificado
salesman_commission decimal Porcentaje de comisión del vendedor
Ejemplo
{
"ticket_id": "00000560",
Versión 3.7 (Nov-2024) Desarrollada por Página 65 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
"invoice_id": 286,
"date": "2023-04-11 15:01:45",
"cancel": null,
"agency_id": 1,
"salesman_id": 3,
"from": "2023-04-01",
"to": "2023-04-30",
"days": "30",
"destiny_id": 840,
"terms": null,
"tpainfo": null,
"insured_count": 7009,
"salesman_commission": 0
}
Versión 3.7 (Nov-2024) Desarrollada por Página 66 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/ticket/ticket_id?w=invoice{}
Parámetros aceptados:
ticket_id entero Número del certificado
Respuesta:
Por cada elemento de records, se incluye:
ticket_id alfanumérico Número del certificado
invoice_id Entero Número de factura
date fecha/hora ANSI Fecha y hora de emisión
cancel fecha/hora ANSI Fecha y hora de cancelación
agency_id entero Id de agencia que emitió el certificado
salesman_id entero Id del usuario vendedor que emitió el
certificado
from fecha ANSI Fecha de inicio de vigencia
to fecha ANSI Fecha de fin de vigencia
days alfanumérico Días de cobertura incluyendo días de salida y
regreso
destiny_id entero Código ISO-3361 de país destino
terms alfanumérico Condiciones particulares del certificado
tpainfo alfanumérico Información complementaria de T.P.A.
invoice objeto Información de la factura asociada
insured_count entero Cantidad de asegurados en el certificado
salesman_commission decimal Porcentaje de comisión del vendedor
Ejemplo
{
"ticket_id": "00000560",
Versión 3.7 (Nov-2024) Desarrollada por Página 67 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
"invoice_id": 286,
"date": "2023-04-11 15:01:45",
"cancel": null,
"agency_id": 1,
"salesman_id": 3,
"from": "2023-04-01",
"to": "2023-04-30",
"days": "30",
"destiny_id": 840,
"terms": null,
"tpainfo": null,
"invoice": {
"id": "286",
"invoice_id": "9000255",
"currency_id": "840",
"exchange": 1,
"agency_id": "1",
"agency_commission": 0,
"amount": 1.35,
"discount": 0,
"tax": 0,
"due_date": "2023-01-04",
"created_at": "2023-04-11 15:01:45",
"updated_at": "2023-04-11 15:01:45",
"description": "Certificado 00000560 emitido el
11/04/2023"
},
"insured_count": 7009,
"salesman_commission": 0
}
Versión 3.7 (Nov-2024) Desarrollada por Página 68 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/ticket/ticket/ticket_id?w=addresses{}
Parámetros aceptados:
ticket_id alfanumérico Número del certificado
Respuesta:
Por cada elemento de records, se incluye:
ticket_id alfanumérico Número del certificado
invoice_id entero Número de factura
date fecha/hora ANSI Fecha y hora de emisión
cancel fecha/hora ANSI Fecha y hora de cancelación
agency_id Entero Id de agencia que emitió el certificado
salesman_id alfanumérico Código del vendedor que emitió el certificado
from fecha ANSI Fecha de inicio de vigencia
to fecha ANSI Fecha de fin de vigencia
days alfanumérico Días de cobertura incluye día de salida y día
de regreso
destiny_id entero Código ISO-3361 de país destino
terms alfanumérico Condiciones particulares del certificado
tpainfo alfanumérico Información complementaria de T.P.A.
addresses
id numérico Identificador de la dirección asociada
ticket_id alfanumérico Número de la póliza o certificado a la que la
dirección está asociada
pax_id alfanumérico Cédula de identidad del asegurado principal
kind alfanumérico Tipo de dirección
email arreglo Arreglo de direcciones de correo
[0] alfanumérico Primera dirección de correo asociada
phone Arreglo de números de teléfono asociados
Versión 3.7 (Nov-2024) Desarrollada por Página 69 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
[0] alfanumérico Primer teléfono de correo asociado
line1 alfanumérico Primera línea de dirección (formato libre)
line2 alfanumérico Segunda línea de dirección (formato libre)
city alfanumérico Ciudad asociada a la dirección
state alfanumérico Provincia o estado asociado a la dirección
country alfanumérico Código ISO-3361 del país asociado a la
dirección
zip alfanumérico Código postal asociado a la dirección
insured_count entero Cantidad de asegurados en el certificado
salesman_commission decimal Porcentaje de comisión del vendedor
Ejemplo
{
"ticket_id": "00000002",
"invoice_id": null,
"date": "2021-10-01 00:00:01",
"cancel": null,
"agency_id": 3,
"salesman_id": 18,
"from": "2021-10-04",
"to": "2021-10-09"
"days": "6",
"destiny_id": 840,
"terms": null,
"tpainfo": null,
"addresses": [
{
"id": "1284",
"ticket_id": "00000560",
"pax_id": null,
"kind": "Contacto",
"email": [],
"phone": [],
"line1": "AVENIDA SARASOTA",
"line2": "EDIFICIO REGATTA IV",
"city": "SANTO DOMINGO",
"state": "DN",
"country": "REPÚBLICA DOMINICANA",
"zip": ""
}
],
"insured_count": "1",
"salesman_commission": 0,
}
Versión 3.7 (Nov-2024) Desarrollada por Página 70 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/issue/pdf/ticket_id
Parámetros aceptados:
ticket_id alfanumérico Número del certificado
Ejemplo
(algunas informaciones han sido pixeladas intencionalmente para protección de la información)
Versión 3.7 (Nov-2024) Desarrollada por Página 71 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/ticket/ticket_id?w=products{w=name,benefits{}}
Asegúrese de ejecutar esta consulta indicando un
número de certificado específico. No envíe la consulta
sin parámetros o con rangos de fecha ya que ralentiza la
respuesta teniendo un alto impacto en el servicio y aumentando
el tráfico de la red al manejar grandes volúmenes de datos.
Parámetros aceptados:
ticket_id alfanumérico Número del certificado
Respuesta:
Por cada elemento de records, se incluye:
ticket_id alfanumérico Número del certificado
invoice_id entero Número de factura
date fecha/hora ANSI Fecha y hora de emisión
cancel fecha/hora ANSI Fecha y hora de cancelación
agency_id entero Id del productor que emitió el certificado
salesman_id entero Id del usuario vendedor que emitió el
certificado
from fecha ANSI Fecha de inicio de vigencia
to fecha ANSI Fecha de fin de vigencia
days alfanumérico Días de cobertura incluyendo días de salida y
regreso
destiny_id entero Código ISO-3361 de país destino
terms alfanumérico Condiciones particulares del certificado
tpainfo alfanumérico Información complementaria de T.P.A.
Versión 3.7 (Nov-2024) Desarrollada por Página 72 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
products arreglo Información de los productos incluidos
insured_count entero Cantidad de asegurados en el certificado
salesman_commission decimal Porcentaje de comisión del vendedor
Por cada elemento de products, se incluye:
name alfanumérico Nombre del producto
id entero Id del producto
benefits arreglo Información de las coberturas del producto
Por cada elemento de benefits, se incluye:
id entero Id de la relación productos/coberturas
product_id entero Id del producto asociado
benefit
_
id entero Id de la cobertura asociada
name alfanumérico Nombre de la cobertura
coverage alfanumérico Etiqueta / valor de la cobertura incluida
status entero Estado de la cobertura
Ejemplo
{
"ticket_id": "00000560",
"invoice_id": 286,
"date": "2023-04-11 15:01:45",
"cancel": null,
"agency_id": 1,
"salesman_id": 3,
"from": "2023-04-01",
"to": "2023-04-30",
"days": "30",
"destiny_id": 840,
"terms": null,
"tpainfo": null,
"products": [
{
"name": "PLAN SMI",
"id": 14,
"benefits": [
{
"id": 309,
"product_id": 14,
"benefit_id": 118,
"name": "Condiciones Preexistentes",
"description": null,
Versión 3.7 (Nov-2024) Desarrollada por Página 73 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
"coverage": "US$5,000",
"status": 1
},
{
...
},
{
"id": 326,
"product_id": 14,
"benefit_id": 135,
"name": "Vigencia Anual",
"description": null,
"coverage": "Hasta 90 días de viaje",
"status": 1
}
]
}
],
"insured_count": 7009,
"salesman_commission": 0
}
(por razones de espacio se muestra solo algunos registros)
Versión 3.7 (Nov-2024) Desarrollada por Página 74 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/ticket?min_issue_date=2023-01-01,
max_issue_date=2023-01-07
Asegúrese de filtrar siempre las consultas de certificados con los
parámetros min_issue_date y max_issue_date , estos pueden
acompañar otros parámetros de su interés. Enviar la consulta sin
parámetros ralentiza la respuesta, tiene un alto impacto en el servicio y
aumenta el tráfico de la red al manejar grandes volúmenes de datos.
Parámetros aceptados:
ticket_id alfanumérico Número del certificado
agency_id arreglo | alfanumérico Id(s) de productor(es)
salesman_id arreglo | alfanumérico Id(s) de usuario(s) vendedor(es)
product_id arreglo | alfanumérico Código(s) de producto(s)
min_issue_date Fecha ANSI (yyyy-mm-dd) Fecha de emisión mínima
max_issue_date Fecha ANSI (yyyy-mm-dd) Fecha de emisión máxima
min_cancel_date Fecha ANSI (yyyy-mm-dd) Fecha de cancelación mínima
max_cancel_date Fecha ANSI (yyyy-mm-dd) Fecha de cancelación máxima
min_from_date Fecha ANSI (yyyy-mm-dd) Fecha de inicio de vigencia mínima
max_from_date Fecha ANSI (yyyy-mm-dd) Fecha de inicio de vigencia máxima
min_to_date Fecha ANSI (yyyy-mm-dd) Fecha de fin de vigencia mínima
max_to_date Fecha ANSI (yyyy-mm-dd) Fecha de fin de vigencia máxima
destiny_id entero Código ISO-3361 de país destino
Respuesta:
Por cada elemento de records, se incluye:
Versión 3.7 (Nov-2024) Desarrollada por Página 75 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
ticket_id alfanumérico Número del certificado. Se aceptan los últimos
4 caracteres del número.
invoice_id entero Número de factura
date fecha/hora ANSI Fecha y hora de emisión
cancel fecha/hora ANSI Fecha y hora de cancelación
agency_id entero Id del productor que emitió el certificado
salesman_id entero Id del usuario vendedor que emitió el
certificado
from fecha ANSI Fecha de inicio de vigencia
to fecha ANSI Fecha de fin de vigencia
days alfanumérico Días de cobertura incluyendo días de salida y
regreso
destiny_id entero Código ISO-3361 de país destino
terms alfanumérico Condiciones particulares del certificado
tpainfo alfanumérico Información complementaria de T.P.A.
insured_count entero Cantidad de asegurados en el certificado
salesman_commission decimal Porcentaje de comisión del vendedor
Ejemplo
{
"records": [
{
"ticket_id": "00000471",
"invoice_id": 197,
"date": "2023-01-04 16:33:55",
"cancel": null,
"agency_id": 1228,
"salesman_id": 93,
"from": "2023-01-05",
"to": "2023-01-09",
"days": "5",
"destiny_id": 484,
"terms": null,
"tpainfo": null,
"insured_count": 2,
"salesman_commission": 0
},
{
...
},
{
"ticket_id": "00000480",
"invoice_id": 206,
"date": "2023-01-16 17:00:02",
"cancel": null,
Versión 3.7 (Nov-2024) Desarrollada por Página 76 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
"agency_id": 1228,
"salesman_id": 19,
"from": "2023-01-16",
"to": "2023-01-20",
"days": "5",
"destiny_id": 484,
"terms": null,
"tpainfo": null,
"insured_count": 2,
"salesman_commission": 0
}
],
"pagination": {
"total": 21,
"pages": 3,
"previous": false,
"next": true
}
}
(por razones de espacio se muestra solo algunos registros)
Versión 3.7 (Nov-2024) Desarrollada por Página 77 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/ticket?min_cancel_date=2022-03-01
&max_cancel_date=2023-03-31
Asegúrese de filtrar siempre las consultas de certificados cancelados
con los parámetros min_cancel_date y max_cancel_date, estos
pueden acompañar otros parámetros de su interés. Enviar la
consulta sin parámetros ralentiza la respuesta, tiene un alto impacto en el
servicio y aumenta el tráfico de la red al manejar grandes volúmenes de datos.
Parámetros aceptados:
ticket_id alfanumérico Número del certificado
agency_id arreglo | alfanumérico Id(s) de productor(es)
salesman_id arreglo | alfanumérico Id(s) de usuario(s) vendedor(es)
product_id arreglo | alfanumérico Código(s) de producto(s)
min_issue_date Fecha ANSI (yyyy-mm-dd) Fecha de emisión mínima
max_issue_date Fecha ANSI (yyyy-mm-dd) Fecha de emisión máxima
min_cancel_date Fecha ANSI (yyyy-mm-dd) Fecha de cancelación mínima
max_cancel_date Fecha ANSI (yyyy-mm-dd) Fecha de cancelación máxima
min_from_date Fecha ANSI (yyyy-mm-dd) Fecha de inicio de vigencia mínima
max_from_date Fecha ANSI (yyyy-mm-dd) Fecha de inicio de vigencia máxima
min_to_date Fecha ANSI (yyyy-mm-dd) Fecha de fin de vigencia mínima
max_to_date Fecha ANSI (yyyy-mm-dd) Fecha de fin de vigencia máxima
destiny_id entero Código ISO-3361 de país destino
Respuesta:
Por cada elemento de records, se incluye:
Versión 3.7 (Nov-2024) Desarrollada por Página 78 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
ticket_id alfanumérico Número del certificado. Se aceptan los últimos
4 caracteres del número.
invoice_id entero Número de factura
date fecha/hora ANSI Fecha y hora de emisión
cancel fecha/hora ANSI Fecha y hora de cancelación
agency_id entero Id del productor que emitió el certificado
salesman_id entero Id del usuario vendedor que emitió el
certificado
from fecha ANSI Fecha de inicio de vigencia
to fecha ANSI Fecha de fin de vigencia
days alfanumérico Días de cobertura incluyendo días de salida y
regreso
destiny_id entero Código ISO-3361 de país destino
terms alfanumérico Condiciones particulares del certificado
tpainfo alfanumérico Información complementaria de T.P.A.
insured_count entero Cantidad de asegurados en el certificado
salesman_commission decimal Porcentaje de comisión del vendedor
Ejemplo
{
"records": [
{
"ticket_id": "00000529",
"invoice_id": 255,
"date": "2023-03-15 16:35:36",
"cancel": "2023-03-17 08:32:09",
"agency_id": 17,
"salesman_id": 93,
"from": "2023-04-16",
"to": "2023-04-21",
"days": "6",
"destiny_id": 192,
"terms": null,
"tpainfo": null,
"insured_count": 1,
"salesman_commission": 0
},
{ ... },
],
"pagination": {
"total": 5,
"pages": 1,
"previous": false,
"next": false
}
Versión 3.7 (Nov-2024) Desarrollada por Página 79 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
}
(por razones de espacio se muestra solo algunos registros)
Versión 3.7 (Nov-2024) Desarrollada por Página 80 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
La Consulta de Certificados y la Consulta de Asegurados utilizan la misma ruta, por esta razón es
posible obtener detalles de los asegurados en un certificado particular con la siguiente consulta:
GET /api/ticket/ticket_id/insured
En todos los casos debe suministrar el número del certificado a consultar.
Parámetros aceptados:
ticket_id alfanumérico Número del certificado
Respuesta:
Por cada elemento de records, se incluye:
id numérico Numero de registro asignado al asegurado para el
certificado
ticket_id alfanumérico Número del certificado
identity alfanumérico Cédula del asegurado
passport alfanumérico Número de pasaporte del asegurado
firstname alfanumérico Nombres del asegurado
lastname alfanumérico Apellidos del asegurado
birthdate fecha/hora ANSI Fecha de nacimiento del asegurado
age numérico Edad del asegurado para el momento de la compra del
certificado
sex alfanumérico Sexo del asegurado, masculino (M) o femenino (F)
status alfanumérico Indica si el asegurado es el principal (P) o un
acompañante (A)
Versión 3.7 (Nov-2024) Desarrollada por Página 81 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Ejemplo
{
"records": [
{
"id": "182168",
"ticket_id": "00000560",
"identity": null,
"passport": "W161355233-0",
"firstname": "ELHMRCAEUONT",
"lastname": "LDUALBVZEAIZ",
"birthdate": "1947-11-10",
"age": "74",
"sex": "M",
"status": "A"
},
{
"id": "182169",
"ticket_id": "00000560",
"identity": null,
"passport": "W161355233-1",
"firstname": "ILAAORIZDF",
"lastname": "ZEITZAMRRRAIENM",
"birthdate": "1947-11-13",
"age": "74",
"sex": "F",
"status": "A"
},
...
],
"pagination": {
"total": 7009,
"pages": 701,
"previous": false,
"next": true
}
}
(los registros se muestran desordenados
para asegurar la confidencialidad de la información)
Versión 3.7 (Nov-2024) Desarrollada por Página 82 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Versión 3.7 (Nov-2024) Desarrollada por Página 83 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
En el siguiente ejemplo ponemos a prueba las capacidades de GAPI para suministrar información
de certificados y las relaciones que estos tienen, para ello observe la siguiente consulta:
GET
/api/ticket?w=ticket_id,date,cancel,from,to,days,insured_count,invoice_id,d
ata{w=TICKET_KIND},destiny_id,destiny{w=name},agency_id,agency{w=name},sale
sman_id,salesman{w=firstname,lastname},products{w=internal_code,name}&kind=
1&min_issue_date=2022-01-01&max_issue_date=2022-01-10&page=1&ordered=0
Y descompongamos esto en secciones para un mejor entendimiento
1. /api/ticket?w=ticket_id,date,cancel,from,to,days,insured_count,invoice_id
2. ,data{w=TICKET_KIND}
3. ,destination_id,destiny{w=name}
4. ,agency_id,agency{w=name}
5. ,salesman_id,salesman{w=firstname,lastname}
6. ,products{w=internal_code,name}
7. &kind=1
8. &min_issue_date=2022-01-01
9. &max_issue_date=2022-01-10
10. &page=1
11. &ordered=0
La primera sección permite indicar las columnas ticket_id, date, cancel, from, to, days,
insured_count e invoice_id en la consulta.
La segunda sección incorpora la propiedad TICKET_KIND del atributo data{} asociado a la tabla
ticket.
La tercera sección agrega la columna destiny_id y su nombre en el arreglo destiny. Este
procedimiento se utiliza en las secciones 4 y 5 para agregar las columnas agency_id y
salesman_id respectivamente, esas aportan detalles en arreglos de nombre agency y salesman.
Versión 3.7 (Nov-2024) Desarrollada por Página 84 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
La sección 6 utiliza esta facilidad de manera diferente porque no agrega una columna llamada
product_id, en su lugar, agrega el arreglo products el cual tiene las columnas necesarias
(product_id y name).
Las secciones 7, 8 y 9 actúan como filtro para limitar la consulta a certificados emitidos entre el
01/01/2022 y el 10/012022, mientras que la sección 10 establece la página a devolver en 1. La
sección 11 establece el orden en que se devolverán los resultados (en este caso sin orden).
Ejemplo
{
"records": [
{
"ticket_id": "00000068",
"date": "2022-01-08 10:50:19",
"cancel": null,
"from": "2022-01-16",
"to": "2022-02-16",
"days": "32",
"invoice_id": null,
"destiny_id": 724,
"agency_id": 1264,
"salesman_id": 49,
"agency": {
"name": "Rosalma Altagracia Chabebe Fernández(132"
},
"data": [],
"destiny": {
"name": "ESPAÑA"
},
"products": [
{
"internal_code": "147",
"name": "Viaja Seguro Schengen",
"id": 11
}
],
"salesman": {
"firstname": "HAROLD ",
"lastname": "MORILLO"
},
"insured_count": 2
},
],
"pagination": {
"total": 6,
"pages": 1,
"previous": false,
"next": false
}
}
Versión 3.7 (Nov-2024) Desarrollada por Página 85 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Exportar
Versión 3.7 (Nov-2024) Desarrollada por Página 86 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
POST /api/issue/email/send
El envío de información confidencial a destinatarios
diferentes de los indicados en la póliza podría dar lugar
a la suspensión del servicio. Agradecemos su atención.
Recuerde: Todas sus acciones quedan auditadas
Parámetros requeridos:
Tipos int: entero
dec: decimal
string: alfanumérico date: fecha ANSI
text: 255 caracteres
Campo Tipo, tamaño Descripción
subject alfanumérico Asunto (título) del correo electrónico
ticket_id alfanumérico Identificador de la póliza emitida
to alfanumérico Dirección de correo a la que se enviarán los
documentos
Respuesta
{
"success": true
}
Versión 3.7 (Nov-2024) Desarrollada por Página 87 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GAPI permite exportar las consultas de asegurados y certificados hacia archivos con formato .csv
(del inglés comma separated values - valores separados por comas) que pueden ser leídos por
Microsoft Excel® , LibreOffice®, Apache OpenOffice® , etc. Para este propósito ejecute la siguiente
consulta:
GET /api/ticket/export/insured?kind=1&min_issue_date=2022-01-01
Asegúrese de filtrar las consultas de este tipo al menos
con un rango de fecha (min_issue_date /
max_issue_date). Enviar la consulta sin parámetros ralentiza la
respuesta, tiene un alto impacto en el servicio y aumenta el
tráfico de la red al manejar grandes volúmenes de datos.
Parámetros aceptados:
ticket_id alfanumérico Número del certificado
min_issue_date Fecha ANSI (yyyy-mm-dd) Fecha de emisión mínima
max_issue_date Fecha ANSI (yyyy-mm-dd) Fecha de emisión máxima
min_cancel_date Fecha ANSI (yyyy-mm-dd) Fecha de cancelación mínima
max_cancel_date Fecha ANSI (yyyy-mm-dd) Fecha de cancelación máxima
min_from_date Fecha ANSI (yyyy-mm-dd) Fecha de inicio de vigencia mínima
max_from_date Fecha ANSI (yyyy-mm-dd) Fecha de inicio de vigencia máxima
min_to_date Fecha ANSI (yyyy-mm-dd) Fecha de fin de vigencia mínima
max_to_date Fecha ANSI (yyyy-mm-dd) Fecha de fin de vigencia máxima
Versión 3.7 (Nov-2024) Desarrollada por Página 88 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
destiny_id entero Código ISO-3361 de país destino
destination_id entero Código ISO-3361 de país destino
Respuesta:
Por cada registro del archivo .csv se incluye:
Código de Agencia Código del productor o agencia
Agencia Nombre del productor o agencia
Certificado Número del certificado
Fecha y hora de Emisión Fecha/hora en que el certificado fue emitido
Fecha y hora de Cancelación Fecha/hora en que el certificado fue cancelado.
Vacío si no fue cancelado
Fecha Salida Fecha de inicio de vigencia de la cobertura
Fecha Regreso Fecha de fin de vigencia de la cobertura
Días de cobertura Cantidad de días de la cobertura
Destino Nombre del país de destino
Código de Producto Identificador del producto emitido
Producto Nombre del producto emitido
Cédula Cédula del asegurado
Pasaporte Número de pasaporte del asegurado
Nombres Nombres del asegurado
Apellidos Apellidos del asegurado
Fecha de Nacimiento Fecha de nacimiento del asegurado
Sexo Sexo del asegurado, masculino (M) o femenino (F)
Versión 3.7 (Nov-2024) Desarrollada por Página 89 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Ejemplo
"Seguros sin Fronteras"
"Consulta de asegurados"
"Usuario","SOPORTE"
"Fecha","09/05/2023 12:10 PM"
"Criterio de filtrado"
"","Certificados retail"
"","Fecha de emisión desde el 01/04/2023"
"Código de Agencia","Agencia","Certificado","Fecha y hora de Emisión","Fecha y hora de Cancelación","Fecha Salida","Fecha Regreso","Días de
cobertura","Destino","Código de Producto","Producto","Cédula","Pasaporte","Nombres","Apellidos","Fecha de Nacimiento","Sexo"
"1104","Ramona Sánchez de Peralta (14484)","00000555","2023-04-03 12:25:58","","2023-04-06","2023-04-10","5","CUBA","5","Viaja Seguro
15K","","RD5202975","GABIRAARLIEMA","DUZAAZEEDRORIQGU","1994-08-27","Femenino"
"17","Negocio Directo Oficinal Principal","00000556","2023-04-03 17:06:56","","2023-04-26","2023-05-02","7","COSTA RICA","6","Viaja Seguro
60K","224-0001330-0","RD6191656","AMTSIAEIBAARR","ZODRRGODIEERGRUUIZ","1986-05-06","Femenino"
"1496","Norma Lidia Guilamo Castillo (13251)","00000557","2023-04-04 11:55:04","","2023-06-29","2023-07-09","11","ESPAÑA","11","Viaja
Seguro Schengen","001-1858428-3","","LDEFWIRO","COIEAENZLZHORGN","1990-08-14","Masculino"
"1496","Norma Lidia Guilamo Castillo (13251)","00000557","2023-04-04 11:55:04","","2023-06-29","2023-07-09","11","ESPAÑA","11","Viaja
Seguro Schengen","025-0051610-5","","LCNIROYLAENADAM","SORVNDIOHCCIOEIE","1994-09-06","Femenino"
"17","Negocio Directo Oficinal Principal","00000558","2023-04-04 15:57:56","","2023-04-05","2023-05-04","30","ESTADOS UNIDOS","7","Viaja
Seguro 35K","","RD6881261","AENRMALETYIAI","OMBDEANICOAIJIFE","1950-02-16","Femenino"
"17","Negocio Directo Oficinal Principal","00000559","2023-04-10 17:31:14","","2023-05-14","2023-05-21","8","ALEMANIA","11","Viaja Seguro
Schengen","001-1826741-8","","ULVLI","AGPAELZOÑENZ","1989-03-29","Femenino"
"17","Negocio Directo Oficinal Principal","00000583","2023-04-22 10:38:26","","2023-04-24","2023-05-01","8","ESTADOS UNIDOS","5","Viaja
Seguro 15K","","00115853046","NANTLAEA","EDALOFOGIZN","1980-10-11","Masculino"
"17","Negocio Directo Oficinal Principal","00000583","2023-04-22 10:38:26","","2023-04-24","2023-05-01","8","ESTADOS UNIDOS","5","Viaja
Seguro 15K","","00117463505","EMYLULSYEEAGSRDA","LFDZDZEAGAEODEDILI","1985-08-24","Femenino"
"2292","HOMERO ALFREDO AUGUSTO HERNANDEZ DALMAU","00000584","2023-04-24 16:21:00","","2023-04-29","2023-05-05","7","ESTADOS
UNIDOS","5","Viaja Seguro 15K","001-1623080-6","RD7389591","NIABNEJM","MANTZVRALLVIAEA","1983-03-31","Masculino"
"1619","QASESORES,SRL (13251)","00000585","2023-04-25 17:12:31","","2023-05-16","2023-05-29","14","ESPAÑA","7","Viaja Seguro 35K","001-
0150611-1","","IVEAMRN","MANAIZAGBURR","1972-03-02","Femenino"
"1619","QASESORES,SRL (13251)","00000585","2023-04-25 17:12:31","","2023-05-16","2023-05-29","14","ESPAÑA","7","Viaja Seguro 35K","001-
0913822-2","","ARAUL","ZRRAAIERBRMAI","1949-11-14","Femenino"
"1619","QASESORES,SRL (13251)","00000586","2023-04-25 17:21:26","","2023-05-19","2023-05-29","11","ESPAÑA","7","Viaja Seguro 35K","402-
1242908-4","","IAL","EZGNRAEMZUP","2003-04-21","Femenino"
"2106","PARIS, POLANCO & ASOCIADOS SRL","00000587","2023-04-26 12:00:56","","2023-04-27","2023-05-02","6","COLOMBIA","5","Viaja Seguro
15K","012-0049374-8","RD5383684","LTBMARROVIORIED","UUDEIRGOEZFREROGI","1975-02-11","Masculino"
"2106","PARIS, POLANCO & ASOCIADOS SRL","00000587","2023-04-26 12:00:56","","2023-04-27","2023-05-02","6","COLOMBIA","5","Viaja Seguro
15K","001-1118026-1","RD5383694","LEBIAEHZAORTS","FEOGZREUDUNIEEÑ","1976-04-20","Femenino"
"2106","PARIS, POLANCO & ASOCIADOS SRL","00000587","2023-04-26 12:00:56","","2023-04-27","2023-05-02","6","COLOMBIA","5","Viaja Seguro
15K","","RD6379671","AEUOBTORROTRR","UNEUREÑFGOZEI","2005-10-11","Masculino"
"2106","PARIS, POLANCO & ASOCIADOS SRL","00000587","2023-04-26 12:00:56","","2023-04-27","2023-05-02","6","COLOMBIA","5","Viaja Seguro
15K","","RD6780344","EIASBSNTA","REZFEINÑUUEGO","2007-11-01","Masculino"
"1695","FELIX ROMAN BENCOSME RODRIGUEZ(13260)","00000588","2023-04-26 16:31:30","","2023-05-01","2023-05-31","31","MÉXICO","5","Viaja
Seguro 15K","402-2335537-7","","NJUNAOAOTNI","SUQANEEOEZSVMBC","1993-11-04","Masculino"
"2127","AA Corredores S.R.L.","00000589","2023-05-02 22:00:55","","2023-05-02","2023-05-06","5","ARUBA","8","Viaja Seguro
150K","","987654987654","JUAN PABLO","RAMIREZ GOMEZ","1983-05-20","Masculino"
"2127","AA Corredores S.R.L.","00000590","2023-05-04 16:52:56","","2023-05-11","2023-05-20","10","ARGELIA","7","Viaja Seguro 35K","001-
0779730-0","","MIGUEL","RAMIREZ","1987-05-19","Masculino"
"267","PEÑA IZQUIERDO S. R. L. (13253)","00000591","2023-06-08 09:24:06","","2023-06-09","2023-06-13","5","ESTADOS UNIDOS","8","Viaja
Seguro 150K","","123456","JUAN ERNESTO","RODRIGUEZ PEREZ","1960-06-15","Masculino"
"267","PEÑA IZQUIERDO S. R. L. (13253)","00000591","2023-06-08 09:24:06","","2023-06-09","2023-06-13","5","ESTADOS UNIDOS","8","Viaja
Seguro 150K","","748954645","SUSANA","MARCANO","1985-06-15","Femenino"
"267","PEÑA IZQUIERDO S. R. L. (13253)","00000592","2023-06-08 10:01:43","","2023-06-09","2023-06-09","1","ALEMANIA","6","Viaja Seguro
60K","","606060","MIGUEL JOSE","GONZALEZ RONDON","1996-10-23","Masculino"
(por razones de espacio no se muestra el archivo completo
Los registros han sido pixelados intencionalmente para protección de los datos presentados)
Versión 3.7 (Nov-2024) Desarrollada por Página 90 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/ticket/export/reinsurance?kind=1&min_issue_date=2022-01-01
Asegúrese de filtrar las consultas de este tipo al menos
con un rango de fecha (min_issue_date /
max_issue_date). Enviar la consulta sin parámetros ralentiza la
respuesta, tiene un alto impacto en el servicio y aumenta el
tráfico de la red al manejar grandes volúmenes de datos.
Parámetros aceptados:
ticket_id alfanumérico Número del certificado
min_issue_date Fecha ANSI (yyyy-mm-dd) Fecha de emisión mínima
max_issue_date Fecha ANSI (yyyy-mm-dd) Fecha de emisión máxima
min_cancel_date Fecha ANSI (yyyy-mm-dd) Fecha de cancelación mínima
max_cancel_date Fecha ANSI (yyyy-mm-dd) Fecha de cancelación máxima
min_from_date Fecha ANSI (yyyy-mm-dd) Fecha de inicio de vigencia mínima
max_from_date Fecha ANSI (yyyy-mm-dd) Fecha de inicio de vigencia máxima
min_to_date Fecha ANSI (yyyy-mm-dd) Fecha de fin de vigencia mínima
max_to_date Fecha ANSI (yyyy-mm-dd) Fecha de fin de vigencia máxima
destiny_id entero Código ISO-3361 de país destino
destination_id entero Código ISO-3361 de país destino
Respuesta:
Por cada registro del archivo .csv se incluye:
Código de Agencia Código del productor o agencia
Agencia Nombre del productor o agencia
Certificado Número del certificado
Versión 3.7 (Nov-2024) Desarrollada por Página 91 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Fecha y hora de Emisión Fecha/hora en que el certificado fue emitido
Fecha Salida Fecha de inicio de vigencia de la cobertura
Fecha Regreso Fecha de fin de vigencia de la cobertura
Días de cobertura Cantidad de días de la cobertura
Destino Nombre del país de destino
Producto Nombre del producto emitido
Valor del certificado Valor del certificado
Valor de la factura Valor facturado.
Si aplica comisión para el productor, esta se resta al valor del
certificado en la factura en facturas emitidas a nombre del
productor. Cuando la factura es emitida a nombre del
asegurado, no se afecta este valor.
Comisión de la agencia Valor absoluto de la comisión abonada al productor si aplica
Porcentaje de comisión de
agencia
Valor porcentual de la comisión abonada al productor si aplica
Cantidad de asegurados Cantidad de asegurados cubiertos por el certificado
Código del vendedor Código del vendedor
Vendedor Nombre del vendedor
Cédula del asegurado Cédula del asegurado
Pasaporte del asegurado Número de pasaporte del asegurado
Nombre del asegurado Nombres y Apellidos del asegurado
Correo electrónico del
asegurado
Dirección de correo electrónico asociada al certificado
emitido.
Edad del asegurado Edad del asegurado
Versión 3.7 (Nov-2024) Desarrollada por Página 92 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Ejemplo
(por razones de espacio no se muestra el archivo completo
Los registros han sido pixelados intencionalmente para protección de los datos presentados)
Versión 3.7 (Nov-2024) Desarrollada por Página 93 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GAPI puede exportar las consultas de asegurados y certificados hacia archivos con formato .xml
(del inglés Extensible Markup Language - Lenguaje de marcado extensible) que pueden ser
utilizado para representar la información transaccional de GOVAL-Web de forma estructurada de
modo que pueda ser almacenada, transmitida, procesada, visualizada e impresa, por diversos tipos
de aplicaciones y dispositivos.
La siguiente consulta permite obtener el archivo XML de los certificados emitidos a partir del
primero de enero del 2022
GET /api/ticket/export/xml?kind=1&min_issue_date=2022-01-01
Asegúrese de filtrar las consultas de este tipo al menos
con un rango de fecha (min_issue_date /
max_issue_date). Enviar la consulta sin parámetros ralentiza la
respuesta, tiene un alto impacto en el servicio y aumenta el
tráfico de la red al manejar grandes volúmenes de datos.
Parámetros aceptados:
ticket_id alfanumérico Número del certificado
min_issue_date Fecha ANSI (yyyy-mm-dd) Fecha de emisión mínima
max_issue_date Fecha ANSI (yyyy-mm-dd) Fecha de emisión máxima
min_cancel_date Fecha ANSI (yyyy-mm-dd) Fecha de cancelación mínima
max_cancel_date Fecha ANSI (yyyy-mm-dd) Fecha de cancelación máxima
min_from_date Fecha ANSI (yyyy-mm-dd) Fecha de inicio de vigencia mínima
max_from_date Fecha ANSI (yyyy-mm-dd) Fecha de inicio de vigencia máxima
min_to_date Fecha ANSI (yyyy-mm-dd) Fecha de fin de vigencia mínima
max_to_date Fecha ANSI (yyyy-mm-dd) Fecha de fin de vigencia máxima
destiny_id entero Código ISO-3361 de país destino
Versión 3.7 (Nov-2024) Desarrollada por Página 94 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
destination_id entero Código ISO-3361 de país destino
[nuevo]
Respuesta:
Por cada elemento de records, se incluye:
<ticket> Elemento de datos del certificado
Por cada elemento de ticket, se incluye:
<ticket_id> Número del certificado
<date> Fecha/hora en que el certificado fue emitido
<cancel> Fecha/hora en que el certificado fue cancelado.
Vacío si no fue cancelado
<agency_id> Código del productor o agencia
<salesman_id> Código del vendedor
<destiny_id> Código ISO del país de destino
<from> Fecha de inicio de vigencia de la cobertura
<to> Fecha de fin de vigencia de la cobertura
<insured_count> Cantidad de asegurados en el certificado
<invoice_id> Número de la factura asociada al certificado
<agency> Elemento de información del productor o agencia
<name> Nombre del productor o agencia
<destiny> Elemento de información del país de destino
<name> Nombre del país de destino
<products> Elemento de información de los productos
<product> Elemento de información del producto
<internal_code> Código interno del producto
<name> Nombre del producto
<salesman> Elemento de información del vendedor
<firstname> Nombres del vendedor
<lastname> Apellidos del vendedor
Versión 3.7 (Nov-2024) Desarrollada por Página 95 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Ejemplo
(por razones de espacio no se muestra el archivo completo
Los registros han sido pixelados intencionalmente para protección de los datos presentados)
Versión 3.7 (Nov-2024) Desarrollada por Página 96 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Transacciones
Versión 3.7 (Nov-2024) Desarrollada por Página 97 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Se denominan transacciones todas aquellas operaciones realizadas en GOVAL-Web que siguen un
flujo controlado y dan como resultado cotizaciones de seguros de viaje, emisiones, cancelaciones
(anulación), etc., en otras palabras: registran datos.
Debido a que el control de este flujo responde a las necesidades del negocio y se rige por reglas,
políticas y procedimientos particulares, es de suma importancia que el equipo de desarrollo
conozca los aspectos fundamentales relacionados con el ciclo de vida del seguro de viaje, para así
evitar errores y sacar el máximo provecho a la interfaz de programación.
Las reglas de negocio indicadas en este documento
pueden variar de acuerdo con las condiciones
contractuales particulares del cliente. Aunque GAPI asegura el
cumplimiento de estos aspectos, es responsabilidad del equipo
de desarrollo mantenerse actualizado y seguir el flujo indicado
para obtener los resultados esperado.
Versión 3.7 (Nov-2024) Desarrollada por Página 98 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Las Reglas del Negocio en GAPI describen las políticas, normas, operaciones, definiciones y
restricciones que GOVAL ha incluido y que son de vital importancia para alcanzar los objetivos
contractuales con el cliente.
Considere este documento un modelo general sobre el que se fundamenta la
operación de seguro de viajes gestionada por Goval-Web:
El proceso de suscripción en GAPI está regido por las siguientes políticas:
1. 2. 3. 4. 5. 6. 7. 8. 9. Solo se emiten seguros de viaje a personas que no posean otro seguro de viaje vigente.
Todos los asegurados incluidos en el certificado deben estar plenamente identificados.
Solo se emiten seguros de viaje con al menos 24 horas de anticipación a la fecha/hora de
salida.
El seguro de viaje solo se emite en el país de origen del viaje.
No se extiende ni se reduce la vigencia de un seguro de viaje.
Los cambios de fecha pueden realizarse siempre que se mantenga la misma cantidad de
días de cobertura y únicamente si el período de vigencia no ha iniciado.
No se incluyen o excluyen personas a un seguro de viaje emitido.
La cancelación (anulación) de un seguro de viaje aplica para todos los asegurados incluidos.
La cobertura del seguro de viaje aplica por igual a todos los asegurados incluidos, salvo que
condiciones particulares del producto establezcan límites de edad y/o género.
10. No se realizan modificaciones a la cobertura del seguro de viaje una vez éste ha sido
emitido.
Versión 3.7 (Nov-2024) Desarrollada por Página 99 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
11. La elegibilidad de algunos productos está sujeta al suministro de información adicional
específica.
1. La cotización debe ser un proceso simplificado con el único propósito de conocer, y
opcionalmente comparar, las coberturas de los productos cotizados y sus tarifas.
2. Toda cotización emitida tiene una vigencia de 30 días calendario, contados a partir de su
emisión.
3. La tarifa y costo del (los) producto (s) cotizado (s) se mantiene durante la vigencia de la
cotización, siempre y cuando se mantengan las características originales indicadas, es decir,
período de cobertura, cantidad de personas y edad de los asegurados.
4. Las cotizaciones emitidas contarán con un identificador exclusivo que permita utilizarla
como fuente de entrada de datos en una emisión regular, pudiendo ser procesada por
cualquier canal (productor/vendedor) salvo que este no tenga acceso a los productos
indicados en ella.
5. Las características de los productos cotizados y sus tarifas pudieran sufrir variaciones al
momento de la emisión. Mantener o no las condiciones originalmente ofrecidas depende
de los acuerdos contractuales con el cliente.
1. 2. 3. Cada productor o agencia debe estar asociado a una sola región.
Un vendedor debe estar asociado a un productor o a todos los productores de una región.
Un vendedor podrá consultar las ventas que ha realizado el productor o agencia al cual está
asociado. En aquellos casos en que esté relacionado a una región en lugar de un productor
o agencia, podrá consultar las ventas de todos los productores o agencias asociados a dicha
región incluyendo las subregiones que dependan de ella, sin embargo, no podrá consultar
Versión 3.7 (Nov-2024) Desarrollada por Página 100 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
4. las ventas de regiones, productores o agencias que no dependan de la región a la que él
pertenece.
Se debe permitir incentivos de comisión por productor o agencia.
1. La emisión de seguro de viaje debe estar asociada a un canal de ventas.
2. La emisión de seguro de viaje debe ser realizada por un vendedor.
3. Al emitir un seguro de viaje solo se podrá escoger un productor.
4. A pesar de que el vendedor cambie su asociación con los canales de venta tras la emisión
de un seguro de viaje, el seguro emitido mantiene los datos que estaban vigentes al
momento de su emisión.
5. Toda emisión debe contar con un producto base y opcionalmente, tantos productos
complementarios como estén disponible.
6. Todo asegurado debe estar identificado con el número de cédula de identidad, el número
de pasaporte o ambos datos. En caso de identificarse con el número de cédula de identidad,
este debe cumplir con el formato de la República Dominicana para que sea considerado
válido.
7. Se debe suministrar la “Fecha de nacimiento” de los asegurados a los efectos de calcular su
edad.
8. Se debe suministrar el género de los asegurados para poder emitir un seguro de viaje.
9. Se debe suministrar la dirección de contacto y opcionalmente tantas direcciones como se
considere necesario.
10. Los certificados que indiquen una dirección de correo electrónica deben recibir el
certificado de viaje y la información adicional que acompaña a este.
11. La emisión de un seguro de viaje concluye con la facturación y el pago de este.
Versión 3.7 (Nov-2024) Desarrollada por Página 101 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
1. Los canales de venta pueden comercializar solo aquellos productos que le han sido
2. 3. 4. 5. 6. 7. 8. 9. asociados.
La asociación de productos responde al canal de ventas y no al vendedor, en tal sentido, un
vendedor puede comercializar los productos “A”, “B” y “D” en un canal de venta, por
ejemplo, y en otro canal solo “B”, “C”, y “H”.
El canal de ventas puede recibir opcionalmente una comisión sobre la venta realizada, la
cual se debe definir previamente a la emisión del seguro de viaje.
La comisión del canal de venta se calculará aplicando un valor porcentual al valor neto de
la factura (después de descuentos e impuestos) y puede aplicar de manera global para
todos los productos, o de manera específica (por producto).
El vendedor puede recibir opcionalmente una comisión sobre la venta realizada, la cual se
debe definir previamente a la emisión del seguro de viaje.
La comisión del vendedor se calculará aplicando un valor porcentual al valor neto de la
factura (después de descuentos e impuestos).
La comisión de venta definida para un vendedor es la misma en todos los canales de venta
en los que esté asociado.
Las comisiones de venta del canal y/o del vendedor se abonan (parcial o totalmente) al
momento del cobro de la factura relacionada.
Toda cancelación de un seguro de viaje generará un reverso de la (s) comisión (es) abonada
(s) tanto al canal de ventas como al vendedor.
1. Las tarifas responden a un esquema regido por la cantidad de días del viaje, la cantidad de
asegurados incluidos y sus edades.
Versión 3.7 (Nov-2024) Desarrollada por Página 102 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
2. Las promociones que se establezcan deben tener una fecha/hora de inicio y una fecha/hora
de finalización.
3. Al establecer una promoción, por ejemplo “Niños Gratis”, el beneficio solo aplica al
producto base, manteniéndose la tarifa de los productos complementarios
1. Se podrán utilizar dos modos de facturación para los seguros de viaje emitidos: facturación
automática o facturación diferida. Estas deben definirse previamente a la emisión del
seguro de viaje.
2. La facturación automática debe aplicar a todos los canales de venta que hayan sido
definidos con esta modalidad y utilizar como encabezado, los datos del canal de venta tales
como nombre comercial, dirección, teléfono y RNC.
3. La facturación diferida debe aplicar a todos los canales de venta que hayan sido definidos
con esta modalidad y utilizar como encabezado datos diferentes a los del canal de venta,
por ejemplo, del asegurado, en lo que se conoce como “Factura a terceros”.
1. Toda factura emitida debe ser pagada a través de medios de pago electrónico, como
tarjetas de crédito, o con cargo a una línea de crédito previamente establecida al canal de
ventas.
2. 3. 4. El pago de una factura no debe realizarse parcialmente sino total.
No se permite la emisión de seguros de viaje con cargo a una línea de crédito si el monto
total a pagar excede el valor disponible en la línea de crédito.
El monto disponible en la línea de crédito disminuirá con cada factura emitida con cargo a
esta y aumentará con los abonos que se realicen a través de depósitos o transferencias
bancarias que hayan sido notificados a GOVAL y que este aplique en su back office.
Versión 3.7 (Nov-2024) Desarrollada por Página 103 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Las transacciones se rigen por flujos controlados por validaciones que dependen del (los)
producto (s) elegido (s), de las condiciones que lo (s) regulen y de aspectos administrativos que el
negocio demande que se cumplan. La emisión de una póliza de seguro de viaje en GAPI tiene como
mínimo tres pasos que se deben cumplir:
1. Cotización
2. Validación
3. Pago
La cotización1 inicia con el llamado a la uri /api/issue/retail/new. Ejemplo:
POST /api/issue/retail/new
Este paso asegura que todos los parámetros requeridos han sido recibidos y que las validaciones
iniciales son satisfechas, estas son:
Productor existe y está activo
Vendedor existe, está activo y está asociado al productor.
Emisión cumple con las reglas del Negocio
a) b) c) d) e) f) Se han suministrado todos los datos de asegurado (s).
Se ha suministrado todos los datos requeridos para el contacto principal
Se ha suministrado al menos un contacto para casos de emergencia
1 Esta cotización no guarda relación con la funcionalidad “Cotización” de GOVAL-Web (también conocida como
presupuesto). Este es el proceso que consiste en determinar las tarifas de los productos sometidos a los efectos de
continuar el flujo.
Versión 3.7 (Nov-2024) Desarrollada por Página 104 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Aunque cada ejemplo proporcionado en esta guía indica con claridad los parámetros requeridos
para cada tipo de emisión de seguro de viajes, se debe tener en cuenta estos aspectos:
Productores y vendedores
Como se indicó en las Reglas del Negocio, un vendedor solo puede emitir seguros de viaje para el
productor al cual está asociado o para todos los productores de una región, solo si ha sido asociado
a dicha región. En los casos que se intente emitir un seguro de viaje con un productor al cual el
vendedor no esté asociado se recibirá este mensaje:
{
"error": true,
"message": {
"agency_id": [
"agency id es inválido"
] ,
"salesman_id": [
"salesman id es inválido"
]
}
}
Productos
Otro aspecto para tomar en cuenta es la disponibilidad del (de los) producto (s). Este (estos) no
solo deben existir; además, deben estar activos y asociados al productor. Cuando esto no ocurre
se pueden recibir mensajes como el siguiente:
{
"error": true,
"message": {
"products": [
"Arreglo de productos es inválido"
]
}
}
Tarifas
Uno de los errores comunes en la emisión de seguros de viaje con GAPI es intentar emitir una
póliza con productos que no tienen tarifa para el período indicado y/o para la cantidad de
asegurados incluidos, en esos casos se recibirá un mensaje como el siguiente:
Versión 3.7 (Nov-2024) Desarrollada por Página 105 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
{
"error": true,
"message": {
"0": "No existen tarifas disponibles para su selección",
"1": "Producto CENTENARIO"
}
}
O puede que el (los) asegurado (s) no cumpla (n) con las condiciones establecidas para la tarifa del
producto solicitado, en esos casos el mensaje de error incluirá el (los) asegurado (s) afectado (s).
{
"error": true,
"message": {
"0": "No existen tarifas disponibles para su selección",
"1": "Victor Davis",
"2": "74 años",
"3": "Producto ESTUDIANTIL"
}
}
Cuando todas las validaciones iniciales son ejecutadas con éxito, GAPI devuelve un identificador
de la cotización (id), el cual debe ser utilizado para avanzar en el fujo del proceso, este puede
consistir en validaciones específicas del (los) producto (s), (en caso de que existan) y/o validación
del encabezado de la factura, si la operación ha fue configurada con factura.
{
"id": 874,
"uri": "https://localhost/api/issue/retail/874/manager"
}
Las validaciones tienen como objetivo asegurar que se suministren todas las informaciones
requeridas por el seguro de viaje y que estas cumplan con las Reglas del Negocio. El flujo es
administrado por el manager de GAPI con base al identificador proporcionado en la cotización y la
uri que le acompaña. Estos dos elementos son necesarios para hacer la llamada al manager de
Versión 3.7 (Nov-2024) Desarrollada por Página 106 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
forma repetitiva y tantas veces como sea necesario, hasta satisfacer todos los requerimientos del
seguro de viaje. Por ejemplo, al recibir una respuesta como esta:
{
"id": 874,
"uri": "https://localhost/api/issue/retail/874/manager"
}
Se debe inicializar el manager de esta manera:
GET /api/issue/retail/874/manager
El identificador de la cotización debe mantenerse durante todo el proceso y será válido mientras
no se haya concluido con la emisión, esto significa que puede retomarse en el momento en que se
desee ya que mientras existan requerimientos que no hayan sido satisfechos, se seguirán
recibiendo mensajes como este:
{
"code": 64,
"message": "Complete todos los datos",
"uri": "https://localhost/api/issue/retail/876/invoice-data"
}
Para explicar en detalle los tipos de mensaje que se pueden recibir al usar el manager,
seguidamente se muestra los más comunes.
Productos complementarios
Generalmente los productos complementarios como el de “cancelación de viaje” o el de
“COVID”, por mencionar dos de ellos, requieren el suministro de información relacionada. Si no se
cumple con este paso se reciben mensajes como este. Ejemplo:
{
"code": 4,
"message": "Indique los datos de su Producto de Cancelación",
"uri": "http://localhost/api/issue/retail/99/cancellation-product"
}
Versión 3.7 (Nov-2024) Desarrollada por Página 107 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Observe que aquí la respuesta tiene un código (code) y un mensaje indicativo de que la validación
del producto de cancelación no está satisfecha. En casos como este debe enviar a la uri entregada
por el manager los datos requeridos para el producto de cancelación, utilizando los parámetros
requeridos, los cuales se indican en los diferentes ejemplos que se muestran en esta guía más
adelante. Si no conoce cuáles son estos valores consulte al Administrador del Sistema.
Cabecera de factura
En los casos en que se haya configurado una operación con factura, el manager requerirá
información del encabezado de esta con un mensaje como el siguiente (nótese la parte final de la
uri /invoice-data):
{
"code": 64,
"message": "Complete todos los datos",
"uri": "http://localhost/api/issue/retail/8648/invoice-data"
}
Para cumplir con lo requerido debe enviarse la información al manager. Ejemplo:
POST /api/issue/retail/8648/invoice-data
No se debe olvidar que siempre que el manager se detenga con mensajes como este, es porque
debe enviarse la consulta utilizando el id y la uri proporcionada en la cotización, junto con los datos
faltantes.
Si la operación ha sido configurada con Comprobante Fiscal, es obligatorio enviar el tipo de
comprobante a utilizar. El siguiente mensaje se obtiene al intentar usar un tipo de comprobante
fiscal no válido:
{
"error": true,
"message": {
"ncf_id": [
"ncf id es inválido."
]
}
}
Versión 3.7 (Nov-2024) Desarrollada por Página 108 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Balance de la línea de crédito
En los casos en que se indique pago con cargo a la línea de crédito del productor y el balance de
esta no cubra la emisión del seguro de viaje, se recibirá un mensaje como el siguiente:
{
"error": true,
"message": "La agencia TROTAMUNDOS (7781) no tiene balance para emitir este
certificado"
}
Cómo entender la información faltante
Al enviar la solicitud a la uri entregada por el manager, el mensaje siempre identificará lo que
detiene el proceso; sin embargo, no ofrecerá mayores detalles sobre cuáles parámetros faltan o
cuáles son incorrectos, por ello recomendamos revisar las Reglas del Negocio y hacer las
comprobaciones de lugar necesarias para asegurar que todo está en orden.
Antes de solicitar apoyo técnico para la emisión de un seguro de viajes con GAPI verifique que se
ha cumplido con todas las afirmaciones que se indican en la tabla de diagnóstico que anexamos a
este documento.
En el ejemplo se muestra el mensaje relacionado con falta de información para un producto de
cancelación:
{
"code": 4,
"message": "Indique los datos de su Producto de Cancelación",
"uri": "http://localhost/api/issue/retail/99/cancellation-product"
}
Observe que el identificador del flujo tiene código 4 y el mensaje señala cuál es el paso que detiene
la continuidad del flujo. Recuerde que, en casos como este, debe enviar los datos utilizando los
parámetros requeridos, los cuales se indican en los diferentes ejemplos de esta guía.
La siguiente tabla ofrece los códigos de respuesta que el manager de GAPI devuelve cuando no se
han proporcionado los parámetros necesarios.
Código Descripción
1 Validación de asegurados con coberturas activas
2 Cálculo de tarifas
Versión 3.7 (Nov-2024) Desarrollada por Página 109 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
4 Validación de productos de cancelación
8 Validación de productos "Niños gratis"
64 Formulario de cabecera de factura
256 Validación de productos "Covid-19"
Finalizado el proceso de validación, el último paso en el flujo del manager es el pago y esto se lleva
a cabo de la siguiente manera:
POST /api/issue/retail/apply/<id>/<payment_kind>
Donde id es el identificador usado durante todo el flujo del proceso y payment_kind es la forma
en que será pagado el seguro de viaje.
Cuando se habla de crédito se refiere al uso de la línea de crédito del productor que le ha sido
habilitada para la venta de seguros de viaje y no al medio electrónico de pago con tarjeta de crédito
o de débito.
Aunque el sistema comercial GOVAL-Web permite el pago con tarjeta de débito o crédito, GAPI no
procesa pagos con este medio debido a las limitaciones impuestas por el procesador de pagos, en
cumplimiento de normas PCI (Payment Card Industry, un conjunto de regulaciones establecidas
para reducir la prevalencia del fraude con tarjetas de crédito). Para mayores detalles sobre el pago
con tarjeta de crédito consulte al Administrador del Sistema.
El proceso de emisión concluye con el pago de la póliza. Hasta que no
sea realizado la póliza no será emitida. Puede usar cualquiera de los
métodos de pago disponible: crédito o contado.
Versión 3.7 (Nov-2024) Desarrollada por Página 110 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Una vez se ha emitido la póliza con éxito, se recibe el mensaje con el número del certificado
asignado a la emisión, así como la uri donde están disponible los datos de este. (Ver Consulta de
certificado específico)
{
"id": "04149753",
"uri": "http://localhost/api/ticket/04149753"
}
Versión 3.7 (Nov-2024) Desarrollada por Página 111 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
POST /api/issue/retail/new
Parámetros requeridos:
Tipos int: entero
dec: decimal
string: alfanumérico date: fecha ANSI
text
Campo Tipo, tamaño Descripción
agency_id int, 5 Id del productor que emite el seguro
discount dec. 5,2 Descuento porcentual que aplica a la venta
salesman_id int, 10 Id del vendedor que emite el seguro
products[0][id] int, 10 Código del producto base
destiny_id int, 3 Código ISO-3361 de país destino
destination_id int, 3 Código ISO-3361 de país destino
from date Fecha de inicio de vigencia (yyyy-mm-dd)
to date Fecha de fin de vigencia (yyyy-mm-dd)
terms text Condiciones particulares
insured[0][identity] string, 13 Cédula del asegurado
insured[0][passport] string, 30 Pasaporte del asegurado
insured[0][firstname] string, 30 Nombres del asegurado
insured[0][lastname] string, 30 Apellidos del asegurado
insured[0][birthdate] date Fecha de nacimiento del asegurado (yyyy-mm-dd)
insured[0][sex] string, 1 Género del asegurado: [M]asculino | [F]emenino
Versión 3.7 (Nov-2024) Desarrollada por Página 112 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
addresses[0][line1] string, 60 1ra línea de la dirección de contacto principal
addresses[0][line2] string, 60 2da línea de la dirección de contacto principal
addresses[0][city] string, 50 Ciudad de la dirección de contacto principal
addresses[0][state] string, 50 Estado/Provincia de la dirección de contacto
principal
addresses[0][country_id] int, 10 Código ISO-3361 de la dirección de contacto
principal
addresses[0][zip] string, 20 Código postal de la dirección de contacto principal
addresses[0][phone] string, 100 Teléfono del contacto principal
addresses[0][email] string, 100 Dirección de correo electrónico del contacto
principal
La primera dirección indicada (addresses[0]) se utiliza como dirección del contacto principal. Las
direcciones sucesivas (addresses[1], addresses[2]... addresses[n]) se utilizan como
direcciones adicionales.
El siguiente paso solo es necesario si su operación
incluye la facturación en GAPI
POST /api/issue/retail/id/invoice-data
Parámetros requeridos para la validación de encabezado de factura:
Tipos int: entero
dec: decimal
string: alfanumérico date: fecha ANSI
text: 255 caracteres
Campo Tipo, tamaño Descripción
id int, 2 ID de la cotización
Versión 3.7 (Nov-2024) Desarrollada por Página 113 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
ncf_id int, 2 ID del tipo de NCF que se aplicará a la factura (ver
Códigos de tipo de NCF)
legal_id string, 20 Número de registro de la administración tributaria
de la empresa (RNC, NIF, CIF, etc.)
name string, 40 Nombre del deudor de la factura
address string, 100 Dirección del deudor. Incluya toda la información
de presentación (linea1, linea2, ciudad, país)
phone string, 50 Teléfono(s) asociados al deudor
email string, 50 Dirección de correo electrónico del deudor
POST /api/issue/retail/apply/id/credit
Recuerde: El proceso de emisión concluye con el pago
de la póliza. No olvide ejecutar el método de pago que
aplique a su caso.
Versión 3.7 (Nov-2024) Desarrollada por Página 114 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
POST /api/issue/retail/new
Parámetros requeridos:
Tipos int: entero
string: alfanumérico
date: fecha ANSI
text: 255 caracteres
Campo Tipo, tamaño Descripción
agency_id int, 5 Id de agencia que emite el seguro
salesman_id int, 10 Id del vendedor que emite el seguro
products[0][id] int, 10 Código del producto base
products[1][id] int, 10 Código del producto complementario
products[1][complement] int, 10 Etiqueta complemento de tarifa del tramo
seleccionado. Debe coincidir exactamente con el
texto de la tarifa
destiny_id int, 3 Código ISO-3361 de país destino
destination_id int, 3 Código ISO-3361 de país destino
From date Fecha de inicio de vigencia
To date Fecha de fin de vigencia
Terms text Condiciones particulares
insured[0][identity] string, 13 Cédula del asegurado
insured[0][passport] string, 30 Pasaporte del asegurado
insured[0][firstname] string, 30 Nombres del asegurado
Versión 3.7 (Nov-2024) Desarrollada por Página 115 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
insured[0][lastname] string, 30 Apellidos del asegurado
insured[0][birthdate] date Fecha de nacimiento del asegurado
insured[0][sex] string, 1 Género del asegurado: [M]asculino | [F]emenino
insured[n][identity] string, 13 Cédula del asegurado n
insured[n][passport] string, 30 Pasaporte del asegurado n
insured[n][firstname] string, 30 Nombres del asegurado n
insured[n][lastname] string, 30 Apellidos del asegurado n
insured[n][birthdate] date Fecha de nacimiento del asegurado n
insured[n][sex] string, 1 Género del asegurado n: [M]asculino | [F]emenino
addresses[0][line1] string, 60 1ra línea de la dirección de contacto principal
addresses[0][line2] string, 60 2da línea de la dirección de contacto principal
addresses[0][city] string, 50 Ciudad de la dirección de contacto principal
addresses[0][state] string, 50 Estado/Provincia de la dirección de contacto
principal
addresses[0][country_id] int, 10 Código ISO-3361 de la dirección de contacto
principal
addresses[0][zip] string, 20 Código postal de la dirección de contacto principal
addresses[0][phone] string, 100 Teléfono del contacto principal
addresses[0][email] string, 100 Dirección de correo electrónico del contacto
principal
La primera dirección indicada (addresses[0]) se utiliza como dirección del contacto principal. Las
direcciones sucesivas (addresses[1], addresses[2]... addresses[n]) se utilizan como
direcciones adicionales.
El siguiente paso solo es necesario si su operación
incluye la facturación en GAPI
POST /api/issue/retail/id/invoice-data
Versión 3.7 (Nov-2024) Desarrollada por Página 116 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Parámetros requeridos para la validación de encabezado de factura:
Tipos int: entero
dec: decimal
string: alfanumérico date: fecha ANSI
text: 255 caracteres
Campo Tipo, tamaño Descripción
ncf_id int, 2 ID del tipo de NCF que se aplicará a la factura (ver
Códigos de tipo de NCF)
legal_id string, 20 Número de registro de la administración tributaria
de la empresa (RNC, NIF, CIF, etc.)
name string, 40 Nombre del deudor de la factura
address string, 100 Dirección del deudor. Incluya toda la información
de presentación (linea1, linea2, ciudad, país)
phone string, 50 Teléfono(s) asociados al deudor
email string, 50 Dirección de correo electrónico del deudor
POST /api/issue/retail/apply/id/credit
Recuerde: el proceso de emisión concluye con el pago
de la póliza. No olvide ejecutar el método de pago que
aplique a su caso.
Versión 3.7 (Nov-2024) Desarrollada por Página 117 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
POST /api/issue/retail/new
Parámetros requeridos:
Tipos int: entero
string: alfanumérico
date: fecha ANSI
text: 255 caracteres
agency_id int, 5 Código de agencia que emite el seguro
salesman_id int, 10 Código del vendedor que emite el seguro
products[0][id] int, 10 Código del producto base
products[1][id] int, 10 Código del producto complementario
products[1][complement] int, 10 Etiqueta complemento de tarifa del tramo
seleccionado. Debe coincidir exactamente con el
texto de la tarifa
products[2][id] int, 10 Código del segundo producto complementario
products[2][complement] int, 10 Etiqueta complemento de tarifa del tramo
seleccionado del segundo producto
complementario. Debe coincidir exactamente con
el texto de la tarifa
products[n][id] int, 10 Código del producto n complementario
Versión 3.7 (Nov-2024) Desarrollada por Página 118 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
products[n][complement] int, 10 Etiqueta complemento de tarifa del tramo
seleccionado del producto complementario n.
Debe coincidir exactamente con el texto de la
tarifa
destiny_id int, 3 Código ISO-3361 de país destino
destination_id int, 3 Código ISO-3361 de país destino
from date Fecha de inicio de vigencia
to date Fecha de fin de vigencia
terms text Condiciones particulares
insured[0][identity] string, 13 Cédula del asegurado
insured[0][passport] string, 30 Pasaporte del asegurado
insured[0][firstname] string, 30 Nombres del asegurado
insured[0][lastname] string, 30 Apellidos del asegurado
insured[0][birthdate] date Fecha de nacimiento del asegurado
insured[0][sex] string, 1 Género del asegurado: [M]asculino | [F]emenino
insured[n][identity] string, 13 Cédula del asegurado n
insured[n][passport] string, 30 Pasaporte del asegurado n
insured[n][firstname] string, 30 Nombres del asegurado n
insured[n][lastname] string, 30 Apellidos del asegurado n
insured[n][birthdate] date Fecha de nacimiento del asegurado n
insured[n][sex] string, 1 Género del asegurado n: [M]asculino | [F]emenino
addresses[0][line1] string, 60 1ra línea de la dirección de contacto principal
addresses[0][line2] string, 60 2da línea de la dirección de contacto principal
addresses[0][city] string, 50 Ciudad de la dirección de contacto principal
addresses[0][state] string, 50 Estado/Provincia de la dirección de contacto
principal
addresses[0][country_id] int, 10 Código ISO-3361 de la dirección de contacto
principal
addresses[0][zip] string, 20 Código postal de la dirección de contacto principal
addresses[0][phone] string, 100 Teléfono del contacto principal
addresses[0][email] string, 100 Dirección de correo electrónico del contacto
principal
addresses[0][email] alfanumérico Dirección de correo dirección del contacto
principal
Versión 3.7 (Nov-2024) Desarrollada por Página 119 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
La primera dirección indicada (addresses[0]) se utiliza como dirección del contacto principal. Las
direcciones sucesivas (addresses[1], addresses[2]... addresses[n]) se utilizan como
direcciones de contacto de emergencia y adicionales.
El siguiente paso solo es necesario si su operación
incluye la facturación en GAPI
POST /api/issue/retail/id/invoice-data
Parámetros requeridos para la validación de encabezado de factura:
Tipos int: entero
dec: decimal
string: alfanumérico date: fecha ANSI
text: 255 caracteres
Campo Tipo, tamaño Descripción
ncf_id int, 2 ID del tipo de NCF que se aplicará a la factura (ver
Códigos de tipo de NCF)
legal_id string, 20 Número de registro de la administración tributaria
de la empresa (RNC, NIF, CIF, etc.)
name string, 40 Nombre del deudor de la factura
address string, 100 Dirección del deudor. Incluya toda la información
de presentación (linea1, linea2, ciudad, país)
phone string, 50 Teléfono(s) asociados al deudor
email string, 50 Dirección de correo electrónico del deudor
POST /api/issue/retail/apply/id/credit
Versión 3.7 (Nov-2024) Desarrollada por Página 120 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Recuerde: el proceso de emisión concluye con el pago
de la póliza. No olvide ejecutar el método de pago que
aplique a su caso.
Versión 3.7 (Nov-2024) Desarrollada por Página 121 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
POST /api/issue/retail/apply/id/credit
{id} es el valor obtenido por la solicitud realizada a GAPI
relacionada con la emisión de la póliza de seguro de
viaje.
Parámetros requeridos:
id entero Identificador de la cotización
Versión 3.7 (Nov-2024) Desarrollada por Página 122 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Los métodos que se muestran en esta sección permiten
realizar cambios en pólizas de seguro emitidas.
Asegúrese de hacer la petición con el identificador
correcto y evitar así afectar otras pólizas. Validar la póliza
correcta es su responsabilidad.
Recuerde: Todas sus acciones quedan auditadas
Versión 3.7 (Nov-2024) Desarrollada por Página 123 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
El método que se muestra a continuación permite mover
la vigencia de una póliza en cualquier sentido siempre
que el usuario utilizado en la consulta tenga el privilegio asociado.
En ningún caso podrá acortar o alargar la vigencia de un
certificado. Las pólizas anuales mantendrán un (1) año calendario
a partir de su inicio.
Recuerde: Todas sus acciones quedan auditadas
PUT /api/ticket/ticket_id/validity
La respuesta del servidor será en todos estos casos el código 204 sin contenido, en caso de que la
petición haya sido ejecutada con éxito.
Parámetros requeridos:
Tipos int: entero
dec: decimal
string: alfanumérico date: fecha ANSI
text: 255 caracteres
Campo Tipo, tamaño Descripción
ticket_id alfanumérico Número del certificado
from date Fecha de inicio de vigencia (yyyy-mm-dd)
Versión 3.7 (Nov-2024) Desarrollada por Página 124 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
El método que se muestra a continuación permite
cambiar el destino de una póliza siempre que el usuario
utilizado en la consulta tenga el privilegio asociado.
Recuerde: Todas sus acciones quedan auditadas
PUT /api/ticket/ticket_id/destiny
La respuesta del servidor será en todos estos casos el código 204 sin contenido, en caso de que la
petición haya sido ejecutada con éxito.
Parámetros requeridos:
Tipos int: entero
dec: decimal
string: alfanumérico date: fecha ANSI
text: 255 caracteres
Campo Tipo, tamaño Descripción
ticket_id alfanumérico Número del certificado
destiny_id entero Identificador ISO 3166-1 del país
Versión 3.7 (Nov-2024) Desarrollada por Página 125 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
El método que se muestra a continuación permite
cambiar la dirección de una póliza emitida siempre que
el usuario utilizado en la consulta tenga el privilegio asociado
Recuerde: Todas sus acciones quedan auditadas
PUT /api/ticket/ticket_id/addresses/all
La respuesta del servidor será en todos estos casos el código 204 sin contenido, en caso de que la
petición haya sido ejecutada con éxito.
Parámetros requeridos:
Tipos int: entero
dec: decimal
string: alfanumérico date: fecha ANSI
text: 255 caracteres
Campo Tipo, tamaño Descripción
ticket_id alfanumérico Número del certificado al que pertenece la dirección
id numérico Identificador de la dirección
destiny_id entero Identificador ISO 3166-1 del país
pax_id alfanumérico Cédula de identidad del asegurado principal
kind alfanumérico Tipo de dirección
email[0] alfanumérico Primera dirección de correo asociada
phone[0] alfanumérico Primer teléfono de correo asociado
line1 alfanumérico Primera línea de dirección (formato libre)
line2 alfanumérico Segunda línea de dirección (formato libre)
city alfanumérico Ciudad asociada a la dirección
state alfanumérico Provincia o estado asociado a la dirección
Versión 3.7 (Nov-2024) Desarrollada por Página 126 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
country alfanumérico Código ISO-3361 del país asociado a la dirección
zip alfanumérico Código postal asociado a la dirección
Versión 3.7 (Nov-2024) Desarrollada por Página 127 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
El método que se muestra a continuación permite
cambiar los datos generales de los asegurados en una
póliza emitida, para esto el usuario utilizado en la solicitud debe
contar con el privilegio asociado. Aunque es posible realizar
cambios en la fecha de nacimiento, el cambio no puede afectar la
edad de los asegurados.
Recuerde: Todas sus acciones quedan auditadas
PUT /api/ticket/ticket_id/insured/id
La respuesta del servidor será en todos estos casos el código 204 sin contenido, en caso de que la
petición haya sido ejecutada con éxito.
Parámetros requeridos:
Tipos int: entero
dec: decimal
string: alfanumérico date: fecha ANSI
text: 255 caracteres
Campo Tipo, tamaño Descripción
ticket_id alfanumérico Número del certificado al que pertenece la dirección
id numérico Identificador del asegurado en la póliza.
birthdate fecha/hora ANSI Fecha de nacimiento (yyyy-mm-dd)
firstname alfanumérico Nombres del asegurado
lastname alfanumérico Apellidos del asegurado
identity alfanumérico Cédula de identidad del asegurado
passport alfanumérico Número de pasaporte del asegurado
sex Alfanumérico Sexo del asegurado (M/F)
Versión 3.7 (Nov-2024) Desarrollada por Página 128 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
El métodos que se muestra a continuación permite
anular pólizas de seguro emitidas. Asegúrese de hacer la
petición con el identificador correcto y evitar así afectar
otras pólizas. Validar la póliza correcta es su responsabilidad.
Recuerde: Todas sus acciones quedan auditadas
POST /api/ticket/ticket_id/cancel
La respuesta del servidor será en todos estos casos el código 204 sin contenido, en caso de que la
petición haya sido ejecutada con éxito.
Parámetros requeridos:
Tipos int: entero
dec: decimal
string: alfanumérico date: fecha ANSI
text: 255 caracteres
Campo Tipo, tamaño Descripción
ticket_id alfanumérico Número del certificado
Versión 3.7 (Nov-2024) Desarrollada por Página 129 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Reportes
Versión 3.7 (Nov-2024) Desarrollada por Página 130 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Se denominan Reportes aquellas consultas que, a diferencia de las vistas hasta ahora, son limitadas
en cuanto a los filtros que se pueden aplicar y no aceptan los atributos data{}, values{} o
addresses{}, por mencionar algunos, no obstante, mantienen la funcionalidad de paginación para
mejorar el peso de la consulta.
El resultado de la consulta siempre se devolverá en formato JSON (como todas las consultas de la
API) y en adición se puede contar con una versión en archivo con formato csv.
La consulta está limitada por las reglas de negocio establecidas para canales de venta y
vendedores. Para mayores detalles consulte “Acerca de canales de venta y vendedores”
Versión 3.7 (Nov-2024) Desarrollada por Página 131 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/report/costs?from=2022-06-01&to=2022-06-30
Se recomienda filtrar las consultas de este tipo al menos
con un rango de fecha (from/to). Enviar la consulta sin
parámetros podría ralentizas la respuesta y aumentar el tráfico
de la red al manejar grandes volúmenes de datos.
Parámetros aceptados:
from Fecha ANSI (yyyy-mm-dd) Fecha de emisión desde
to Fecha ANSI (yyyy-mm-dd) Fecha de emisión hasta
agency_id alfanumérico Código de agencia que emitió el certificado
region_id numérico ID de la región a la que pertenece la(s)
agencia(s) de los certificados
Respuesta:
Por cada elemento de records, se incluye:
ticket_id Numero del certificado emitido en el período indicado
agency_id Código del productor o agencia
agency Nombre del productor o agencia
illness Monto del costo por enfermedad
accident Monto del costo por accidente
accidental_death Monto del costo por muerte accidental
retention Monto del costo de la retención aplicada
intermediation Monto del costo de intermediación
Versión 3.7 (Nov-2024) Desarrollada por Página 132 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
total Monto de los costos totales aplicados al certificado
Ejemplo
{
"records": [
{
"ticket_id": "00008378",
"date": "2022-06-01 12:34:54",
"cancel": null,
"agency_id": "00655",
"agency": "VENTAS ONLINE",
"illness": 40.9029,
"accident": 0,
"accidental_death": 0,
"retention": 9.8901,
"intermediation": 22.2,
"total": 72.99
},
{
"ticket_id": "00008379",
"date": "2022-06-01 12:51:49",
"cancel": null,
"agency_id": "00803",
"agency": "GLOBALTOURS",
"illness": 29.3139,
"accident": 0,
"accidental_death": 0,
"retention": 12.5631,
"intermediation": 28.2,
"total": 70.08
},
{
"ticket_id": "00008387",
"date": "2022-06-02 10:44:13",
"cancel": null,
"agency_id": "99997",
"agency": "TROTAMUNDOS",
"illness": 1.516,
"accident": 0,
"accidental_death": 0,
"retention": 0.65,
"intermediation": 0.5416,
"total": 2.71
}
],
Versión 3.7 (Nov-2024) Desarrollada por Página 133 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
...
"pagination": {
"total": 33,
"pages": 4,
"previous": false,
"next": true
}
}
Versión 3.7 (Nov-2024) Desarrollada por Página 134 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/report/costs?region_id=5&from=2022-06-
01&to=2022-06-30
Se recomienda filtrar las consultas de este tipo al menos
con un rango de fecha (from/to). Enviar la consulta sin
parámetros podría ralentizas la respuesta y aumentar el tráfico
de la red al manejar grandes volúmenes de datos.
Parámetros aceptados:
from Fecha ANSI (yyyy-mm-dd) Fecha de emisión desde
to Fecha ANSI (yyyy-mm-dd) Fecha de emisión hasta
agency_id alfanumérico Código de agencia que emitió el certificado
region_id numérico ID de la región a la que pertenece la(s)
agencia(s) de los certificados
Respuesta:
Por cada elemento de records, se incluye:
ticket_id Numero del certificado emitido en el período indicado
agency_id Código del productor o agencia
agency Nombre del productor o agencia
illness Monto del costo por enfermedad
accident Monto del costo por accidente
accidental_death Monto del costo por muerte accidental
Versión 3.7 (Nov-2024) Desarrollada por Página 135 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
retention Monto del costo de la retención aplicada
intermediation Monto del costo de intermediación
total Monto de los costos totales aplicados al certificado
Ejemplo
{
"records": [
{
"ticket_id": "00008379",
"date": "2022-06-01 12:51:49",
"cancel": null,
"agency_id": "00803",
"agency": "GLOBALTOURS",
"illness": 29.3139,
"accident": 0,
"accidental_death": 0,
"retention": 12.5631,
"intermediation": 28.2,
"total": 70.08
},
...
"pagination": {
"total": 14,
"pages": 2,
"previous": false,
"next": true
}
}
Versión 3.7 (Nov-2024) Desarrollada por Página 136 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/report/values?from=2022-06-01&to=2022-06-30
Se recomienda filtrar las consultas de este tipo al menos
con un rango de fecha (from/to). Enviar la consulta sin
parámetros podría ralentizas la respuesta y aumentar el tráfico
de la red al manejar grandes volúmenes de datos.
Parámetros aceptados:
from Fecha ANSI (yyyy-mm-dd) Fecha de emisión desde
to Fecha ANSI (yyyy-mm-dd) Fecha de emisión hasta
agency_id alfanumérico Código de agencia que emitió el certificado
region_id numérico ID de la región a la que pertenece la(s)
agencia(s) de los certificados
Respuesta:
Por cada elemento de records, se incluye:
ticket_id Número del certificado emitido en el período indicado
date Fecha y hora de emisión del certificado
cancel Fecha y hora de cancelación (en caso de que fuera cancelado)
agency_id Código del productor o agencia
agency Nombre del productor o agencia
amount Monto del certificado según tarifa aplicada
discount Monto del descuento aplicado para facturar
tax Monto del impuesto aplicado para facturar
Versión 3.7 (Nov-2024) Desarrollada por Página 137 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
total Monto facturado del certificado
Ejemplo
{
"records": [
{
"ticket_id": "00008378",
"date": "2022-06-01 12:34:54",
"cancel": null,
"agency_id": "00655",
"agency": "VENTAS ONLINE",
"amount": 141,
"discount": 0,
"tax": 0,
"total": 141
},
{
"ticket_id": "00008379",
"date": "2022-06-01 12:51:49",
"cancel": null,
"agency_id": "00803",
"agency": "GLOBALTOURS",
"amount": 67,
"discount": 0,
"tax": 0,
"total": 67
},
],
...
"pagination": {
"total": 33,
"pages": 4,
"previous": false,
"next": true
}
}
Versión 3.7 (Nov-2024) Desarrollada por Página 138 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/report/cardnet?from=2022-05-16&to=2022-06-10
Se recomienda filtrar las consultas de este tipo al menos
con un rango de fecha (from/to). Enviar la consulta sin
parámetros podría ralentizas la respuesta y aumentar el tráfico
de la red al manejar grandes volúmenes de datos.
Parámetros aceptados:
from Fecha ANSI (yyyy-mm-dd) Fecha de emisión desde
to Fecha ANSI (yyyy-mm-dd) Fecha de emisión hasta
agency_id alfanumérico Código de agencia que emitió el certificado
Respuesta:
Por cada elemento de records, se incluye:
id Código del productor o agencia
reference Tipo de transacción afectada
reference_id Número de la transacción afectada
currency_id Código de la moneda en la que se realizó el pago
currency Nombre de la moneda en la que se realizó el pago
Versión 3.7 (Nov-2024) Desarrollada por Página 139 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
amount Monto del pago2
agency_id Código del productor o agencia
agency Nombre del productor o agencia
created_at Fecha y hora en la que se realizó el pago en formato ANSI
(yyyy-mm-dd hh:mm:ss)
response_code Código de respuesta del suplidor CARDNET
Ver anexo “Códigos de respuesta CARDNET”
authorization_code Número de la autorización otorgada por el suplidor CARDNET
En los casos en que la transacción no se haya completado el
campo mostrará “N/A”
credit_card_number Número enmascarado de la tarjeta de crédito o débito
empleada. Se reciben los primero 6 y últimos 4 dígitos
legibles, el resto llega enmascarado.
retrieval_reference_number Número de referencia único asignado por el suplidor
CARDNET.
Ejemplo
{
"records": [
{
"id": "24",
"reference": "CERTIFICADO",
"reference_id": "00005606",
"currency_id": "214",
"currency": "RD$",
"amount": 77.63,
"agency_id": "99997",
"agency ": "VENTAS ONLINE",
"created_at": "2022-05-16 21:18:01",
"response_code": "00",
"authorization_code": "874313",
"credit_card_number": "548925******5583",
"retrieval_reference_number": "767454430134"
},
{
"id": "25",
"reference": "CERTIFICADO",
2 Este monto puede estar afectado por el cálculo de la tasa de cambio vigente para el momento del pago.
Versión 3.7 (Nov-2024) Desarrollada por Página 140 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
"reference_id": "00005607",
"currency_id": "214",
"currency": "RD$",
"amount": 77.63,
"agency_id": "99997",
"agency ": "VENTAS ONLINE",
"created_at": "2022-05-16 21:19:08",
"response_code": "TF",
"authorization_code": "N/A",
"credit_card_number": "476134______0050",
"retrieval_reference_number": "000000000104"
},
{
"id": "27",
"reference": "CERTIFICADO",
"reference_id": "00005607",
"currency_id": "214",
"currency": "RD$",
"amount": 77.63,
"agency_id": "99997",
"agency ": "VENTAS ONLINE",
"created_at": "2022-05-16 21:23:54",
"response_code": "00",
"authorization_code": "007281",
"credit_card_number": "546134______2700",
"retrieval_reference_number": "000000024709"
},
...
],
"pagination": {
"total": 16,
"pages": 2,
"previous": false,
"next": true
}
}
Versión 3.7 (Nov-2024) Desarrollada por Página 141 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/report/cardnet/export?from=2022-05-
16&to=2022-06-10
Se recomienda filtrar las consultas de este tipo al menos
con un rango de fecha (from/to). Enviar la consulta sin
parámetros podría ralentizas la respuesta y aumentar el tráfico
de la red al manejar grandes volúmenes de datos.
Parámetros aceptados:
from Fecha ANSI (yyyy-mm-dd) Fecha de emisión desde
to Fecha ANSI (yyyy-mm-dd) Fecha de emisión hasta
region_id numérico Código de la región que agrupa los
productores que emitieron certificados
agency_id alfanumérico Código de agencia que emitió el certificado
Respuesta:
Por cada elemento del archivo csv, se incluye:
id Código del productor o agencia
reference Tipo de transacción afectada
Versión 3.7 (Nov-2024) Desarrollada por Página 142 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
reference_id Número de la transacción afectada
currency_id Código de la moneda en la que se realizó el pago
currency Nombre de la moneda en la que se realizó el pago
amount Monto del pago3
agency_id Código del productor o agencia
agency Nombre del productor o agencia
created_at Fecha y hora en la que se realizó el pago en formato ANSI
(yyyy-mm-dd hh:mm:ss)
response_code Código de respuesta del suplidor CARDNET
Ver anexo “Códigos de respuesta CARDNET”
authorization_code Número de la autorización otorgada por el suplidor CARDNET
En los casos en que la transacción no se haya completado el
campo mostrará “N/A”
credit_card_number Número enmascarado de la tarjeta de crédito o débito
empleada. Se reciben los primero 6 y últimos 4 dígitos
legibles, el resto llega enmascarado.
retrieval_reference_number Número de referencia único asignado por el suplidor
CARDNET.
Ejemplo
"Seguros Sin Fronteras"
"Transacciones CardNET"
"Usuario","SERVICIOS API"
"Fecha","15/06/2022 15:12 PM"
"Criterio de filtrado"
"","Fecha de emisión entre 16/05/2022 y 10/06/2022"
"Código de Agencia","Agencia","Fecha de emisión","Referencia","Referencia
Número","Monto","Tarjeta","Código Autorización","Código de respuesta","Respuesta"
"99997","VENTAS ONLINE","2022-05-16
21:18:01","COTIZACIÓN","5699","77.63","548925******5583","874313","00","Aprobada"
"99997","VENTAS ONLINE","2022-05-16
21:19:08","COTIZACIÓN","5700","77.63","476134______0050","N/A","TF","Solicitud de
autenticación rechazada o no completada."
"99997","VENTAS ONLINE","2022-05-16
21:23:54","COTIZACIÓN","5700","77.63","546134______2700","007281","00","Aprobada"
3 Este monto puede estar afectado por el cálculo de la tasa de cambio vigente para el momento del pago.
Versión 3.7 (Nov-2024) Desarrollada por Página 143 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
"99997","VENTAS ONLINE","2022-05-17
08:42:08","COTIZACIÓN","5701","77.63","545569******4588","952412","00","Aprobada"
"99997","VENTAS ONLINE","2022-05-17
08:47:30","COTIZACIÓN","5702","77.63","546134______2700","007283","00","Aprobada"
"99997","VENTAS ONLINE","2022-05-25
10:02:08","COTIZACIÓN","8476","77.63","461882*****4443","150703","00","Aprobada"
"99997","VENTAS ONLINE","2022-05-25
10:13:56","COTIZACIÓN","8477","77.63","476134______0050","019920","00","Aprobada"
"99997","VENTAS ONLINE","2022-05-25
10:18:25","COTIZACIÓN","8478","77.63","476134______0050","N/A","51","Fondos insuficientes"
"99997","VENTAS ONLINE","2022-05-25
10:21:44","COTIZACIÓN","8478","77.63","476134______0050","N/A","51","Fondos insuficientes"
"99997","VENTAS ONLINE","2022-05-25
10:23:21","COTIZACIÓN","8478","77.63","546134______0050","007623","00","Aprobada"
"99997","VENTAS ONLINE","2022-05-25
16:29:52","COTIZACIÓN","8484","77.63","546134______0050","007635","00","Aprobada"
"99992","INTELIGROUP","2022-05-26
13:44:58","COTIZACIÓN","8490","2587.5","545465******7321","146193","00","Aprobada"
"99992","INTELIGROUP","2022-05-30
17:40:30","COTIZACIÓN","8492","2702.5","542278*****4678","979444","00","Aprobada"
"99992","INTELIGROUP","2022-05-30
17:50:06","COTIZACIÓN","8493","2645","445590**3456","410423","00","Aprobada"
"99997","VENTAS ONLINE","2022-06-01
16:43:05","COTIZACIÓN","8508","76.95","546134______2700","007844","00","Aprobada"
"99997","VENTAS ONLINE","2022-06-07
20:03:36","COTIZACIÓN","8520","76.95","556865*****9256","751462","00","Aprobada"
Versión 3.7 (Nov-2024) Desarrollada por Página 144 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
GET /api/report/invoice?from=2022-07-15&to=2022-07-15
Se recomienda filtrar las consultas de este tipo al menos
con un rango de fecha (from/to). Enviar la consulta sin
parámetros podría ralentizas la respuesta y aumentar el tráfico
de la red al manejar grandes volúmenes de datos.
Parámetros aceptados:
from Fecha ANSI (yyyy-mm-dd) Fecha de emisión desde de la factura
to Fecha ANSI (yyyy-mm-dd) Fecha de emisión hasta de la factura
region_id numérico Código de la región que agrupa los
productores que emitieron certificados
agency_id alfanumérico Código de agencia que emitió el certificado
Respuesta:
Por cada elemento del archivo csv, se incluye:
id Código interno de la factura
invoice_id Número de la factura
agency_id Código del productor o agencia
agency Nombre del productor o agencia
ncf_type Tipo de Comprobante Fiscal aplicado a la factura
ncf Nombre del Comprobante Fiscal aplicado a la factura
ncf_number Número del Comprobante Fiscal aplicado a la factura
Versión 3.7 (Nov-2024) Desarrollada por Página 145 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
ncf_due_date Fecha de vencimiento del Comprobante Fiscal aplicado a la
factura
legal_id Número de RNC del deudor de la factura
customer Nombre del deudor de la factura
address Dirección del deudor de la factura
phone Teléfono del deudor de la factura
email Correo electrónico del deudor de la factura
currency_id Código de la moneda en que se realizó la factura
exchange Tasa de cambio aplicada al momento de emisión de la factura
total Monto total facturado
date Fecha y hora de emisión de la factura
reference Tipo de operación facturada
tickets Arreglo de certificados que cubre la factura
Ejemplo
{
"records": [
{ "id": "28",
"invoice_id": "1000026",
"agency_id": "99992",
"agency": "PRUEBA",
"ncf_type": "01",
"ncf": "FACTURA CREDITO FISCAL",
"ncf_number": "X0100000001",
"ncf_due_date": "2099-12-31",
"legal_id": "123456789",
"customer": "JUAN PEREZ",
"address": "AV SARASOTA\r\nCENTRO COMERCIAL BELLA VISTA\r\nSANTO DOMINGO. DN. ",
"phone": "809-625-5555",
"email": "deudor@micorreo.com",
"currency_id": "840",
"exchange": 1,
"total": 41,
"date": "2022-07-05 14:34:06",
"reference": "ticket",
"tickets": [
"00008412"
]
},
{
"id": "29",
Versión 3.7 (Nov-2024) Desarrollada por Página 146 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
"invoice_id": "1000027",
"agency_id": "99992",
"agency": "PRUEBA",
"ncf_type": "01",
"ncf": "FACTURA CREDITO FISCAL",
"ncf_number": "X0100000002",
"ncf_due_date": "2099-12-31",
"legal_id": "130-555-55555555",
"customer": "CREDIMATIC SRL",
"address": "AV. VALLES DE ARAGUA #45\r\nENSANCHE MIS SUEÑOS\r\nREP. DOMINICANA",
"phone": "849-600-1100",
"email": "credimatic@micorreo.com ",
"currency_id": "840",
"exchange": 1,
"total": 46,
"date": "2022-07-05 18:22:12",
"reference": "ticket",
"tickets": [
"00008414"
]
}
],
"pagination": {
"total": 2,
"pages": 1,
"previous": false,
"next": false
}
}
Versión 3.7 (Nov-2024) Desarrollada por Página 147 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Solución de
problemas
Versión 3.7 (Nov-2024) Desarrollada por Página 148 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
{
"code": 1,
"message": "Al menos una persona entre las indicadas posee un producto básico
activo",
"found": [
{
"ticket_id": "09230151",
"identity": "00121944790",
"passport": "PASS67135",
"firstname": "Roxanne",
"lastname": "Schiller",
"birthdate": "1963-06-14"
}
],
"uri": "http://<uri>/api/issue/retail/09230757/confirm-insured"
}
Respuesta
El servidor ha rechazado la solicitud debido a que el (los) asegurado (s) indicado (s) en el json
tiene (n) póliza (s) vigente (s), lo que rompe con las Políticas del servicio (ver Reglas de Negocio).
Solución:
Consulte al Administrador del Sistema
Versión 3.7 (Nov-2024) Desarrollada por Página 149 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
{
"error": true,
"message": {
"insured": [
"Arreglo de asegurados es inválido",
]
}
Respuesta
El servidor ha rechazado la solicitud debido a que el (los) asegurado (s) indicado (s) en el json no
cumple con los requerimientos de tipo de campo o tamaño.
Solución:
Revise la solicitud contra los requerimientos y haga los ajustes necesarios.
{
"error": true,
"message": {
"address": [
"Arreglo de direcciones es inválido",
]
}
Respuesta
El servidor ha rechazado la solicitud debido a que el (las) dirección (es) indicada (s) en el json no
cumple con los requerimientos de tipo de campo o tamaño.
Versión 3.7 (Nov-2024) Desarrollada por Página 150 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Solución:
Revise la solicitud contra los requerimientos y haga los ajustes necesarios.
{
"error": true,
"message": {
"products": [
"Arreglo de productos es inválido",
]
}
Respuesta
El servidor ha rechazado la solicitud debido a que el (los) producto (s) indicado (s) en el json no
cumple con los requerimientos de tipo de campo o tamaño.
Solución:
Revise la solicitud contra los requerimientos y haga los ajustes necesarios.
{
"error": true,
"message": {
"from": [
"from no corresponde al formato Y-m-d"
]
}
}
Versión 3.7 (Nov-2024) Desarrollada por Página 151 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Respuesta
El servidor ha rechazado el formato de fecha enviado en el parámetro “from”
Solución:
Asegúrese de enviar el parámetro en formato ANSI (yyyy-mm-dd). Ejemplo: “2020-02-29”
Respuesta 1
La solicitud ha sido rechazada debido a la falta de parámetros requeridos cuando se intentó
ejecutar una transacción. En todos los casos se devuelve código de error: true como se indica a
continuación (el ejemplo se refiere al código del productor)
{
"error": true,
"message": {
"agency_id": [
"El campo agency id es obligatorio."
]
}
}
Otros campos son tratados de la misma manera:
{
"error": true,
"message": {
"agency_id": [
"El campo agency id es obligatorio."
],
"salesman_id": [
"El campo salesman id es obligatorio."
],
"products": [
Versión 3.7 (Nov-2024) Desarrollada por Página 152 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
"El campo products es obligatorio."
],
"product_ids": [
"El campo product ids es obligatorio."
],
"destination_id": [
"El campo destination_id es obligatorio."
],
"from": [
"El campo from es obligatorio."
],
"to": [
"El campo to es obligatorio."
],
"insured": [
"El campo insured es obligatorio."
],
"addresses": [
"El campo addresses es obligatorio."
]
}
}
Respuesta 2
Hay casos específicos donde el mensaje de error ocurre porque los datos que se envían no tienen
una carga útil de tamaño significativa, en esos casos considere el content-type “application/x-
www-form-urlencoded” en lugar de “multipart/form-data”, una explicación más detallada sobre
esto se encuentra en “Construcción de consultas/Paso de parámetros”.
{
"error": true,
"message": "El certificado ya ha sido cancelado"
}
Versión 3.7 (Nov-2024) Desarrollada por Página 153 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Respuesta
El servidor ha rechazado la solicitud debido a que la póliza indicada para anular ya se encuentra
en estado anulado
Solución:
Compruebe el estado del certificado a través de una consulta.
{
"error": true,
"message": "La agencia PRUEBA no tiene balance para emitir a crédito."
}
Respuesta
El servidor ha rechazado la solicitud debido a que el productor indicado no posee balance
disponible en su línea de crédito para cubrir completamente el pago de la póliza.
Solución:
Contacte al ejecutivo de cuenta para más detalles.
{
"error": true,
"message": [
Versión 3.7 (Nov-2024) Desarrollada por Página 154 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
"El destino es inválido o no esta disponible."
]
}
Respuesta
El servidor ha rechazado la solicitud debido a que el código ISO 3166-1 del país que ha enviado es
incorrecto, o no está disponible para su asignación como destino válido de una póliza.
Solución:
Vea Consulta de países para conocer la lista de países admitidos o contacte a su ejecutivo de
cuenta
{
"error": true,
"message": {
"ncf_id": [
"ncf id es inválido."
]
}
}
Respuesta
El servidor ha rechazado la solicitud debido a que no se recibió el tipo de comprobante fiscal a
utilizar en el encabezado de la factura o se indicó un tipo de comprobante fiscal incorrecto.
Solución:
1. Verifique que el parámetro ncf_id sea uno de los valores proporcionados en la tabla
Códigos de Tipo de NCF.
Versión 3.7 (Nov-2024) Desarrollada por Página 155 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
{
"error": true,
"message": {
"0": "No existen tarifas disponibles para su selección"
}
}
Respuesta
El servidor ha rechazado la solicitud debido a que no encontró ninguna tarifa del producto base o
complementario que cumpla con los requisitos de período o edad del (los) asegurado (s)
indicado (s).
Solución:
2. 3. 4. 5. Verifique el período (from - to)
Verifique la edad de los asegurados (birthdate)
Verifique el valor del producto complementario (en caso de que lo esté incluyendo), este
debe ser igual a la etiqueta que aparece en la columna complemento de la tarifa
contacte al ejecutivo de cuenta para más detalles.
{
"error": true,
"message": "No se encontraron datos usando sus criterios"
}
Versión 3.7 (Nov-2024) Desarrollada por Página 156 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Respuesta
La consulta no produjo resultados con el criterio indicado. En caso de que no se haya indicado
criterios de filtrado, entonces no se tiene acceso a los datos.
Solución:
Contacte al ejecutivo de cuenta para más detalles.
{
"error": true,
"message": " No se pudo procesar su solicitud "
}
Respuesta
La consulta incluye un atributo no permitido. Probablemente se intenta utilizar data{} o
values{} sin que esté permitido para la consulta.
Solución:
Revise la consulta y haga las correcciones de lugar
Method Not Allowed
Versión 3.7 (Nov-2024) Desarrollada por Página 157 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Respuesta
La solicitud pudiera estar utilizando el método POST cuando en realidad solo permite el método
GET o viceversa.
Solución:
Verifique que utiliza el método correcto: GET o POST.
{
"error": true,
"message": "Not Found"
}
Respuesta
1. La consulta hace una llamada a un método no existente en GAPI.
2. La consulta intenta acceder a un registro no existente.
Solución:
1. Verifique la documentación de GAPI y asegúrese de que utiliza el método correcto.
2. Asegúrese de que intenta obtener el registro correcto.
{
"error": true,
"message": {
"salesman_id": [
"salesman id es inválido"
Versión 3.7 (Nov-2024) Desarrollada por Página 158 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
]
}
}
Respuesta
El servidor ha rechazado la solicitud debido a que no encontró un vendedor con el id
suministrado
Solución:
1. 2. 3. Verifique que usa el id del usuario (vendedor) en lugar del código interno
Verifique que el usuario (vendedor) está asociado a la agencia que realizará la emisión
Contacte al ejecutivo de cuenta para más detalles.
{
"message": [
"Token expirado"
]
}
Respuesta
Los toques emitidos por GAPI tienen una vigencia de 5 minutos, cualquier consulta que se realice
utilizando un token después de expirada su vigencia, obtendrán este mensaje.
Solución:
Solicite un nuevo token.
Versión 3.7 (Nov-2024) Desarrollada por Página 159 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
{
"message": "Usted no tiene acceso a esta acción"
}
Respuesta
Los privilegios de la cuenta utilizada no permiten acceder a la consulta solicitada.
Solución:
Asegúrese de que sus privilegios le permiten acceder a la consulta. Contacte a su ejecutivo de
cuenta para más detalles.
Versión 3.7 (Nov-2024) Desarrollada por Página 160 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Glosario de
Términos
Versión 3.7 (Nov-2024) Desarrollada por Página 161 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Agencia: Ver Canal de ventas/
Asegurado (pasajero): Persona cubierta por un certificado de seguro de viaje.
Canal de ventas (agencia o productor): Medio utilizado por GOVAL-Web para comercializar
productos de seguro de viaje.
Cancelación (anulación): Evento que anula un seguro de viaje emitido.
Certificado de seguro de viaje: Documento electrónico que acredita un seguro de viaje emitido.
Contiene la información relacionada al viaje, su vigencia, productos, coberturas y condiciones
generales y particulares.
Certificado precompra: Una de las modalidades de emisión de seguros de viaje donde el cliente
adquiere una cantidad de días anticipadamente para un producto específico, que puede consumir
durante un año con diversos asegurados.
Certificado retail: Una de las modalidades de emisión de seguros de viaje a demanda. Requiere
pago para completar la emisión.
Certificado cancelado: En el contexto de GOVAL-Web, es un seguro de viaje anulado.
Certificado vigente: En el contexto de GOVAL-Web, es un seguro de viaje donde su “fecha de salida”
entró en vigor y que no ha alcanzado su “fecha de regreso”.
Cobertura: Protección que brinda los productos de seguro de viaje expresados en un conjunto de
beneficios con límites y sublímites.
Coordinador: En el contexto de GOVAL-Web, es el usuario que gestiona los canales de venta
asegurando que cuenten con todas las herramientas para su manejo.
cURL: Herramienta de línea de comandos para obtener o enviar datos utilizando la sintaxis de URL.
Si trabaja como desarrollador o en la función de soporte, el comando cURL le ayuda a solucionar
problemas de aplicaciones web.
Formato .csv: Formato de almacenamiento para archivos que puede ser leídos por Microsoft
Excel®, LibreOffice®, Apache OpenOffice® , etc.
Formato .pdf: Formato de almacenamiento para documentos digitales independiente de
plataformas de software o hardware, lanzado como estándar abierto en julio de 2008 y publicado
por la Organización Internacional de Estandarización (ISO) como ISO 32000-1.
Versión 3.7 (Nov-2024) Desarrollada por Página 162 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Formato .xml: Formato de almacenamiento que puede ser utilizado para representar la
información transaccional de GOVAL-Web de forma estructurada de modo que pueda ser
almacenada, transmitida, procesada, visualizada e impresa, por diversos tipos de aplicaciones y
dispositivos.
GAPI: Siglas de GOVAL-Web Application Programming Interface (Interfaz de Programación de
Aplicaciones de GOVAL-Web. Conjunto de rutinas, funciones y procedimientos (métodos) que
permite utilizar recursos de la plataforma GOVAL-Web, sirviendo como una capa de abstracción o
intermediario.
localhost: En el contexto de redes TCP/IP, localhost es un nombre reservado que tienen todas las
computadoras, routers o dispositivos independientemente de que dispongan o no de una tarjeta
de red ethernet.
login: En el ámbito de seguridad informática, log in o log on es el proceso que controla el acceso
individual a un sistema informático mediante la identificación del usuario utilizando credenciales
provistas por el usuario.
pasajero Ver asegurado.
password (contraseña o clave): Forma de autentificación que utiliza información secreta para
controlar el acceso hacia algún recurso. La contraseña debe mantenerse en secreto ante aquellos
a quien no se les permite el acceso.
Póliza: Ver Certificado de Seguro de Viaje.
Producto: En el contexto del seguro de viaje, es un producto asegurador que permite al
asegurado realizar viajes protegido y despreocupado para así poder disfrutar del mismo.
Producto base: Producto que incluye coberturas tradicionales de viaje tales como: pérdida de
vuelo, pérdida de equipaje, enfermedad, etc.
Producto complementario: Producto que cubre necesidades específicas del viaje ampliando la
cobertura estándar, tales como: cancelación de viaje, cobertura por COVID-19, deportes
extremos, etc.
Productor: Ver canal de ventas.
RNC: Número de identificación del Registro Nacional de Contribuyente, dependiendo del país en
que ha sido configurado GOVAL-Web. Este campo puede recibir otros nombres tales como RUC
(Registro Único de Contribuyente), RIF (Registro de Información Fiscal), etc. En todos los casos,
Versión 3.7 (Nov-2024) Desarrollada por Página 163 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
este campo se refiere a un valor que sirve para identificar a la persona jurídica o física ante la
Administración Tributaria del país. Esta información será la que aparecerá en las facturas
emitidas a nombre del canal de ventas.
Vendedor: En el contexto de GOVAL-Web, es el usuario que realiza la emisión de un seguro de
viaje.
Web Token (JSON Web Token o simplemente JWT): Estándar abierto (RFC 7519) que define una
forma compacta y autónoma de transmitir información de forma segura entre las partes como un
objeto JSON. Esta información se puede verificar y confiar en ella porque está firmada
digitalmente.
Versión 3.7 (Nov-2024) Desarrollada por Página 164 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
Anexos
Versión 3.7 (Nov-2024) Desarrollada por Página 165 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
RESPONSE
CODE DESCRIPCIÓN CLIENTE RESPONSE
CODE DESCRIPCIÓN CLIENTE
00 Aprobada 39 Tarjeta Invalida
01 Llamar al Banco 40 Función no Soportada
02 Llamar al Banco 41 Transacción No Aprobada
03 Comercio Invalido 42 Cuenta Invalida
04 Rechazada 43 Transacción No Aprobada
05 Rechazada 44 No investment account
06 Error en Mensaje 51 Fondos insuficientes
07 Tarjeta Rechazada 52 Cuenta Invalidad
08 Llamar al Banco 53 Cuenta Invalidad
09 Request in progress 54 Tarjeta vencida
10 Aprobación Parcial 56 Cuenta Invalidad
11 Approved VIP 57 Transacción no permitida
12 Transacción Invalida 58 Transacción no permitida
en terminal
13 Monto Invalido 60 Contactar Adquirente
14 Cuenta Invalida 61 Excedió Limte de Retiro
15 No such issuer 62 Tarjeta Restringida
16 Approved update track 3 65 Excedió Cantidad de
Intento
17 Customer cancellation 66 Contactar Adquirente
18 Customer dispute 67 Hard capture
19 Reintentar Transacción 68 Response received too late
20 No tomo acción 75 Pin excedió Limite de
Intentos
21 No tomo acción 77 Captura de Lote Invalida
22 Transacción No Aprobada 78 Intervención del Banco
Requerida
23 Transacción No Aceptada 79 Rechazada
24 File update not supported 81 Pin invalido
25 Unable to locate record 82 PIN Required
26 Duplicate record 85 Llaves no disponibles
Versión 3.7 (Nov-2024) Desarrollada por Página 166 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
RESPONSE
CODE DESCRIPCIÓN CLIENTE RESPONSE
CODE DESCRIPCIÓN CLIENTE
27 File update edit error 89 Terminal Invalida
28 File update file locked 90 Cierre en proceso
30 File update failed 91 Host No Disponible
31 Bin no soportado 92 Error de Ruteo
32 Tx. Completada
Parcialmente
94 Duplicate Transaction
33 Tarjeta Expirada 95 Error de Reconciliación
34 Transacción No Aprobada 96 Error de Sistema
35 Transacción No Aprobada 97 Emisor no Disponible
36 Transacción No Aprobada 98 Excede Límite de Efectivo
37 Transacción No Aprobada 99 CVV or CVC Error response
38 Transacción No Aprobada TF Solicitud de autenticación
rechazada o no
completada.
Versión 3.7 (Nov-2024) Desarrollada por Página 167 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
ID Tipo Nombre Para
Facturar
1 01 FACTURA CREDITO FISCAL 1
2 02 FACTURA CONSUMIDOR FINAL 1
3 03 NOTA DE DEBITO 0
4 04 NOTA DE CREDITO POR DEVOLUCION 0
5 05 PROVEEDOR INFORMAL 0
6 06 REGISTRO UNICO INGRESO 0
7 07 REGISTRO GASTOS MENORES 0
8 14 FACTURA EMPRESAS REGIMENES
ESPECIALES
1
9 15 INSTITUCION GUBERNAMENTAL 1
Versión 3.7 (Nov-2024) Desarrollada por Página 168 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
La siguiente tabla tiene por objeto evaluar si se ha cumplido con la Reglas del Negocio para emitir
un seguro de viaje. Utilícela siempre antes de solicitar asistencia técnica.
7
10 11 12 13 14
1 El usuario de GAPI que utilizo ha sido autenticado correctamente y tengo un
token vigente que es el que utilizo para emitir el seguro de viajes.
2 Me he asegurado de que todo el proceso se ha ejecutado antes de que el token
de GAPI haya vencido
3 El productor está correctamente identificado, (uso el id y no el
internal_code).
4 El productor está activo y su balance en la línea de crédito cubre
completamente la tarifa del seguro de viaje.
5 El (los) producto (s) indicado (s) está (n) correctamente identificado (s), (uso el
id y no el internal_code).
6 El (los) producto (s) indicado (s) está (n) asociado (s) al productor.
He indicado solo un producto base y de haber indicado producto (s)
complementario (s) me he asegurado de suministrar toda la información
requerida por esto (s).
8 El usuario vendedor está correctamente identificado, (uso el id y no el
internal_code).
9 El usuario vendedor está asociado al productor de la emisión o a la región a la
que pertenece el productor.
La fecha de inicio de la cobertura del seguro de viaje inicia posterior a la fecha
en que se realiza la emisión del seguro.
El país de destino está correctamente identificado, (uso el id).
He suministrado todos los datos de los asegurados
Los asegurados están correctamente identificados (uso id , passport o
ambos parámetros)
He suministrado las fechas de nacimiento de los asegurados en el formato
indicado, también he suministrado el sexo de los asegurados en las opciones
disponible.
Versión 3.7 (Nov-2024) Desarrollada por Página 169 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
15 16 He suministrado al menos una dirección completa
He suministrado toda la información de encabezado de factura


REGLAS DEL NEGOCIO: 
Este paso asegura que todos los parámetros requeridos han sido recibidos y que las validaciones
iniciales son satisfechas, estas son:
Productor existe y está activo
Vendedor existe, está activo y está asociado al productor.
Emisión cumple con las reglas del Negocio
a) b) c) d) e) f) Se han suministrado todos los datos de asegurado (s).
Se ha suministrado todos los datos requeridos para el contacto principal
Se ha suministrado al menos un contacto para casos de emergencia

Las Reglas del Negocio en GAPI describen las políticas, normas, operaciones, definiciones y
restricciones que GOVAL ha incluido y que son de vital importancia para alcanzar los objetivos
contractuales con el cliente.
Considere este documento un modelo general sobre el que se fundamenta la
operación de seguro de viajes gestionada por Goval-Web:
El proceso de suscripción en GAPI está regido por las siguientes políticas:
1. 2. 3. 4. 5. 6. 7. 8. 9. Solo se emiten seguros de viaje a personas que no posean otro seguro de viaje vigente.
Todos los asegurados incluidos en el certificado deben estar plenamente identificados.
Solo se emiten seguros de viaje con al menos 24 horas de anticipación a la fecha/hora de
salida.
El seguro de viaje solo se emite en el país de origen del viaje.
No se extiende ni se reduce la vigencia de un seguro de viaje.
Los cambios de fecha pueden realizarse siempre que se mantenga la misma cantidad de
días de cobertura y únicamente si el período de vigencia no ha iniciado.
No se incluyen o excluyen personas a un seguro de viaje emitido.
La cancelación (anulación) de un seguro de viaje aplica para todos los asegurados incluidos.
La cobertura del seguro de viaje aplica por igual a todos los asegurados incluidos, salvo que
condiciones particulares del producto establezcan límites de edad y/o género.
10. No se realizan modificaciones a la cobertura del seguro de viaje una vez éste ha sido
emitido.
Versión 3.7 (Nov-2024) Desarrollada por Página 99 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
11. La elegibilidad de algunos productos está sujeta al suministro de información adicional
específica.
1. La cotización debe ser un proceso simplificado con el único propósito de conocer, y
opcionalmente comparar, las coberturas de los productos cotizados y sus tarifas.
2. Toda cotización emitida tiene una vigencia de 30 días calendario, contados a partir de su
emisión.
3. La tarifa y costo del (los) producto (s) cotizado (s) se mantiene durante la vigencia de la
cotización, siempre y cuando se mantengan las características originales indicadas, es decir,
período de cobertura, cantidad de personas y edad de los asegurados.
4. Las cotizaciones emitidas contarán con un identificador exclusivo que permita utilizarla
como fuente de entrada de datos en una emisión regular, pudiendo ser procesada por
cualquier canal (productor/vendedor) salvo que este no tenga acceso a los productos
indicados en ella.
5. Las características de los productos cotizados y sus tarifas pudieran sufrir variaciones al
momento de la emisión. Mantener o no las condiciones originalmente ofrecidas depende
de los acuerdos contractuales con el cliente.
1. 2. 3. Cada productor o agencia debe estar asociado a una sola región.
Un vendedor debe estar asociado a un productor o a todos los productores de una región.
Un vendedor podrá consultar las ventas que ha realizado el productor o agencia al cual está
asociado. En aquellos casos en que esté relacionado a una región en lugar de un productor
o agencia, podrá consultar las ventas de todos los productores o agencias asociados a dicha
región incluyendo las subregiones que dependan de ella, sin embargo, no podrá consultar
Versión 3.7 (Nov-2024) Desarrollada por Página 100 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
4. las ventas de regiones, productores o agencias que no dependan de la región a la que él
pertenece.
Se debe permitir incentivos de comisión por productor o agencia.
1. La emisión de seguro de viaje debe estar asociada a un canal de ventas.
2. La emisión de seguro de viaje debe ser realizada por un vendedor.
3. Al emitir un seguro de viaje solo se podrá escoger un productor.
4. A pesar de que el vendedor cambie su asociación con los canales de venta tras la emisión
de un seguro de viaje, el seguro emitido mantiene los datos que estaban vigentes al
momento de su emisión.
5. Toda emisión debe contar con un producto base y opcionalmente, tantos productos
complementarios como estén disponible.
6. Todo asegurado debe estar identificado con el número de cédula de identidad, el número
de pasaporte o ambos datos. En caso de identificarse con el número de cédula de identidad,
este debe cumplir con el formato de la República Dominicana para que sea considerado
válido.
7. Se debe suministrar la “Fecha de nacimiento” de los asegurados a los efectos de calcular su
edad.
8. Se debe suministrar el género de los asegurados para poder emitir un seguro de viaje.
9. Se debe suministrar la dirección de contacto y opcionalmente tantas direcciones como se
considere necesario.
10. Los certificados que indiquen una dirección de correo electrónica deben recibir el
certificado de viaje y la información adicional que acompaña a este.
11. La emisión de un seguro de viaje concluye con la facturación y el pago de este.
Versión 3.7 (Nov-2024) Desarrollada por Página 101 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
1. Los canales de venta pueden comercializar solo aquellos productos que le han sido
2. 3. 4. 5. 6. 7. 8. 9. asociados.
La asociación de productos responde al canal de ventas y no al vendedor, en tal sentido, un
vendedor puede comercializar los productos “A”, “B” y “D” en un canal de venta, por
ejemplo, y en otro canal solo “B”, “C”, y “H”.
El canal de ventas puede recibir opcionalmente una comisión sobre la venta realizada, la
cual se debe definir previamente a la emisión del seguro de viaje.
La comisión del canal de venta se calculará aplicando un valor porcentual al valor neto de
la factura (después de descuentos e impuestos) y puede aplicar de manera global para
todos los productos, o de manera específica (por producto).
El vendedor puede recibir opcionalmente una comisión sobre la venta realizada, la cual se
debe definir previamente a la emisión del seguro de viaje.
La comisión del vendedor se calculará aplicando un valor porcentual al valor neto de la
factura (después de descuentos e impuestos).
La comisión de venta definida para un vendedor es la misma en todos los canales de venta
en los que esté asociado.
Las comisiones de venta del canal y/o del vendedor se abonan (parcial o totalmente) al
momento del cobro de la factura relacionada.
Toda cancelación de un seguro de viaje generará un reverso de la (s) comisión (es) abonada
(s) tanto al canal de ventas como al vendedor.
1. Las tarifas responden a un esquema regido por la cantidad de días del viaje, la cantidad de
asegurados incluidos y sus edades.
Versión 3.7 (Nov-2024) Desarrollada por Página 102 de 170
GAPI - Interfaz de Programación
de Aplicaciones de GOVAL-Web
2. Las promociones que se establezcan deben tener una fecha/hora de inicio y una fecha/hora
de finalización.
3. Al establecer una promoción, por ejemplo “Niños Gratis”, el beneficio solo aplica al
producto base, manteniéndose la tarifa de los productos complementarios
1. Se podrán utilizar dos modos de facturación para los seguros de viaje emitidos: facturación
automática o facturación diferida. Estas deben definirse previamente a la emisión del
seguro de viaje.
2. La facturación automática debe aplicar a todos los canales de venta que hayan sido
definidos con esta modalidad y utilizar como encabezado, los datos del canal de venta tales
como nombre comercial, dirección, teléfono y RNC.
3. La facturación diferida debe aplicar a todos los canales de venta que hayan sido definidos
con esta modalidad y utilizar como encabezado datos diferentes a los del canal de venta,
por ejemplo, del asegurado, en lo que se conoce como “Factura a terceros”.
1. Toda factura emitida debe ser pagada a través de medios de pago electrónico, como
tarjetas de crédito, o con cargo a una línea de crédito previamente establecida al canal de
ventas.
2. 3. 4. El pago de una factura no debe realizarse parcialmente sino total.
No se permite la emisión de seguros de viaje con cargo a una línea de crédito si el monto
total a pagar excede el valor disponible en la línea de crédito.
El monto disponible en la línea de crédito disminuirá con cada factura emitida con cargo a
esta y aumentará con los abonos que se realicen a través de depósitos o transferencias
bancarias que hayan sido notificados a GOVAL y que este aplique en su back office.