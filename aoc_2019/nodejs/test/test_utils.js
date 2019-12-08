module.exports = {
    get_input,
    get_example,
};

var fs = require('fs');
var path = require('path');

function get_input(day, separator='\n', map_fn=Object) {
    var input_path = path.join(__dirname, `../../data/${day}_input.txt`);
    return get_contents(input_path, separator, map_fn);
}

function get_example(day, separator='\n', map_fn=Object, suffix='') {
    var input_path = path.join(__dirname, `../../data/${day}_example${suffix}.txt`);
    return get_contents(input_path, separator, map_fn);
}

function get_contents(input_path, separator='\n', map_fn=Object) {
    var input = fs.readFileSync(input_path, 'utf-8');
    var vals = input.split(separator).map(map_fn);
    return vals;
}
