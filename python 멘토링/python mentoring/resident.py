while True:
    residentNum = input('주민등록번호를 입력하세요. ex)010101-3030300: ')

    if len(residentNum) == 14 and residentNum[6] == '-': #문자열이 '-'포함 14자리이고 7번째 문자가 '-'이 있는지
        data = residentNum.split('-')
        s = data[1] #성별

        if s[0] == '1' or s[0] =='3':
            print('생년월일: ', data[0], ', 성별: 남자')
            continue
        else:
            print('생년월일: ', data[0], ', 성별: 여자')
            continue
    elif residentNum == 'done':
        print('프로그램을 종료합니다.')
        break
    else:
        print('잘못된 형식입니다.')
        continue