const CustomError = require("./Flyweight")
class PortSingletonCheck {
    check() {
        return true;
    }
}

// Chanin of commands for checking config
class PortCheck extends PortSingletonCheck {
    check(config) {
        if (!config.port) throw new Error(
            CustomError.getInstance()
                .searchError(1, "No port provide").errorMsg);
        return super.check();
    }
}

const portChecker = new PortCheck();

module.exports = portChecker;