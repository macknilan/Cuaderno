# Serverless Framework en AWS

```bash
__                          _                   ___                                            _                     _  __    __  __    
/ _\ ___ _ ____   _____ _ __| | ___  ___ ___    / __\ __ __ _ _ __ ___   _____      _____  _ __| | __   ___ _ __     /_\/ / /\ \ \/ _\   
\ \ / _ \ '__\ \ / / _ \ '__| |/ _ \/ __/ __|  / _\| '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /  / _ \ '_ \   //_\\ \/  \/ /\ \    
_\ \  __/ |   \ V /  __/ |  | |  __/\__ \__ \ / /  | | | (_| | | | | | |  __/\ V  V / (_) | |  |   <  |  __/ | | | /  _  \  /\  / _\ \   
\__/\___|_|    \_/ \___|_|  |_|\___||___/___/ \/   |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\  \___|_| |_| \_/ \_/\/  \/  \__/
```

¿Que es Serverless?

Serverless es una manera de crear y ejecutar aplicaciones y servicios sin tener que administrar infraestructura.

En lugar de configurar y administrar servidores, los desarrolladores simplemente cargan su código en la nube y la plataforma
se encarga de ejecutarlo automáticamente en función de la demanda. Además, las plataformas sin servidor suelen cobrar solo por
el tiempo que se ejecuta el código, lo que significa que los desarrolladores solo pagan por lo que usan.

¿Ecosistema Serverless?

Hay varias maneras de hacer aplicar la arquitectura serverless. Algunas de ellas son:

1. `Cliente-Servidor` : El modelo cliente-servidor es un modelo de arquitectura de software en el que las aplicaciones están divididas en dos partes principales: el cliente y el servidor.El modelo cliente-servidor es un modelo de arquitectura de software en el que las aplicaciones están divididas en dos partes principales: el cliente y el servidor.
2. `El cliente`: es la interfaz de usuario que se ejecuta en el dispositivo del usuario, ya sea una computadora de escritorio, un teléfono inteligente o una tableta.
3. `El servidor`: es el componente que se ejecuta en una computadora remota y es responsable de procesar y almacenar la información que solicita el cliente.
4. `Cloud`: es un conjunto de servidores que nos ofrecen una gama de servicios y recursos(Almacenamiento, computo etc…).
5. `Cloud provider`: Es una empresa que provee esos servicios y recursos de manera amigable.
    - Los Cloud Provider mas usados son:
        - AWS
        - Azure
        - Google Cloud platform.
    - Cada uno de esos providers tienen servidores y servicios basicos enfocados a Serverless.

Serverless en AWS:

- Algunos de los servicios serverless de AWS son:
    1. Lambda
    2. Step functions
    3. S3 buket
    4. SNS, SQS
    5. Aurora
    6. API Getaway
    7. Dynamo DB
    8. Entre otros…

¿Que es Serverless framework? 🌩️ [Serverless Framework](https://www.serverless.com/) 🔗 ↗️

__Serverless framework es una herramienta que nos permite desplegar aplicaciones serverless sin tanto esfuerzo.__

**IaC**: Infrastructure as Code(Infraestructura como Código)

Los principios generales de orientación en AWS (WAF) son una herramienta que ayuda a los arquitectos de la nube a crear una arquitectura segura, de alto rendimiento, resistente y eficiente. Son 6 pilares, de los cuáles te cuento en qué aporta cada una de las ventajas serverless a estos pilares desde mi perspectiva:

- Rápida escalabilidad
- Excelente relación costo - beneficio
- Sencillo de operar y desplegar
- Servicios serverless con buenas prácticas
- Fácil integración con otros servicios del ecosistema

[AWS Well-Architected](https://aws.amazon.com/es/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc) 🔗 ↗️

AWS Well-Architected y los seis pilares(Vista general del marco)  
> AWS Well-Architected Framework describe los conceptos clave, los principios de diseño y las prácticas recomendadas de arquitectura para diseñar y ejecutar cargas de trabajo en la nube. Responda un conjunto de preguntas básicas para descubrir hasta qué punto su arquitectura está en consonancia con las prácticas recomendadas en la nube y obtenga orientación para mejorarla.

1. __Excelencia operativa__, porque ejecutan y supervisan el / los sistemas que aportan valor al dominio del negocio.
2. __Seguridad__, El pilar de la seguridad se concentra en proteger la información y los sistemas. Entre los temas clave se incluyen la confidencialidad y la integridad de los datos, la administración de los permisos de usuarios y el establecimiento de controles para detectar eventos de seguridad.
3. __Fiabilidad__, El pilar de fiabilidad se centra en las cargas de trabajo que realizan las funciones previstas y en cómo recuperarse rápidamente de los errores para cumplir con las demandas. Entre los temas clave se incluyen el diseño de sistemas distribuidos, la planificación de la recuperación y cómo adaptarse a los requisitos cambiantes.
4. __Eficacia del rendimiento__, El pilar de eficacia del rendimiento se centra en la asignación estructurada y simplificada de TI y en los recursos informáticos. Entre los temas clave se incluyen la selección de los tipos y tamaños de recursos optimizados para los requisitos de la carga de trabajo, la supervisión del rendimiento y el mantenimiento de la eficacia a medida que evolucionan las necesidades de la empresa.
5. __Optimización de costos__, El pilar de optimización de costos se centra en evitar gastos innecesarios. Entre los temas clave se incluyen la comprensión del tiempo dedicado y el control de la asignación de fondos, la selección de recursos para el tipo y la cantidad adecuados y el escalado para cumplir con las necesidades de la empresa sin gastos excesivos.
6. __Sostenibilidad__, El pilar de sostenibilidad se centra en minimizar los impactos ambientales de ejecutar cargas de trabajo en la nube. Entre los temas clave se incluyen un modelo de responsabilidad compartida para la sostenibilidad, la comprensión del impacto y la maximización del uso para minimizar los recursos necesarios y reducir los impactos posteriores.

- Para trabajar en un entorno local se usa:
    1. Javascript - NodeJS(motor de ejecución de Javascript) - NPM(Gestor de paquetes de Node)
    2. Python
    3. AWS CLI para usar los recursos de AWS desde la consola
    4. [Serverless Framework](https://www.serverless.com/) 🔗 ↗️

Para saber si ya encuentra una configuración el AWS CLI

```bash
aws configure list
```

Para configurar el AWS CLI se tiene que tener una cuenta en AWS y tener las credenciales de la cuenta.

```bash
aws configure
```

Ejemplo de como se muestra en consola para configurar los profiles(users)

```bash
AWS Access Key ID [None]: <NAME-USER-IN-AIM/Access-Key-ID-of-the-user>
AWS Secret Access Key [None]: <Secret-access-key-of-the-user>
Default region name [None]: <ESTABLECER-PREFERIA-PORDEFAULT>
Default output format [None]:
```

Serverless Framework es agnóstico de un lenguaje de programación y de un cloud Provider

Para efectos del curso se clonar repo

```bash
git clone https://github.com/platzi/serverless-framework
```

El archivo package.json se cambian las dependencias por las siguientes.

```bash
{
  "name": "hola-mundo",
  "version": "1.0.0",
  "description": "",
  "main": "handler.js",
  "scripts": {
    "test": "echo \"Error: no test specified\""
  },
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "aws-sdk": "^2.1532.0",
    "serverless": "^3.38.0",
    "serverless-offline": "^13.3.2"
  },
  "dependencies": {
    "serverless-dynamodb": "^0.2.47"
  }
}
```

En el archivo `serverless.yml` raíz del proyecto clonado se cambia.

```bash
plugins:
  - serverless-offline
  - serverless-dynamodb-local
```

por

```bash
plugins:
  - serverless-offline
  - serverless-dynamodb
```

Se instalan las dependencias

```bash
cd serverless-framework
# Se instalan las dependencias
npm install
```

Instalar serverless framework de forma global

```bash
npm install -g serverless
```

Para comprobar que se instalo correctamente

```bash
sls --help
```

Configuramos DynamoDB en Local

```bash
sls dynamodb install
```

Para comprobar que se instalo correctamente

```bash
sls dynamodb start
```

Para comprobar que se instalo correctamente

```bash
sls offline start
```

Después para que funcione `sls offline start` se tiene que actualizar _SDK Javascrip V2 a V3_ como se menciona en la documentación oficial de AWS. 👇

0. [Migrating your code to SDK for JavaScript V3](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/migrating-to-v3.html) 🔗 ↗️
1. [What's the AWS SDK for JavaScript?](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/welcome.html) 🔗 ↗️

Para cambiar los archivos `handler.js` que se encuentran en las carpetas del proyecto clonado

```bash
npx aws-sdk-js-codemod -t v2-to-v3 getusers/handler.js
```

En caso se que encuentren problemas para ejecutar el comando anterior.

En caso de presentarse el error

- Post de posibles soluciones/problemas
  - [Error getting DynamoDb local latest tar.gz location undefined: 403 #294"](https://github.com/99x/serverless-dynamodb-local/issues/294#issuecomment-1492058675) :octocat: 🔗 ↗️
  - [https://github.com/99x/serverless-dynamodb-local/issues/294#issuecomment-1492058675"](https://github.com/99x/serverless-dynamodb-local/issues/294#issuecomment-1492058675) :octocat: 🔗 ↗️


🔗 ↗️ [Serverless.yml Reference](https://www.serverless.com/framework/docs/providers/aws/guide/serverless.yml)

- El `serverles.yml` se divide principalmente en:
  - __Service:__ es el nombre de la aplicación
  - __Provider:__ es la cloud provider (proveedor de nube) y las variables de entorno
  - __Plugins:__ Uso de plugins para optimizar la experiencia de desarrollo
  - __Custom:__ Permite definir cualquier propiedad de forma personalizada, para definir recursos exclusivo
  - __Functions:__ declara y define las funciones con su lógica, los eventos y triggers que disparan las lógicas (HTTP (API GATEWAY), SQS)
  - __Resources:__ IAC (infraestructura como código), definir con sintaxis de cloudFormation para definir los recursos que necesitemos

Los comandos `serverless` y `sls` son completamente iguales al momento de instalar la libraría.

Cuando se ejecuta

```bash
sls
AWS - Node.js - Starter 
  AWS - Node.js - HTTP API 
  AWS - Node.js - Scheduled Task 
  AWS - Node.js - SQS Worker 
  AWS - Node.js - Express API 
  AWS - Node.js - Express API with DynamoDB 
  AWS - Python - Starter 
  AWS - Python - HTTP API 
  AWS - Python - Scheduled Task 
  AWS - Python - SQS Worker 
  AWS - Python - Flask API 
  AWS - Python - Flask API with DynamoDB 
  Other 
```

Comandos útiles

```bash
serverless --help
```

👇

```bash
Serverless Framework v3.34.0

Usage
serverless <command> <options>
sls <command> <options>

Get started
Run serverless to interactively setup a project.
Use --help-interactive to display the interactive setup help.

Monitoring
Enable performance and error monitoring with the Serverless Dashboard.
Learn more: https://serverless.com/monitoring

Plugins
Extend the Serverless Framework with plugins.
Explore plugins: https://serverless.com/plugins

Options
--help / -h                     Show this message
--version / -v                  Show version info
--verbose                       Show verbose logs
--debug                         Namespace of debug logs to expose (use "*" to display all)

Main commands
deploy                          Deploy a Serverless service
deploy function                 Deploy a single function from the service
info                            Display information about the service
invoke                          Invoke a deployed function
invoke local                    Invoke function locally
logs                            Output the logs of a deployed function

Other commands
deploy list                     List deployed version of your Serverless Service
deploy list functions           List all the deployed functions and their versions
metrics                         Show metrics for a specific function
remove                          Remove Serverless service and all resources
rollback                        Rollback the Serverless service to a specific deployment
rollback function               Rollback the function to the previous version
test                            Run HTTP tests
package                         Packages a Serverless service
plugin install                  Install and add a plugin to your service
plugin uninstall                Uninstall and remove a plugin from your service
print                           Print your compiled and resolved config file
config                          Configure Serverless
config credentials              Configures a new provider profile for the Serverless Framework
create                          Create new Serverless service
dashboard                       Open the Serverless dashboard
doctor                          Print status on reported deprecations triggered in the last command run
generate-event                  Generate event
help                            Show this help
install                         Install a Serverless service from GitHub or a plugin from the Serverless registry
login                           Login or sign up for Serverless
logout                          Logout from Serverless
output get                      Get value of dashboard deployment profile parameter
output list                     List all dashboard deployment profile parameters
param get                       Get value of dashboard service output
param list                      List all dashboard deployment profile parameters
plugin list                     Lists all available plugins
plugin search                   Search for plugins
slstats                         Enable or disable stats
```

Para crear un proyecto desde una plantilla

```bash
sls create --help
create                          Create new Serverless service
--template / -t                 Template for the service. Available templates: 
                                             "aws-clojure-gradle", "aws-clojurescript-gradle", "aws-nodejs", "aws-nodejs-docker", "aws-nodejs-typescript", "aws-alexa-typescript", "aws-nodejs-ecma-script", "aws-python"
                                             "aws-python3", "aws-python-docker", "aws-groovy-gradle", "aws-java-maven", "aws-java-gradle", "aws-kotlin-jvm-maven", "aws-kotlin-jvm-gradle", "aws-kotlin-jvm-gradle-kts"
                                             "aws-kotlin-nodejs-gradle", "aws-scala-sbt", "aws-csharp", "aws-fsharp", "aws-go", "aws-go-dep", "aws-go-mod", "aws-ruby"
                                             "aws-provided"
                                             "tencent-go", "tencent-nodejs", "tencent-python", "tencent-php"
                                             "azure-csharp", "azure-nodejs", "azure-nodejs-typescript", "azure-python"
                                             "cloudflare-workers", "cloudflare-workers-enterprise", "cloudflare-workers-rust"
                                             "fn-nodejs", "fn-go"
                                             "google-nodejs", "google-nodejs-typescript", "google-python", "google-go"
                                             "kubeless-python", "kubeless-nodejs"
                                             "knative-docker"
                                             "openwhisk-java-maven", "openwhisk-nodejs", "openwhisk-php", "openwhisk-python", "openwhisk-ruby", "openwhisk-swift"
                                             "spotinst-nodejs", "spotinst-python", "spotinst-ruby", "spotinst-java8"
                                             "twilio-nodejs"
                                             "aliyun-nodejs"
                                             "plugin"
                                             "hello-world"
--template-url / -u             Template URL for the service. Supports: GitHub, BitBucket
--template-path                 Template local path for the service.
--path / -p                     The path where the service should be created (e.g. --path my-service)
--name / -n                     Name for the service. Overwrites the default name of the created service.
--help / -h                     Show this message
--version / -v                  Show version info
--verbose                       Show verbose logs
--debug                         Namespace of debug logs to expose (use "*" to display all)
```

Para efectos demostrativos de una plantilla para el curso

```bash
serverless create --path hola-mundo --template-url https://github.com/platzi/serverless-framework/tree/main/hola-mundo
# Ó
sls create --path hola-mundo --template-url https://github.com/platzi/serverless-framework/tree/main/hola-mundo
```

Para desplegar en AWS la plantilla descargada de la lambda se tiene que ejecutar dentro donde se encuentra el archivo `serverless.yml`

```bash
sls deploy --verbose
```

Cuando se ejecuta el comando en AWS se realizan pasos para poder crear la lambda "hola-mundo" de forma automática y la bandera `--verbose` nos ayuda a saber

Se actualiza la estructura como código con __CloudFormation__ en el cual se puede ver en la consola como se va creando los recursos.


```bash
To ensure safe major version upgrades ensure "frameworkVersion" setting in service configuration (recommended setup: "frameworkVersion: ^3.34.0")


Deploying hola-mundo to stage dev (us-east-1)

Packaging
Excluding development dependencies for service package
Retrieving CloudFormation stack
Creating CloudFormation stack
Creating new change set
Waiting for new change set to be created
Change Set did not reach desired state, retrying
Executing created change set
  CREATE_IN_PROGRESS - AWS::CloudFormation::Stack - hola-mundo-dev
  CREATE_IN_PROGRESS - AWS::S3::Bucket - ServerlessDeploymentBucket
  CREATE_IN_PROGRESS - AWS::S3::Bucket - ServerlessDeploymentBucket
  CREATE_COMPLETE - AWS::S3::Bucket - ServerlessDeploymentBucket
  CREATE_IN_PROGRESS - AWS::S3::BucketPolicy - ServerlessDeploymentBucketPolicy
  CREATE_IN_PROGRESS - AWS::S3::BucketPolicy - ServerlessDeploymentBucketPolicy
  CREATE_COMPLETE - AWS::S3::BucketPolicy - ServerlessDeploymentBucketPolicy
  CREATE_COMPLETE - AWS::CloudFormation::Stack - hola-mundo-dev
Uploading
Uploading CloudFormation file to S3
Uploading State file to S3
Uploading service hola-mundo.zip file to S3 (606 B)
Updating CloudFormation stack
Creating new change set
Waiting for new change set to be created
Change Set did not reach desired state, retrying
Executing created change set
  UPDATE_IN_PROGRESS - AWS::CloudFormation::Stack - hola-mundo-dev
  CREATE_IN_PROGRESS - AWS::ApiGateway::RestApi - ApiGatewayRestApi
  CREATE_IN_PROGRESS - AWS::Logs::LogGroup - HelloDashworldLogGroup
  CREATE_IN_PROGRESS - AWS::IAM::Role - IamRoleLambdaExecution
  CREATE_IN_PROGRESS - AWS::IAM::Role - IamRoleLambdaExecution
  CREATE_IN_PROGRESS - AWS::Logs::LogGroup - HelloDashworldLogGroup
  CREATE_IN_PROGRESS - AWS::ApiGateway::RestApi - ApiGatewayRestApi
  CREATE_COMPLETE - AWS::Logs::LogGroup - HelloDashworldLogGroup
  CREATE_COMPLETE - AWS::ApiGateway::RestApi - ApiGatewayRestApi
  CREATE_IN_PROGRESS - AWS::ApiGateway::Resource - ApiGatewayResourceHello
  CREATE_IN_PROGRESS - AWS::ApiGateway::Resource - ApiGatewayResourceHello
  CREATE_COMPLETE - AWS::ApiGateway::Resource - ApiGatewayResourceHello
  CREATE_COMPLETE - AWS::IAM::Role - IamRoleLambdaExecution
  CREATE_IN_PROGRESS - AWS::Lambda::Function - HelloDashworldLambdaFunction
  CREATE_IN_PROGRESS - AWS::Lambda::Function - HelloDashworldLambdaFunction
  CREATE_COMPLETE - AWS::Lambda::Function - HelloDashworldLambdaFunction
  CREATE_IN_PROGRESS - AWS::Lambda::Version - HelloDashworldLambdaVersionKpP2WqlwzH4RY27TrZV6SleS0S5xZLTsdNwrJ26dkDc
  CREATE_IN_PROGRESS - AWS::Lambda::Permission - HelloDashworldLambdaPermissionApiGateway
  CREATE_IN_PROGRESS - AWS::Lambda::Version - HelloDashworldLambdaVersionKpP2WqlwzH4RY27TrZV6SleS0S5xZLTsdNwrJ26dkDc
  CREATE_COMPLETE - AWS::Lambda::Version - HelloDashworldLambdaVersionKpP2WqlwzH4RY27TrZV6SleS0S5xZLTsdNwrJ26dkDc
  CREATE_IN_PROGRESS - AWS::Lambda::Permission - HelloDashworldLambdaPermissionApiGateway
  CREATE_COMPLETE - AWS::Lambda::Permission - HelloDashworldLambdaPermissionApiGateway
  CREATE_IN_PROGRESS - AWS::ApiGateway::Method - ApiGatewayMethodHelloGet
  CREATE_IN_PROGRESS - AWS::ApiGateway::Method - ApiGatewayMethodHelloGet
  CREATE_COMPLETE - AWS::ApiGateway::Method - ApiGatewayMethodHelloGet
  CREATE_IN_PROGRESS - AWS::ApiGateway::Deployment - ApiGatewayDeployment1692150057397
  CREATE_IN_PROGRESS - AWS::ApiGateway::Deployment - ApiGatewayDeployment1692150057397
  CREATE_COMPLETE - AWS::ApiGateway::Deployment - ApiGatewayDeployment1692150057397
  UPDATE_COMPLETE_CLEANUP_IN_PROGRESS - AWS::CloudFormation::Stack - hola-mundo-dev
  UPDATE_COMPLETE - AWS::CloudFormation::Stack - hola-mundo-dev
Retrieving CloudFormation stack
Removing old service artifacts from S3

✔ Service deployed to stack hola-mundo-dev (89s)

endpoint: GET - https://e9xu802ko9.execute-api.us-east-1.amazonaws.com/dev/hello
functions:
  hello-world: hola-mundo-dev-hello-world (606 B)

Stack Outputs:
  HelloDashworldLambdaFunctionQualifiedArn: arn:aws:lambda:us-east-1:148037648285:function:hola-mundo-dev-hello-world:1
  ServiceEndpoint: https://e9xu802ko9.execute-api.us-east-1.amazonaws.com/dev
  ServerlessDeploymentBucketName: hola-mundo-dev-serverlessdeploymentbucket-i8txjjbdghk0

Need a faster logging experience than CloudWatch? Try our Dev Mode in Console: run "serverless dev"
```

Los servicios que se crearon fueron 12:

1. CREATE_COMPLETE - AWS::S3::Bucket - ServerlessDeploymentBucket
2. CREATE_COMPLETE - AWS::S3::BucketPolicy - ServerlessDeploymentBucketPolicy
3. CREATE_COMPLETE - AWS::CloudFormation::Stack - hola-mundo-dev
4. CREATE_COMPLETE - AWS::Logs::LogGroup - HelloDashworldLogGroup
5. CREATE_COMPLETE - AWS::ApiGateway::RestApi - ApiGatewayRestApi
6. CREATE_COMPLETE - AWS::ApiGateway::Resource - ApiGatewayResourceHello
7. CREATE_COMPLETE - AWS::IAM::Role - IamRoleLambdaExecution
8. CREATE_COMPLETE - AWS::Lambda::Function - HelloDashworldLambdaFunction
9. CREATE_COMPLETE - AWS::Lambda::Version - HelloDashworldLambdaVersionKpP2WqlwzH4RY27TrZV6SleS0S5xZLTsdNwrJ26dkDc
10. CREATE_COMPLETE - AWS::Lambda::Permission - HelloDashworldLambdaPermissionApiGateway
11. CREATE_COMPLETE - AWS::ApiGateway::Method - ApiGatewayMethodHelloGet
12. CREATE_COMPLETE - AWS::ApiGateway::Deployment - ApiGatewayDeployment1692150057397

Cuando se actualiza cualquier parte del código de la lambda se tiene que actualizar el stack en aws con el mismo
comando que con el que se desplegó la primera vez.

```bash
sls deploy --verbose
```

Para eliminar el servicio serverless y todos sus recursos, dentro de la carpeta del proyecto.

```bash
sls remove --verbose
```

Para crear un template de una lambda con python con el método GET, se ejecuta

```bash
sls
```
Para poder seleccionar la plantilla de python

```bash
...
AWS - Python - HTTP API
...
```

Con `sls invoke` se puede invocar la lambda que esta desplegada en AWS

Con `sls invoke local --function hello` se puede invocar la lambda que esta en local para hacer pruebas.  
El nombre de la función se encuentra en el archivo `serverless.yml` en la sección `functions:`

```bash
functions:
  hello:  # NOMBRE DE LA FUNCIÓN
    handler: handler.hello
```

Alternativamente, también es posible emular(no por completo), API Getaway y Lambda localmente usando el plugin `serverless-offline` :octocat: [GitHub repository](https://github.com/dherault/serverless-offline) . Para hacerlo, se ejecuta el siguiente comando:

[serverless-offline](https://www.npmjs.com/package/serverless-offline) 🔗 ↗️  
[npm serverless-offline](https://www.npmjs.com/package/serverless-offline) 🔗 ↗️

```bash
sls plugin install -n serverless-offline
```

Se añade el plugin `serverless-offline` en `devDependencies` en el archivo `package.json` y se añade en `plugins` en `serverless.yml`.

Si no se tiene el archivo `package.json` al ejecutar el comando `sls plugin install -n serverless-offline` se crea el archivo `package.json` con las dependencias necesarias.

Con la instalación usando el comando `sls --help` se puede ver que añadió el plugin `ServerlessOffline`

Después de la instalación se puede ejecutar con el comando

```bash
sls offline start
```

👇

```bash
sls offline start
Running "serverless" from node_modules

Starting Offline at stage dev (us-east-1)

Offline [http for lambda] listening on http://localhost:3002
Function names exposed for local invocation by aws-sdk:
           * hello: aws-python-http-api-project-dev-hello

   ┌─────────────────────────────────────────────────────────────────────────┐
   │                                                                         │
   │   GET | http://localhost:3000/                                          │
   │   POST | http://localhost:3000/2015-03-31/functions/hello/invocations   │
   │                                                                         │
   └─────────────────────────────────────────────────────────────────────────┘

Server ready: http://localhost:3000 🚀
```

En una pagina del navegador  con la dirección `http://localhost:3000/` se puede ver el mensaje de respuesta de la función lambda.

Si se modifica el archivo `handler.py` y se guarda, se tiene que volver a ejecutar el comando `sls offline start` para que se actualice el cambio.

Para poder invocar la lambda con python y con dependencias se tiene que instalar el plugin `serverless-python-requirements` 

- :octocat: [GitHub repository](https://github.com/serverless/serverless-python-requirements)
- [How to Handle your Python packaging in Lambda with Serverless plugins](https://www.serverless.com/blog/serverless-python-packaging/) 🔗 ↗️


```bash
sls plugin install -n serverless-python-requirements
```

Despúes de la instlación se añade el plugin `serverless-python-requirements` en `devDependencies` en el archivo `package.json` 

Y en el archivo `serverless.yml` en la sección de `plugins` se añade

```bash
plugins:
  - serverless-offline
  - serverless-python-requirements # 👈
```

También se añade en la sección de `custom`

```bash
custom:
  pythonRequirements:
    dockerizePip: true
```

Para que quede de la siguiente manera

```yml
service: crud-serverless-users
frameworkVersion: '3'

provider:
  name: aws
  runtime: python3.11

plugins:
  - serverless-offline
  - serverless-python-requirements

custom:
  pythonRequirements:
    dockerizePip: true

functions:
  get-users:
    handler: handler.get_users
    events:
      - httpApi:
          path: /users
          method: get
```

Se tiene que crear un ambiente virtual de python para poder instalar las dependencias de python

```bash
python3 -m venv ~/venv_python/<NOMBRE-DEL-AMBIENTE-VIRTUAL>
```

Instalar las dependencias de python

```bash
pip install boto3
```

Crear el archivo `requirements.txt` con las dependencias de python en la carpeta raíz del proyecto donde se encuentra el archivo `serverless.yml`

```bash
pip freeze > requirements.txt
```

Activar el ambiente virtual de python

```bash
source /path/of/the/folder/venv_python/app_gerentes_home_admon_test/bin/activate
```

Ejecutar el comando para poder ejecutar la lambda en local

```bash
sls offline start
```

Para hacer la consulta en DynamoDB en la lambda se tiene que instalar le plugin

- [NPM serverless-dynamodb](https://www.npmjs.com/package/serverless-dynamodb) 🔗 ↗️

Se ocupa como referencia [serverless-dynamodb-local](https://www.serverless.com/plugins/serverless-dynamodb-local) 🔗 ↗️ pero no se utiliza por que esta descontinuado.

```bash
npm install --save serverless-dynamodb-local
```

En el archivo `package.json` se añade en `devDependencies`

```json
"dependencies": {
    "serverless-dynamodb": "^0.2.47"
  }
```

En el archivo `serverless.yml` se añade en `plugins`

```yml
plugins:
  - serverless-python-requirements
  - serverless-dynamodb
  - serverless-offline
```

Tomando en cuenta la documentación del plugin `serverless-dynamodb` se añade en `custom` en el archivo `serverless.yml` para que quede de la siguiente manera (hay más opciones en la documentación oficial)

```yml
custom:
  pythonRequirements:
    dockerizePip: true
  serverless-dynamodb: # 👈 
    # If you only want to use DynamoDB Local in some stages, declare them here
    stages:
      - dev
    start:
      port: 8000
      inMemory: true
      migrate: true
    # Uncomment only if you already have a DynamoDB running locally
    # noStart: true
```

Tambien en la documentación del plugin `serverless-dynamodb` se añade en `resources` para poder crear la tabla de DynamoDB

```yml
resources:
  Resources:
    usersTable:
      Type: AWS::DynamoDB::Table
      Properties:
        TableName: usersTable
        AttributeDefinitions:
          - AttributeName: pk
            AttributeType: S
        KeySchema:
          - AttributeName: pk
            KeyType: HASH
        ProvisionedThroughput:
          ReadCapacityUnits: 1
          WriteCapacityUnits: 1
```

El archivo python `handler.py` puede quedar se la siguiente manera para poder hacer la consulta a DynamoDB

```py
import json
from datetime import datetime
from typing import Any

import boto3
from boto3.dynamodb.conditions import Key


def dynamo_table_name(t: str) -> Any:
    """
    FUNCIÓN PARA SELECCIONAR LA TABLA EN DYNAMODB
    """
    _DYNAMODB = boto3.resource(
        "dynamodb",  # 👈
        region_name="localhost",  # 👈
        endpoint_url="http://localhost:8000"  # 👈
    )
    _table_selected = _DYNAMODB.Table(t)

    return _table_selected


def get_users(event, context):
    """
    FUNCIÓN PARA OBTENER LOS USUARIOS DE LA TABLA USERS
    """

    table_users_get = dynamo_table_name("usersTable")

    response = table_users_get.query(KeyConditionExpression=Key("pk").eq("1"))
    result = response["Items"]

    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }
```

Para poder ejecutar la lambda en local se tiene que ejecutar el comando

```bash
sls offline start
```

Para hacer el despliegue de la lambda en AWS se tiene modificar el archivo `handler.py` poder ser dinámico al momento de ejecutarlo en local y en AWS.

```py
import json
import logging
import os
from typing import Any

import boto3
from boto3.dynamodb.conditions import Key

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

is_offline = os.environ.get(
    "IS_OFFLINE"
)  # VARIABLE DE ENTORNO PARA SABER SI SE ESTÁ EN LOCAL O EN LA NUBE


def dynamo_table_name(t: str, is_offline: str) -> Any:
    """
    FUNCIÓN PARA SELECCIONAR LA TABLA EN DYNAMODB
    """
    if is_offline:
        _DYNAMODB = boto3.resource(
            "dynamodb",
            region_name="localhost",
            endpoint_url="http://localhost:8000",
        )
    if is_offline == "None":
        _DYNAMODB = boto3.resource("dynamodb")

    _table_selected = _DYNAMODB.Table(t)

    return _table_selected


def get_users(event: any, context: any) -> dict:
    """
    FUNCIÓN PARA OBTENER LOS USUARIOS DE LA TABLA USERS
    """

    logger.info(f"EVENT --> {event}")

    table_users_get = dynamo_table_name("usersTable", str(is_offline))

    user_id: str = str(event["pathParameters"]["id"])

    # OBTENER EL ITEM
    response = table_users_get.query(KeyConditionExpression=Key("pk").eq(user_id))
    result = response["Items"]

    return {"statusCode": 200, "body": json.dumps(result)}

```

Se tiene que modificar el archivo `serverless.yml` en la sección de `functions` para poder pasar el parámetro `id` en la ruta de la API Getaway

```yml
functions:
  get-users:
    handler: handler.get_users
    events:
      - httpApi:
          path: /users/{id} 👈
          method: get
```

Hacer el despliegue de la lambda en AWS

```bash
sls deploy --verbose
```

En el archivo `serverless.yml` se añade en la sección de `provider` el permiso para que se pueda ocupar DynamoDB, todas las acciones pero solo para la tabla `usersTable`

```yml
provider:
  name: aws
  runtime: python3.11
  iam:
    role:
      statements:
        - Effect: Allow
          Action: 'dynamodb:*'
          Resource: arn:aws:dynamodb: # 👈
```

Se crea el CRUD para la tabla `usersTable` en DynamoDB con la siguiente estructura de carpetas y archivos

```bash
create_users
├── handler.py
delete_users
├── handler.py
get_users
├── handler.py
update_users
└── handler.py
```

`create_users`

```py
import json
import logging
import os
import uuid
from typing import Any

import boto3
from boto3.dynamodb.conditions import Key

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

is_offline = os.environ.get(
    "IS_OFFLINE"
)  # VARIABLE DE ENTORNO PARA SABER SI SE ESTÁ EN LOCAL O EN LA NUBE


def dynamo_table_name(t: str, is_offline: str) -> Any:
    """
    FUNCIÓN PARA SELECCIONAR LA TABLA EN DYNAMODB
    """
    if is_offline:
        _DYNAMODB = boto3.resource(
            "dynamodb",
            region_name="localhost",
            endpoint_url="http://localhost:8000",
        )
    if is_offline == "None":
        _DYNAMODB = boto3.resource("dynamodb")

    _table_selected = _DYNAMODB.Table(t)

    return _table_selected


def create_users(event: any, context: any) -> dict:
    """
    FUNCIÓN PARA CREAR UN USUARIO EN LA TABLA USERS
    """

    logger.info(f"EVENT --> {event}")

    table_users_post = dynamo_table_name("usersTable", str(is_offline))

    pre_payload = json.loads(event["body"])
    payload: dict[str, str] = {
        "pk": str(uuid.uuid4()),
        "nombre": pre_payload["nombre"],
        "telefono": pre_payload["telefono"],
    }

    # INSERCIÓN DEL ITEM
    table_users_post = dynamo_table_name("usersTable", str(is_offline))
    response = table_users_post.put_item(Item=payload)

    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        return {"statusCode": 200, "body": json.dumps(payload)}
    else:
        return {"statusCode": 200, "body": {}}

```

`update_users`

```py
import json
import logging
import os
import uuid
from typing import Any

import boto3
from boto3.dynamodb.conditions import Key

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

is_offline = os.environ.get(
    "IS_OFFLINE"
)  # VARIABLE DE ENTORNO PARA SABER SI SE ESTÁ EN LOCAL O EN LA NUBE


def dynamo_table_name(t: str, is_offline: str) -> Any:
    """
    FUNCIÓN PARA SELECCIONAR LA TABLA EN DYNAMODB
    """
    if is_offline:
        _DYNAMODB = boto3.resource(
            "dynamodb",
            region_name="localhost",
            endpoint_url="http://localhost:8000",
        )
    if is_offline == "None":
        _DYNAMODB = boto3.resource("dynamodb")

    _table_selected = _DYNAMODB.Table(t)

    return _table_selected


def update_users(event: any, context: any) -> dict:
    """
    FUNCIÓN PARA ACTUALIZAR UN USUARIO EN LA TABLA USERS
    """
    logger.info(f"EVENT --> {event}")
    table_users_put = dynamo_table_name("usersTable", str(is_offline))

    # BÚSQUEDA QUE EXISTA ITEM A ACTUALIZAR
    # item_found = table_users_put.query(
    #     KeyConditionExpression=Key("pk").eq(event["body"]["pk"])
    # )

    # if len(item_found["Items"]) == 0:
    #     return (422, "Item no existe.")

    pre_payload = json.loads(event["body"])
    logger.info(f"PRE_PAYLOAD --> {pre_payload}")

    logger.info(f"PATHPARAMETERS_ID --> {event['pathParameters']['id']}")

    # ACTUALIZACIÓN DEL ITEM
    response = table_users_put.update_item(
        Key={"pk": event["pathParameters"]["id"]},
        UpdateExpression="SET #nombre = :val1, \
            #telefono = :val2",
        ExpressionAttributeNames={
            "#nombre": "nombre",
            "#telefono": "telefono",
        },
        ExpressionAttributeValues={
            ":val1": pre_payload["nombre"],
            ":val2": pre_payload["telefono"],
        },
        ReturnValues="ALL_NEW",
    )

    logger.info(f"RESPONSE --> {response}")

    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        return {"statusCode": 200, "body": json.dumps(response["Attributes"])}
    else:
        return {"statusCode": 200, "body": {}}
```

`delete_users`

```py
import json
import logging
import os
import uuid
from typing import Any

import boto3
from boto3.dynamodb.conditions import Key

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

is_offline = os.environ.get(
    "IS_OFFLINE"
)  # VARIABLE DE ENTORNO PARA SABER SI SE ESTÁ EN LOCAL O EN LA NUBE


def dynamo_table_name(t: str, is_offline: str) -> Any:
    """
    FUNCIÓN PARA SELECCIONAR LA TABLA EN DYNAMODB
    """
    if is_offline:
        _DYNAMODB = boto3.resource(
            "dynamodb",
            region_name="localhost",
            endpoint_url="http://localhost:8000",
        )
    if is_offline == "None":
        _DYNAMODB = boto3.resource("dynamodb")

    _table_selected = _DYNAMODB.Table(t)

    return _table_selected


def delete_users(event: any, context: any) -> dict:
    """
    FUNCIÓN PARA ELIMINAR UN USUARIO EN LA TABLA USERS
    """
    logger.info(f"EVENT --> {event}")
    table_users_put = dynamo_table_name("usersTable", str(is_offline))

    # BÚSQUEDA QUE EXISTA ITEM A ELIMINAR
    # item_found = table_users_put.query(
    #     KeyConditionExpression=Key("pk").eq(event["body"]["pk"])
    # )

    # if len(item_found["Items"]) == 0:
    #     return (422, "Item no existe.")

    logger.info(f"PATHPARAMETERS_ID --> {event['pathParameters']['id']}")

    # ELIMINACIÓN DEL ITEM
    response = table_users_put.delete_item(Key={"pk": event["pathParameters"]["id"]})

    logger.info(f"RESPONSE --> {response}")

    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        return {
            "statusCode": response["ResponseMetadata"]["HTTPStatusCode"],
            "body": json.dumps({"message": "Item deleted successfully"}),
        }
    else:
        return {
            "statusCode": response["ResponseMetadata"]["HTTPStatusCode"],
            "body": json.dumps({"message": "Error deleting item"}),
        }
```

El archivo `serverless.yml` quedaría de la siguiente manera

```yml
service: crud-serverless-users
frameworkVersion: '3'

provider:
  name: aws
  runtime: python3.11
  iam:
    role:
      statements:
        - Effect: Allow
          Action: 'dynamodb:*'
          Resource: arn:aws:...

plugins:
  - serverless-python-requirements
  - serverless-dynamodb
  - serverless-offline


package:
  individually: true
  patterns:
    - "!*/**"
    # EL PATRON COINCIDE CON TODOS LOS ARCHIVOS EN EN LOS DIRECTORIOS DEBEN DE SER IGNORADOS/EXCLUIRSE

custom:
  pythonRequirements:
    dockerizePip: true
  serverless-dynamodb:
    # If you only want to use DynamoDB Local in some stages, declare them here
    stages:
      - dev
    start:
      port: 8000
      inMemory: true
      migrate: true
    # Uncomment only if you already have a DynamoDB running locally
    # noStart: true

functions:
  get-users:
    handler: get_users/handler.get_users
    package:
      patterns:
        - "get_users/handler.py" # EL PATRON ESTABLECE QUE SOLO SE DEBE DE INCLUIR EL ARCHIVO handler.py
    events:
      - httpApi:
          path: /users/{id}
          method: GET
  create-users:
    handler: create_users/handler.create_users
    package:
      patterns:
        - "create_users/handler.py"
    events:
      - httpApi:
          path: /users
          method: POST
  update-users:
    handler: update_users/handler.update_users
    package:
      patterns:
        - "update_users/handler.py"
    events:
      - httpApi:
          path: /users/{id}
          method: PUT
  delete-users:
    handler: delete_users/handler.delete_users
    package:
      patterns:
        - "delete_users/handler.py"
    events:
      - httpApi:
          path: /users/{id}
          method: DELETE

resources:
  Resources:
    usersTable:
      Type: AWS::DynamoDB::Table
      Properties:
        TableName: usersTable
        AttributeDefinitions:
          - AttributeName: pk
            AttributeType: S
        KeySchema:
          - AttributeName: pk
            KeyType: HASH
        ProvisionedThroughput:
          ReadCapacityUnits: 1
          WriteCapacityUnits: 1
```


Los pasos para poder integrar CD/CI con GitHub Actions.

Ir a IAM (servicio de Amazon donde se administran los permisos y accesos)

![iam_aws_cd_ci_serverless_framework](/Aws/imgs/iam_aws_cd_ci_serverless_framework_00.png)


Seleccionar el boton **Create access key**

![iam_aws_cd_ci_serverless_framework](/Aws/imgs/iam_aws_cd_ci_serverless_framework_01.png)

Aquí podrás crear un par de keys, estas keys son ultra secretas, ya que con ellas puedes tener acceso programático a tus recursos de AWS, puedes crear, borrar o editar recursos accediendo a través de ellas a tu cuenta de AWS usando el CLI de AWS, Serverless Framework, Terraform o cualquier otra herramienta, son como las llaves de tu casa y por eso debes darle un tratamiento especial.

Por esta misma razón AWS nos dará un grupo de opciones alternativas que podrían servir nuestra necesidad, para este caso vamos a seleccionar “Other” y continuaremos.

![iam_aws_cd_ci_serverless_framework](/Aws/imgs/iam_aws_cd_ci_serverless_framework_02.png)

Después agregaremos una descripción opcional a nuestras Keys y crearemos nuestras keys haciendo click en **Create access key**

![iam_aws_cd_ci_serverless_framework](/Aws/imgs/iam_aws_cd_ci_serverless_framework_03.png)

De esta forma ya se tienen las keys de acceso a AWS

![iam_aws_cd_ci_serverless_framework](/Aws/imgs/iam_aws_cd_ci_serverless_framework_04.png)

**Nota:** Estas keys son super secretas, por ningún motivo subas esto a un repositorio público e intenta no subirlas a un repositorio privado, con estas credenciales se podría hacer cualquier cosa con tu cuenta de AWS lo cual en manos equivocadas podría incurrir en costos exagerados en tu tarjeta de crédito. A pesar de que los permisos de estas keys se limitan a los permisos de su dueño, te recomendamos tener especial cuidado con ellas y que las borres cuando termines el curso.

Con las keys en mano ir al repositorio de GitHub donde quieres correr los workflows de GitHub Actions y entraras

- `Settings`
- `Actions` → `General`, allí habilitar el uso de Actions para este repositorio haciendo click en __“Allow all actions and reusable workflows”__.

![iam_aws_cd_ci_serverless_framework](/Aws/imgs/iam_aws_cd_ci_serverless_framework_05.png)

Después iras a la sección

- `Secrets and variables` → `Actions`, acá podrás agregar secretos para tu repositorio u organización, continuas entonces en New repository secret

![iam_aws_cd_ci_serverless_framework](/Aws/imgs/iam_aws_cd_ci_serverless_framework_06.png)

Agregaremos primero nuestro secreto `AWS_ACCESS_KEY_ID`

![iam_aws_cd_ci_serverless_framework](/Aws/imgs/iam_aws_cd_ci_serverless_framework_07.png)

Después agregaremos nuestro secreto `AWS_SECRET_ACCESS_KEY`

![iam_aws_cd_ci_serverless_framework](/Aws/imgs/iam_aws_cd_ci_serverless_framework_08.png)

Ya se debería tener tus dos secretos listos para tu repositorio y puedes empezarlos a usar en tus workflows de _GitHub Actions_

![iam_aws_cd_ci_serverless_framework](/Aws/imgs/iam_aws_cd_ci_serverless_framework_09.png)

![Arquitectura avanzada de Serverless Framework en AWS](/Aws/imgs/arq_avanzada_crud_con_imagenes.png)

## Repositorio de GitHub del proyecto como ejemplo

🚨 :octocat: [my-framework-serverless-proyect](https://github.com/macknilan/my-framework-serverless-proyect) 🚨

Referencias de AWS S3 Buckets para configuración del archivo `serverless.yml` para poder hacer el despliegue de la lambda en AWS

- [Amazon Simple Storage Service (Amazon S3) resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3.html) 🔗 ↗️

Para poder hacer el despliegue de la lambda en AWS se tiene que modificar el archivo `serverless.yml` en la sección de `provider` el permiso para que se pueda ocupar el bucket de S3, todas las acciones pero solo para el bucket `s3-bucket-${self:service}-bucket`.

Además se tiene que crear la configuración para la función lambda `singed-url` para que firme la imagen y después se pueda hacer la subida de archivos a S3.

1. Mediante el método `GET` se manda el nombre del archivo que se quiere subir a S3 por medio de query string `filename` y se regresa la url firmada para poder subir el archivo a S3.
2. Mediante el método `PUT` se sube el archivo a S3 con la url firmada que se obtuvo en el método `GET`.

> [Presigned URLs](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html)  🔗 ↗️
>
> A user who does not have AWS credentials or permission to access an S3 object can be granted temporary access by using a presigned URL.  
>
> A presigned URL is generated by an AWS user who has access to the object. The generated URL is then given to the unauthorized user. The presigned URL can be entered in a browser or used by a program or HTML webpage. The credentials used by the presigned URL are those of the AWS user who generated the URL.
>
> A presigned URL remains valid for a limited period of time which is specified when the URL is generated.

[generate_presigned_post](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/generate_presigned_post.html#generate-presigned-post) 🔗 ↗️

**Crea la URL y los campos de formulario utilizados para un formulario pre-firmado S3 POST.**

```yml
provider:
  name: aws
  runtime: python3.11
  iam:
    role:
      statements:
        - Effect: Allow
          Action: 'dynamodb:*'
          Resource: arn:aws:dynamodb:us-east-1:148037648285:table/usersTable
        - Effect: Allow
          Action: 's3:*'
          Resource: arn:aws:s3:::s3-bucket-${self:service}-bucket/*
  environment:
    BUCKET: s3-bucket-${self:service}-bucket
...
  singed-url:
    handler: singed_url/handler.singed_url
    package:
      patterns:
        - "singed_url/handler.py"
    events:
      - http:
          path: /singedurl
          method: GET
          request:
            parameters:
              querystrings:
                filename: true # EL PARÁMETRO filename ES OBLIGATORIO
...
    # <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-bucket.html#aws-resource-s3-bucket--examples>
    S3Bucket:
      Type: 'AWS::S3::Bucket'
      Properties:
        PublicAccessBlockConfiguration:
          BlockPublicAcls: false
          BlockPublicPolicy: false
        BucketName: s3-bucket-${self:service}-bucket
        CorsConfiguration:
          CorsRules:
            - AllowedOrigins:
                - '*'
              AllowedHeaders:
                - '*'
              AllowedMethods:
                - GET
                - PUT
                - POST
                - DELETE
                - HEAD
              MaxAge: 3000
    SampleBucketPolicy:
      Type: AWS::S3::BucketPolicy
      Properties:
        Bucket: !Ref S3Bucket
        PolicyDocument:
          Version: '2012-10-17'
          Statement:
            - Action:
                - 's3:GetObject'
              Effect: Allow
              Resource: 'arn:aws:s3:::s3-bucket-${self:service}-bucket/*'
              Principal: '*'
```

Para poder firmar la url se tiene que modificar el archivo `handler.py` de la siguiente manera

```py
def singed_url(event: any, context: any) -> Any:
    """
    GENERAR UNA URL PRE-FIRMADA PARA SUBIR UN OBJETO S3
    """

    logger.info(f"EVENT --> {event}")

    file_name: str = str(event["queryStringParameters"]["filename"])
    logger.info(f"FILE_NAME_QRY_STR --> {file_name}")

    logger.info(f"BUCKET --> {os.environ.get('BUCKET')}")

    # GENERAR URL PRE-FIRMADA
    response_presigned_url: str = S3_CLIENT.generate_presigned_post(
        Bucket=os.environ.get("BUCKET"),
        Key=f"upload/{file_name}",
        ExpiresIn=600,  # TIEMPO DE EXPIRACIÓN DE LA URL EN SEGUNDOS (150s = 2.5min)
    )

    logger.info(f"RESPONSE_PRESIGNED_URL --> {response_presigned_url}")

    return {
        "statusCode": 200,
        "body": json.dumps({"singed_url": response_presigned_url}),
    }
```

Para poder realizar el método GET con POSTMAN como ejemplo se tiene que hacer lo siguiente.

![presigned GET](/Aws/imgs/presigned_post_00.png)

Para poder hacer realizar el método POST con Postman de la forma `multipart/form-data` con lados que regresa el método GET previo.

![presigned POST](/Aws/imgs/presigned_post_01.png)

## Para poder hacer el que se generen thumbnails al momento de subir una imagen a S3

Se tiene que crear una función lambda que se ejecute cuando se suba una imagen a S3 y guarde el thumbnail en otra carpeta de S3.

![Thumbnail Generator](/Aws/imgs/s3_lambda_trigger_thumbnail_generator.png)

Se modifica el archivo `serverless.yml` en la sección de `functions` para poder crear la función lambda que se ejecutará cuando se suba una imagen a S3

- [S2 Serverless Framework Documentation](https://www.serverless.com/framework/docs/providers/aws/events/s3) 🔗 ↗️
- [Amazon Simple Storage Service (Amazon S3) resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3.html)
- [AWS::S3::Bucket](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-bucket.html) 🔗 ↗️

```yml
  thumbnail-generator:
    handler: thumbnail/handler.thumbnail_generator
    package:
      patterns:
        - "thumbnail/handler.py"
    events:
      - s3: # 👈 SE ESTABLECE EL EVENTO DE S3
          bucket: s3-bucket-${self:service}-bucket # 👈 SE ESTABLECE EL BUCKET DE S3
          event: s3:ObjectCreated:* # 👈 SE ESTABLECE EL EVENTO DE S3 CUANDO SE CREA UN OBJETO <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-lambdaconfiguration.html#cfn-s3-bucket-lambdaconfiguration-event>
          existing: true # 👈 SE ESTABLECE QUE SE OCUPE EL BUCKET EXISTENTE <https://www.serverless.com/framework/docs/providers/aws/events/s3>
          rules:
            - prefix: upload/ # 👈 SE ESTABLECE EL PREFIJO DE LA CARPETA DONDE SE SUBEN LAS IMÁGENES
```

[Tutorial: Using an Amazon S3 trigger to create thumbnail images
](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-tutorial.html) 🔗 ↗️

Para crear una lambda layer utilizando python.

- [Working with Lambda layers](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html) 🔗 ↗️
- [AWS CLI Lambda Cli](https://docs.aws.amazon.com/cli/latest/reference/lambda/publish-layer-version.html) 🔗 ↗️


| Layer paths for each Lambda runtime       |                                                                                    |
|-------------------------------------------|------------------------------------------------------------------------------------|
| Runtime                                   | Path                                                                               |
|                 Node.js                   |                 nodejs/node_modules                                                |
|                                           |                 nodejs/node14/node_modules (NODE_PATH)                             |
|                                           |                 nodejs/node16/node_modules (NODE_PATH)                             |
|                                           |                 nodejs/node18/node_modules (NODE_PATH)                             |
|                 Python                    |                 python 👈                                                          |
|                                           |                 python/lib/python3.x/site-packages (site directories) 👈           |
|                 Java                      |                 java/lib (CLASSPATH)                                               |
|                 Ruby                      |                 ruby/gems/2.7.0 (GEM_PATH)                                         |
|                                           |                 ruby/lib (RUBYLIB)                                                 |
|                 All runtimes              |                 bin (PATH)                                                         |
|                                           |                 lib (LD_LIBRARY_PATH)                                              |

Preferentemente para instalar diferentes versiones de python se tiene que utilizar `pyenv` para poder instalar diferentes versiones de python.

### Crear un ambiente virtual con Python 3

#### Crear un ambiente virtual con `pyenv`

- :link: :octocat: [Using Different Versions of Python - pyenv](https://github.com/pyenv/pyenv)
- 🔗 ↗️ [Set up multiple python versions on your computer](https://k0nze.dev/posts/install-pyenv-venv-vscode/)

Instalar `pyenv` clonar el repo :octocat: [pyenv](https://github.com/pyenv/pyenv)

```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

Después de instalar `pyenv` se tiene que configurar para añadir al `$PATH` del sistema en linux.

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
```

Después reiniciar shell para que los cambios tengan efecto.

Para listar todas las versiones de `pyenv` que se pueden instalar

```bash
pyenv install -l
```

Para instalar algunas de las versiones de python listadas.

```bash
pyenv install [PYTHON_VERSION]
# ejem la ultima version de 3.9

pyenv install 3.9.16
```

Mostrar las versiones instaladas en la maquina.

```bash
pyenv versions                                                  

# output
* system (set by /home/mack/.pyenv/version)
  3.9.16
```

Para establecer una version de python diferente a la predeterminada de forma _global_

```bash
pyenv global [PYTHON_VERSION]
```

Para instalar una version diferente a la predeterminada en la terminal actual hasta que se cierre la terminal.

```bash
pyenv shell [PYTHON_VERSION]
```

Para configurar una versión de Python del proyecto que esté activa tan pronto como se entra a la carpeta `cd` del proyecto.

Esto crea dentro del proyecto una carpeta `.python-version` que contiene `[PYTHON_VERSION]` en la cual se establece la version de python que se ocupara para el proyecto.

Incluso se puede comprobar ingresando `pyenv version`, he indicará en función de qué configuración se seleccionó la versión de Python actualmente activa.


```bash
pyenv local [PYTHON_VERSION]
```

Dentro de la carpeta se crea un el archivo `.python-version` en el cual se establece que la version de python para **todo** lo que desarrolle dentro de la carpeta.

La lista de comandos para `pyenv` :octocat: [Pyenv commands](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md)

Para actualizar `pyenv` cuando se encuentre se instala clonando el repo :octocat:

```bash
cd $(pyenv root) # cd ~/.pyenv
git pull

```

1. Crear un folder para la lambda layer poniendo como nombre la librería que se va a instalar en la lambda layer.

```bash

```bash
mkdir requests-layer
cd requests-layer
```

Instalar con `venv` la versión de python que se va a ocupar para la lambda layer.

```bash
pyenv local 3.11.7
```
Crear el ambiente virtual con `venv`

```bash
python3 -m venv ~/path/of/env/folder/requests_layer
```

Activar el ambiente virtual

```bash
source ~/path/of/env/folder/requests_layer/bin/activate
```

Instalar la librería que se va a ocupar en la lambda layer

```bash
pip install requests
```

En la carpeta del ambiente virtual donde se instaló la librería se crean los directorios.

```bash
/path/of/env/folder/requests_layer/
├── bin
├── include
├── lib
└── lib64 -> lib
```

Hacer una copia de la carpeta `requets_layer` y renombrarla a `python`.

De acuerdo con la documentación de AWS y con tabla de arriba solo se tiene que tomar en cuenta la carpeta `lib` y `lib64` para crear la lambda layer.

Para que quede de la siguiente manera el folder `python`

```bash
python
├── lib
│   └── python3.11
│       └── site-packages
│           ├── certifi
│           ├── certifi-2023.11.17.dist-info
│           ├── charset_normalizer
│           ├── charset_normalizer-3.3.2.dist-info
│           ├── _distutils_hack
│           ├── idna
│           ├── idna-3.6.dist-info
│           ├── pip
│           ├── pip-23.3.2.dist-info
│           ├── pkg_resources
│           ├── requests
│           ├── requests-2.31.0.dist-info
│           ├── setuptools
│           ├── setuptools-65.5.0.dist-info
│           ├── urllib3
│           └── urllib3-2.1.0.dist-info
└── lib64 -> lib

```

Crear un archivo zip de la carpeta python.

```bash
zip -r -9 requests_layer.zip python
```
El archivo `requests_layer.zip` se tiene que copiar en la carpeta raíz del proyecto donde se encuentra el archivo `serverless.yml`


Con respecto a la documentación en [Creating and deleting layers in Lambda](https://docs.aws.amazon.com/lambda/latest/dg/creating-deleting-layers.html) 🔗 ↗️ se ejecuta el siguiente comando para subir la lambda layer a AWS.

```bash
aws lambda publish-layer-version --layer-name pillow_layer_10_2_0 \
    --description "Layer for Pillow" \
    --license-info "MIT" \
    --zip-file fileb://pillow_layer.zip \
    --compatible-runtimes python3.11 \
    --compatible-architectures "x86_64"
```
En el apartado de _Layers_ se tiene que mostrar la lambda layer creada. `pillow_layer_10_2_0`
 
Se tiene que modificar el archivo `serverless.yml` después de la sección de `functions` para poder ocupar la lambda layer creada.

```yml
...
plugins:
  - serverless-dynamodb
  - serverless-offline

package:
  individually: true
  patterns:
    - "!*/**"
    - "!*.zip" # 👈 SE EXCLUYE EL ARCHIVO ZIP DE LA LAMBDA LAYER
...

# EN LA SECCIÓN DE functions EN LA LAMBDA DE thumbnail-generator
  thumbnail-generator:
    handler: thumbnail/handler.thumbnail_generator
    layers: # 👈 SE AÑADE LA SECCIÓN DE LAYERS
      - !Ref BaseLambdaLayer # 👈 SE AÑADE LA LAMBDA LAYER <https://www.serverless.com/framework/docs/providers/aws/guide/layers>
    package:
      patterns:
        - "thumbnail/handler.py"
    events:
      - s3:
          bucket: s3-bucket-${self:service}-bucket
          event: s3:ObjectCreated:*
          existing: true
          rules:
            - prefix: upload/
...
# DESPUÉS DE LA SECCIÓN DE functions SE AÑADE LA SECCIÓN DE LAYERS
layers:
  base:
    name: "pillow_layer_10_2_0" # 👈 SE AÑADE EL NOMBRE DE LA LAMBDA LAYER
    compatibleRuntimes:
      - python3.11  # 👈 SE AÑADE LA VERSIÓN DE PYTHON QUE SE OCUPA
    package:
      artifact: pillow_layer.zip  # 👈 SE AÑADE EL NOMBRE DEL ARCHIVO ZIP DE LA LAMBDA LAYER

...
```

🐳 [https://hub.docker.com/_/amazonlinux](https://hub.docker.com/_/amazonlinux) 🔗 ↗️ 

Otra forma de hacerlo es ocupando la imagen de docker 🐳 de **amazonlinux** la cual se puede usar con las dos arquitecturas `amd64` y `arm64v8`.

Se tiene que entrar en la imagen descargada y realizar el mismo procedimiento de instalación de la librería que se va a ocupar en la lambda layer.

Para después copiar el archivo `.zip` del docker a la maquina host.

### Crear API Gateway con el servicio de AWS

![API Gateway](/Aws/imgs/api_gateway_00.png)

Para crear API Gateway con el servicio de AWS por medio de serverless framework.


Se tiene que modificar el archivo `serverless.yml` en la sección de `functions` para poder indicarle a la lambda que se desea que de tipo **privada** 

```yml
functions:
  get-users:
    handler: get_users/handler.get_users
    package:
      patterns:
        - "get_users/handler.py" # EL PATRON ESTABLECE QUE SOLO SE DEBE DE INCLUIR EL ARCHIVO handler.py
    events:
      - http:
          private: true # 👈 ESTABLECE QUE LA RUTA ES PRIVADA
          path: /users/{id}
          method: GET
          request:
            parameters:
              paths:
                id: true # EL PARÁMETRO id ES OBLIGATORIO

```

Después en la sección de `providers` se estable el API Gateway

```yml
service: crud-serverless-users
frameworkVersion: '3'

provider:
  name: aws
  runtime: python3.11
  apiGateway: # 👈 SE ESTABLECE EL API GATEWAY
    apiKeys: # 👈 SE ESTABLECE LA API KEY
      - crud-serverless-users-api-key # 👈 ESTABLECE LA API KEY PARA TODAS LAS RUTAS DE LA API
  iam:
    role:
      statements:
        - Effect: Allow
          Action: 'dynamodb:*'
          Resource: arn:aws:dynamodb:us-east-1:148037648285:table/usersTable
        - Effect: Allow
          Action: 's3:*'
          Resource: arn:aws:s3:::s3-bucket-${self:service}-bucket/*
  environment:
    BUCKET: s3-bucket-${self:service}-bucket
```
Para que se muestre en la consola de AWS en API Gateway

![API Gateway](/Aws/imgs/api_gateway_01.png)

Y el `API key` es el que se estable al momento de hacer la llamada a la lambda que se marco como privada.

![Llamada al método GET de API Gateway](/Aws/imgs/api_gateway_03.png)


### Crear un Custom Authorizer para API Gateway

Para crear un Custom Authorizer a diferencia que "API Key" por que esta última es un string que no cambia y siempre es constante para todas las llamadas a la API.

Se puede crear un Custom Authorizer para que se pueda validar el token de acceso que se genera al momento de hacer login en la aplicación.

En la consola de AWS -> AWS Systems Manager -> Parameter Store

![Parameter Store](/Aws/imgs/aws_systems_manager_parameter_store_secrets_and_configuration_data_management_00.png)

Se crea un parámetro con el nombre `SECRET_CRUD_SERVERLESS_FRAMEWOR` y se le asigna un valor.

Puede ser cualquier nombre que haga referencia a la aplicación y se le asigna un valor.

![Parameter Store](/Aws/imgs/aws_systems_manager_parameter_store_secrets_and_configuration_data_management_01.png)

Y se modifica el archivo `serverless.yml` en la sección de `provider` para poder indicarle en `enviroments` que lo tome directamente desde el parámetro de AWS Systems Manager.

Y quede disponible en todas las lambdas.

```yml
service: crud-serverless-users
frameworkVersion: '3'

provider:
  name: aws
  runtime: python3.11
  apiGateway:
    apiKeys:
      - crud-serverless-users-api-key # ESTABLECE LA API KEY PARA TODAS LAS RUTAS DE LA API
  iam:
    role:
      statements:
        - Effect: Allow
          Action: 'dynamodb:*'
          Resource: arn:aws:dynamodb:us-east-1:148037648285:table/usersTable
        - Effect: Allow
          Action: 's3:*'
          Resource: arn:aws:s3:::s3-bucket-${self:service}-bucket/*
  environment:
    BUCKET: s3-bucket-${self:service}-bucket
    SECRET_EEG: ${ssm:/SECRET_CRUD_SERVERLESS_FRAMEWOR} # 👈 OBTIENE EL VALOR DE UN PARÁMETRO DE SSM
```

Tambien se añade en el archivo `serverless.yml` en al sección de `functions` la lambda que se va a encargar de la logica de la validación del token de acceso.

```yml
functions:
  custom-authorizer:
    handler: authorizer/handler.authorize
    package:
      patterns:
        - "authorizer/handler.py"
```

> Esta petición no esta siendo llamada por ningún método HTTP, si no que va a ser llamado por el mismo API Gateway para verificar que la petición que se esta haciendo a la API es válida.

Para hacer esto se tiene que modificar la lambda que se quiera proteger con el archivo `serverless.yml` en la sección de `functions` y se le añade la sección de `authorizer` y se le indica que lambda se va a encargar de la validación del token de acceso.

```yml
  create-users:
    handler: create_users/handler.create_users
    package:
      patterns:
        - "create_users/handler.py"
    events:
      - http:
          path: /users
          authorizer:
            name: custom-authorizer # 👈 ESTABLECE EL NOMBRE DEL AUTORIZADOR
            resultTtlInSeconds: 15 # 👈 ESTABLECE EL TIEMPO DE VIDA DE LA AUTORIZACIÓN EN CACHE segundos
            identitySource: method.request.header.Authorization # 👈 ESTABLECE LA FUENTE DE LA AUTORIZACIÓN
            type: request # 👈 ESTABLECE EL TIPO DE AUTORIZACIÓN
          method: POST
          request:
            schemas:
              application/json: ${file(schemas/user-schema.json)}
              # EL ESQUEMA DEBE DE ESTAR EN LA CARPETA schemas PARA VALIDAR EL BODY
              # https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings-models.html
```

- [Reserved Concurrency](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html) 🔗 ↗️
  - Es el máximo numero de instancias concurrentes que deseas asignar para tu función. No pueden utilizarse más instancias concurrentes de las configuradas. No tiene un coste de billing por su configuración

- [Provisioned Concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html) 🔗 ↗️
  - Es el número de pre-inicializados ambientes de ejecución que deseas asignar para tu función. El ambiente pre-inicializado está preparado para responder inmediatamente. Sí tiene un coste de billing por su configuración.


Para poder implementar a la arquitectura anterior un ejemplo de colas implementando asincronismo con una lambda y guardando data en DynamoDB.

![API Gateway AQS Lambda DynamoDB](/Aws/imgs/api_gateway_aqs_lambda_aync_00.png)


Para poder realizar esto con plugins de serverless framework.

1. [Serverless APIGateway Service Proxy](https://www.serverless.com/plugins/serverless-apigateway-service-proxy) 🔗 ↗️

Se instala el plugin con el comando

```bash
serverless plugin install -n serverless-apigateway-service-proxy
```


En el archivo `serverless.yml` se modifica en la sección de `plugins` para poder indicarle que se va a ocupar el plugin.

```yml
plugins:
  - serverless-dynamodb
  - serverless-offline
  - serverless-apigateway-service-proxy # 👈 SE INSTALA EL PLUGIN
```

En la sección de `custom` se añade la sección de `apigatewayServiceProxies` para poder indicarle que se va a ocupar el plugin.

```yml
custom:
  pythonRequirements:
    dockerizePip: true
  serverless-dynamodb:
    # If you only want to use DynamoDB Local in some stages, declare them here
    stages:
      - dev
    start:
      port: 8000
      inMemory: true
      migrate: true
    # Uncomment only if you already have a DynamoDB running locally
    # noStart: true
  apiGatewayServiceProxies: # 👈 👇
    - sqs:
        path: /likeuser  # RUTA EN LA CUAL VAN A CAER LOS REQUEST
        method: post
        queueName: likequeues # OBTIENE EL NOMBRE DE LA COLA DE SQS
        cors: true # ESTABLECE QUE LA RUTA ES PUBLICA Y PUEDE SER ACCEDIDA POR CUALQUIER DOMINIO
        response:
          template:
            # `success` is used when the integration response is 200
            success: |-
              { "message: "accepted" }
            # `clientError` is used when the integration response is 400
            clientError: |-
              { "message": "there is an error in your request" }
            # `serverError` is used when the integration response is 500
            serverError: |-
              { "message": "there was an error handling your request" }
```

El segundo plugin para crear colas de SQS es el siguiente.

2. [Serverless Lift](https://www.serverless.com/plugins/lift) 🔗 ↗️

- :octocat: [https://github.com/getlift/lift](https://github.com/getlift/lift) 🔗 ↗️
- :octocat: [https://github.com/getlift/lift/blob/master/docs/queue.md](https://github.com/getlift/lift/blob/master/docs/queue.md) 🔗 ↗️

Tomando en cuenta documentación AWS CloudFormation para crear la cola de SQS [AWS::SQS::Queue](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html)

Se instala el plugin. 

```bash
serverless plugin install -n serverless-lift
```

Para que en archivo `serverless.yml` se modifique en la sección de `plugins` para poder indicarle que se va a ocupar el plugin.

```yml
plugins:
  - serverless-dynamodb
  - serverless-offline
  - serverless-apigateway-service-proxy
  - serverless-lift # 👈 SE INSTALA EL PLUGIN
``` 

En el archivo `serverless.yml` se añade la sección `construc` como lo indica la documentación del plugin.

```yml
constructs: # 👈 SE AÑADE LA SECCIÓN DE CONSTRUCTS PARA PODER CREAR LA COLA DE SQS 👇 
    sqs-queue:
      type: queue
      batchSize: 1 # QUE TANTOS DOCUMENTOS DE LA COLA VAN A SER DIGERIDOS POR EL LAMBDA 1:1
      worker:
        handler: like_user/handler.like_user
        reservedConcurrency: 1 # ESTABLECE QUE SOLO UN LAMBDA VA A SER EJECUTADO A LA VEZ
        package:
          patterns:
            - "like_user/handler.py"
      extensions:
        queue:
          Properties:
            QueueName: likequeues # ESTABLECE EL NOMBRE DE LA COLA DE SQS
            # AWS::SQS::Queue <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.html>
```
Y también se crea la lamda para poder consumir la cola de SQS, en la misma sección `construcs`

En caso de que se presente el siguiente error al momento de hacer `sls deploy --vervose`

```bash
Error:
CREATE_FAILED: SqsDashqueueWorkerLambdaFunction (AWS::Lambda::Function)
Resource handler returned message: "Specified ReservedConcurrentExecutions for function decreases account's UnreservedConcurrentExecution below its minimum value of [10]. (Service: Lambda, Status Code: 400, Request ID: 288ff7f3-XXXX-XXXX-XXXX-XXXXXXXXXXXX)" (RequestToken: 41be889b-276d-XXXX-XXXX-XXXXXXXXXXXX, HandlerErrorCode: InvalidRequest)
````

De acuerdo con la documentación de AWS

- [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) 🔗 ↗️
- [Configuring reserved concurrency](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html) 🔗 ↗️
- [My Lambda concurrency applied quota is only 10? But why](https://benellis.cloud/my-lambda-concurrency-applied-quota-is-only-10-but-why) 🔗 ↗️

Una forma de poder solucionar el problema es ir a la consola de AWS -> Service Quotas View and manage AWS quotas -> Buscar el servicio de AWS Lambda -> Editar el valor de `Concurrent executions` y aumentarlo a un valor mayor a 10(100).


```bash
Retrieving CloudFormation stack
Serverless APIGateway Service Proxy OutPuts
endpoints:
  POST - https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/dev/likeuser # 👈 RUTA DE LA COLA DE SQS

Removing old service artifacts from S3

✔ Service deployed to stack crud-serverless-users-dev (132s)

api keys:
  crud-serverless-users-api-key: XXXXXXXXXXV4LUrWMbbAxaKDTvu5B9
endpoints:
  GET - https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/dev/users/{id}
  POST - https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/dev/users
  PUT - https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/dev/users/{id}
  DELETE - https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/dev/users/{id}
  GET - https://XXXXXXXXXX.execute-api.us-east-1.amazonaws.com/dev/singedurl
functions:
  custom-authorizer: crud-serverless-users-dev-custom-authorizer (87 kB)
  get-users: crud-serverless-users-dev-get-users (87 kB)
  create-users: crud-serverless-users-dev-create-users (87 kB)
  update-users: crud-serverless-users-dev-update-users (87 kB)
  delete-users: crud-serverless-users-dev-delete-users (87 kB)
  singed-url: crud-serverless-users-dev-singed-url (87 kB)
  thumbnail-generator: crud-serverless-users-dev-thumbnail-generator (87 kB)
  sqs-queueWorker: crud-serverless-users-dev-sqs-queueWorker (86 kB) # 👈 LAMBDA QUE CONSUME LA COLA DE SQS
layers:
  base: arn:aws:lambda:us-east-1:148037648285:layer:pillow_layer_10_2_0:4
```

La lambda para manejar la logica de ir sumando los "likes" podría quedarse de la siguiente manera.

```py
def like_user(event: any, context: any) -> Any:
    """
    FUNCIÓN PARA DAR LIKE A UN USUARIO
    MEDIANTE EL TRIGGER SQS EN LA LAMBDA
    """
    logger.info(f"EVENT --> {event}")
    pre_payload = json.loads(event["Records"][0]["body"])
    logger.info(f"PRE_PAYLOAD --> {pre_payload}")

    # ACTUALIZACIÓN DEL ITEM
    table_users_put = dynamo_table_name("usersTable")
    response = table_users_put.update_item(
        Key={"pk": pre_payload["id"]},
        UpdateExpression="ADD likes :val1",
        ExpressionAttributeValues={":val1": 1},
        ReturnValues="ALL_NEW"
    )
    logger.info(f"RESPONSE --> {response}")

    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        return {
            "statusCode": 200,
            "body": json.dumps(response["Attributes"], cls=DecimalEncoder),
        }
    else:
        return {"statusCode": 200, "body": {}}
```

![Método POST para Api Gateway SQS Lambda_Async](/Aws/imgs/api_gateway_aqs_lambda_aync_01.png)


### AWS Route 53

AWS Route 53 es el servicio de DNS de AWS, este nos ayuda a gestionar nuestros dominios, aqui podremos configurar diferentes tipos de registros A, CNAME, TXT, entre otros para que nuestros servicios sean visibles y accesibles.

![AWS Route 53](/Aws/imgs/aws_route_53_00.png)

En Serverless Framework en AWS creamos diferentes funciones lambda que son accesibles mediante un dominio que API Gateway nos entrega, este dominio lo puedes encontrar en los detalles de cada Stage del tu API. Sin embargo estos APIs tienen una URL que no sigue una convención de nombres y ademas entrega algo de información sensible ante posibles usuarios mal intencionados, como dar detalles del Cloud Provider que usas y la región en la que alojas tus servicios, adicionalmente usar la URL de API Gateway directamente en tus consultas desde internet puede indicar que posiblemente no tienes una protección a nivel de CDN y Cache, estas ultimas las puedes lograr usando servicios como Cloudfront para disponer tus APIs en los Edge Location de AWS o incluso usando servicios de terceros como Cloudflare para proteger tus endpoints.

Vamos a configurar el Custom Domain Name para que resuelva los llamados HTTP a nuestro API mediante la URL sub-dominio.dominio.com.

A continuación vas a encontrar una guia detallada de como crear un Custom Domain Name y enlazarlo a un API Gateway para que tus endpoints tengan mejores practicas a nivel de seguridad y cache. En esta guia vamos a usar AWS API Gateway que es el servicio que nos permite exponer nuestra logica de negocio y Cloudflare como capa de CDN y DNS.

![AWS Route 53](/Aws/imgs/aws_route_53_00.png)

Paso 1: Creación del certificado en AWS ACM

Entramos a AWS Certificate Manager (ACM) y solicitamos un certificado, en mi caso es la opción de Request a Certificate.

![AWS Route 53](/Aws/imgs/aws_route_53_01.png)

Posteriormente, nos preguntara por el tipo de certificado (Publico o Privado), en nuestro caso dado que no tenemos ningun Certificate Authority (CA) privado, seleccionamos la primera opcion

![AWS Route 53](/Aws/imgs/aws_route_53_02.png)

A continuación, podras completar la información asociada al nombre de dominio, el metodo de validación y el algoritmo de encripción. En este caso nuestro FQDN sera el asociado al curso de Serverless Framework en AWS (slscourse.mack.host). El metodo de validación sera mediante DNS, el cual exige tener control sobre nuestro nombre de dominio, esto para poder crear registros que permitan validar que es un dominio de nuestra propiedad. Finalmente, en cuanto al algoritmo de encripción, AWS usa por defecto para ACM el algoritmo RSA 2048, [te dejamos la documentación](https://docs.aws.amazon.com/acm/latest/userguide/acm-certificate.html#algorithms) 🔗 ↗️ donde puedes encontrar mas información sobre las características de cada algoritmo y de los certificados ACM.

![AWS Route 53](/Aws/imgs/aws_route_53_03.png)

![AWS Route 53](/Aws/imgs/aws_route_53_04.png)

_Nota: Al final de la página encontrarás una sección de Tags, estos te van a permitir definir etiquetas que son de utilidad en diferentes aspectos, tales como inventario de recursos, costos asociados, entre otros. Como buena practica te recomendamos crear Tags que te permitan diferenciar los proyectos a los que se asociada cada recurso, recuerda que como buena practica entre mas segregados puedas tener tus recursos o puedas visualizarlos mejor, asi podrás tener una vista global de tu infraestructura (Propietario o Owner, Proyecto o Vertical, Centro de costos, entre otros.)_

Despues de presionar el boton de Request, podemos ver que AWS nos informa el estado del certificado y la información necesaria para poder crear los registros CNAME en nuestro gestor de DNS.

![AWS Route 53](/Aws/imgs/aws_route_53_05.png)

Paso 1.5: Validación del nombre de dominio con DNS

La validación podemos lograrla agregando un registro CNAME en nuestro gestor de DNS, al entrar al certificado que tiene Status Pendiente de validación (Pending Validation) vemos los siguientes detalles.

![AWS Route 53](/Aws/imgs/aws_route_53_06.png)

Debemos copiar el nombre y el valor del CNAME, y los registramos en el DNS (En nuestro caso sera Cloudflare).

![AWS Route 53](/Aws/imgs/aws_route_53_07.png)

Después de aproximadamente 5 o 10 minutos ya debe haberse replicado el registro CNAME en los multiples DNS y AWS ya mostrara nuestro certificado como Issued (Emitido).

![AWS Route 53](/Aws/imgs/aws_route_53_08.png)

Paso 2: Creación del Custom Domain Name en AWS

Después de tener nuestro certificado validado/issued ya puedes usarlo en la creación de un Custom Domain Name, para esto entramos a API Gateway, click en el submenu de Custom domain names, presionamos el boton Create.

![AWS Route 53](/Aws/imgs/aws_route_53_09.png)

Al presionar la opcion Create, podremos completar la información asociada a nuestro nombre de dominio y certificado (Creado previamente).

En esta vista notaras dos formas de configurar nuestro endpoint, uno de forma regional y otro optimizado en el borde (Edge Optimized). El primero sera un endpoint que AWS usara para apuntar a recursos especificos en una región, y el segundo sera accesible mediante una distribución de Cloudfront directamente desde los Edge Location de la infraestructura de AWS. Cada uno tiene diferentes ventajas y desventajas, pero deberíamos escoger el que mas convenga dependiendo del caso de uso. En nuestro ejemplo, seleccionaremos un endpoint de tipo Regional, el cual nos va a permitir a futuro agregar compatibilidad multi-region a nuestra aplicación, y generar políticas de enrutamiento basado en latencia.

![AWS Route 53](/Aws/imgs/aws_route_53_10.png)

![AWS Route 53](/Aws/imgs/aws_route_53_11.png)

Después de presionar el botón Create domain name podremos ver el dominio personalizado creado y asociado a nuestro certificado. De esta vista es importante resaltar el valor de API Gateway domain name, el que inicia con “d-….”

```bash
**API Gateway domain name:**
[d-by0ua7r9w4.execute-api.us-east-1.amazonaws.com](http://d-by0ua7r9w4.execute-api.us-east-1.amazonaws.com/)
```

![AWS Route 53](/Aws/imgs/aws_route_53_12.png)

Después de tener configurado nuestro Custom Domain, debemos hacer un mappeo de nuestro dominio a nuestro API Gateway, esto lo logramos mediante la sección de API Mappings.

![AWS Route 53](/Aws/imgs/aws_route_53_13.png)

Aqui debemos presionar la opcion Configure API mappings, y posteriormente podremos seleccionar nuestro API, el Stage, y de forma opcional

Paso 4: Configurar nuestro nombre de Dominio

Hasta este momento ya hemos creado nuestro certificado, hemos creado un nombre de dominio personalizado (Custom Domain Name), sin embargo este dominio sigue sin ser disponible desde internet. Esto por que ningún servidor de DNS del mundo sabe a donde debe dirigir cada peticion cuando entremos a slscourse.mack.host. Recuerda que la configuracion que hicimos fue solo para validar el certificado, sin embargo no hemos configurado ningún registro DNS para enviar trafico a nuestro Custom Domain Name.

Para esto debemos crear un registro CNAME en nuestro DNS apuntando slscourse a la ruta del API Gateway domain name, es el valor que inicia con “d-”

```bash
**Registro CNAME**
**Name**: slscourse
**Value**: [d-by0ua7r9w4.execute-api.us-east-1.amazonaws.com](http://d-by0ua7r9w4.execute-api.us-east-1.amazonaws.com/)
**TTL**: Auto
***Proxy status**: Esta propiedad solo aplica si usas Cloudflare*
```

![AWS Route 53](/Aws/imgs/aws_route_53_14.png)

Nota: La propiedad Proxy status: Proxied nos permite definir que Cloudflare aplicara todas las capas de seguridad y cache a cualquier usuario que intente acceder a nuestro target mediante slscourse.mack.host

Paso 5: Enlazar API Gateway

Se ve mas a detalle mas a adelante, en la cual vamos a aprender como usar Custom Domain Names para nuestro proyecto.

El paso de enlazar es relativamente corto y sencillo, despues de tener nuestro dominio configurado y el custom domain name creado, debemos hacer un mapeo para enlazar nuestro API Gateway a una ruta de nuestra preferencia. Esto lo logramos mediante la opción Configure API mappings, y luego Add new mapping (agregar un nuevo mapping) y save (Guardar)

![AWS Route 53](/Aws/imgs/aws_route_53_15.png)

![AWS Route 53](/Aws/imgs/aws_route_53_16.png)

Con esta configuración todos los llamados que hagamos a slscourse.mack.host/api/users/ seran atentidos mediante nuestro API Gateway y todas las lambdas desarrolladas hasta este momento serán accesibles mediante ese nombre de dominio.

Más adelante se vera una explicación mas a detalle de como lograr esta configuración, tambien realizaremos pruebas con Postman, validando que los API Keys sigan siendo validos mediante el Custom Domain Name.

En esta clase de lectura hemos configurado este dominio personalizado para que nuestros recursos sean accedidos mediante el path: /api/, en la próxima clase configuraremos este nombre de dominio mediante un plugin de Serverless Framework, también usaremos un mapeo totalmente diferente para que notes la flexibilidad de estos nombres de dominio y los mappings.







































