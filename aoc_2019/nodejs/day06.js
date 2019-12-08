module.exports = {
    part1,
    part2,
};

class Body {
    constructor(name) {
        this.name = name;
        this.count = 0;
        this.inners = [];
        this.outers = [];
    }
}

const COM = 'COM';

function read_map(space_map) {
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
        bodies[outer_name].inners.push(bodies[inner_name]);
        i += 1;
    }
    return bodies;
}

function part1(space_map) {
    const bodies = read_map(space_map);
    count(bodies[COM], 0);
    return Object.values(bodies).map(body => body.count).reduce((a, b) => a + b, 0);
}

function count(body, depth) {
    body.count = depth;
    body.outers.forEach(outer =>
        count(outer, depth+1)
    );
}

const YOU = 'YOU';
const SAN = 'SAN';

function part2(space_map) {
    const bodies = read_map(space_map);
    traverse(bodies[YOU], 0);
    // subtract two since problem states to not count the endpoints
    return bodies[SAN].count - 2;
}

function traverse(body, depth) {
    body.count = depth;
    body.outers.forEach(outer => {
        if (outer.count == 0) traverse(outer, depth+1);
    });
    body.inners.forEach(inner => {
        if (inner.count == 0) traverse(inner, depth+1);
    });
}
