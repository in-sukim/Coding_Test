from collections import defaultdict
def solution(id_list, report, k):
    # 누가, 누굴 신고했는지 pair로 관리하여 중복 처리.
    # k번 이상 신고 당하면 정지.
    # 해당 유저 신고한 사람에게 메일 발송
    report_dic = defaultdict(set)
    for i in report:
        user, report = i.split(' ')
        report_dic[report].add(user)
    
    mail_dic = {i:0 for i in id_list}
    
    for report_user, users in report_dic.items():
        if len(users) >= k:
            for user in users:
                mail_dic[user] += 1
    return list(mail_dic.values())
        
            
    