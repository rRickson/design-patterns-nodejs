
const SingletonDB = require('./designs/Singleton')
const portChecker = require('./designs/ChainOfResp')
const Server = require('./designs/Prototype')

const server = new Server(8080);
server.listen();

server.express.get("/init", (req, res) => {
    /**
     * Singleton is most used for instances that can be called allways with the same state.
     * always. DB Connection is one of the most types that use singleton
     */
    try {
        portChecker.check({});
        const initType = SingletonDB.init(3000);
        const singletonIsntance = SingletonDB.getInstance().status();
        if (typeof initType === 'string') {
            res.status(200).send(`SINGLETON ALLREADY CREATED! ${singletonIsntance}`);
        } else {
            res.status(200).send(`SINGLETON CREATED!${singletonIsntance}`);
        }

    } catch (e) {
        console.log(e)
        res.status(401).send(`ERROR ON PORT CHECK`);

    }

});

