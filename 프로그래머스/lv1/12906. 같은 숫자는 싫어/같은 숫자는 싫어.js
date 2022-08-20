function solution(arr)
{
    let prev = -1;
    const ans = [];
    arr.forEach(a => {
        if (a !== prev) {
            ans.push(a)
            prev = a
        }
    })
    
    return ans;
}