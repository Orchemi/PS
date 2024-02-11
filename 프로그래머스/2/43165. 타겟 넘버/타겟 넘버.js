function solution(numbers, target) {
    const l = numbers.length;
    const dfs = (i, s) => {
        if (i === l) return s === target ? 1 : 0;
        return dfs(i+1, s+numbers[i]) + dfs(i+1, s-numbers[i]);
    }
    return dfs(0, 0);
}