const gulp = require('gulp');
const server = require('gulp-server-livereload');

gulp.task('build', function(cb) {
    console.log('Construyendo el sitio');
    setTimeout(cb, 1200);
});

// SE LE DICE A GULP QUE INICI IN SERVER
gulp.task('serve', function(cb) {
    gulp.src('www') // DONDE SE VA A GUARGAR LA WEB
        .pipe(server({ //SE TOMA EL "STREAM" PARA DAR ACCESO A NUESTRO SERVIDOR
            livereload: true, // SE ACTUALIZE AUTOMATICAMENTE
            open: true, // QUE AUTOMATICAMENTE NOS HABRA EL CODIGO
        }));
});


// PARA EJECUTAR DOS TAREAS CON GULP
gulp.task('default', gulp.series('build', 'serve'));