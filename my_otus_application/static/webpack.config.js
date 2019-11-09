const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    entry: './js/scripts.js',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.min.js',
    },
    resolve: {
        modules: [
            "node_modules",
            "./app"
        ],
        extensions: [".js", ".json", ".jsx", ".css"],
    },
    plugins: [
        new HtmlWebpackPlugin()
    ]
};