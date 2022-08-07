class Command {
    execute() {
        return new Error("Implemente metodo de execução");
    }
}
class Stream {
    constructor() {
        this._handlers = {};
    }
    on(key, command) {
        this._handlers[key] = command;
    }
    connect() {
        if (this._handlers['connect']) {
            this._handlers['connect'].execute();
        }
        if (this._handlers['disconnect']) {
            this._handlers['disconnect'].execute();
        }
    }
}

class ConnectCallback extends Command {
    execute() {
        console.log("websocket look a like.");
    }
}
class DisconnectCallback extends Command {
    execute() {
        console.log("websocket look a like.");
    }
}
const exampleStream = new Stream();
exampleStream.on('connect', new ConnectCallback());
exampleStream.on('disconnect', new DisconnectCallback());

exampleStream.connect();
module.exports = Stream();