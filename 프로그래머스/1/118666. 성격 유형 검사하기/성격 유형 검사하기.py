from collections import defaultdict

def compare(dic, left, right):
    left_score = dic[left]
    right_score = dic[right]
    return left if left_score >= right_score else right

def solution(survey, choices):
    survey_dic = defaultdict(int)
    
    # 점수 계산
    for idx, choice in enumerate(choices):
        if choice < 4:  # 비동의 관련 선택지
            survey_dic[survey[idx][0]] += 4 - choice
        elif choice > 4:  # 동의 관련 선택지
            survey_dic[survey[idx][1]] += choice - 4
            
    # 성격 유형 결정
    result = ''
    compare_list = [['R','T'], ['C','F'], ['J','M'], ['A','N']]
    for left, right in compare_list:
        result += compare(survey_dic, left, right)
        
    return result