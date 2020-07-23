// const element = document.createElement('h1');
// element.innerText = 'Hello, Platzi Badges!';

// const container = document.getElementById('app');

// container.appendChild(element);

import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.css';

import './global.css';
/* import Badge from './components/Badge' */
// import BadgeNew from './pages/BadgeNew'
// import Badges from './pages/Badges';
import App from './components/App';


/* const jsx = <h1> Hello, Platzi Badges!</h1>; */
/* const element = React.createElement('a', {
        href: 'https://platzi.com'
    }, 'Ir a Platzi'); */

/* const name = 'Rodo'; */
/* const element = React.createElement('h1', {}, `Hola, soy ${name}`); */

/* const jsx = <h1>Hola,soy {name}</h1>; */
/* const jsx = <h1>Hola,soy {2 + 2}</h1>; */
/* const sum = () => 3 + 3; */
/* const jsx = <h1>Hola,soy {sum()}</h1>; */
/* const jsx = <h1>Hola,soy {__expressions__}</h1>; */

/* const jsx = (
    <div>
        <h1>Hola soy Ro</h1>
        <p>Soy Inge</p>
    </div>
); */

const container = document.getElementById('app');

// ReactDOM.render(__qué__, __dónde__);
/* ReactDOM.render(<Badge />, container); */
/* ReactDOM.render(
    <Badge
      firstName="Richard"
      lastName="Kaufman"
      avatarUrl="https://www.gravatar.com/avatar/21594ed15d68ace3965642162f8d2e84?d=identicon"
      jobTitle="Frontend Engineer"
      twitter="sparragus"
    />,
    container
); */
/* ReactDOM.render(<BadgeNew />, container); */
/* ReactDOM.render(<Badges />, container); */
ReactDOM.render(<App />, container);