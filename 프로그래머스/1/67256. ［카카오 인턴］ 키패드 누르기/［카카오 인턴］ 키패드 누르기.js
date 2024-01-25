const findPosition = (n) => n ? [Math.trunc((n-1)/3), (n-1)%3] : [3, 1];
const calcDistance = (p1, p2) => Math.abs(p1[0]-p2[0]) + Math.abs(p1[1]-p2[1]);

function solution(numbers, hand) {
    let L = 'L', R = 'R', M = 'M';
    const choices = [M, L, M, R, L, M, R, L, M, R];
    const positions = { 'L': [3, 0], 'R': [3, 2] };
    
    const moveList = numbers.map((n) => {
        const curPos = findPosition(n);
        const move = (P) => {
            positions[P] = curPos;
            return P;
        }
        switch (choices[n]) {
            case L: return move(L);
            case R: return move(R);
            case M:
                const leftDistance = calcDistance(curPos, positions[L]);
                const rightDistance = calcDistance(curPos, positions[R]);
                if (leftDistance > rightDistance) return move(R);
                if (leftDistance < rightDistance) return move(L);
                return hand === 'right' ? move(R) : move(L);
        }
    })
    return moveList.join('');
}