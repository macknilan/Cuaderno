const passport = require("passport");
const { BasicStrategy } = require("passport-http");
const boom = require("@hapi/boom");
const bcrypt = require("bcrypt");
const MongoLib = require("../../../lib/mongo");

passport.use(
  new BasicStrategy(async function(username, password, cb) {
    const mongoDB = new MongoLib();

    try {
      const [user] = await mongoDB.getAll("users", { username });

      if (!user) {
        return cb(boom.unauthorized(), false);
      }

      if (!(await bcrypt.compare(password, user.password))) {
        return cb(boom.unauthorized(), false);
      }
      // SE REGRESA EL USUARIO SI EXISTE
      return cb(null, user); // ERROR FIRST CALLBACK
    } catch (error) {
      return cb(error);
    }
  })
);