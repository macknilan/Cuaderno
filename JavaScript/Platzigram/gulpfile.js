var gulp = require('gulp'); // SE REQUIRE gulp LO BUSCA EN LA CARPETA node_modules
var sass = require('gulp-sass'); // SE REQUIERE gulp-sass LO BUSCA EN LA CARPETA node_modules
var rename = require('gulp-rename')


gulp.task('styles', function() { // SE DEFINE UNA TAREA styles - EL 2DO PARAMETRO ES UNA FUNC QUE SE EJECUTA
    gulp
        .src('index.scss') // QUE TOME UN ARCHIVO UNICIAL DE sass Y QUE LO PASE POR EL PROCESADOR sass
        .pipe(sass()) // QUE LO PASE POR sass
        .pipe(rename('app.css'))
        .pipe(gulp.dest('public'));  // QUE EL ARCHIVO QUE PROCESO DONDE LO QUIERE PONER "EN LA CARPETA public"
    })

gulp.task('default', ['styles']) // ESTA ES LA TAREA PREDETERMINADA CON NOMBRE "default" ejecuta un arreglo de tareas