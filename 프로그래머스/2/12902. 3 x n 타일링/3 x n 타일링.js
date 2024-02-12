function solution(n) {
    if (!n) return 0;
    if (n%2) return 0;
    let acc = 1;
    const M = 1000000007;
    const dp = new Array(n+1).fill(0);
    dp[0] = 1;
    dp[2] = 3;
    for (let i=4; i<=n; i+=2) {
        dp[i] = acc*2 + dp[i-2]*3;
        dp[i] = dp[i] % M;
        acc = (acc + dp[i-2]) % M;
    }
    console.log(dp);
    return dp[n];
}