const Joi = require('@hapi/joi');
const Boom = require("@hapi/boom");


function validate(data, schema) {
    // const { error } = Joi.validate(data, schema);
    // console.log(data)
    const { error } = Joi.object(schema).validate(data)
    return error;
}
  
function validationHandler(schema, check = "body") {
    return function(req, res, next) {
        const error = validate(req[check], schema);
        // RETURNS A 400 BAD REQUEST ERROR
        error ? next(Boom.badRequest(error)) : next();
    };
}

module.exports = validationHandler;