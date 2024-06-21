module.exports = {
    publicPath: "./",
    outputDir: "dist",
    assetsDir: "static",
    // 关闭线上源码

    productionSourceMap: false,
    chainWebpack: (config) => {
        const svgRule = config.module.rule('svg');
     
        svgRule.uses.clear();
     
        svgRule
          .use('babel-loader')
          .loader('babel-loader')
          .end()
          .use('vue-svg-loader')
          .loader('vue-svg-loader');
      },
    devServer: {
        proxy: {
            '/api': {
                target: 'http://127.0.0.1:5000',
                ws: true,
                changeOrigin: true,
                pathRewirte: {
                    '^/api': ''
                }
            }
        }
    }
}