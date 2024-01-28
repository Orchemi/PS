function solution(park, routes) {
    const dirs = {
        'E': [0, 1],
        'N': [-1, 0],
        'W': [0, -1],
        'S': [1, 0]
    }
    
    const mat = park.map((l) => l.split(''));
    const I = mat.length;
    const J = mat[0].length;
    
    const findInitialPosition = () => {
        for (i=0; i<I; i++) {
            for (j=0; j<J; j++) {
                if (mat[i][j] === 'S') {
                    return [i, j];
                }
            }
        }
    }
    
    let pos = findInitialPosition();
    
    const findTargetPosition = (d, v) => {
        const [di, dj] = dirs[d];
        return [pos[0]+di*v, pos[1]+dj*v];
    }
    
    const checkIsInBoundary = (d, v) => {
        const [ti, tj] = findTargetPosition(d, v);
        if (0 > ti || ti >= I) return false;
        if (0 > tj || tj >= J) return false;
        return true;
    }
    
    const checkIsSafeRoute = (d, v) => {
        const [di, dj] = dirs[d];
        let [ni, nj] = [...pos];
        for (i=0; i<v; i++) {
            ni += di;
            nj += dj;
            if (mat[ni][nj] === 'X') return false;
        }
        return true;
    }
    
    routes.forEach((route) => {
        const [d, _v] = route.split(' ');
        const v = Number(_v);
        if (!checkIsInBoundary(d, v)) return;
        if (!checkIsSafeRoute(d, v)) return;
        pos = findTargetPosition(d, v);
    })
    return pos;
}