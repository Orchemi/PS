function solution(a, b, n) {
    let ret = 0;
    let empty = 0;
    let fill = n;
    
    const checkExchangable = () => empty >= a;
    
    const exchange = () => {
        const exchangeCount = Math.trunc(empty/a);
        empty -= exchangeCount * a;
        fill += exchangeCount * b;
        ret += exchangeCount * b;
    }
    
    const drink = () => {
        empty += fill;
        fill = 0;
    }
    
    
    while (true) {
        drink();
        if (!checkExchangable()) return ret;
        exchange();
    }
}