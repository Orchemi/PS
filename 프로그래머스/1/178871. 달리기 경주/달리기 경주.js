function solution(players, callings) {
    const orderName = {};
    const nameOrder = {};
    players.forEach((p, i) => {
        orderName[i] = p;
        nameOrder[p] = i;
    });
    
    callings.forEach((p) => {
        const currentOrder = nameOrder[p];
        const prevPlayer = orderName[currentOrder-1];
        orderName[currentOrder-1] = p;
        nameOrder[p] = currentOrder-1;
        orderName[currentOrder] = prevPlayer;
        nameOrder[prevPlayer] = currentOrder;
    })
    
    const ret = [];
    for (i=0; i<players.length; i++) {
        ret.push(orderName[i]);
    }
    return ret;
}