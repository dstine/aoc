module.exports = {
    part1,
};

function part1(digits, width, height) {
    const layers = get_layers(digits, width, height);

    let min0s = Number.POSITIVE_INFINITY;
    let selected_layer;
    for (let i=0; i<layers.length; i++) {
        const layer = layers[i];
        const num0s = count_digits(layer, 0);
        if (num0s < min0s) {
            min0s = num0s;
            selected_layer = layer;
        }
    }

    const num1s = count_digits(selected_layer, 1);
    const num2s = count_digits(selected_layer, 2);
    return num1s * num2s;
}

function get_layers(digits, width, height) {
    const layer_size = width * height;
    const num_layers = digits.length / layer_size;
    const layers = [];
    for (let i=0; i<num_layers; i++) {
        const layer = digits.slice(i*layer_size, (i+1)*layer_size);
        layers.push(layer);
    }
    return layers;
}

function count_digits(layer, required_digit) {
    return layer.reduce(((count, digit) => digit == required_digit ? count+1 : count), 0);
}
