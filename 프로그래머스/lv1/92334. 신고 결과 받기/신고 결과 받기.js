function solution(id_list, report, k) {
    const reportList = {};
    const reportedList = {};
    
    report.forEach((item) => {
        const [report, reported] = item.split(' ')
        // 신고자 등록
        if (!reportList[report]) {
            reportList[report] = new Set();
        }
        reportList[report].add(reported)
        
        // 신고대상 등록
        if (!reportedList[reported]) {
            reportedList[reported] = new Set();
        }
        reportedList[reported].add(report)
    })
    
    // 정지 계정 목록
    const stoped = new Set(id_list.filter(id => {
        if (reportedList[id]) {
           return reportedList[id].size >= k 
        }
    }))
    
    // 결과
    return id_list.map(id => {
        let cnt = 0;
        if (reportList[id]) {
            reportList[id].forEach((rep) => {
                cnt += stoped.has(rep)
            })
            return cnt;
        } else {
            return 0
        }
    });
}