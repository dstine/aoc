module.exports.get_input = get_input;

var fs = require('fs');
var path = require('path');

function get_input(day) {
    var input_path = path.join(__dirname, `../../data/${day}_input.txt`);
    var input = fs.readFileSync(input_path, 'utf-8');
    var lines = input.split('\n');
    return lines;
}
