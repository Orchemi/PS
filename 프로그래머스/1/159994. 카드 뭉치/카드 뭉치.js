function solution(cards1, cards2, goal) {
    let i1=0, i2=0;
    let p1=true, p2=true;
    const maxI1=cards1.length, maxI2=cards2.length;
    
    
    const l = goal.length;
    for (let i=0; i<l; i++) {
        const target = goal[i];
        console.log(target, i1, i2);
        if (p1 && cards1[i1] === target) {
            i1++;
            if (i1 === maxI1) p1=false;
            continue;
        }
        
        if (p2 && cards2[i2] === target) {
            i2++;
            if (i2 === maxI2) p2=false;
            continue;
        }
        return 'No';
    }
    return 'Yes';
}