class Prototype {

    constructor(name) {
        this.name = name;
    }

    compare(prot1, prot2) {
        if(prot1 !== prot2){return 'diferentes'}else{ return 'iguais'}
    }
    clone(newName){
        return new Prototype(newName);
    }
}

module.exports = Prototype;