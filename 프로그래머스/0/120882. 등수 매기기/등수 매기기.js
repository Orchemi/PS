function solution(score) {
    const avgs = score.map(([a, b]) => (a+b)/2);
    const sortedAvgs = [...avgs].sort((a, b) => b-a);
    return avgs.map((avg) => sortedAvgs.indexOf(avg)+1);
}