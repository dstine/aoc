module.exports = {
    get_input,
    get_example,
};

const fs = require('fs');
const path = require('path');

function get_input(day, separator='\n', map_fn=Object) {
    const input_path = path.join(__dirname, `../../data/${day}_input.txt`);
    return get_contents(input_path, separator, map_fn);
}

function get_example(day, separator='\n', map_fn=Object, suffix='') {
    const input_path = path.join(__dirname, `../../data/${day}_example${suffix}.txt`);
    return get_contents(input_path, separator, map_fn);
}

function get_contents(input_path, separator='\n', map_fn=Object) {
    const input = fs.readFileSync(input_path, 'utf-8');
    const vals = input.split(separator).map(map_fn);
    return vals;
}
