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
se encarga de ejecutarlo automáticamente en función de la demanda.Además, las plataformas sin servidor suelen cobrar solo por
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


```bash
```

```bash
```
