function solution(price, money, count) {
    const acc = count*(count+1)/2;
    console.log('money-acc*price', money)
    return Math.max(0, acc*price - money);
}