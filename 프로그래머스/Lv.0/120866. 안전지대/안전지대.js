function solution(board) {    
    const makeEmptyMap = () => {
        let ret = [];
        for (i=0; i<N; i++) {
            ret.push([])
            for (j=0; j<N; j++) {
                ret[i].push(0)
            }
        }
        return ret;
    }

    const checkAround = (M, i, j) => {
        for (ii=i-1; ii<=i+1; ii++) {
            if (ii<0 || ii>=N) continue;
            for (jj=j-1; jj<=j+1; jj++) {
                if (jj<0 || jj>=N) continue;
                M[ii][jj] = 1;
            }
        }
        return M;
    }

    const countAll = (M) => {
        let ret = 0;
        for (i=0; i<N; i++) {
            for (j=0; j<N; j++) {
                if (!M[i][j]) ret++;
            }
        }
        return ret;
    }
    
    
    let N = board.length;
    let retMap = makeEmptyMap()
    for (i=0; i<N; i++) {
        for (j=0; j<N; j++) {
            if (!board[i][j]) continue
            retMap = checkAround(retMap, i, j);
        }
    }
    return countAll(retMap);
}