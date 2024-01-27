

function solution(friends, gifts) {
    const fl = friends.length;
    const createInitialFields = () => {
        let ret = {};
        friends.forEach((f) => {
            const target = {};
            friends.filter((v) => v !== f).forEach((f2) => {
                target[f2] = 0;
            })
            ret[f] = target;
        });
        return ret;
    }
    
    const calcGiftScores = (obj) => Object.values(obj).reduce((a, b) => a+b);
    
    const gives = createInitialFields();
    const givens = createInitialFields();
    gifts.forEach((trade) => {
        const [giver, givener] = trade.split(' ');
        gives[giver][givener]++;
        givens[givener][giver]++;
    })
    
    const giftScores = {};
    friends.forEach((f) => {
        giftScores[f] = calcGiftScores(gives[f]) - calcGiftScores(givens[f]);
    })
    
    let ret = {};
    friends.forEach((f) => ret[f] = 0);
    for (i1=0; i1<fl-1; i1++) {
        for (i2=i1+1; i2<fl; i2++) {
            const fa = friends[i1];
            const fb = friends[i2];
            const fromFaToFb = gives[fa][fb];
            const fromFbToFa = gives[fb][fa];
            if (fromFaToFb === fromFbToFa) {
                const ga = giftScores[fa];
                const gb = giftScores[fb];
                if (ga === gb) continue;
                ga > gb ? ret[fa]++ : ret[fb]++;
                continue;
            }
            fromFaToFb > fromFbToFa ? ret[fa]++ : ret[fb]++;
        }
    }
    
    return Math.max(...Object.values(ret));
}