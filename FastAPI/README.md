
```
    .     .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .    .  .       . . 
  .    .   .       .  ;8X88@8@8S8; . .     .  .;ttttt%tttt.. .     .       .       .  ..    .      . :tt.  .     .;tSSSS%t: .    .tt; .     . .       
     .   .   .  .  .X8S tt;tX8; ; 8S.  .     ..Xt t t.%.%;S   .  .   .  .    .  .    S%8   .  .  .  t8S 8;   .  .%.t %.% t:@%%  .t:tX.   .      . .  .
  .    .      .    8% ;;:;;;@8.;:;;:@.   .     XtX;;::;:;:. .   .     .   .   .   .  8%X .         .@t:;:@.   .  %t S. .:S@%;%S  ;% S     .  .        
    .     . .   . 8% ;:::::8%%:.:::::X.   . .  @@8t.   .    %8X@8S8%.  .  ;888SX8t   8 X88888  . . 8 %88 St.     S;:@    . @::8:.%t.S .     .  .  . . 
  .   .          %t ;::::;8;:88S::.::;8       .8;@   .    . S8@88@;tX.  .X.%@S888@  .8t;X8X@@S    S%:8 tSS8S .  .S;:@. .   tt 8  tt:S   .             
    .   . .  . . S ;::.::8: :t %88%:.:8;.  .  .@t%@S8S8X8X        tS.@. %;tS...  .   8 8     :  .;%;@  .%t;@:  . S;.S..::%8X:;@  %t:S .   .  .  . .  .
  .         .    S;::.::%. .   S %;;:88: .    .8ttX@8@8888   .tX8SSX%8:..8.;@@.  .  .8.S     .   X:St    S.:@ .  S;.t%%%t::.%8   %t:S         .       
     . .  .    . 8;.::.:88@8: 8t::;.ttt.   . ..XX8: ... :  t88St%%tS:8:..SX@t;%XX;  :8:8t     . Xt%888S@SXt.@%.  S;.%X@X@XX@;   .t;.S  . .  .   .  .  
  .          .   .8.::8%8;88 8t::.::.SX. .    .8;@:    ...;%.8@    8;8;..    SX%:tS  8 %      .;@%X8%@@t@88.:S.. S;.St . ;    .  %t.%.            .  .
    .  . . .     :X%:;ttt;tS;%.:.::.:S ..     .@%@: .   . tt:%..  :@:8.     .  S;.8 .X:t;     .8 t8       ;88XS  S;:X    . .     %t.S   .  .  . .     
  .           .    S88%%tt;@8.:::.:88;  . . . .8:@:   . . .X:;@@888S;8 .t8S888@8.%S .@t.8SSX88tS:8%        8S:8;.S;.X....    .   %t.% .            .  
    . .  .  .  .  .. :S@St.;..::8S8%:         .88S::    ...:XS8S8%8@SX:.t%@Xt88@8;.   t8X%88@@88S@        :.88XX t8@8  .  .    . ;SS8. .  . .  .  .   
  .       .      .  . . %8XXXt8@t..   . .  .   .;  ..        .      ..   ::  ..:.     .:   :.  :           .:: . .::.       .     ..    .       .   . 
     . .     .  .    . .....:...:   .    .   .      . . .  . .       .  . .    .   .   ..   .   . .       .. . .      . . .   .      .     .  .       
  .      . .       .  .         ..     .       . .        .           .   .    ..   .  ..   .   .   .    .     .  .  .      .   .  .   . .       . .  
```

# FastAPI

🔗 [FastAPI](https://fastapi.tiangolo.com/) ↗️  
🔗 [uvicorn.org/](https://www.uvicorn.org/) ↗️  
🔗 [starlette.io](https://www.starlette.io/) ↗️  
🔗 [pydantic-docs.helpmanual.io](https://pydantic-docs.helpmanual.io/) ↗️  

:octocat: [curso-fastapi-fundamentos-path-validaciones](https://github.com/platzi/curso-fastapi-fundamentos-path-validaciones "curso-fastapi-fundamentos-path-validaciones") ↗️

FastAPI utiliza otros frameworks dentro de si para funcionar

- **Uvicorn**: es una librería de Python que funciona de servidor, es decir, permite que cualquier computadora se convierta en un servidor.  
- **Starlette**: es un framework de desarrollo web de bajo nivel, para desarrollar aplicaciones con este requieres un amplio conocimiento de Python, entonces FastAPI se encarga de añadirle funcionalidades por encima para que se pueda usar mas fácilmente.  
- **Pydantic**: Es un framework que permite trabajar con datos similar a pandas, pero este te permite usar modelos los cuales aprovechara FastAPI para crear la API  

Para empezar a ocupar FastAPI se puede hacer como se muestra en la documentación. [#optional-dependencies](https://fastapi.tiangolo.com/#optional-dependencies) ↗️

```py
pip install "fastapi[all]"
```

Para empezar y no instalar todas librerías se puede instalar lo básico.

```py
pip install fastapi uvicorn
```

🔗 [openapis.org](https://www.openapis.org/) ↗️  
🔗:octocat:  [redoc](https://github.com/Redocly/redoc) ↗️  
🔗 [swagger.io](https://swagger.io/) ↗️  

FastAPI también está parado sobre los hombros de OpenAPI, el cual es un conjunto de reglas que permite definir cómo describir, crear y visualizar APIs.  Open apI ES una especificación de como definir una API

Es un conjunto de reglas que permiten decir que una API está bien definida.

OpenAPI necesita de un software, el cual es Swagger, que es un conjunto de softwares que permiten trabajar con APIs.

FastAPI funciona sobre un programa de Swagger el cual es Swagger UI, que permite mostrar la API documentada en HTML.

Acceder a la documentación interactiva con Swagger UI:

```bash
{localhost}/docs
```

Acceder a la documentación interactiva con Redoc:

```bash
{localhost}/redoc
```

Se esta usando OAS3 - Open api specification version 3

**OPEN API**: es una especificación que define como describir, crear y visualizar API’s. Permite reconocer si una API está definida adecuadamente. Require de Swagger.

**Swagger**: software para trabajar API’s.

**ReDoc**: es una alternativa de Swagger instalada por default con FastAPI.

FastAPI funciona sobre SwaggerUI (User Interface) que permite mostrar gráficamente la API documentada. SwaggerUI obtiene especificaciones de OPEN API y la muestra por Fast API.

## Query Parameters & Path Parameters

**Path Parameter**  

🔗 [fastapi tutorial path-params](https://fastapi.tiangolo.com/tutorial/path-params/) ↗️

Los parámetros de ruta son partes variables de una ruta URL . Por lo general, se utilizan para señalar un recurso específico dentro de una colección, como un usuario identificado por ID.

Una URL puede tener varios parámetros de ruta.

```py
app.get("/items/{item_id}")  # <-- item_id
```

**Query Parameters:**  
Un _Query Patameter_ es un conjunto de elementos opcionales los cuales son añadidos al finalizar la ruta, con el objetivo de definir contenido o acciones en la url, estos elementos se añaden después de un `?` para agregar más query parameters utilizamos `&`

```bash
"/tweets/{tweet_id}/details?age=30&height=184"
```

![Query Parameters](imgs/url%2Bparameter%2Bcomponents.png "Query Parameters")

## Models

🔗 [sql-databases](https://fastapi.tiangolo.com/tutorial/sql-databases/ "models") ↗️  
🔗 [response-models](https://fastapi.tiangolo.com/tutorial/response-model/ "response-models") ↗️  

Los modelos son la representación de una entidad en código, una entidad es un objeto de la vida real, que tiene ciertos atributos.  
Por ejemplo:
    - Carro: color
    - motor
    - año
    - marca

Persona
    + edad
    + nombres
    + apellidos
    + altura

Para poder crear modelos en el código se utiliza la librería `Pydantic`, importando la clase `BaseModel`:

🔗 [Body - Fields](https://fastapi.tiangolo.com/tutorial/body-fields/ "Body - Fields") ↗️  

The same way you can declare additional validation and metadata in path operation function parameters with `Query`, `Path` and `Body`, you can declare validation and metadata inside of Pydantic models using Pydantic's Field.

Declare body parameters as optional, by setting the default to `None`

## Validaciones: Query Parameters

Las validaciones tal como se definen, nos sirven para comprobar si son correctos los parámetros entregados en cada una de las peticiones. Estas validaciones funcionan restringiendo o indicando el formato de entrega en cada una de las peticiones.

_Query parameters_
Entonces, se definen las validaciones para las Query Parameters para definir un estándar de consulta y especificar cómo se deben entregar los datos.

```py
"""
Script de FastAPI de hello word

Run:
    uvicorn main:app --reload
"""
# python


# Pydantic
from pydantic import BaseModel, Field

# fastpi
from fastapi import FastAPI, Query

app = FastAPI()

# models
class Person(BaseModel):
    first_name: str = Field(title="First name", min_length=8, max_length=20)
    last_name: str = Field(title="Last name", min_length=8, max_length=20)
    age: int = Field(default=0, title="The age", gt=1, le=100)
    hair_color: str | None = Field(
        default=None, title="Hair color", max_length=20
    )  # optional parameter
    is_married: bool | None = Field(
        default=None, title="Is Married"
    )  # optional parameter


@app.get("/")
def home():
    return {"Hello": "World"}


@app.post("/person/add")
def add_person(person: Person):
    return person


@app.get("/person/detail")
def detail_person(
    name: str
    | None = Query(
        default=None, min_length=8, max_length=50
    ),  # Query Parameters opcional
    age: int = Query(gt=1, le=100),  # Query Parameters obligatorio
):
    return {name: age}

```

## Validaciones: explorando más parameters

Para especificar las validaciones, debemos pasar le como parámetros a la función `Query` lo que necesitemos validar.

Para tipos de datos str:

- `max_length`: Para especificar el tamaño máximo de la cadena.
- `min_length`: Para especificar el tamaño mínimo de la cadena.
- `regex`: Para especificar expresiones regulares.

Para tipos de datos int:

- `ge`: (_greater or equal than ≥_) Para especificar que el valor debe ser mayor o igual.
- `le`: (_less or equal than ≤_) Para especificar que el valor debe ser menor o igual.
- `gt`: (_greater than >_) Para especificar que el valor debe ser mayor.
- `lt`: (_less than <_) Para especificar que el valor debe ser menor.

Es posible dotar de mayor contexto a nuestra documentación. Se deben usar los parámetros title y description.

- `title`: Para definir un título al parámetro.
- `description`: Para especificar una descripción al parámetro.

## Validaciones: Path Parameters

- 🔗 [#path-parameters](https://fastapi.tiangolo.com/tutorial/path-params/#path-parameters "#path-parameters") ↗️
- 🔗 [#order-matters](https://fastapi.tiangolo.com/tutorial/path-params/#order-matters "#order-matters") ↗️

[#path-parameters-and-numeric-validations](https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/#path-parameters-and-numeric-validations "#path-parameters-and-numeric-validations") ↗️  
☝️👇

> In the same way that you can declare more validations and metadata for query parameters with `Query`, you can declare the same type of validations and metadata for path parameters with `Path`.

```py
@app.get("/person/detail/{person_id}")
def detail_person(
    person_id: int = Path(
        gt=0,
        title="The ID of the item(person) to get title",
        description="This is the ID person. It's required.",
    )
):
    return {person_id: "It exist"}
```

## Validaciones: Request Body

- 🔗 [#body-multiple-parameters](https://fastapi.tiangolo.com/tutorial/body-multiple-params/#body-multiple-parameters "#body-multiple-parameters") ↗️
- 🔗 [#body-fields](https://fastapi.tiangolo.com/tutorial/body-fields/ "body-fields") ↗️
- 🔗 [#body-nested-models](https://fastapi.tiangolo.com/tutorial/body-nested-models/#body-nested-models "#body-nested-models") ↗️

> With FastAPI, you can define, validate, document, and use arbitrarily deeply nested models (thanks to Pydantic).

```py
# PRIMERA OPCIÓN
# @app.put("/person/detail/{person_id}")
# async def update_person(
#     person: Person,
#     location: Location,
#     person_id: int = Path(
#         gt=0,
#         title="The ID of the item(person) to get title",
#         description="This is the ID person. It's required.",
#     ),
# ):
#     results = person.dict()
#     results.update(location.dict())
#     return results


# SEGUNDA OPCIÓN
# @app.put("/person/detail/{person_id}")
# def update_person(
#     person_id: int,
#     person: Person,
#     location: Location,
# ):
#     results = {"person_id": person_id, "person": person, "location": location}
#     return results


# TERCERA OPCIÓN
@app.put("/person/detail/{person_id}")
def update_person(
    person: Person,
    location: Location,
    person_id: int = Path(
        gt=0,
        title="The ID of the item(person) to get title",
        description="This is the ID person. It's required.",
    ),
):
    results = {"person_id": person_id, "person": person, "location": location}
    return results
```

```py
```

```py
```

```py
```
