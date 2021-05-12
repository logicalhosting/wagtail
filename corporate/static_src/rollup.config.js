import babel from 'rollup-plugin-babel';
import pkg from './package.json';
import {terser} from 'rollup-plugin-terser';
import autoprefixer from 'autoprefixer';
import postcss from 'rollup-plugin-postcss';

export default [
    // CommonJS
    {
        preserveModules: true,
        input: './src/main.js',
        output: [
            {
                dir: '../static/js',
                format: 'es'
            }
        ],
        external: [
            ...Object.keys(pkg.dependencies || {})
        ],
        plugins: [
            babel({
                exclude: 'node_modules/**'
            }),
            postcss({
                plugins: [autoprefixer()],
                sourceMap: true,
                extract: true,
                minimize: true
            }),
            terser() // minifies generated bundles
        ]
    }
];