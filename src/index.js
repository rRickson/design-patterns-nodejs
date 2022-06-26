
const SingletonDB = require('./designs/Singleton')
const portChecker = require('./designs/ChainOfResp')
const express = require("express");
const app = express();
const port = 8080
app.on('error', err => {
    console.log(
        "err")
})
app.get("/init", (req, res) => {

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
        res.status(401).send(`ERROR ON PORT CHECK`);

    }

});

app.listen(port, () => {
    console.log(`Listening to requests on http://localhost:${port}`);
});