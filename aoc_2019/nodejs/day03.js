module.exports = {
    walk: walk,
    dist: dist,
    intersection: intersection,
    part1: part1,
    //part2: part2,
};

function walk(moves) {
    var points = [];
    var start_xy = [0,0];
    var segment = 0;
    while (segment < moves.length) {
        var x = start_xy[0];
        var y = start_xy[1];
        var move = moves[segment];
        var dir = move.substring(0,1);
        var steps = Number(move.substring(1));
        switch (dir) {
            case "U":
                for (var s=1; s<=steps; s++) {
                    points.push([x, y+s]);
                }
                break;
            case "D":
                for (var s=1; s<=steps; s++) {
                    points.push([x, y-s]);
                }
                break;
            case "R":
                for (var s=1; s<=steps; s++) {
                    points.push([x+s, y]);
                }
                break;
            case "L":
                for (var s=1; s<=steps; s++) {
                    points.push([x-s, y]);
                }
                break;
        }
        start_xy = points[points.length - 1];
        segment += 1;
    }
    return points;
}

function dist(a, b) {
    return Math.abs(a[0]-b[0]) + Math.abs(a[1]-b[1]);
}

function intersection(w1_moves, w2_moves) {
    var w1_points = walk(w1_moves);
    var w2_points = walk(w2_moves);
    var intersection = [];
    for (var i=0; i<w1_points.length; i++) {
        var w1_point = w1_points[i];
        for (var j=0; j<w2_points.length; j++) {
            var w2_point = w2_points[j];
            if (w1_point[0] == w2_point[0] && w1_point[1] == w2_point[1]) {
                intersection.push(w1_point);
                break;
            }
        }
    }
    return intersection;
}

function part1(w1_moves, w2_moves) {
    var int = intersection(w1_moves, w2_moves);
    var min = Number.POSITIVE_INFINITY;
    int.forEach(function(point) {
        var d = dist([0,0], point);
        min = Math.min(d, min);
    });
    return min;
}
