const autoprefixer = require('autoprefixer');

module.exports = {
    entry: ['./src/scss/main.scss'],
    mode: 'development',
    module: {
        rules: [
            {
                test: /\.scss$/,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            name: '../../static/css/bundle.css',
                        },
                    },
                    {loader: 'extract-loader'},
                    {loader: 'css-loader'},
                    {
                        loader: 'postcss-loader',
                        options: {
                          postcssOptions: {
                            
                            plugins: [
                                require('cssnano')({
                                    preset: 'default',
                                }),
                            ],
                          }
                        }
                    },
                    {
                        loader: 'sass-loader',
                        options: {
                            sassOptions: {
                                implementation: require('sass'),
                                includePaths: ['node_modules'],
                            },
                        },
                    }
                ],
            },
        ],
    },
};