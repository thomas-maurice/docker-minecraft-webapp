module.exports = function(grunt) {
    // Grunt config
    var dest = "./common/static";

    grunt.initConfig({
        copy: {
            main: {
                files: [
                {
                    expand: true,
                    cwd: 'bower_components/bootstrap/dist',
                    src: ['**/*.min.*', 'fonts/**'],
                    dest: dest
                },
                {
                    expand: true,
                    cwd: 'bower_components/font-awesome/',
                    src: ['css/*.min.css', 'fonts/*'],
                    dest: dest
                },
                {
                    expand: true,
                    cwd: 'bower_components/jquery/dist',
                    src: ['jquery.min.js', 'jquery.min.map'],
                    dest: dest + '/js/'
                },
                {
                    expand: true,
                    cwd: 'bower_components/jquery.cookie',
                    src: ['jquery.cookie.js'],
                    dest: dest + '/js/'
                },
                {
                    expand: true,
                    cwd: 'bower_components/Keypress',
                    src: ['keypress.js'],
                    dest: dest + '/js/'
                },
                { // Notify
                    expand: true,
                    cwd: 'bower_components/notifyjs/dist',
                    src: ['notify-combined.min.js'],
                    dest: dest + '/js/'
                },
                {
                    expand: true,
                    cwd: 'bower_components/hint.css',
                    src: ['hint.min.css'],
                    dest: dest + '/css/'
                },
                {
                    expand: true,
                    cwd: 'static',
                    src: ['**/*'],
                    dest: dest
                },
            ]
        }
    },
    clean: {
        build: [
            'build'
        ],
        static: [
            'bower_components'
        ],
        modules: [
            'node_modules',
        ]
    },
    coffee: {
        compile: {
            expand: true,
            flatten: false,
            cwd: 'src/',
            src: ['**/*.coffee'],
            dest: 'build/app/',
            ext: '.js'
        }
    },
})

  // Loads the grunt tasks
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-run');

  // Task definition
  grunt.registerTask('default', ['copy'])
}
