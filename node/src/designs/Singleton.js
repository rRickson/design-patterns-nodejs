class SingletonDB {
    constructor(port) {
      this._port = port;
    }
    static init(port) {
      if (typeof SingletonDB.instance === 'object') {
        return `Instance already created`;
      }
      SingletonDB.instance = new SingletonDB(port);
      return SingletonDB.instance;
    }
    static getInstance() {
      if (typeof SingletonDB.instance === 'object') {
        return SingletonDB.instance;
      }
      SingletonDB.instance = new SingletonDB(8080);
      return SingletonDB.instance;
    }
    status() {
      console.log("Server listening on port " + this._port);
      return(this._port)
    }
  }
  module.exports = SingletonDB
