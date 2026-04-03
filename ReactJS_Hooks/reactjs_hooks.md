# React Hooks

¿Qué son los React Hooks y cómo cambian el desarrollo con React?

Es una característica que salió en la versión 16.8 en febrero de 2019.

Los Hooks vienen a cambiar la forma de desarrollo en React.
⠀
Vienen a resolver problemas ligados a React, como la complejidad de los componentes, no se podía compartir la lógica de estado entre componentes, Component Hell, etc.

Los Hooks presentan una alternativa al desarrollo con clases, ya que estos vienen a trabajar con funciones.

Un Hook es una función especial que nos permitirá conectarnos a características de React, para trabajar con métodos especiales, los cuales nos permitirán manejar el estado de mejor forma sin depender de clases.

**Hooks** son una nueva característica en React desde 16.8. Estos te permiten usar el estado y otras características de React sin escribir una clase.

- 🚨 Algunas reglas para el uso de Hooks:
  1. Se tienen que usar en el nivel más alto de tu componente.
  2. Llamar hooks solo en **componentes** de React.
  3. No llamar hooks de manera condicional.

Hooks centrales:

- `useState`: Nos ayuda a manejar el estado en componentes creados como funciones
- `useEffect`:
  - Se manda a llamar cuando ciertos parámetros cambian y/o funciones, cuando ciertos valores cambian.
  - Nos permite manejar efectos que van a ser transmitidos dentro del componente.
  - Su callback no puede ser async, pero si se puede llamar una función async dentro de este.
  - Puede ser utilizado para hacer llamadas a una API, para hacer un fetch, para hacer un cambio en el DOM, es el último donde se busca cuando un componente se **desmonta**.
- `useContext`: Resuelve el problema de pasar información entre componentes, poderlos interconectar sin necesidad del prop y estarán ligadas de padre a hijo; es la fusión de React Hooks y React Context
- `useReducer`: Implementa una forma más amigable y con más características para trabajar con el estado; es como `useState`, pero más escalable.Se tiene un estado inicial, un reducer y un dispatch para mandar la información.

Hooks de rendimiento:

- `useMemo` Nos ayuda a evitar cálculos innecesarios utilizando la memoización.
- `useRef`:
  - Referenciar un valor que no es necesario para renderizar.
  - Es el manejo profesional de inputs y formularios, todo esto para manejar como las referencias a los formularios e inputs.
  - ejemplo: `const data = useRef([])` la variable data es mutable.
  - `data.current = valoresDeUnJson` para actualizar el valor.
  - `data.current` para acceder al valor actual.
  - Nos permite **mantener una referencia mutable** a un elemento del DOM.
  - Nos permite actualizar un valor pero no actualizar un componente.
- `useCallback` Nos ayuda a evitar cálculos innecesarios en funciones

Nuevos Hooks en React 18.3:

- `useTransition` Nos permite manejar las transiciones de los elementos de la interfaz de usuario.
- `useDeferredValue` Nos permite manejar el diferimiento de los valores de los elementos de la interfaz de usuario.
- `useOpaqueIdentifier` Nos permite manejar la identificación de los elementos de la interfaz de usuario.

React DOM Hooks (para aplicaciones web):

- `useLayoutEffect`: es similar a `useEffect`, pero se ejecuta de forma sincronía después de todas las mutaciones del DOM.
- `useImperativeHandle`: personaliza la instancia de un componente hijo que se expone a un componente padre.

- `useActionState`:
- `useDebugValue`:
- `useOptimistic`:
- `useSyncExternalStore`:

- `Custom hooks`:
  - Se crean con la palabra `use` al inicio, después con nombre descriptivo.
  - _Es una función que "puede" contener uno o más hooks_ cuando es utilizado por componentes.
  - Se crean cuando se necesita reutilizar lógica en diferentes componentes.
  - En React Hooks podemos realizar hooks personalizados con los cuales podemos separar lógica y separarlos de cualquier componente; es la abstracción en la lógica de tus componentes.

2. Introducción a React Hooks

## `useState`: estado en componentes creados como funciones

Este Hook nos ayuda a manejar el estado en componentes creados como funciones

**useState**
Te permite poder usar variables de estado dentro de componentes funcionales.

El Hook useState siempre nos retorna un array de dos posiciones. En la primera posición [0] vamos a tener el estado y él la segunda posición [1] vamos a tener la funciona para manipular el estado.

```js
const [state, setState] = useState(0);
```

En este caso hacemos uso de la desestructuración del array una característica de ES6.

`state ⇒ 0` `setState` ⇒ **Función que actualiza el estado**

- Nuestro estado puede ser de los siguente tipos:
  - String
  - Boolean
  - Number
  - Float
  - Null
  - Undefined
  - Object
  - Array

```js
// traemos useState al documento
import React, { useState } from "react";

const Header = () => {
  /*
   * Integrar useState a esta logica
   * useState va a manejar este estado
   * y haremos una función que cambia de Darmode a lightmode
   */

  /*
   * Constante que va a estructurar 2 elementos
   * el primero(darkMode) es el estado
   * el segundo(setDarkMode) es la función que cambiará al estado(darkMode)
   * de useState y lo pasamos como una función con estado inicial false
   */
  const [darkMode, setDarkMode] = useState(false);

  /*
   * Función para hacer los cambios de estado
   */
  const handleClick = () => {
    setDarkMode(!darkMode);
  };

  /*
   * Creamos el header con el logo
   * y un boton para activar el DarkMode
   * dentro del boton ingresamos la logica para mostrar darkmode o lightMode
   */
  return (
    <div className="Header">
      <h1>React hooks</h1>
      <button type="button" onClick={handleClick}>
        {darkMode ? "Dark Mode" : "Light Mode"}
      </button>
      <button type="button" onClick={() => setDarkMode(!darkMode)}>
        {darkMode ? "Dark Mode 2" : "Light Mode 2"}
      </button>
    </div>
  );
};

export default Header;
```

## `useEffect`: olvida el ciclo de vida, ahora piensa en efectos

**useEffect** nos permite manejar efectos que van a ser transmitidos dentro del componente.

En este ejemplo se llama a una API, traemos la información y la ejecutaremos en el componente

```js
import React, { useState, useEffect } from "react";

const Characters = () => {
  const [characters, setCharacters] = useState([]);

  useEffect(() => {
    fetch("https://rickandmortyapi.com/api/character/")
      .then((response) => response.json())
      .then((data) => setCharacters(data.results));
  }, []);

  return (
    <div className="Characters">
      {characters.map((character) => (
        <h2>{character.name}</h2>
      ))}
    </div>
  );
};

export default Characters;
```

Alternativa de ejemplo con **asyn/await**

```js
import React, { useState, useEffect } from "react";

const Characters = () => {
  const [characters, setCharacters] = useState([]);

  const getCharacters = async () => {
    const response = await fetch("https://rickandmortyapi.com/api/character");
    const data = await response.json();
    setCharacters(data.results);
  };

  useEffect(() => {
    getCharacters();
  }, []);

  return (
    <div className="Characters">
      {characters.map((character) => (
        <h2 key={character.id}>{character.name}</h2>
      ))}
    </div>
  );
};

export default Characters;
```

TODO: Crea una API con Strapi CMS y consúmela con React.js
