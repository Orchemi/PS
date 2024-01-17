function solution(lines) {
    const createFields = () => {
        var fields = {};
        for (i=-101; i<101; i++) {
            fields[i] = 0;
        }
        return fields;
    }
    
    const checkLine = (line) => {
        const [s, e] = line;
        for (i=s; i<e; i++) {
            fields[i]++;
        }
    }
    
    
    const fields = createFields();
    lines.forEach((line) => checkLine(line))
    return Object.values(fields).filter((val) => val > 1).length;
}