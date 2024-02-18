function solution(picks, minerals) {
    const tier = { diamond: 0, iron: 1, stone: 2 };
    const tiredMat = [[1, 1, 1], [5, 1, 1], [25, 5, 1]];
    
    const sum = (list) => list.reduce((a, c) => a+c);
    const removePick = (picks, removePickIdx) => {
        const _picks = [...picks];
        _picks[removePickIdx]--;
        return _picks;
    }
    
    const getNeedsPicks = () => {
        let restNeedsPickCount = Math.ceil(minerals.length/5);
        let currentPickCount = 0;
        if (picks[0] >= restNeedsPickCount) return [restNeedsPickCount, 0, 0];
        currentPickCount += picks[0];
        restNeedsPickCount -= picks[0];
        
        if (picks[1] >= restNeedsPickCount) return [picks[0], restNeedsPickCount, 0];
        currentPickCount += picks[1];
        restNeedsPickCount -= picks[1];
        
        if (picks[2] >= restNeedsPickCount) return [picks[0], picks[1], restNeedsPickCount];
        return picks;
    }
    
    const dig = (count, tiredness, restPicks) => {
        const currentDigMinerals = minerals.slice(count*5, Math.min(count*5+5, minerals.length));
        if (!sum(restPicks) || !currentDigMinerals.length) return tiredness;
        
        const minTirednessList = [...restPicks].map((pickCount, pi) => {
            if (!pickCount) return false;
            const currentDigTiredness = sum(currentDigMinerals.map((m) => tiredMat[pi][tier[m]]));
            const currentRestPicks = removePick(restPicks, pi);
            const currentMinTiredness = dig(count+1, tiredness+currentDigTiredness, currentRestPicks);
            return currentMinTiredness;
        }).filter(v => v);
        return Math.min(...minTirednessList);
    }
    
    return dig(0, 0, getNeedsPicks(picks));
}