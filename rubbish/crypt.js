

fetch('https://api.coindesk.com/v1/bpi/currentprice.json')
  .then(function(response) {
    return response.json();
  })
  .then(function(myJson) {
    // console.log(JSON.stringify(myJson));
    data = myJson;

    console.log(data);

    $('.cd-datetime').html(data.time.updated)

    $('.cd-usd').html(data.bpi.USD.rate_float)

    $('.cd-eur').html(data.bpi.EUR.rate_float)
  });


  fetch('https://api.coinbase.com/v2/prices/BTC-USD/spot')
    .then(function(response) {
      return response.json();
    })
    .then(function(myJson) {
      // console.log(JSON.stringify(myJson));
      data = myJson;

      console.log(data);

      $('.cb-usd').html(data.data.amount)

    });

    fetch('https://api.coinbase.com/v2/prices/BTC-EUR/spot')
      .then(function(response) {
        return response.json();
      })
      .then(function(myJson) {
        // console.log(JSON.stringify(myJson));
        data = myJson;

        console.log(data);

        $('.cb-eur').html(data.data.amount)

      });

      fetch('https://kiwi-coin.com/api/ticker',
      {
        responseType:'application/json',
        headers: {
          'Access-Control-Allow-Credentials' : true,
          'Access-Control-Allow-Origin':'*',
          'Access-Control-Allow-Methods':'GET',
          'Access-Control-Allow-Headers':'application/json',
        },}
      )
        .then(function(response) {
          return response.json();
        })
        .then(function(myJson) {
          // console.log(JSON.stringify(myJson));
          data = myJson;

          console.log("kiwicoin", data);

          $('.cb-eur').html(data.data.amount)

        });
