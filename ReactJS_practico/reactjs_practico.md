# Curso Práctico de React JS
:link: [Repo del proyecto del curso](https://github.com/platzi/PlatziVideo)

## 1. ¿Qué es React JS?
### 1. ¿Qué es React JS?

**React** es una librería desarrollada por Facebook que nos ayuda a construir interfaces de usuario interactivas para todo tipo de aplicaciones: web, móviles o de escritorio.

Cada pequeña parte de nuestra página web la conoceremos como **“Componente”**. Cada componente se encargará de una función en específico. Además, podremos reutilizar nuestros componentes siempre que lo necesitemos.

Al unir todos nuestros componentes tendremos una página web que nos permite cambiar, actualizar o eliminar elementos de forma muy sencilla.

![React.svg](https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/React.svg/245px-React.svg.png)

**React** \(también llamada **React.js** o ReactJS\) es una biblioteca [Javascript](https://es.wikipedia.org/wiki/JavaScript) de [código abierto](https://es.wikipedia.org/wiki/C%C3%B3digo_abierto) diseñada para crear [interfaces de usuario](https://es.wikipedia.org/wiki/Interfaz_de_usuario) con el objetivo de facilitar el desarrollo de [aplicaciones en una sola página](https://es.wikipedia.org/wiki/Single-page_application). Es mantenido por [Facebook](https://es.wikipedia.org/wiki/Facebook) y la comunidad de [software libre](https://es.wikipedia.org/wiki/Software_libre), han participado en el proyecto más de mil [desarrolladores](https://es.wikipedia.org/wiki/Desarrollador_de_software) diferentes. [1](https://es.wikipedia.org/wiki/React#cite_note-infoworld-1)​

React intenta ayudar a los desarrolladores a construir [aplicaciones](https://es.wikipedia.org/wiki/Aplicaci%C3%B3n_inform%C3%A1tica) que usan datos que cambian todo el [tiempo](https://es.wikipedia.org/wiki/Tiempo). Su objetivo es ser sencillo, declarativo y fácil de combinar. React sólo maneja la [interfaz de usuario](https://es.wikipedia.org/wiki/Interfaz_de_usuario) en una aplicación; React es la **Vista** en un contexto en el que se use el patrón [MVC](https://es.wikipedia.org/wiki/Modelo%E2%80%93vista%E2%80%93controlador) \(Modelo-Vista-Controlador\) o [MVVM](https://es.wikipedia.org/wiki/Modelo%E2%80%93vista%E2%80%93modelo_de_vista) \(Modelo-vista-modelo de vista\). También puede ser utilizado con las extensiones de React-based que se encargan de las partes no-UI \(que no forman parte de la interfaz de usuario\) de una [aplicación web](https://es.wikipedia.org/wiki/Aplicaci%C3%B3n_web).

Según el servicio de análisis Javascript \(en inglés "javascript analytics service"\), Libscore, React actualmente está siendo utilizado en las páginas principales de Imgur, Bleacher Informe, [Feedly](https://es.wikipedia.org/wiki/Feedly), [Airbnb](https://es.wikipedia.org/wiki/Airbnb), SeatGeek, HelloSign, y otras.[2](https://es.wikipedia.org/wiki/React#cite_note-2)​

### Historia

React fue creada por Jordan Walke, un ingeniero de software en Facebook, inspirado por los problemas que tenía la compañía con el mantenimiento del código de los anuncios dentro de su plataforma. Enfocado en la experiencia del usuario y la eficiencia para sus programadores, influenciado por XHP \(un marco de componentes de [HTML](https://es.wikipedia.org/wiki/HTML) para [PHP](https://es.wikipedia.org/wiki/PHP)\), nace el prototipo ReactJS.


### 2. DOM, Virtual DOM y React DOM

El **DOM** es el código HTML que se transforma en páginas web.

Cada vez que cambiamos alguna parte del **DOM**, también estamos actualizando el HTML con el que interactúan nuestros usuarios. El problema es que todas las operaciones, comparaciones y actualizaciones en el **DOM** son muy costosas.

El **Virtual DOM** es una herramienta que usan tecnologías como React y Vue para mejorar el rendimiento (_performance_) y velocidad de nuestras aplicaciones.

Es una copia exacta del **DOM**, pero mucho más ligera, ya que los cambios no actualizan el verdadero HTML de nuestras páginas web. Gracias al Virtual **DOM** podemos hacer operaciones y comparaciones de forma sumamente rápida.

Recuerda que los cambios en el Virtual **DOM** no afectan el HTML que ven los usuarios, así que debemos estar sincronizando constantemente las copias con el **DOM**. Pero no te preocupes, React DOM lo hace por nosotros.


## 2. Crear una Aplicación con React JS
### 3. Create React App y Tipos de Componentes
**NOTA** Mi repo commit `Add. _Curso Practico ReactJS_ 3. Create React App y Tipos de Componentes`

Inicialización de un proyecto en React
Creación de nuestro sitio web usando la plantilla por defecto de :link:[Create React App](https://create-react-app.dev/docs/getting-started/)
```bash
npx create-react-app nombre-de-tu-proyecto
```
Iniciar el servidor de desarrollo:
```
npm start
```
Quick Start
```bash
npx create-react-app my-app
cd my-app
npm start
```

**Creación y Tipos de Componentes**  
Los nombres de nuestros componentes deben empezar con una letra mayúscula, al igual que cada nueva palabra del componente. Esto lo conocemos como Pascal Case o Upper Camel Case.

Los componentes **Stateful** son los más robustos de React. Los usamos creando **clases que extiendan** de `React.Component`. Nos permiten manejar estado y ciclo de vida (más adelante los estudiaremos a profundidad).

```js
import React, { Component } from 'react';

class Stateful extends Component {
  constructor(props) {
    super(props);

    this.state = { hello: 'hello world' };
  }

  render() {
    return (
      <h1>{this.state.hello}h1>
    );
  }
}

export default Stateful;
```
También tenemos componentes **Stateless** o **Presentacionales**. Los usamos creando funciones que devuelvan código en formato **JSX** (del cual hablaremos en la próxima clase).
```js
import React from 'react';

const Stateless = () => {
  return (
    <h1>¡Hola!h1>
  );
}

// Otra forma de crearlos:
const Stateless = () => <h1>¡Hola!h1>;

export default Stateless;
```
### 4. JSX: JavaScript + HTML
**NOTA** Mi repo commit `Add. _Curso Practico ReactJS_ 9. Agregando compatibilidad con todos los navegadores usando Babel`

:link: [Introducing JSX](https://reactjs.org/docs/introducing-jsx.html)


Estamos acostumbrados a escribir código HTML en archivos `.html` y la lógica de JavaScript en archivos `.js`.

React usa `JSX`: una sintaxis que nos permite escribir la estructura HTML y la lógica en JavaScript desde un mismo lugar: nuestros componentes.
```js
import React from 'react';

const HolaMundo = () => {
    const Hello = '!Hola Mundo';
    const isTrue = false;
    return(
        <div className="HolaMundo">
            <h1>{Hello}</h1>
            <h2>Curso especial de React</h2>
            <img src="https://arepa.s3.amazonaws.com/react.png" alt="React" />
            { isTrue ? <h4>Esto es verdadero</h4> : <h5>Soy Falso</h5> }
            { isTrue && <h4>Soy verdadero</h4> }
        </div>
    )
}
export default HolaMundo;
```

#### Presentando JSX

Considera la declaración de esta variable:

```
const element = <h1>Hello, world!</h1>;
```

Esta curiosa sintaxis de etiquetas no es ni un string ni HTML.

Se llama JSX, y es una extensión de la sintaxis de JavaScript. Recomendamos usarlo con React para describir cómo debería ser la interfaz de usuario. JSX puede recordarte a un lenguaje de plantillas, pero viene con todo el poder de JavaScript.

JSX produce “elementos” de React. Exploraremos como renderizarlos en el DOM en la  [siguiente sección](https://es.reactjs.org/docs/rendering-elements.html). A continuación puedes encontrar lo básico de JSX que será necesario para empezar.

#### ¿Por qué JSX?

React acepta el hecho de que la lógica de renderizado está intrínsecamente unida a la lógica de la interfaz de usuario: cómo se manejan los eventos, cómo cambia el estado con el tiempo y cómo se preparan los datos para su visualización.

En lugar de separar artificialmente  _tecnologías_  poniendo el maquetado y la lógica en archivos separados, React  [separa  _intereses_](https://es.wikipedia.org/wiki/Separaci%C3%B3n_de_intereses)  con unidades ligeramente acopladas llamadas “componentes” que contienen ambas. Volveremos a los componentes en  [otra sección](https://es.reactjs.org/docs/components-and-props.html), pero si aún no te sientes cómodo maquetando en JS,  [esta charla](https://www.youtube.com/watch?v=x7cQ3mrcKaY)  podría convencerte de lo contrario.

React  [no requiere](https://es.reactjs.org/docs/react-without-jsx.html)  usar JSX, pero la mayoría de la gente lo encuentra útil como ayuda visual cuando trabajan con interfaz de usuario dentro del código Javascript. Esto también permite que React muestre mensajes de error o advertencia más útiles.

Con eso fuera del camino, ¡empecemos!

#### Insertando expresiones en JSX

En el ejemplo a continuación, declaramos una variable llamada  `name`  y luego la usamos dentro del JSX envolviéndola dentro de llaves:

```js
const name = 'Josh Perez';
const element = <h1>Hello, {name}</h1>;

ReactDOM.render(
  element,
  document.getElementById('root')
);
```

Puedes poner cualquier  [expresión de JavaScript](https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Expressions_and_Operators)  dentro de llaves en JSX. Por ejemplo,  `2 + 2`,  `user.firstName`, o  `formatName(user)`  son todas expresiones válidas de Javascript.

En el ejemplo a continuación, insertamos el resultado de llamar la función de JavaScript,  `formatName(user)`, dentro de un elemento  `<h1>`.

```js
function formatName(user) {
  return user.firstName + ' ' + user.lastName;
}

const user = {
  firstName: 'Harper',
  lastName: 'Perez'
};

const element = (
  <h1>
    Hello, {formatName(user)}!
  </h1>
);

ReactDOM.render(
  element,
  document.getElementById('root')
);
```

[**Pruébalo en CodePen**](https://es.reactjs.org/redirect-to-codepen/introducing-jsx)

Dividimos JSX en varias líneas para facilitar la lectura. Aunque no es necesario, cuando hagas esto también te recomendamos envolverlo entre paréntesis para evitar errores por la  [inserción automática del punto y coma](https://stackoverflow.com/q/2846283).

#### JSX también es una expresión

Después de compilarse, las expresiones JSX se convierten en llamadas a funciones JavaScript regulares y se evalúan en objetos JavaScript.

Esto significa que puedes usar JSX dentro de declaraciones  `if`  y bucles  `for`, asignarlo a variables, aceptarlo como argumento, y retornarlo desde dentro de funciones:

```js
function getGreeting(user) {
  if (user) {
    return <h1>Hello, {formatName(user)}!</h1>;
  }
  return <h1>Hello, Stranger.</h1>;
}
```

#### Especificando atributos con JSX

Puedes utilizar comillas para especificar strings literales como atributos:

```js
const element = <div tabIndex="0"></div>;
```

También puedes usar llaves para insertar una expresión JavaScript en un atributo:

```js
const element = <img src={user.avatarUrl}></img>;
```

No pongas comillas rodeando llaves cuando insertes una expresión JavaScript en un atributo. Debes utilizar comillas (para los valores de los strings) o llaves (para las expresiones), pero no ambas en el mismo atributo.

> **Advertencia:**
> 
> Dado que JSX es más cercano a JavaScript que a HTML, React DOM usa la convención de nomenclatura  `camelCase`  en vez de nombres de atributos HTML.
> 
> Por ejemplo,  `class`  se vuelve  [`className`](https://developer.mozilla.org/es/docs/Web/API/Element/className)  en JSX, y  `tabindex`  se vuelve  [`tabIndex`](https://developer.mozilla.org/es/docs/Web/API/HTMLElement/tabIndex).

#### Especificando hijos con JSX

Si una etiqueta está vacía, puedes cerrarla inmediatamente con  `/>`, como en XML:

```jsx
const element = <img src={user.avatarUrl} />;
```

Las etiquetas de Javascript pueden contener hijos:

```jsx
const element = (
  <div>
    <h1>Hello!</h1>
    <h2>Good to see you here.</h2>
  </div>
);
```

#### JSX previene ataques de inyección

Es seguro insertar datos ingresados por el usuario en JSX:

```jsx
const title = response.potentiallyMaliciousInput;
// Esto es seguro:
const element = <h1>{title}</h1>;
```

Por defecto, React DOM  [escapa](https://stackoverflow.com/questions/7381974/which-characters-need-to-be-escaped-on-html)  cualquier valor insertado en JSX antes de renderizarlo. De este modo, se asegura de que nunca se pueda insertar nada que no esté explícitamente escrito en tú aplicación. Todo es convertido en un string antes de ser renderizado. Esto ayuda a prevenir vulnerabilidades  [XSS (cross-site-scripting)](https://es.wikipedia.org/wiki/Cross-site_scripting).

#### JSX representa objetos

Babel compila JSX a llamadas de  `React.createElement()`.

Estos dos ejemplos son idénticos:

```jsx
const element = (
  <h1 className="greeting">
    Hello, world!
  </h1>
);
```

```js
const element = React.createElement(
  'h1',
  {className: 'greeting'},
  'Hello, world!'
);
```

`React.createElement()`  realiza algunas comprobaciones para ayudarte a escribir código libre de errores, pero, en esencia crea un objeto como este:

```jsx
// Nota: Esta estructura está simplificada
const element = {
  type: 'h1',
  props: {
    className: 'greeting',
    children: 'Hello, world!'
  }
};
```

Estos objetos son llamados “Elementos de React”. Puedes pensar en ellos como descripciones de lo que quieres ver en pantalla. React lee estos objetos y los usa para construir el DOM y mantenerlo actualizado.

Vamos a explorar el renderizado de los elementos de React al DOM en la siguiente sección.

> **Tip:**
> 
> Recomendamos usar la  [Definición del lenguaje en “Babel”](https://babeljs.io/docs/editors)  en tu editor de elección para que tanto el código en ES6 como el código en JSX sea resaltado apropiadamente. Este sitio web utiliza el esquema de color  [Oceanic Next](https://labs.voronianski.com/oceanic-next-color-scheme/), el cual es compatible con esto.

#### Estilo y CSS

**¿Cómo agrego clases CSS a los componentes?**

Pasa una string como la prop  `className`:

```jsx
render() {
  return <span className="menu navigation-menu">Menu</span>
}
```

Es común que las clases CSS dependan de las props o del estado del componente:

```jsx
render() {
  let className = 'menu';
  if (this.props.isActive) {
    className += ' menu-active';
  }
  return <span className={className}>Menu</span>
}
```

> Tip
> 
> Si a menudo escribes código como este, el paquete  [classnames](https://www.npmjs.com/package/classnames#usage-with-reactjs)  puede hacerlo más simple.

#### ¿Puedo usar estilos en línea?

Sí, ve la documentación sobre estilo  [aquí](https://es.reactjs.org/docs/dom-elements.html#style).

#### ¿Los estilos en línea son malos?

Las clases CSS son generalmente mejores para el rendimiento que los estilos en línea.

#### ¿Qué es CSS-in-JS?

“CSS-in-JS” se refiere a un patrón donde el CSS se compone usando JavaScript en lugar de definirlo en archivos externos. Lee una comparación de las bibliotecas CSS-in-JS  [aquí](https://github.com/MicheleBertoli/css-in-js).

_Ten en cuenta que esta funcionalidad no es parte de React, sino que es proporcionada por bibliotecas de terceros._  React no tiene una opinión sobre cómo se definen los estilos; en caso de dudas, un buen punto de partida es definir tus estilos en un archivo  `*.css`  separado como de costumbre y referirse a ellos usando  [`className`](https://es.reactjs.org/docs/dom-elements.html#classname).

#### ¿Puedo hacer animaciones en React?
React puede usarse para potenciar animaciones. Revisa  [React Transition Group](https://reactcommunity.org/react-transition-group/)  y  [React Motion](https://github.com/chenglou/react-motion)  o  [React Spring](https://github.com/react-spring/react-spring), por ejemplo.

### 5. Props: Comunicación entre Componentes
Las **Props** son la forma de enviar y recibir información en nuestros componentes. Son la forma de comunicar cada componente con el resto de la aplicación. Son muy parecidas a los parámetros y argumentos de las funciones en cualquier lenguaje de programación.

```js
// Button.jsx
import React from 'react';

const Button = props => {
    const { text } = props;
    return (
        <div>
            <button type="button">{props.text}</button>
            <button type="button">{text}</button>
        </div>
    )
};
export default Button;
```

```js
// index.jsx
import React from 'react';
import Button from './components/Button';

ReactDOM.render(
  <Button text="¡Hola!" />,
  document.getElementByid('root'),
);
```
Las props son la forma de enviar y recibir información en nuestros componentes, se podría decir que son los ‘argumentos’ que reciben un componente y se escriben como los atributos de html.
```js
<Componente atributo="valor" />
```
Estos props salen de los argumentos de nuestros componentes funcionales o de una variable de clase dentro de this.props y los valores son asignados directamente en el `ReactDOM.render()`.
```js
const ComponenteFuncional = (props) => { // <-- Las props son el único argumento que recibe nuestra función
    ...
}

class ComponenteClaseextendsReact.Component{
    const {
        children,
        ...
    } = this.props; // <-- Una prop se llama con this.props
    ...
}
```
Algunos atributos de html que funcionan como props serían por ejemplo: **src, href, class, id,** en React éstos pasan a ser props que pueden ser manejadas dentro de javascript tal cual como argumentos, por ejemplo podríamos hacer lo siguiente:
```js
const Padre = () => (<Linkto="/home" />);

const Link = (props)=>{
    return <a href={props.to}>{props.children}></a>
}
```
En el ejemplo anterior manejamos una prop nativa de React que son los children, mismos que serían los hijos de nuestro componente, osea todo lo que está dentro del componente `<Componente>hijos</Componente>`

Cuando creamos un componente propio en React, no se manejan los childrens, pero cuando creamos elementos de html, éstos se manejan tal cual como funciona html, así que es completamente posible que un componente que creemos y le pongamos hijos no renderice ninguno de éstos.

**Lectura, escritura, reactividad, no reactividad de props**

React es bastante flexible pero no permite a los componentes modificar sus propias props, pero sí se lo permite al componente padre.
```js
const Componente = (props)=>{
    // props.name = `${props.name} el mejor` // No hacer ésto
    name = `${props.name} el mejor`
    return (
        <div>
            {name}
        </div>
    )
}
```
Que un componente padre pueda modificar las props de sus hijos, pero éstos no puedan es lo correcto, porque las props son la manera de comunicación entre el componente padre y sus hijos y si se pudieran modificar no sabríamos quien generó este mensaje, generando un problema de reactividad por la propagación de los cambios.
```js
const Padre = () => {
    const droidName = `C${Math.random()*100}`PO;
    const changeName=()=>{...} // de alguna manera cambiar el nombre del hijo
    return (
        <Hijoon Click={changeName}nombre={droidName} />
    )
}
```
_Podríamos decir que un componente sin estado_ **(stateless)** funciona como una función puras, **ya que siempre regresará algo**, pero ésto no se modificará a menos que se modifiquen los argumentos.

Tales funciones son llamadas  por que no tratan de cambiar sus entradas, y siempre devuelven el mismo resultado para las mismas entradas.

Los componentes permiten separar la interfaz de usuario en piezas independientes, reutilizables y pensar en cada pieza de forma aislada.Esta página proporciona una introducción a la idea de los componentes. Puedes encontrar una  [API detallada sobre componentes aquí](https://es.reactjs.org/docs/react-component.html).

Conceptualmente, los componentes son como las funciones de JavaScript. Aceptan entradas arbitrarias (llamadas “props”) y devuelven a React elementos que describen lo que debe aparecer en la pantalla.

#### Componentes funcionales y de clase

La forma más sencilla de definir un componente es escribir una función de JavaScript:

```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```

Esta función es un componente de React válido porque acepta un solo argumento de objeto “props” (que proviene de propiedades) con datos y devuelve un elemento de React. Llamamos a dichos componentes “funcionales” porque literalmente son funciones JavaScript.

También puedes utilizar una  [clase de ES6](https://developer.mozilla.org/es/docs/Web/JavaScript/Referencia/Classes)  para definir un componente:

```jsx
class Welcome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```

Los dos componentes anteriores son equivalentes desde el punto de vista de React.

Las clases tienen algunas características adicionales que veremos en las  [próximas secciones](https://es.reactjs.org/docs/state-and-lifecycle.html). Hasta entonces, usaremos componentes funcionales por su brevedad.

#### Renderizando un componente

Anteriormente, sólo encontramos elementos de React que representan las etiquetas del DOM:

```jsx
const element = <div />;
```

Sin embargo, los elementos también pueden representar componentes definidos por el usuario:

```jsx
const element = <Welcome name="Sara" />;
```

Cuando React ve un elemento representando un componente definido por el usuario, pasa atributos JSX a este componente como un solo objeto. Llamamos a este objeto “props”.

Por ejemplo, este código muestra “Hello, Sara” en la página:

```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

const element = <Welcome name="Sara" />;
ReactDOM.render(
  element,
  document.getElementById('root')
);
```

[**Pruébalo en CodePen**](https://es.reactjs.org/redirect-to-codepen/components-and-props/rendering-a-component)

Recapitulemos lo que sucede en este ejemplo:

1.  Llamamos a  `ReactDOM.render()`  con el elemento  `<Welcome name="Sara" />`.
2.  React llama al componente  `Welcome`  con  `{name: 'Sara'}`  como “props”.
3.  Nuestro componente  `Welcome`  devuelve un elemento  `<h1>Hello, Sara</h1>`  como resultado.
4.  React DOM actualiza eficientemente el DOM para que coincida con  `<h1>Hello, Sara</h1>`.

> **Nota:**  Comienza siempre los nombres de componentes con una letra mayúscula.
> 
> React trata los componentes que empiezan con letras minúsculas como etiquetas del DOM. Por ejemplo,  `<div />`  representa una etiqueta div HTML pero  `<Welcome />`  representa un componente y requiere que  `Welcome`  esté definido.
> 
> Para saber más sobre el razonamiento detrás de esta convención, puedes consultar  [JSX en profundidad](https://es.reactjs.org/docs/jsx-in-depth.html#user-defined-components-must-be-capitalized).

#### Composición de componentes

Los componentes pueden referirse a otros componentes en su salida. Esto nos permite utilizar la misma abstracción de componente para cualquier nivel de detalle. Un botón, un cuadro de diálogo, un formulario, una pantalla: en aplicaciones de React, todos son expresados comúnmente como componentes.

Por ejemplo, podemos crear un componente  `App`  que renderiza  `Welcome`  muchas veces:

```jsx
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

function App() {
  return (
    <div>
      <Welcome name="Sara" />
      <Welcome name="Cahal" />
      <Welcome name="Edite" />
    </div>
  );
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
```

[**Pruébalo en CodePen**](https://es.reactjs.org/redirect-to-codepen/components-and-props/composing-components)

Por lo general, las aplicaciones de React nuevas tienen un único componente  `App`  en lo más alto. Sin embargo, si se integra React en una aplicación existente, se podría empezar de abajo hacia arriba con un pequeño componente como  `Button`  y poco a poco trabajar el camino a la cima de la jerarquía de la vista.

#### Extracción de componentes

No tengas miedo de dividir los componentes en otros más pequeños.

Por ejemplo, considera este componente  `Comment`:

```jsx
function Comment(props) {
  return (
    <div className="Comment">
      <div className="UserInfo">
        <img className="Avatar"
          src={props.author.avatarUrl}
          alt={props.author.name}
        />
        <div className="UserInfo-name">
          {props.author.name}
        </div>
      </div>
      <div className="Comment-text">
        {props.text}
      </div>
      <div className="Comment-date">
        {formatDate(props.date)}
      </div>
    </div>
  );
}
```

[**Pruébalo en CodePen**](https://es.reactjs.org/redirect-to-codepen/components-and-props/extracting-components)

Acepta  `author`  (un objeto),  `text`  (un string), y  `date`  (una fecha) como props, y describe un comentario en una web de redes sociales.

Este componente puede ser difícil de cambiar debido a todo el anidamiento, y también es difícil reutilizar partes individuales de él. Vamos a extraer algunos componentes del mismo.

Primero, vamos a extraer  `Avatar`:

```jsx
function Avatar(props) {
  return (
    <img className="Avatar"
      src={props.user.avatarUrl}
      alt={props.user.name}
    />
  );
}
```

El  `Avatar`  no necesita saber que está siendo renderizado dentro de un  `Comment`. Esto es por lo que le dimos a su propiedad un nombre más genérico:  `user`  en vez de  `author`.

Recomendamos nombrar las props desde el punto de vista del componente, en vez de la del contexto en el que se va a utilizar.

Ahora podemos simplificar  `Comment`  un poquito:

```jsx
function Comment(props) {
  return (
    <div className="Comment">
      <div className="UserInfo">
        <Avatar user={props.author} />
        <div className="UserInfo-name">
          {props.author.name}
        </div>
      </div>
      <div className="Comment-text">
        {props.text}
      </div>
      <div className="Comment-date">
        {formatDate(props.date)}
      </div>
    </div>
  );
}
```

A continuacion, vamos a extraer un componente  `UserInfo`  que renderiza un  `Avatar`  al lado del nombre del usuario:

```jsx
function UserInfo(props) {
  return (
    <div className="UserInfo">
      <Avatar user={props.user} />
      <div className="UserInfo-name">
        {props.user.name}
      </div>
    </div>
  );
}
```

Esto nos permite simplificar  `Comment`  aun más:

```jsx
function Comment(props) {
  return (
    <div className="Comment">
      <UserInfo user={props.author} />
      <div className="Comment-text">
        {props.text}
      </div>
      <div className="Comment-date">
        {formatDate(props.date)}
      </div>
    </div>
  );
}
```

[**Pruébalo en CodePen**](https://es.reactjs.org/redirect-to-codepen/components-and-props/extracting-components-continued)

Extraer componentes puede parecer un trabajo pesado al principio, pero tener una paleta de componentes reutilizables vale la pena en aplicaciones más grandes. Una buena regla en general es que si una parte de su interfaz de usuario se usa varias veces (`Button`,  `Panel`,  `Avatar`), o es lo suficientemente compleja por sí misma (`App`,  `FeedStory`,  `Comment`), es buen candidato para ser un componente reutilizable.

#### Las props son de solo lectura

Ya sea que declares un componente  [como una función o como una clase](https://es.reactjs.org/docs/components-and-props.html#function-and-class-components), este nunca debe modificar sus props. Considera esta función  `sum`  :

```jsx
function sum(a, b) {
  return a + b;
}
```

Tales funciones son llamadas  [“puras”](https://es.wikipedia.org/wiki/Programaci%C3%B3n_funcional#Funciones_puras)  por que no tratan de cambiar sus entradas, y siempre devuelven el mismo resultado para las mismas entradas.

En contraste, esta función es impura por que cambia su propia entrada:

```jsx
function withdraw(account, amount) {
  account.total -= amount;
}
```

React es bastante flexible pero tiene una sola regla estricta:

**Todos los componentes de React deben actuar como funciones puras con respecto a sus props.**

### 6. ¿Qué son los métodos del ciclo vida?
**¿Qué son los métodos del ciclo vida?**  
Todos los componentes en React pasan por una serie de fases que generalmente se denominan “Ciclo de Vida del componente” es un proceso que React hace en cada componente, en algunos casos no podemos verlos como un bloque de código y en otros podemos llamarlos en nuestro componente para asignar una actividad según sea el caso necesario.

Los componentes en react pasan por un **Montaje**, **Actualización**, **Desmontaje** y **Manejo de errores.**

+ **Montaje**:
  + En esta fase nuestro componente se crea junto a la lógica y los componentes internos y luego es insertado en el DOM.
+ Actualización:
  + En esta fase nuestro componente está al pendiente de cambios que pueden venir a través de un cambio en “state” o “props” esto en consecuencia realizan una acción dentro de un componente.
+ **Desmontaje**:
  + En esta etapa nuestro componente “Muere” cuando nosotros no necesitamos un elemento de nuestra aplicación, podemos pasar por este ciclo de vida y de esta forma eliminar el componente de la representación que tiene en el DOM.
+ **Manejo de Errores**:
  * Cuando nuestro código se ejecuta y tiene un error, podemos entrar en una fase donde se puede entender mejor qué está sucediendo con la aplicación.

Algo que debemos tener en cuenta es que un componente NO debe pasar por toda las fases, un componente puede ser montado y desmontado sin pasar por la fase de actualización o manejo de errores.

Ahora que entendemos las fases que cumple el ciclo de vida en React vamos a entrar a detalle en cada uno de ellos para ver qué piezas de código se ejecutan y nos ayudarán a crear aplicaciones en React pasando por un ciclo de vida bien estructurado.

+ **Montado**:
  1. `Constructor()` Este es el primer método al que se hace un llamado, aquí es donde se inicializan los métodos controladores, eventos del estado.
  2. `getDerivedStateFromProps()` Este método se llama antes de presentarse en el DOM y nos permite actualizar el estado interno en respuesta a un cambio en las propiedades, es considerado un método de cuidado, ya que su implementación puede causar errores sutiles.
  3. `render()` Si queremos representar elementos en el DOM en este método es donde se escribe esta lógica, usualmente utilizamos JSX para trabajar y presentar nuestra aplicación.
  4. `ComponentDidMount()` Este método se llama inmediatamente que ha sido montado en el DOM, aquí es donde trabajamos con eventos que permitan interactuar con nuestro componente.

+ **Actualización**:
  1. `getDerivedStateFromProps()` Este método es el primero en ejecutarse en la fase de actualización y funciona de la misma forma que en el montaje.
  2. `shouldComponentUpdate()` Dentro de este método se puede controlar la fase de actualización, podemos devolver un valor entre verdadero o falso si queremos actualizar o no el componente y es utilizado principalmente para optimización.
  3. `render()` Se llama el método render que representa los cambios en el DOM.
  4. `componentDidUpdate()` Este método es invocado inmediatamente después de que el componente se actualiza y recibe como argumentos las propiedades y el estado y es donde podemos manejar nuestro componente.

+ **Desmontado**
  1. `componentWillUnmount()` Este método se llama justo antes de que el componente sea destruido o eliminado del DOM.
  2. `Manejo de Errores:`
    1. `getDerivedStateFromError()` Una vez que se lanza un error este es el primer método que se llama, el cual recibe el error como argumento y cualquier valor devuelto en este método es utilizado para actualizar el estado del componente.
    2. `componentDidCatch()` Este método es llamado después de lanzarse un error y pasa como argumento el error y la información representada sobre el error.

Ahora que entendemos cada una de las fases que tiene el ciclo de vida de react, podemos utilizarlas según sea necesario en nuestra aplicación y de esta forma crear las interacciones que necesitemos.

#### Estado y ciclo de vida
Esta página introduce el concepto de estado y ciclo de vida en un componente de React. Puedes encontrar una  [referencia detallada de la API de un componente aquí](https://es.reactjs.org/docs/react-component.html).

Consideremos el ejemplo del reloj de  [una de las secciones anteriores](https://es.reactjs.org/docs/rendering-elements.html#updating-the-rendered-element). En  [Renderizando elementos](https://es.reactjs.org/docs/rendering-elements.html#rendering-an-element-into-the-dom), aprendimos solo una forma de actualizar la interfaz de usuario. Invocamos a  `ReactDOM.render()`  para que cambie el resultado renderizado.

```jsx
function tick() {
  const element = (
    <div>
      <h1>Hello, world!</h1>
      <h2>It is {new Date().toLocaleTimeString()}.</h2>
    </div>
  );
  ReactDOM.render(
    element,
    document.getElementById('root')
  );
}

setInterval(tick, 1000);
```

[**Pruébalo en CodePen**](https://codepen.io/gaearon/pen/gwoJZk?editors=0010)

En esta sección, aprenderemos como hacer al componente  `Clock`  verdaderamente reutilizable y encapsulado. Configurarás tu propio temporizador y se actualizará cada segundo.

Podemos comenzar por encapsular cómo se ve el reloj:

```jsx
function Clock(props) {
  return (
    <div>
      <h1>Hello, world!</h1>
      <h2>It is {props.date.toLocaleTimeString()}.</h2>
    </div>
  );
}

function tick() {
  ReactDOM.render(
    <Clock date={new Date()} />,
    document.getElementById('root')
  );
}

setInterval(tick, 1000);
```

[**Pruébalo en CodePen**](https://codepen.io/gaearon/pen/dpdoYR?editors=0010)

Sin embargo, se pierde un requisito crucial: el hecho de que  `Clock`  configure un temporizador y actualice la interfaz de usuario cada segundo debe ser un detalle de implementación de  `Clock`.

Idealmente, queremos escribir esto una vez y que  `Clock`  se actualice a sí mismo:

```jsx
ReactDOM.render(
  <Clock />,
  document.getElementById('root')
);
```

Para implementar esto, necesitamos agregar «estado» al componente  `Clock`.

El estado es similar a las props, pero es privado y está completamente controlado por el componente.

#### Convertir una función en una clase

Se puede convertir un componente de función como  `Clock`  en una clase en cinco pasos:

1.  Crear una  [clase ES6](https://developer.mozilla.org/es/docs/Web/JavaScript/Referencia/Classes)  con el mismo nombre que herede de  `React.Component`.
2.  Agregar un único método vacío llamado  `render()`.
3.  Mover el cuerpo de la función al método  `render()`.
4.  Reemplazar  `props`  con  `this.props`  en el cuerpo de  `render()`.
5.  Borrar el resto de la declaración de la función ya vacía.

```jsx
class Clock extends React.Component {
  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.props.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}
```

[**Pruébalo en CodePen**](https://codepen.io/gaearon/pen/zKRGpo?editors=0010)

`Clock`  ahora se define como una clase en lugar de una función.

El método  `render`  se invocará cada vez que ocurre una actualización; pero, siempre y cuando rendericemos  `<Clock />`  en el mismo nodo del DOM, se usará solo una única instancia de la clase  `Clock`. Esto nos permite utilizar características adicionales como el estado local y los métodos de ciclo de vida.

#### Agregar estado local a una clase

Moveremos  `date`  de las props hacia el estado en tres pasos:

1.  Reemplazar  `this.props.date`  con  `this.state.date`  en el método  `render()`:

```jsx
class Clock extends React.Component {
  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}
```

2.  Añadir un  [constructor de clase](https://developer.mozilla.org/es/docs/Web/JavaScript/Referencia/Classes#Constructor)  que asigne el  `this.state`  inicial:

```jsx
class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {date: new Date()};
  }

  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}
```

Nota cómo pasamos  `props`  al constructor base:

```jsx
  constructor(props) {
    super(props);
    this.state = {date: new Date()};
  }
```

Los componentes de clase siempre deben invocar al constructor base con  `props`.

3.  Eliminar la prop  `date`  del elemento  `<Clock />`:

```jsx
ReactDOM.render(
  <Clock />,
  document.getElementById('root')
);
```

Posteriormente regresaremos el código del temporizador al propio componente.

El resultado es el siguiente:

```jsx
class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {date: new Date()};
  }

  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}

ReactDOM.render(
  <Clock />,
  document.getElementById('root')
);
```

[**Pruébalo en CodePen**](https://codepen.io/gaearon/pen/KgQpJd?editors=0010)

A continuación, haremos que  `Clock`  configure su propio temporizador y se actualice cada segundo.

#### Agregar métodos de ciclo de vida a una clase

En aplicaciones con muchos componentes, es muy importante liberar recursos tomados por los componentes cuando se destruyen.

Queremos  [configurar un temporizador](https://es.reactjs.org/docs/%60https://developer.mozilla.org/es/docs/Web/API/WindowTimers/setInterval%60)  cada vez que  `Clock`  se renderice en el DOM por primera vez. Esto se llama «montaje» en React.

También queremos  [borrar ese temporizador](https://developer.mozilla.org/es/docs/Web/API/WindowTimers/clearInterval)  cada vez que el DOM producido por  `Clock`  se elimine. Esto se llama «desmontaje» en React.

Podemos declarar métodos especiales en la clase del componente para ejecutar algún código cuando un componente se monta y desmonta:

```jsx
class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {date: new Date()};
  }

  componentDidMount() {

  }

  componentWillUnmount() {

  }

  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}
```

Estos métodos son llamados «métodos de ciclo de vida».

El método  `componentDidMount()`  se ejecuta después que la salida del componente ha sido renderizada en el DOM. Este es un buen lugar para configurar un temporizador:

```jsx
  componentDidMount() {
    this.timerID = setInterval(
      () => this.tick(),
      1000
    );
  }
```

Nota como guardamos el ID del temporizador en  `this`  (`this.timerID`).

Si bien  `this.props`  es configurado por el mismo React y  `this.state`  tiene un significado especial, eres libre de añadir campos adicionales a la clase manualmente si necesitas almacenar algo que no participa en el flujo de datos (como el ID de un temporizador).

Eliminaremos el temporizador en el método de ciclo de vida  `componentWillUnmount()`:

```jsx
  componentWillUnmount() {
    clearInterval(this.timerID);
  }
```

Finalmente, implementaremos un método llamado  `tick()`  que el componente  `Clock`  ejecutará cada segundo.

Utilizará  `this.setState()`  para programar actualizaciones al estado local del componente.

```jsx
class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = {date: new Date()};
  }

  componentDidMount() {
    this.timerID = setInterval(
      () => this.tick(),
      1000
    );
  }

  componentWillUnmount() {
    clearInterval(this.timerID);
  }

  tick() {
    this.setState({
      date: new Date()
    });
  }

  render() {
    return (
      <div>
        <h1>Hello, world!</h1>
        <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
      </div>
    );
  }
}

ReactDOM.render(
  <Clock />,
  document.getElementById('root')
);
```

[**Pruébalo en CodePen**](https://codepen.io/gaearon/pen/amqdNA?editors=0010)

Ahora el reloj cambia cada segundo.

Repasemos rápidamente lo que está sucediendo y el orden en que se invocan los métodos:

1.  Cuando se pasa  `<Clock />`  a  `ReactDOM.render()`, React invoca al constructor del componente  `Clock`. Ya que  `Clock`  necesita mostrar la hora actual, inicializa  `this.state`  con un objeto que incluye la hora actual. Luego actualizaremos este estado.
2.  React invoca entonces al método  `render()`  del componente  `Clock`. Así es como React sabe lo que se debe mostrar en pantalla. React entonces actualiza el DOM para que coincida con la salida del renderizado de  `Clock`.
3.  Cuando la salida de  `Clock`  se inserta en el DOM, React invoca al método de ciclo de vida  `componentDidMount()`. Dentro de él, el componente  `Clock`  le pide al navegador que configure un temporizador para invocar al método  `tick()`  del componente una vez por segundo.
4.  Cada segundo el navegador invoca al método  `tick()`. Dentro de él, el componente  `Clock`  planifica una actualización de la interfaz de usuario al invocar a  `setState()`  con un objeto que contiene la hora actual. Gracias a la invocación a  `setState()`, React sabe que el estado cambió e invoca de nuevo al método  `render()`  para saber qué debe estar en la pantalla. Esta vez,  `this.state.date`  en el método  `render()`  será diferente, por lo que el resultado del renderizado incluirá la hora actualizada. Conforme a eso React actualiza el DOM.
5.  Si el componente  `Clock`  se elimina en algún momento del DOM, React invoca al método de ciclo de vida  `componentWillUnmount()`, por lo que el temporizador se detiene.

#### Usar el estado correctamente

Hay tres cosas que debes saber sobre  `setState()`.

### [](https://es.reactjs.org/docs/state-and-lifecycle.html#do-not-modify-state-directly)No modifiques el estado directamente

Por ejemplo, esto no volverá a renderizar un componente:

```jsx
// Incorrecto
this.state.comment = 'Hello';
```

En su lugar utiliza  `setState()`:

```jsx
// Correcto
this.setState({comment: 'Hello'});
```

El único lugar donde puedes asignar  `this.state`  es el constructor.

#### Las actualizaciones del estado pueden ser asíncronas

React puede agrupar varias invocaciones a  `setState()`  en una sola actualización para mejorar el rendimiento.

Debido a que  `this.props`  y  `this.state`  pueden actualizarse de forma asincrónica, no debes confiar en sus valores para calcular el siguiente estado.

Por ejemplo, este código puede fallar en actualizar el contador:

```jsx
// Incorrecto
this.setState({
  counter: this.state.counter + this.props.increment,
});
```

Para arreglarlo, usa una segunda forma de  `setState()`  que acepta una función en lugar de un objeto. Esa función recibirá el estado previo como primer argumento, y las props en el momento en que se aplica la actualización como segundo argumento:

```jsx
// Correcto
this.setState((state, props) => ({
  counter: state.counter + props.increment
}));
```

Anteriormente usamos una  [función flecha](https://developer.mozilla.org/es/docs/Web/JavaScript/Referencia/Funciones/Arrow_functions), pero se podría haber hecho igualmente con funciones comunes:

```jsx
// Correcto
this.setState(function(state, props) {
  return {
    counter: state.counter + props.increment
  };
});
```

#### Las actualizaciones de estado se fusionan

Cuando invocas a  `setState()`, React combina el objeto que proporcionaste con el estado actual.

Por ejemplo, tu estado puede contener varias variables independientes:

```jsx
  constructor(props) {
    super(props);
    this.state = {
      posts: [],
      comments: []
    };
  }
```

Luego puedes actualizarlas independientemente con invocaciones separadas a  `setState()`:

```jsx
  componentDidMount() {
    fetchPosts().then(response => {
      this.setState({
        posts: response.posts
      });
    });

    fetchComments().then(response => {
      this.setState({
        comments: response.comments
      });
    });
  }
```

La fusión es superficial, asi que  `this.setState({comments})`  deja intacto a  `this.state.posts`, pero reemplaza completamente  `this.state.comments`.

#### Los datos fluyen hacia abajo

Ni los componentes padres o hijos pueden saber si un determinado componente tiene o no tiene estado y no les debería importar si se define como una función o una clase.

Por eso es que el estado a menudo se le denomina local o encapsulado. No es accesible desde otro componente excepto de aquel que lo posee y lo asigna.

Un componente puede elegir pasar su estado como props a sus componentes hijos:

```jsx
<h2>It is {this.state.date.toLocaleTimeString()}.</h2>
```

Esto también funciona para componentes definidos por el usuario:

```jsx
<FormattedDate date={this.state.date} />
```

El componente  `FormattedDate`  recibiría  `date`  en sus props y no sabría si vino del estado de  `Clock`, de los props de  `Clock`, o si se escribió manualmente:

```jsx
function FormattedDate(props) {
  return <h2>It is {props.date.toLocaleTimeString()}.</h2>;
}
```

[**Pruébalo en CodePen**](https://codepen.io/gaearon/pen/zKRqNB?editors=0010)

A esto comúnmente se le llama flujo de datos «descendente» o «unidireccional». Cualquier estado siempre es propiedad de algún componente específico, y cualquier dato o interfaz de usuario derivados de ese estado solo pueden afectar los componentes «debajo» de ellos en el árbol.

Si imaginas un árbol de componentes como una cascada de props, el estado de cada componente es como una fuente de agua adicional que se le une en un punto arbitrario, pero también fluye hacia abajo.

Para mostrar que todos los componentes están verdaderamente aislados, podemos crear un componente  `App`  que represente tres componentes  `<Clock>`:

```jsx
function App() {
  return (
    <div>
      <Clock />
      <Clock />
      <Clock />
    </div>
  );
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
```

[**Pruébalo en CodePen**](https://codepen.io/gaearon/pen/vXdGmd?editors=0010)

Cada  `Clock`  configura su propio temporizador y se actualiza de forma independiente.

En las aplicaciones de React, si un componente tiene o no estado se considera un detalle de implementación del componente que puede cambiar con el tiempo. Puedes usar componentes sin estado dentro de componentes con estado y viceversa.

### 7. State - Events
```jsx
import React from 'react';

class Button extends React.Component{
    state = {
        count: 0,
    }
    handleClick = () => {
        this.setState({
            count: this.state.count + 1,
        })
    }
    render() {
        const { count } = this.state;
        return(
            <div>
                <h1>Manzanas: {count}</h1>
                <button type="button" onClick={this.handleClick}>
                    Agregar
                </button>
            </div>

        )
    }
}

export default Button;
```
Manejar eventos en elementos de React es muy similar a manejar eventos con elementos del DOM. Hay algunas diferencias de sintaxis:

-   Los eventos de React se nombran usando camelCase, en vez de minúsculas.
-   Con JSX pasas una función como el manejador del evento, en vez de un string.

Por ejemplo, el HTML:

```jsx
<button onclick="activateLasers()">
  Activate Lasers
</button>
```

En React es algo diferente:

```jsx
<button onClick={activateLasers}>
  Activate Lasers
</button>
```

Otra diferencia es que en React no puedes retornar  `false`  para prevenir el comportamiento por defecto. Debes, explícitamente, llamar  `preventDefault`. Por ejemplo, en un HTML plano, para prevenir el comportamiento por defecto de un enlace de abrir una nueva página, puedes escribir:

```jsx
<a href="#" onclick="console.log('The link was clicked.'); return false">
  Click me
</a>
```

En cambio en React, esto podría ser:

```jsx
function ActionLink() {
  function handleClick(e) {
    e.preventDefault();
    console.log('The link was clicked.');
  }

  return (
    <a href="#" onClick={handleClick}>
      Click me
    </a>
  );
}
```

Aquí,  `e`  es un evento sintético. React define estos eventos sintéticos acorde a las  [especificaciones W3C](https://www.w3.org/TR/DOM-Level-3-Events/), entonces no debes preocuparte por la compatibilidad a tráves de los navegadores. Mira la guía de referencia  [`SyntheticEvent`](https://es.reactjs.org/docs/events.html)  para aprender más.

Cuando estás utilizando React, generalmente, no debes llamar  `addEventListener`  para agregar escuchadores de eventos a un elemento del DOM después de que este es creado. Por el contrario, solo debes proveer un manejador de eventos cuando el elemento es inicialmente renderizado.

Cuando defines un componente usando una  [clase de ES6](https://developer.mozilla.org/es/docs/Web/JavaScript/Referencia/Classes), un patrón muy común es que los manejadores de eventos sean un método de la clase. Por ejemplo, este componente  `Toggle`  renderiza un botón que permite al usuario cambiar el estado entre “ENCENDIDO” y “APAGADO”:

```jsx
class Toggle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {isToggleOn: true};

    // Este enlace es necesario para hacer que `this` funcione en el callback
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.setState(state => ({
      isToggleOn: !state.isToggleOn
    }));
  }

  render() {
    return (
      <button onClick={this.handleClick}>
        {this.state.isToggleOn ? 'ON' : 'OFF'}
      </button>
    );
  }
}

ReactDOM.render(
  <Toggle />,
  document.getElementById('root')
);
```

[**Pruébalo en CodePen**](https://codepen.io/gaearon/pen/xEmzGg?editors=0010)

Tienes que tener mucho cuidado en cuanto al significado de  `this`  en los callbacks de JSX. En JavaScript, los métodos de clase no están  [ligados](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_objects/Function/bind)  por defecto. Si olvidas ligar  `this.handleClick`  y lo pasas a  `onClick`,  `this`  será  `undefined`  cuando se llame la función.

Esto no es un comportamiento especifico de React; esto hace parte de  [como operan las funciones JavaScript](https://www.smashingmagazine.com/2014/01/understanding-javascript-function-prototype-bind/). Generalmente, si refieres un método sin usar  `()`  después de este, tal como  `onClick={this.handleClick}`, deberías ligar ese método.

Si te molesta llamar  `bind`, existen dos maneras de evitarlo. Si usas la sintaxis experimental  [campos públicos de clases](https://babeljs.io/docs/plugins/transform-class-properties/), puedes usar los campos de clases para ligar los callbacks correctamente:

```jsx
class LoggingButton extends React.Component {
  // Esta sintaxis nos asegura que `this` está ligado dentro de handleClick
  // Peligro: esto es una sintaxis *experimental*
  handleClick = () => {
    console.log('this is:', this);
  }

  render() {
    return (
      <button onClick={this.handleClick}>
        Click me
      </button>
    );
  }
}
```

Esta sintaxis está habilitada por defecto en  [Create React App](https://github.com/facebookincubator/create-react-app).

Si no estas usando la sintaxis de campos públicos de clases, puedes usar una  [función flecha](https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Functions/Arrow_functions)  en el callback:

```jsx
class LoggingButton extends React.Component {
  handleClick() {
    console.log('this is:', this);
  }

  render() {
    // Esta sintaxis nos asegura que `this` esta ligado dentro de handleClick
    return (
      <button onClick={(e) => this.handleClick(e)}>
        Click me
      </button>
    );
  }
}
```

El problema con esta sintaxis es que un callback diferente es creado cada vez que  `LogginButton`  es renderizado. En la mayoría de los casos, esto está bien. Sin embargo, si este callback se pasa como una propiedad a componentes más bajos, estos componentes podrían renderizarse nuevamente. Generalmente, recomendamos ligar en el constructor o usar la sintaxis de campos de clases, para evitar esta clase de problemas de rendimiento.

#### Pasando argumentos a escuchadores de eventos

Dentro de un bucle es muy común querer pasar un parámetro extra a un manejador de eventos. Por ejemplo, si  `id`  es el ID de una fila, cualquiera de los códigos a continuación podría funcionar:

```jsx
<button onClick={(e) => this.deleteRow(id, e)}>Delete Row</button>
<button onClick={this.deleteRow.bind(this, id)}>Delete Row</button>
```

Las dos líneas anteriores son equivalentes, y utilizan  [funciones flecha](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)  y  [`Function.prototype.bind`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_objects/Function/bind)  respectivamente.

En ambos casos, el argumento  `e`  que representa el evento de React va a ser pasado como un segundo argumento después del ID. Con una función flecha, tenemos que pasarlo explícitamente, pero con  `bind`  cualquier argumento adicional es pasado automáticamente.

### 8. Instalación y configuración de entorno
**NOTA** Commit `Add. _Curso Practico ReactJS_ 8. Instalación y configuración de entorno` en mi repo

```bash
mkdir PlatziVideo && cd PlatziVideo
```
```bash
$ npm init -y
```
Estructura basica
```bash
.
├── package.json
├── public
│   └── index.html
└── src
    └── components
    └── index.js

```
Instalar react
```bash
$ npm install react react-dom
```

### 9. Agregando compatibilidad con todos los navegadores usando Babel
:link: [BabelJS](https://babeljs.io/)
**NOTA**
**Babel** es una herramienta muy popular para escribir JavaScript moderno y transformarlo en código que pueda entender cualquier navegador.

Instalación de **Babel** y otras herramientas para que funcione con React:
```bash
npm install --save-dev @babel/core @babel/preset-env @babel/preset-react babel-loader
```
Configuración de Babel `.babelrc` archivo que tiene que estar en la raiz del proyecto:
```json
{
  "presets": [
    "@babel/preset-env",
    "@babel/preset-react"
  ],
}
```
`HellowWorld.js`
```jsx
import React from 'react';

const HellowWorld = () => {
    <h1>Hola Mundo</h1>
};

export default HellowWorld;
```
`index.js`
```jsx
import React from 'react';
import ReactDOM from 'react-dom';

import HellowWorld from './components/HelloWorld'

ReactDOM.render(<HelloWorld />, document.getElementById('app'));
```
`index.html`
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Platzi Video</title>
    <link rel="stylesheet" href="">
</head>
<body>
    <div id='app'></div>
</body>
</html>
```

## 3. Configurar un entorno de trabajo profesional
### 10. Webpack: Empaquetando nuestros módulos
**NOTA** Mi repo commit `Add. _Curso Practico ReactJS_ 10. Webpack: Empaquetando nuestros módulos`

**Webpack** es una herramienta que nos ayuda a compilar multiples archivos (JavaScript, HTML, CSS, imágenes) en uno solo (o a veces un poco más) que tendrá todo nuestro código listo para producción.

Instalación de **Webpack** y algunos plugins:
```bash
npm install webpack webpack-cli html-webpack-plugin html-loader  --save-dev
```
Configuración de Webpack `webpack.config.js` que tiene que estar instalado en la raiz del proyecto, a la misma altura de `package.json`:
```js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
  },
  resolve: {
    extensions: ['.js', '.jsx'],
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        },
      },
      {
        test: /\.html$/,
        use: {
          loader: 'html-loader',
        },
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './public/index.html',
      filename: './index.html',
    }),
  ],
};
```
Script para ejecutar las tareas de Webpack `package.json` se modifica añadiendo lo siguiente para compilar el proyecto
```json
{
  "scripts": {
    "build": "webpack --mode production"
  },
}
```
Ejecutar
```bash
npm run build
```
salida..(EXITOSA)
```
> PlatziVideo@1.0.0 build /home/mack/Documents/mi_cuaderno/Practico_ReactJS/PlatziVideo
> webpack --mode production

Hash: 039c06a7b28ab43d2de5
Version: webpack 4.43.0
Time: 7014ms
Built at: 05/11/2020 8:10:11 PM
       Asset       Size  Chunks             Chunk Names
./index.html  134 bytes          [emitted]  
   bundle.js    128 KiB       0  [emitted]  main
Entrypoint main = bundle.js
[7] ./src/index.js + 1 modules 390 bytes {0} [built]
    | ./src/index.js 212 bytes [built]
    |     + 1 hidden module
    + 7 hidden modules
Child HtmlWebpackCompiler:
     1 asset
    Entrypoint HtmlWebpackPlugin_0 = __child-HtmlWebpackPlugin_0
    [0] ./node_modules/html-webpack-plugin/lib/loader.js!./public/index.html 165 bytes {0} [built]

```

### 11. Webpack Dev Server: Reporte de errores y Cambios en tiempo real
**NOTA** Mi repo commit `Add. _Curso Practico ReactJS_ 11. Webpack Dev Server: Reporte de errores y Cambios en tiempo real`

Para probrar lo que estamos contruyendo y crear un entorno de desarrollo local que nos permita ver los cambios en tiempo real.

Instalación de Webpack Dev Server:
```bash
npm install --save-dev webpack-dev-server
```
Script para ejecutar el servidor de Webpack y visualizar los cambios en tiempo real (package.json):

Modo de desarrollo
```bash
{
  "scripts": {
    "build": "webpack --mode production",
    "start": "webpack-dev-server --open --mode development"
  },
}
```
Para iniciar el servidor se ejecuta el comando `npm run start` y se abre en el explirardor en la dirección `localhost:8081`


### 12. Estilos con SASS
**NOTA** Mi repo commit `Add. _Curso Practico ReactJS_ 12. Estilos con SASS`


Los **preprocesadores** como _Sass_ son herramientas que nos permiten escribir CSS con una sintaxis un poco diferente y más amigable que luego se transformará en CSS normal. Gracias a _Sass_ podemos escribir CSS con variables, mixins, bucles, entre otras características.

Instalación de _Sass_:
```bash
npm install --save-dev mini-css-extract-plugin css-loader node-sass sass-loader
```
Se añade una nueva regla "test" a la Configuración de Sass en Webpack `webpack.config.js`:
```js
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
// ...
module: {
  rules: [
    {
      test: /\.(s*)css$/,
      use: [
        { loader: MiniCssExtractPlugin.loader },
        'css-loader',
        'sass-loader',
      ],
    }, 
  ],
},
// ...
plugins: [
  new MiniCssExtractPlugin({
    filename: 'assets/[name].css',
  }),
],`
```
La estructura recomendada es que dentro de la carpeta `src` se se cree la carpeta `assets` y dentro de esta, crear otra carpeta llamada `styles` y se crea el archivo `App.scss`

Hasta el momento la estructura
```
src
├── assets
│   └── styles
│       └── App.scss
├── components
│   └── HelloWorld.jsx
└── index.js
```
`App.scss`
```scss
body {
    margin: 0;
    background-color: red;
}
```
Dentro del archivo `HelloWorld.js` se importa.

### 13. Configuración final: ESLint y Git Ignore
**NOTA** Mi repo commit `Add. _Curso Practico ReactJS_ 13. Configuración final: ESLint y Git Ignore`

El **Git Ignore** es un archivo que nos permite definir qué archivos **NO** queremos publicar en nuestros repositorios. Solo debemos crear el archivo .gitignore y escribir los nombres de los archivos y/o carpetas que no queremos publicar.

Los _linters_ como **ESLint** son herramientas que nos ayudan a seguir buenas prácticas o guías de estilo de nuestro código.
Se encargan de revisar el código que escribimos para indicarnos dónde tenemos errores o posibles errores. En algunos casos también pueden solucionar los errores automáticamente. De esta manera podemos solucionar los errores incluso antes de que sucedan.
Instalación de **ESLint**:
```bash
npm install --save-dev eslint babel-eslint eslint-config-airbnb eslint-plugin-import eslint-plugin-react eslint-plugin-jsx-a11y
```
El archivo recomendado por Platzi de [.gitignore](https://gist.github.com/gndx/747a8913d12e96ff8374e2125efde544) es el siguiente
```
# Node template

# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Directory for instrumented libs generated by jscoverage/JSCover
lib-cov

# Coverage directory used by tools like istanbul
coverage

# nyc test coverage
.nyc_output

# Grunt intermediate storage (http://gruntjs.com/creating-plugins#storing-task-files)
.grunt

# Bower dependency directory (https://bower.io/)
bower_components

# node-waf configuration
.lock-wscript

# Compiled binary addons (https://nodejs.org/api/addons.html)
build/Release

# Dependency directories
node_modules/
jspm_packages/

# Typescript v1 declaration files
typings/

# Optional npm cache directory
.npm

# Optional eslint cache
.eslintcache

# Optional REPL history
.node_repl_history

# Output of 'npm pack'
*.tgz

# Yarn Integrity file
.yarn-integrity

# dotenv environment variables file
.env

# IDE
.idea/*
*.iml
*.sublime-*

# OSX
.DS_Store
.vscode

# Docs Custom
.cache/
yarn-error.log

# Build
dist/
```

El archivo recomendado por Platzi para buenas practicas con [ESLint](https://gist.github.com/gndx/60ae8b1807263e3a55f790ed17c4c57a) es el siguiente y se debe de llamar `.eslintrc` y tienen que estar localizado en la la raiz del proyecto.
```json
{
  "env": {
    "browser": true,
    "es6": true,
    "node": true
  },
  "extends": ["airbnb"],
  "globals": {
    "document": false,
    "escape": false,
    "navigator": false,
    "unescape": false,
    "window": false,
    "describe": true,
    "before": true,
    "it": true,
    "expect": true,
    "sinon": true
  },
  "parser": "babel-eslint",
  "plugins": [
    "react",
    "jsx-a11y",
    "import"
  ],
  "rules": {
    "react/jsx-filename-extension": 0,
    "array-bracket-spacing": 2,
    "arrow-body-style": 0,
    "block-scoped-var": 2,
    "brace-style": [2, "1tbs", { "allowSingleLine": true }],
    "comma-spacing": [2, { "before": false, "after": true }],
    "comma-style": [2, "last"],
    "complexity": 0,
    "consistent-return": 1,
    "consistent-this": 0,
    "curly": [2, "multi-line"],
    "default-case": 0,
    "dot-location": [2, "property"],
    "dot-notation": 0,
    "eol-last": 2,
    "eqeqeq": [2, "allow-null"],
    "func-names": 0,
    "func-style": 0,
    "generator-star-spacing": [2, "both"],
    "guard-for-in": 0,
    "handle-callback-err": [2, "^(err|error|anySpecificError)$" ],
    "indent": [2, 2, { "SwitchCase": 1 }],
    "key-spacing": [2, { "beforeColon": false, "afterColon": true }],
    "linebreak-style": 0,
    "max-depth": 0,
    "max-len": [2, 1550, 4],
    "max-nested-callbacks": 0,
    "max-params": 0,
    "max-statements": 0,
    "new-cap": [2, { "newIsCap": true, "capIsNew": false }],
    "newline-after-var": [0, "never"],
    "new-parens": 2,
    "no-alert": 0,
    "no-array-constructor": 2,
    "no-bitwise": 0,
    "no-caller": 2,
    "no-catch-shadow": 0,
    "no-cond-assign": 2,
    "no-console": 0,
    "no-constant-condition": 0,
    "no-continue": 0,
    "no-control-regex": 2,
    "no-debugger": 0,
    "no-delete-var": 2,
    "no-div-regex": 0,
    "no-dupe-args": 2,
    "no-dupe-keys": 2,
    "no-duplicate-case": 2,
    "no-else-return": 2,
    "no-empty": 0,
    "no-empty-character-class": 2,
    "no-labels": 2,
    "no-eq-null": 0,
    "no-eval": 2,
    "no-ex-assign": 2,
    "no-extend-native": 2,
    "no-extra-bind": 2,
    "no-extra-boolean-cast": 2,
    "no-extra-parens": 0,
    "no-extra-semi": 0,
    "no-extra-strict": 0,
    "no-fallthrough": 2,
    "no-floating-decimal": 2,
    "no-func-assign": 2,
    "no-implied-eval": 2,
    "no-inline-comments": 0,
    "no-inner-declarations": [2, "functions"],
    "no-invalid-regexp": 2,
    "no-irregular-whitespace": 2,
    "no-iterator": 2,
    "no-label-var": 2,
    "no-lone-blocks": 0,
    "no-lonely-if": 0,
    "no-loop-func": 0,
    "no-mixed-requires": 0,
    "no-mixed-spaces-and-tabs": [2, false],
    "no-multi-spaces": 2,
    "no-multi-str": 0,
    "no-multiple-empty-lines": [2, { "max": 1 }],
    "no-native-reassign": 2,
    "no-negated-in-lhs": 2,
    "no-nested-ternary": 0,
    "no-new": 2,
    "no-new-func": 2,
    "no-new-object": 2,
    "no-new-require": 2,
    "no-new-wrappers": 2,
    "no-obj-calls": 2,
    "no-octal": 2,
    "no-octal-escape": 2,
    "no-path-concat": 0,
    "no-plusplus": 0,
    "no-process-env": 0,
    "no-process-exit": 0,
    "no-proto": 2,
    "no-redeclare": 2,
    "no-regex-spaces": 2,
    "no-reserved-keys": 0,
    "no-restricted-modules": 0,
    "no-script-url": 0,
    "no-self-compare": 2,
    "no-sequences": 2,
    "no-shadow": 0,
    "no-shadow-restricted-names": 2,
    "no-spaced-func": 2,
    "no-sparse-arrays": 2,
    "no-sync": 0,
    "no-ternary": 0,
    "no-throw-literal": 2,
    "no-trailing-spaces": 2,
    "no-undef": 0,
    "no-undef-init": 2,
    "no-undefined": 0,
    "no-underscore-dangle": 0,
    "no-unneeded-ternary": 2,
    "no-unreachable": 2,
    "no-unused-expressions": 0,
    "no-unused-vars": [2, { "vars": "all", "args": "none" }],
    "no-var": 2,
    "no-void": 0,
    "no-warning-comments": 0,
    "no-with": 2,
    "object-curly-newline": 0,
    "object-curly-spacing": [2, "always"],
    "one-var": 0,
    "operator-assignment": 0,
    "operator-linebreak": [2, "after"],
    "padded-blocks": 0,
    "prefer-const": 2,
    "quote-props": 0,
    "quotes": [2, "single", "avoid-escape"],
    "radix": 2,
    "jsx-quotes": [2, "prefer-single"],
    "jsx-a11y/click-events-have-key-events": 0,
    "jsx-a11y/no-noninteractive-element-interactions": 0,
    "jsx-a11y/media-has-caption": 0,
    "react/display-name": 0,
    "react/jsx-boolean-value": 0,
    "react/jsx-closing-bracket-location": 2,
    "react/jsx-curly-spacing": [2, "never"],
    "react/jsx-equals-spacing": [2, "never"],
    "react/jsx-indent-props": [2, 2],
    "react/jsx-no-bind": [2, { "allowArrowFunctions": true }],
    "react/jsx-no-undef": 2,
    "react/jsx-pascal-case": 2,
    "react/jsx-sort-prop-types": 0,
    "react/jsx-sort-props": 0,
    "react/jsx-uses-react": 2,
    "react/jsx-uses-vars": 2,
    "react/no-did-mount-set-state": 2,
    "react/no-did-update-set-state": 2,
    "react/no-multi-comp": 0,
    "react/no-unknown-property": 2,
    "react/prop-types": 0,
    "react/forbid-prop-types": 0,
    "react/prefer-stateless-function": 0,
    "react/require-default-props": 0,
    "react/react-in-jsx-scope": 2,
    "react/self-closing-comp": 2,
    "react/sort-comp": 0,
    "react/jsx-wrap-multilines": 2,
    "semi-spacing": 0,
    "sort-vars": 0,
    "space-before-blocks": [2, "always"],
    "space-before-function-paren": [2, {"anonymous": "always", "named": "never"}],
    "space-in-parens": [2, "never"],
    "space-infix-ops": 2,
    "keyword-spacing": 2,
    "space-unary-ops": [2, { "words": true, "nonwords": false }],
    "spaced-comment": [0, "always"],
    "strict": 0,
    "use-isnan": 2,
    "valid-jsdoc": 0,
    "valid-typeof": 2,
    "vars-on-top": 2,
    "wrap-iife": [2, "any"],
    "wrap-regex": 0,
    "yoda": [2, "never"]
  }
}
```
### 14. Arquitectura de componentes para Platzi Video


## 4. Llevar un diseño de HTML y CSS a React
### 15. Estructura del Header


### 16. Estilos del Header
### 17. Estructura y Estilos del Buscador
### 18. Estructura y Estilos de Carousel y Carousel Item
### 19. Estructura y Estilos del Footer
### 20. Añadiendo imágenes con Webpack
### 21. Imports, Variables y Fuentes de Google en Sass

## 5. Uso de una API de desarrollo (Fake API)
### 22. Creando una Fake API
**NOTA**: Mi repo commit `Add. _Curso Practico ReactJS_ 22. Creando una Fake API`

:link: [initialState.json - Archivo que funciona como FALE API para el proyecto](https://gist.github.com/gndx/d4ca4739450afaa614efe4570ac362ee), y este se debe de encontrar en la raiz del proyecto.

Para usar **JSON Server** para crear una _Fake API_: una API **falsa** construida a partir de un archivo JSON que nos permite preparar nuestro código para consumir una API de verdad en el futuro.

Instalación de **JSON Server**:
```bash
sudo npm install json-server -g
```

Ejecutar el servidor de JSON Server, 

```bash
json-server <NOMBRE_DE_ARCHIVO_QUE_CONTIENE_API>.json
```
**NOTA**: La parte que dice **initalState** está mal, es **initialState**
```bash
$ json-server initialState.json 

  \{^_^}/ hi!

  Loading initialState.json
  Done

  Resources
  http://localhost:3000/initialState

  Home
  http://localhost:3000

  Type s + enter at any time to create a snapshot of the database

```

### 23. React Hooks: useEffect y useState

**React Hooks**: una característica de React disponible a partir de la versión _16.8_ que nos permite agregar estado y ciclo de vida a nuestros componentes creados como funciones.

React es una librería desarrollada por _Facebook_ que nos ayuda a construir interfaces de usuario interactivas para todo tipo de aplicaciones: páginas web, aplicaciones móviles o de escritorio, experiencias de realidad virtual, entre otras.


> Son funciones que nos permiten acceder a **casi todas** las caracteristicas de RactJs desde componentes funcionales

### 24. Lectura React Hooks

Los **React Hooks** son una característica de React que tenemos disponible a partir de la versión 16.8. Nos permiten agregar estado y ciclo de vida a nuestros componentes creados como funciones.

El Hook `useState` nos devuelve un array con dos elementos: la primera posición es el valor de nuestro estado, la segunda es una función que nos permite actualizar ese valor.

El argumento que enviamos a esta función es el valor por defecto de nuestro estado (_initial state_).

```jsx
import React, { useState } from 'react';

const Component = () => {
  const [name, setName] = useState('Nombre por defecto');

  return <div>{name}div>;
}
```
**El Hook** `useEffect` nos permite ejecutar código cuando se monta, desmonta o actualiza nuestro componente.

El primer argumento que le enviamos a `useEffect` es una función que se ejecutará cuando React monte o actualice el componente. Esta función puede devolver otra función que se ejecutará cuando el componente se desmonte.

El segundo argumento es un array donde podemos especificar qué propiedades deben cambiar para que React vuelva a llamar nuestro código. Si el componente actualiza pero estas props no cambian, la función no se ejecutará.

Por defecto, cuando no enviamos un segundo argumento, React ejecutará la función de `useEffect` cada vez que el componente o sus componentes padres actualicen. En cambio, si enviamos un array vacío, esta función solo se ejecutará al montar o desmontar el componente.

```jsx
import React, { useState, useEffect } from 'react';

const Component = () => {
  const [name, setName] = useState('Nombre por defecto');

  useEffect(() => {
    document.title = name;
    return () => {
      document.title = 'el componente se desmontó';
    };
  }, [name]);

  return <div>{name}div>;
}
```
**No olvidar importar** las funciones de los hooks desde la librería de React.  
También puedes usarlos de esta forma: `React.useNombreDelHook`



### 25. Conectando la información de la API
### 26. Custom Hooks
### 27. PropTypes

## 6. Usar React Tools
### 28. Debuggeando React con React DevTools
### 29. Prepárate para lo que sigue




































































