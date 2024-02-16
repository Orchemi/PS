function solution(bandage, health, attacks) {
    const attackLength = attacks.length;
    let attackIdx = 0;
    let [nextAttackTime, nextAttackDamage] = attacks[attackIdx++];
    
    const [bandageTotalCount, bandageHealPerSec, bandageSuccessBonus] = bandage;
    let bandageCount = 0;
    let currentHealth = health;
    let currentTime = 0;
    
    while (true) {
        if (currentTime === nextAttackTime) {
            currentHealth -= nextAttackDamage;
            bandageCount = 0;
            
            if (currentHealth <= 0) return -1;
            if (attackIdx >= attackLength) return currentHealth;
            [nextAttackTime, nextAttackDamage] = attacks[attackIdx++];
        } else {
            if (bandageCount+1 === bandageTotalCount) {
                currentHealth = Math.min(currentHealth+bandageHealPerSec+bandageSuccessBonus, health)
                bandageCount = 0;
            } else {
                currentHealth = Math.min(currentHealth+bandageHealPerSec, health)
                bandageCount++;
            }
        }
        currentTime++;
    }
}