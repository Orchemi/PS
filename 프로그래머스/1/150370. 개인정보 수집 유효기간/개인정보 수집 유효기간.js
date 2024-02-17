

function solution(today, terms, privacies) {
    const ONE_DAY = 1;
    const ONE_MONTH = ONE_DAY*28;
    const ONE_YEAR = ONE_MONTH*12;
    const convertDateToValue = (date) => {
        const [year, month, day] = date.split('.').map(v => +v);
        return year*ONE_YEAR + month*ONE_MONTH + day*ONE_DAY;
    }
    
    const rules = {};
    terms.forEach((term) => {
        const [name, period] = term.split(' ');
        rules[name] = +period;
    })
    
    const todayDateValue = convertDateToValue(today);
    const ret = [];
    privacies.forEach((privacy, i) => {
        const [date, rule] = privacy.split(' ');
        const dateValue = convertDateToValue(date);
        const saveDateValue = dateValue + rules[rule]*ONE_MONTH - 1;
        if (saveDateValue < todayDateValue) {
            ret.push((i+1));
        }
    })
    
    return ret;
}