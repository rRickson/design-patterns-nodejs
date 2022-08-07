const express = require("express");

class Server {

    constructor(port) {
        this._port = port;
        this.express = express(); 
    }

    listen() {
        this.express.listen(this._port, () => {
            console.log(`Listening to requests on http://localhost:${this._port}`);
        });
    }
}

module.exports = Server;