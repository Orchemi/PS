const findPosition = (n) => n ? [Math.floor((n-1)/3), (n-1)%3] : [3, 1];
const calcDistance = (positions1, positions2) => {
    const _y = positions1[0] - positions2[0];
    const _x = positions1[1] - positions2[1];
    const dy = _y > 0 ? _y : -_y;
    const dx = _x > 0 ? _x : -_x;
    return dx + dy;
}

function solution(numbers, hand) {
    let L = 'L', R = 'R', M = 'M';
    const choices = [M, L, M, R, L, M, R, L, M, R];
    
    let ret = '';
    let leftPositions = [3, 0];
    let rightPositions = [3, 2];
    
    const moveRight = (currentPositions) => {
        ret += R;
        rightPositions = currentPositions;
    }
    
    const moveLeft = (currentPositions) => {
        ret += L;
        leftPositions = currentPositions;
    }
    
    numbers.forEach((n) => {
        const currentPositions = findPosition(n);
        switch (choices[n]) {
            case L: 
                moveLeft(currentPositions);
                break;
            case R: 
                moveRight(currentPositions);
                break;
            case M:
                const leftDistance = calcDistance(currentPositions, leftPositions);
                const rightDistance = calcDistance(currentPositions, rightPositions);
                console.log(n, leftDistance, rightDistance);
                if (leftDistance > rightDistance) {
                    moveRight(currentPositions);
                } else if (leftDistance < rightDistance) {
                    moveLeft(currentPositions);
                } else {
                    hand === 'right' ? moveRight(currentPositions) : moveLeft(currentPositions);
                }
                break;
        }
    })
    return ret;
}