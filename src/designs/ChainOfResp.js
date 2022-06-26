class PortSingletonCheck {
    check() {
        return true;
    }
}

// Chanin of commands for checking config
class PortCheck extends PortSingletonCheck {
    check(config) {
        if (!config.port) throw new Error("No port provide");
            return super.check();
    }
}

const portChecker = new PortCheck();

module.exports = portChecker;