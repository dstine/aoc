module.exports = {
    count_orbits,
};

class Body {
    constructor(name) {
        this.name = name;
        this.count = 0;
        this.orbitees = [];
    }
}

var COM = 'COM';

function count_orbits(space_map) {
    // AAA)BBB means  "BBB is in orbit around AAA"
    var bodies = { COM: new Body(COM) };
    var i = 0;
    while (i < space_map.length) {
        var halves = (space_map[i]).split(')');
        var inner = halves[0];
        var name = halves[1];
        if (!bodies[name]) {
            bodies[name] = new Body(name);
        }
        if (!bodies[inner]) {
            bodies[inner] = new Body(inner);
        }
        bodies[inner].orbitees.push(name);
        i += 1;
    }

    count(bodies, bodies[COM], 0);
    var total = 0;
    for (let [name, body] of Object.entries(bodies)) {
        total += body.count;
    }
    return total;
}

function count(bodies, body, n) {
    body.count = n;
    if (body.orbitees.length == 0) {
        return n+1;
    } else {
        return body
            .orbitees
            .map(function(orbitee) {
                var next = bodies[orbitee];
                return 1 + count(bodies, next, n+1);
            })
            .reduce((a, b) => a + b, 0);
    }
}
