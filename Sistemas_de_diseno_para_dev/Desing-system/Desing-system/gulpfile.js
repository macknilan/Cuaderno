var gulp = require('gulp');
var sass = require('gulp-sass');
var minifyCSS = require('gulp-minify-css');
var concat = require('gulp-concat');
// var version = require('./package.json');

// npm install gulp --save --only=dev
gulp.task('hello', async () => {
  console.log('Hello ');
});

// npm install gulp-sass
gulp.task('sass', async () => {
  return gulp
    .src('scss/**/*.scss')
    .pipe(sass()) // Converts Sass to CSS with gulp-sass
    .pipe(gulp.dest('public/stylesheets'));
});

// npm install gulp-minify-css
// npm install gulp-concat
gulp.task('style_min', () => {
  return gulp
    .src('scss/**/*.scss')
    .pipe(sass())
    .pipe(minifyCSS())
    .pipe(concat('style_main.min.css'))
    .pipe(gulp.dest('public/stylesheets'))
});

// npm install gulp-watch
gulp.task('watch', () => {
    gulp.watch('scss/**/*.scss', gulp.series('style_min'));
});
