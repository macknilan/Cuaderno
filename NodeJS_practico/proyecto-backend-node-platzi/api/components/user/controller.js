// SE USA NANOID PARA GENERAR RANDOM ID
const { nanoid } = require("nanoid");
// EL INDEX DEFINE CUAL ES EL ALMACENAMIENTO DE PRODUCCION
// POR QUE AUTOMATICAMENTE SE SE INSERTA EN EL CONTROLADOR EL METODO DE ALMACENAMIENTO
const auth = require("../auth");

// user ES EL PARAMETRO(NOMBRE DE LA TABLA A BUSCAR) A BUSCAR EN LA BD
const TABLA = "user";

module.exports = function (injectStore) {
  let store = injectStore;
  if (!store) {
    store = require("../../../store/mysql");
  }

  function list() {
    return store.list(TABLA);
  }
  function get(id) {
    return store.get(TABLA, id);
  }
  // FUNCION ASYNCRONA PARA CAMBIAR USUARIO/CONTRASEÑA
  async function upsert(body) {
    const user = {
      name: body.name,
      username: body.username,
    };
    if (body.id) {
      user.id = body.id;
    } else {
      user.id = nanoid();
    }
    // SI HAY UNA CONTRASEÑA O USERNAME QUE SE QUIEREN CAMBIAR
    if (body.password || body.username) {
      await auth.upsert({
        id: user.id,
        username: user.username,
        password: body.password,
      });
    }

    return store.upsert(TABLA, user);
  }
  // FUNCION QUE ENCARGA DE PASAR DESDE LA url DEL USUARIO QUE ESTA LOGEADO
  // A QUE OTRO USUARIO VA A SEGUIR '/follow/:id'
    function follow(from, to) {
        console.log(`from-> ${from} - to-> ${to}`)
        // TABLA + '_follow', = user_follow
        return store.upsert(TABLA + '_follow', {
            user_from: from,
            user_to: to,
        });
    }

  return {
    list,
    get,
    upsert,
    follow
  };
};
