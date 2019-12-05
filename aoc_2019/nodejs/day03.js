class Point {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}

module.exports = {
    Point: Point,
    walk: walk,
    dist: dist,
    intersection: intersection,
    part1: part1,
    //part2: part2,
};

var ORIGIN = new Point(0, 0);

function walk(moves) {
    var points = [];
    var segment_start = ORIGIN;
    var segment = 0;
    while (segment < moves.length) {
        var x = segment_start.x;
        var y = segment_start.y;
        var move = moves[segment];
        var dir = move.substring(0,1);
        var steps = Number(move.substring(1));
        switch (dir) {
            case "U":
                for (var s=1; s<=steps; s++) {
                    points.push(new Point(x, y+s));
                }
                break;
            case "D":
                for (var s=1; s<=steps; s++) {
                    points.push(new Point(x, y-s));
                }
                break;
            case "R":
                for (var s=1; s<=steps; s++) {
                    points.push(new Point(x+s, y));
                }
                break;
            case "L":
                for (var s=1; s<=steps; s++) {
                    points.push(new Point(x-s, y));
                }
                break;
        }
        segment_start = points[points.length - 1];
        segment += 1;
    }
    return points;
}

function dist(a, b) {
    return Math.abs(a.x-b.x) + Math.abs(a.y-b.y);
}

function intersection(w1_moves, w2_moves) {
    var w1_points = walk(w1_moves);
    var w2_points = walk(w2_moves);
    var intersection = [];
    for (var i=0; i<w1_points.length; i++) {
        var w1_point = w1_points[i];
        for (var j=0; j<w2_points.length; j++) {
            var w2_point = w2_points[j];
            if (w1_point.x == w2_point.x && w1_point.y == w2_point.y) {
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
        var d = dist(ORIGIN, point);
        min = Math.min(d, min);
    });
    return min;
}
