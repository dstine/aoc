class Point {
    constructor(x, y, total_steps) {
        this.x = x;
        this.y = y;
        this.total_steps = total_steps;
    }
}

module.exports = {
    Point,
    walk,
    dist,
    intersection,
    part1,
    part2,
};

const ORIGIN = new Point(0, 0, 0);

function walk(moves) {
    const points = [];
    let segment_start = ORIGIN;
    let segment = 0;
    let total_steps = 0;
    while (segment < moves.length) {
        const x = segment_start.x;
        const y = segment_start.y;
        const move = moves[segment];
        const dir = move.substring(0,1);
        const steps = Number(move.substring(1));
        switch (dir) {
            case "U":
                for (let s=1; s<=steps; s++) {
                    total_steps += 1;
                    points.push(new Point(x, y+s, total_steps));
                }
                break;
            case "D":
                for (let s=1; s<=steps; s++) {
                    total_steps += 1;
                    points.push(new Point(x, y-s, total_steps));
                }
                break;
            case "R":
                for (let s=1; s<=steps; s++) {
                    total_steps += 1;
                    points.push(new Point(x+s, y, total_steps));
                }
                break;
            case "L":
                for (let s=1; s<=steps; s++) {
                    total_steps += 1;
                    points.push(new Point(x-s, y, total_steps));
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
    const w1_points = walk(w1_moves);
    const w2_points = walk(w2_moves);
    let intersection = [];
    for (let i=0; i<w1_points.length; i++) {
        const w1_point = w1_points[i];
        for (let j=0; j<w2_points.length; j++) {
            const w2_point = w2_points[j];
            if (w1_point.x == w2_point.x && w1_point.y == w2_point.y) {
                intersection.push([w1_point, w2_point]);
                break;
            }
        }
    }
    return intersection;
}

function part1(w1_moves, w2_moves) {
    const int = intersection(w1_moves, w2_moves);
    let min = Number.POSITIVE_INFINITY;
    int.forEach(function(points) {
        // either point will do since we don't need total_steps
        const point = points[0];
        const d = dist(ORIGIN, point);
        min = Math.min(d, min);
    });
    return min;
}

function part2(w1_moves, w2_moves) {
    const int = intersection(w1_moves, w2_moves);
    let min = Number.POSITIVE_INFINITY;
    int.forEach(function(points) {
        const total_steps = points[0].total_steps + points[1].total_steps;
        min = Math.min(total_steps, min);
    });
    return min;
}
