function solution(data, col, row_begin, row_end) {
    const stdI = col-1;
    const sortedData = data.sort((a, b) => 
        a[stdI] === b[stdI] ? b[0] - a[0] : a[stdI] - b[stdI]
    );
    
    const sList = [];
    for (i=row_begin-1; i<row_end; i++) {
        sList.push(sortedData[i].reduce((a, b) => a + (b%(i+1)), 0));
    }
    
    let ret = sList[0];
    for (i=1; i<sList.length; i++) {
        ret = ret^sList[i];
    }
    return ret;
}