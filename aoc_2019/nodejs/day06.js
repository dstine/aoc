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

const COM = 'COM';

function count_orbits(space_map) {
    // AAA)BBB means  "BBB is in orbit around AAA"
    const bodies = { COM: new Body(COM) };
    let i = 0;
    while (i < space_map.length) {
        const halves = (space_map[i]).split(')');
        const inner = halves[0];
        const name = halves[1];
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
    return Object.values(bodies).map(body => body.count).reduce((a, b) => a + b, 0);
}

function count(bodies, body, depth) {
    body.count = depth;
    if (body.orbitees.length == 0) {
        return;
    }
    body.orbitees.forEach(orbitee =>
        count(bodies, bodies[orbitee], depth+1)
    );
}
