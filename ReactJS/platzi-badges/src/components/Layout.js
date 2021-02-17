import React from 'react';

import Navbar from './Navbar';

function Layout(props) {
  // const children = props.children;
/* SIEMPRE QUE SE REGRESA EL elemento en el render SE TIENE QUE REGRESAR UN ELEMENTO 
PARA NO TENER UN div FORZADO EN TODOS LOS COMPONENTES EN LOS QUE SE USA `React.Fragment`
COMPONENTE ESPECIAL QUE REACT ENTIENDE Y QUE HACE QUE REGRESEMOS MAS DE UN ELEMENTO, AUNQUE PARESCA QUE SOLO ES NO */
  return (
    <React.Fragment>
      <Navbar />
      {props.children}
    </React.Fragment>
  );
}

export default Layout;