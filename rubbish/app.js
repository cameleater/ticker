var bl3p = require('bl3p');
var public_key = 'YOUR_PUBLIC_KEY';
var private_key = 'YOUR_PRIVATE_KEY';

var bl3p_auth = new bl3p.Bl3pAuth(public_key, private_key);

// bl3p_auth.account_info(function(error, data){
//   if(data){
//     console.log(data, "AUTH DATA");
//   }else{
//     console.log(error, "AUTH FAIL");
//   }
// });
//
//   SHOWS STREAM OF TRADES
// bl3p.trades(function(error, data){
//   if(data){
//     console.log(data, "TRADES DATA");
//   }else{
//     console.log(error, "TRADES FAIL");
//   }
// });
//

// PINGS ORDERBOOK TO GET PRICES
var fs = require('fs');

var outputFilename = 'logs/20190627';

bl3p.orderbook(function(error, data){
  if(data){
    console.log(data, "ORDERBOOK DATA");

    fs.writeFile(outputFilename, JSON.stringify(data, null, 4), function(err) {
        if(err) {
          console.log(err);
        } else {
          console.log("JSON saved to " + outputFilename);
        }
    });
  }else{
    console.log(error);
  }
});


// bl3p.trades(function(error, data){
//   if(data){
//     console.log(data, "ACCOUNT INFO");
//   }else{
//     console.log(error, "ERROR FAIFALFIFALI");
//   }
//
// });
