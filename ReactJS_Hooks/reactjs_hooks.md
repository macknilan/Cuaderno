
# React Hooks

¿Qué son los React Hooks y cómo cambian el desarrollo con React?
Es una característica que salió en la versión 16.8 en febrero de 2019.
Los Hooks vienen a cambiar la forma de desarrollo en React.
⠀
Vienen a resolver problemas ligados a React, como la complejidad de los componentes, no se podía compartir la lógica de estado entre componentes, Component Hell, etc.

Los Hooks presentan una alternativa al desarrollo con clases, ya que estos vienen a trabajar con funciones.

Un Hook es una función especial que nos permitirá conectarnos a características de React, para trabajar con métodos especiales, los cuales nos permitirán manejar el estado de mejor forma sin depender de clases.

**Hooks** son una nueva característica en React 16.8. Estos te permiten usar el estado y otras características de React sin escribir una clase.

**useState**
`useState` nos ayuda a manejar el estado en componentes creados como funciones

**useEffect**
`useEffect` nos permite manejar efectos que van a ser transmitidos dentro del componente.

**useContext**
`useContext` Resuelve el problema de pasar información entre componentes, poderlos interconectar sin necesidad del prop y estarán ligadas de padre a hijo; es la fusión de React Hooks y React Context

**useReducer**
`useReducer` Implementa una forma más amigable y con más características para trabajar con el estado; es como `useState`, pero más escalable.
Se tiene un estado inicial, un reducer y un dispatch para mandar la información.

**useMemo**
`useMemo` Nos ayuda a evitar cálculos innecesarios utilizando la memoización.

**useRef**
`useRef` Es el manejo profesional de inputs y formularios, todo esto para manejar como las referencias a los formularios e inputs.

**useCallback**
`useCallback` Nos ayuda a evitar cálculos innecesarios en funciones

**Custom hooks**
En React Hooks podemos realizar hooks personalizados con los cuales podemos separar lógica y separarlos de cualquier componente; es la abstracción en la lógica de tus componentes.

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

+ Nuestro estado puede ser de los siguente tipos:
  + String
  + Boolean
  + Number
  + Float
  + Null
  + Undefined
  + Object
  + Array

```js
// traemos useState al documento
import React, {useState} from 'react'

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
            <button type="button" onClick={handleClick}>{darkMode ? 'Dark Mode' : 'Light Mode'}</button>
            <button type="button" onClick={() => setDarkMode(!darkMode)}>{darkMode ? 'Dark Mode 2' : 'Light Mode 2'}</button>
        </div>
    )
}

export default Header
```

## `useEffect`: olvida el ciclo de vida, ahora piensa en efectos

**useEffect** nos permite manejar efectos que van a ser transmitidos dentro del componente.

En este ejemplo se llama a una API, traemos la información y la ejecutaremos en el componente

```js
import React, { useState, useEffect } from 'react';

const Characters = () => {
  const [characters, setCharacters] = useState([]);

  useEffect(() => {
    fetch('https://rickandmortyapi.com/api/character/')
      .then(response => response.json())
      .then(data => setCharacters(data.results));
  }, []);

  return (
    <div className="Characters">
      {characters.map(character => (
        <h2>{character.name}</h2>
      ))}
    </div>
  );
}

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

## `useContext`: la fusión de React Hooks y React Context

## `useReducer`: como useState, pero más escalable

## ¿Qué es memoization? Técnicas de optimización en programación funcional

## `useMemo`: evita cálculos innecesarios en componentes

## `useRef`: manejo profesional de inputs y formularios

## `useCallback`: evita cálculos innecesarios en funciones

## Optimización de componentes en React con React.memo

## Custom hooks: abstracción en la lógica de tus componentes

## Third Party Custom Hooks de Redux y React Router

3. Configura un entorno de desarrollo profesional

## Proyecto: análisis y retos de Platzi Conf Store

## Instalación de Webpack y Babel: presets, plugins y loaders

## Configuración de Webpack 5 y webpack-dev-server

## Configuración de Webpack 5 con loaders y estilos

## Loaders de Webpack para Preprocesadores CSS

## Flujo de desarrollo seguro y consistente con ESLint y Prettier

## Git Hooks con Husky

4. Estructura y creación de componentes para Platzi Conf Store

## Arquitectura de vistas y componentes con React Router DOM

## Maquetación y estilos del home

## Maquetación y estilos de la lista de productos

## Maquetación y estilos del formulario de checkout

## Maquetación y estilos de la información del usuario

## Maquetación y estilos del flujo de pago

## Integración de íconos y conexión con React Router

5. Integración de React Hooks en Platzi Conf Merch

## Creando nuestro primer custom hook

## Implementando useContext en Platzi Conf Merch

## useContext en la página de checkout

## useRef en la página de checkout

## Integrando third party custom hooks en Platzi Conf Merch

6. Configura mapas y pagos con PayPal y Google Maps

## Paso a paso para conectar tu aplicación con la API de PayPal

## Integración de pagos con la API de PayPal

## Completando la integración de pagos con la API de PayPal

## Paso a paso para conectar tu aplicación con la API de Google Maps

## Integración de Google Maps en el mapa de checkout

## Creando un Custom Hook para Google Maps

7. Estrategias de deployment profesional

## Continuous integration y continuous delivery con GitHub Actions

## Compra del dominio y despliega con Cloudflare

8. Optimización de aplicaciones web con React

## Integración de React Helmet para mejorar el SEO con meta etiquetas

## Análisis de performance con Google Lighthouse

## Convierte tu aplicación de React en PWA

9. Bonus: trabaja con Strapi CMS para crear tu propia API

## Crea una API con Strapi CMS y consúmela con React.js
