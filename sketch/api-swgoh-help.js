const ApiSwgohHelp = require('api-swgoh-help');

const swapi = new ApiSwgohHelp({
    "username": "YOUR_USERNAME",
    "password": "YOUR_PASSWORD",
    "client_id": "YOUR_ID",
    "client_secret": "YOUR_SECRET"
});

let allycode = 123456789;

swapi.fetchPlayer({ allycode: allycode })
    .then(player => {
        console.log(player);
    })
    .catch(error => {
        console.error('Error fetching player data:', error);
    });