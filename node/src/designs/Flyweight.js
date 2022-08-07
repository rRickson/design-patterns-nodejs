class CustomError extends Error {
    constructor(code, errorMsg) {
        super(errorMsg);
        this.code = code;
        this.errorMsg = errorMsg;
    }
}
class CustomErrorFactor {

    constructor() {
        this.errorCodes = {};
    }

    static getInstance() {
        if (typeof CustomErrorFactor.instace === 'object') {
            return CustomErrorFactor.instace;
        }
        CustomErrorFactor.instace = new CustomErrorFactor();
        return CustomErrorFactor.instace;
    }

    searchError(code, msg) {
        if (typeof this.errorCodes[code] === 'object') {
            console.log('Error already trigged.')
            return this.errorCodes[code];
        }
        this.errorCodes[code] = new CustomError(code, msg);
        return this.errorCodes[code];
    }
}

module.exports = CustomErrorFactor;