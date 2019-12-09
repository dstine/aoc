module.exports = {
    part1,
    part2,
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

const BLACK = 0;
const WHITE = 1;
const TRANSPARENT = 2;

function part2(digits, width, height) {
    const layers = get_layers(digits, width, height);

    const rows = [];
    for (let y=0; y<height; y++) {
        const row = Array(width).fill(TRANSPARENT);
        rows.push(row);
    }
    print_image(rows);

    for (let i=0; i<layers.length; i++) {
        const layer = layers[i];
        for (let r=0; r<height; r++) {
            for (let c=0; c<width; c++) {
                const existing_pixel = rows[r][c];
                if (existing_pixel == TRANSPARENT) {
                    rows[r][c] = layer[r*width + c];
                }
            }
        }
    }
    print_image(rows, true);
}

function get_layers(digits, width, height) {
    const layer_size = width * height;
    const num_layers = digits.length / layer_size;

    return [...Array(num_layers).keys()].map(i => {
        return digits.slice(i*layer_size, (i+1)*layer_size);
    });
}

function count_digits(layer, required_digit) {
    return layer.reduce(((count, digit) => digit == required_digit ? count+1 : count), 0);
}

function print_image(rows, translate=false) {
    console.log('----------');
    for (let r=0; r<rows.length; r++) {
        let row = rows[r];
        if (translate) {
            row = row.map(val => val == 1 ? '#' : ' ');
        }
        console.log(row.join(''));
    }
}
