function solution(food) {
    let left = '';
    for (i=1; i<food.length; i++) {
        left += `${i}`.repeat(food[i]/2)
    }
    let right = '';
    for (i=left.length-1; i>=0; i--) {
        right += left[i]
    }
    return left + '0' + right;
}