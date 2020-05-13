'use strict'
const utils = require('./utils')
const webpack = require('webpack')
const config = require('../config')
const merge = require('webpack-merge')
const path = require('path')
const baseWebpackConfig = require('./webpack.base.conf')
const CopyWebpackPlugin = require('copy-webpack-plugin')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const FriendlyErrorsPlugin = require('friendly-errors-webpack-plugin')
const portfinder = require('portfinder')
const axios = require('axios');
const url = require('url');
const HOST = process.env.HOST
const PORT = process.env.PORT && Number(process.env.PORT)
const fs =  require('fs')
const crypto = require('crypto');
var express = require('express');
var resumable = require('./resumable-node.js')('tmp');
var app = express();
var multipart = require('connect-multiparty');
var bodyParser = require('body-parser');
const uuidv1 = require('uuid/v1');
// app.use(express.static(__dirname + '/public'));

// var upload = multer(multer({
//   storage: multer.diskStorage({
//      destination: (req, file, cb) => {
//         cb(null, path.join(__dirname, '../uploads'))
//    },
//    filename: (req, file, cb) => {
//       let customFileName = crypto.randomBytes(18).toString('hex'),
//           fileExtension = file.originalname.split('.')[1] // get file extension from original file name
//           cb(null, customFileName + '.' + fileExtension)
//        }
//     })
// }))
const apiurl="http://localhost:5000/"
const FormData = require('form-data')
var multipartMiddleware = multipart();

//const apiurl="http://108.161.131.123:8089/"
const devWebpackConfig = merge(baseWebpackConfig, {
  module: {
    rules: utils.styleLoaders({ sourceMap: config.dev.cssSourceMap, usePostCSS: true })
  },
  // cheap-module-eval-source-map is faster for development
  devtool: config.dev.devtool,

  // these devServer options should be customized in /config/index.js
  devServer: {
    before: function(app, server) {
      app.use(bodyParser.json({limit: '200mb'}));
      app.use(bodyParser.urlencoded({
      limit: '200mb',
      extended: true,
      parameterLimit:50000
      }))
     // app.use(multipart());
   // Uncomment to allow CORS

 app.use(multipart({
  encoding: 'utf8',
  uploadDir: 'tmp',
  limit: '1000mb'
}));

   app.get('/get', async  function(req, res) {
    var parts = url.parse(req.url, true);
    var apipath =parts.query.url;
    // return res.json(parts)
    if(parts.query.response=='image')
    {
      return await axios.get(apiurl+apipath, {
      responseType: 'arraybuffer'
    }) .then(function (response) {
        var headers = {'Content-Type': 'image/jpeg'};
        res.writeHead(200, headers);
        res.end(response.data, 'binary');
    })
    .catch(function (error) {
        res.send("error:" + error);
    });
    }
    else if(parts.query.response=='xlsx')
    {
      return await axios.get(apiurl+apipath, {
      responseType: 'arraybuffer'
    }) .then(function (response) {
        var headers = {'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        "Content-Disposition": "attachment; filename=  Report.xlsx"}

        res.writeHead(200, headers);
        res.end(response.data, 'binary');
    })
    .catch(function (error) {
        res.send("error:" + error);
    });
    }
    else if(parts.query.response=='zip')
    {

      return await axios.get(apiurl+apipath, {
      responseType: 'arraybuffer'
    }) .then(function (response) {
        var headers = {
        "Content-Disposition": "attachment; filename=  Report.zip"}

        res.writeHead(200, headers);
        res.end(response.data, 'binary');
    })
    .catch(function (error) {
        res.send("error:" + error);
    });
    }
    else if(parts.query.response=='csv')
    {
      return await axios.get(apiurl+apipath, {
      responseType: 'arraybuffer'
    }) .then(function (response) {
        var headers = {'Content-Type': 'text/csv',
        "Content-Disposition": "attachment; filename=  Report.csv"}

        res.writeHead(200, headers);
        res.end(response.data, 'binary');
    })
    .catch(function (error) {
        res.send("error:" + error);
    });
    }
    else
    {
      console.log(apiurl+apipath)
     var  response=await axios.get(apiurl+apipath)

     res.json(response.data)
    }

       //
      });
      app.get('/getweather', async  function(req, res) {
        var parts = url.parse(req.url, true);
        var locationid =parts.query.locationid;
        var cstart_date = parts.query.start_date;
        var end_date = parts.query.end_date;

        var  response=await axios.get('https://openweathermap.org/data/2.5/find?callback=jQuery19104940901942926661_1562608925783&q=malaysia&type=like&sort=population&cnt=30&appid=b6907d289e10d714a6e88b30761fae22&_=1562608925785', {
          headers: {
              'Access-Control-Allow-Origin': '*',
              Accept: '*/*',
          }
        });
        res.json(response.data)
           //
          });

    app.post('/post', async  function(req, res) {
    var parts = url.parse(req.url, true);
    var apipath =parts.query.url;
    var postBody=req.body;
    console.log(apiurl+apipath+" postData:"+JSON.stringify(postBody))
    var response=await axios.post(apiurl+apipath,postBody)
       res.json(response.data)
      });

//allow CORS


// Handle uploads through Resumable.js
app.post('/upload', function(req, res){
  try {
    console.log('UPLOAD STARTED')
    console.log('UPLOAD REQUEST',req)
  var freq = req;
  var axios = axios;
  // req.body.uploaddownloadservice = uploaddownloadservice;
  resumable.post(req, function(status, filename, original_filename, identifier){
      console.log('POST', status, original_filename, identifier);
      console.log('Request',req)
      var uuid = uuidv1();
      freq.body.uuid = uuid;
      var response = {"Status": status }
      if(status=='done'){
        var re = /(?:\.([^.]+))?$/;
        var ext = re.exec(freq.body.resumableFilename)[1];
        response.status = "completed";
        response.uploadedfilelocation  = identifier;
        // response.uploadedfilelocation = freq.body.type + "/" + freq.body.userid + "/" + freq.body.uuid + '.'+ ext;
        response.resumableFilename = freq.body.resumableFilename;
      }


      res.send(response);
  });
}catch(e){
  console.log('UPLOAD FAILED')
  console.log('POST', status, original_filename, identifier);
  console.log('Request',req)
}
});

// Handle status checks on chunks through Resumable.js
app.get('/upload', function(req, res){
  console.log('upload GET Reached');
  resumable.get(req, function(status, filename, original_filename, identifier){
      console.log('GET', status);

      res.send((status == 'found' ? 200 : 404), status);
  });
});



    // app.get('/getfile', async  function(req, res) {
    // var parts = url.parse(req.url, true);
    // var apipath =parts.query.url;
    // var isDownload =parts.query.download || 0;
    // var filePath = parts.query.url.split("?filepath=")[0];
    // return await axios.get(uploaddownloadservice+apipath, {
    //   responseType: 'arraybuffer'
    // }) .then(function (response) {
    //     var ext = path.extname(filePath).toLowerCase();
    //     var contentType =mime.lookup(filePath) ;
    //     var filename = filePath.replace(/^.*[\\\/]/, '')
    //     if(isDownload==1){
    //       res.setHeader('Content-disposition', 'attachment; filename='+filename);
    //     }

    //     res.setHeader('Content-Type', contentType);
    //     res.end(response.data, 'binary');
    // })
    // .catch(function (error) {
    //     res.send("error:" + error);
    // });

    //   });

// Old Upload
    // app.post('/postupload', upload.single('file'),async  function(req, res) {
    //     var parts = url.parse(req.url, true);
    //     var apipath =parts.query.url;
    //     var postBody=req.body;

    //     let form = new FormData()

    //     form.append('file', fs.createReadStream(req.file.path), {
    //     filename: req.file.originalname
    //     });

    //     axios.create({
    //     headers: form.getHeaders(),
    //     maxContentLength: 100000000,
    //     maxBodyLength: 1000000000
    //     }).post(apiurl+apipath, form).then(response => {
    //     res.json(response.data)
    //     console.log(response);
    //     }).catch(error => {
    //     if (error.response) {
    //     console.log(error.response);
    //     }
    //     console.log(error.message);
    //     });
          // console.log(apiurl+apipath+" postData:"+JSON.stringify(postBody))
        // console.log(req)
        // console.log(req.file)
        // console.log(req.files)
        // console.log(req.Files)
        // console.log(req.File)
        // var response=await axios.post(apiurl+apipath,form,{
        //   headers: {
        //       'Content-Type': 'multipart/form-data',
        //       'file':req.file,
        //   }
        // })
        //    res.json(response.data)
        // });
    },

    clientLogLevel: 'warning',
    historyApiFallback: {
      rewrites: [
        { from: /.*/, to: path.posix.join(config.dev.assetsPublicPath, 'index.html') },
      ],
    },
    hot: true,
    contentBase: false, // since we use CopyWebpackPlugin.
    compress: true,
    host: HOST || config.dev.host,
    port: PORT || config.dev.port,
    open: config.dev.autoOpenBrowser,
    overlay: config.dev.errorOverlay
      ? { warnings: false, errors: true }
      : false,
    publicPath: config.dev.assetsPublicPath,
    proxy: config.dev.proxyTable,
    quiet: true, // necessary for FriendlyErrorsPlugin
    watchOptions: {
      poll: config.dev.poll,
    }
  },
  plugins: [
    new webpack.DefinePlugin({
      'process.env': require('../config/dev.env')
    }),
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NamedModulesPlugin(), // HMR shows correct file names in console on update.
    new webpack.NoEmitOnErrorsPlugin(),
    // https://github.com/ampedandwired/html-webpack-plugin
    new HtmlWebpackPlugin({
      filename: 'index.html',
      template: 'index.html',
      inject: true
    }),
    // copy custom static assets
    new CopyWebpackPlugin([
      {
        from: path.resolve(__dirname, '../static'),
        to: config.dev.assetsSubDirectory,
        ignore: ['.*']
      }
    ])
  ]
})

module.exports = new Promise((resolve, reject) => {
  portfinder.basePort = process.env.PORT || config.dev.port
  portfinder.getPort((err, port) => {
    if (err) {
      reject(err)
    } else {
      // publish the new Port, necessary for e2e tests
      process.env.PORT = port
      // add port to devServer config
      devWebpackConfig.devServer.port = port

      // Add FriendlyErrorsPlugin
      devWebpackConfig.plugins.push(new FriendlyErrorsPlugin({
        compilationSuccessInfo: {
          messages: [`Your application is running here: http://${devWebpackConfig.devServer.host}:${port}`],
        },
        onErrors: config.dev.notifyOnErrors
        ? utils.createNotifierCallback()
        : undefined
      }))

      resolve(devWebpackConfig)
    }
  })
})
