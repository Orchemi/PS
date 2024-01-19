function solution(name, yearning, photo) {
    const createScoreMap = () => {
        const scoreMap = {};
        name.forEach((n, i) => scoreMap[n] = yearning[i])
        return scoreMap;
    }
    
    const calcGroupScore = (group) => {
        const scoreList = group.map((name) => scoreMap[name] ?? 0)
        return scoreList.reduce((a, b) => a+b, 0);
    }
    
    const scoreMap = createScoreMap();
    return photo.map((group) => calcGroupScore(group))
}