
////////////////////////////////
		//Setup//
////////////////////////////////

// Plugins
var gulp = require('gulp'),
      pjson = require('./package.json'),
      gutil = require('gulp-util'),
      sass = require('gulp-sass'),
      autoprefixer = require('gulp-autoprefixer'),
      cssnano = require('gulp-cssnano'),
      rename = require('gulp-rename'),
      del = require('del'),
      plumber = require('gulp-plumber'),
      pixrem = require('gulp-pixrem'),
      uglify = require('gulp-uglify'),
      imagemin = require('gulp-imagemin'),
      exec = require('child_process').exec,
      runSequence = require('run-sequence'),
      browserSync = require('browser-sync').create(),
      babelify = require('babelify'),
      browserify = require('browserify'),
      watchify = require('watchify'),
      source = require('vinyl-source-stream'),
      cache = require('gulp-cache'),
      assign = require('lodash.assign'),
      reload = browserSync.reload;


// Relative paths function
var pathsConfig = function (appName) {
  this.app = "./" + (appName || pjson.name);

  return {
    app: this.app,
    templates: this.app + '/templates',
    css: this.app + '/static/css',
    sass: this.app + '/static/sass',
    fonts: this.app + '/static/fonts',
    images: this.app + '/static/images',
    js: this.app + '/static/js',
    react: this.app + '/static/react',
  }
};

var paths = pathsConfig();

/////////////// GULP //////////////
gulp.task('default', function() {
    runSequence(['imgCompression', 'watch'], 'runserver');
});

//////////////////////////////////
////// React and JS //////////////
//////////////////////////////////
var customOpts = {
  entries: [paths.react + '/js/index.js'],
  debug: true
};
var opts = assign({}, watchify.args, customOpts);
var b = watchify(browserify(opts));

function bundle (bundler) {
    return bundler
        .on('error', gutil.log.bind(gutil, 'Browserify Error'))
        .transform("babelify", {
            presets: ["es2015", "react"],
        })
        .bundle()
        .on('error', function (e) {
            gutil.log(e);
        })
	.pipe(plumber())
        .pipe(source('index.js'))
        .pipe(rename('bundle.js'))
        .pipe(gulp.dest(paths.react))
        .pipe(browserSync.stream());
}

gulp.task('watch_react', function() {
    var watcher = b;
    bundle(b);
    watcher.on('update', function () {
        bundle(watcher);
    });
    watcher.on('log', gutil.log);

});

// Javascript minification
gulp.task('scripts', function() {
  return gulp.src(paths.js + '/project.js')
    .pipe(plumber()) // Checks for errors
    .pipe(uglify()) // Minifies the js
    .pipe(rename({ suffix: '.min' }))
    .pipe(gulp.dest(paths.js));
});
//////////////////////////////////////////////////////////////

////////////////////////////////
	///// RunServer //////
////////////////////////////////

// Run django server
gulp.task('runserver', ['scripts'], function() {
  exec('python manage.py runserver', function (err, stdout, stderr) {
    console.log(stdout);
    console.log(stderr);
  });

  browserSync.init(
      [paths.css + "/*.css", paths.js + "*.js", paths.templates + '*.html', paths.react + "js/*.js"], {
        proxy:  "localhost:8000",
        logFileChanges: false
    });
});


////////////////////////////////
///// CSS and Images ////////
////////////////////////////////

// Styles autoprefixing and minification
gulp.task('styles', function() {
  return gulp.src(paths.sass + '/project.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(plumber()) // Checks for errors
    .pipe(autoprefixer({browsers: ['last 2 version']})) // Adds vendor prefixes
    .pipe(pixrem())  // add fallbacks for rem units
    .pipe(gulp.dest(paths.css))
    .pipe(rename({ suffix: '.min' }))
    .pipe(cssnano()) // Minifies the result
    .pipe(gulp.dest(paths.css));
});

// Image compression
gulp.task('imgCompression', function(){
  return gulp.src(paths.images + '/*')
    .pipe(cache(imagemin({
	    interlaced: true
	})))
    .pipe(gulp.dest(paths.images))
});


////////////////////////////////
		//Watch//
////////////////////////////////

exec('jest --watch', function (err, stdout, stderr) {
    console.log(stdout);
    console.log(stderr);
    });

// Watch
gulp.task('watch', ['watch_react'], function() {

  gulp.watch(paths.sass + '/*.scss', ['styles']).on("change", reload);
  gulp.watch(paths.js + '/*.js', ['scripts']).on("change", reload);
  gulp.watch(paths.images + '/*', ['imgCompression']);
  gulp.watch(paths.templates + '/**/*.html').on("change", reload);

});
