module.exports = {
    count_orbits,
};

class Body {
    constructor(name) {
        this.name = name;
        this.count = 0;
        this.outers = [];
    }
}

const COM = 'COM';

function count_orbits(space_map) {
    // AAA)BBB means  "BBB is in orbit around AAA"
    const bodies = { COM: new Body(COM) };
    let i = 0;
    while (i < space_map.length) {
        const halves = space_map[i].split(')');
        const inner_name = halves[0];
        const outer_name = halves[1];
        if (!bodies[outer_name]) {
            bodies[outer_name] = new Body(outer_name);
        }
        if (!bodies[inner_name]) {
            bodies[inner_name] = new Body(inner_name);
        }
        bodies[inner_name].outers.push(bodies[outer_name]);
        i += 1;
    }

    count(bodies[COM], 0);
    return Object.values(bodies).map(body => body.count).reduce((a, b) => a + b, 0);
}

function count(body, depth) {
    body.count = depth;
    if (body.outers.length == 0) {
        return;
    }
    body.outers.forEach(outer =>
        count(outer, depth+1)
    );
}
