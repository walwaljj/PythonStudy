


# result = [([[18, 6], [158, 6], [158, 38], [18, 38]], '107rㄱㄱ1 6540가00', 0.9519319570751127)]
# result = [([[211, 63], [592, 63], [592, 219], [211, 219]], '1 4허', 0.3559324513717813), ([[603, 187], [633, 187], [633, 207], [603, 207]], '터', 0.6102641144427459), ([[634.1085781235672, 49.13833124025691], [891.6076436367551, 31.146572866935415], [890.8914218764328, 142.86166875974308], [634.3923563632449, 160.85342713306457]], '9834', 0.8153638291032407), ([[694.5134117075056, 170.6620705367551], [750.8231735137781, 164.17778449378636], [752.4865882924944, 182.3379294632449], [696.1768264862219, 188.82221550621364]], "무리봇디'@", 0.00023655969933683297), ([[627.438262381114, 182.75060990489115], [696.7831577361851, 171.09426908638216], [699.561737618886, 193.24939009510885], [630.2168422638149, 204.90573091361784]], "석]디'디", 0.00043736682172603543)]

# result = ['9', '8', '5', '4', '1', '4', '하', '읽', '디', '태', '디', '라', '하']
result = [([[306.2788511321733, 50.12407281199574], [451.91226133010076, 32.96435453843374], [457.7211488678267, 142.87592718800425], [312.08773866989924, 159.03564546156628]], "9854'", 0.38875285736461235), ([[95.18251969601066, 77.09743317289913], [302.18709853788476, 58.27151305392426], [306.8174803039893, 203.90256682710088], [98.81290146211524, 223.72848694607575]], '14하', 0.42204072737788406), ([[343.5857864376269, 170.5857864376269], [376.5504699710346, 164.73665409767554], [379.4142135623731, 183.4142135623731], [346.4495300289654, 189.26334590232446]], "''읽디#", 0.0004523109326374824), ([[296.00992561958003, 190.800992561958], [348.58661865218056, 173.7823624297219], [354.99007438041997, 192.199007438042], [302.41338134781944, 209.2176375702781]], '태 디라하 ', 0.0031037940610875283)]

# result = [([[18, 6], [158, 6], [158, 38], [18, 38]], '107가6540', 0.9519319570751127)]
#-------------------------------------------------------------------------------------------
print(result)
import re
first_num = 'err'
second_num = 'err'
first_sec_num = ''

for a in result:
    if re.match(r'[0-9]{2,3}[가-힣]{1}[0-9]{4}',a[1].replace(' ','')):
        fir_sec_num = a[1].replace(' ','')
    if re.match(r'[0-9]{2,3}[가-힣]', re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》;]','', a[1])):
        first_num = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》];','', a[1])
    elif re.match(r'[0-9]{4}', re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》];','', a[1])):
        second_num = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》];','', a[1].replace(" ", ""))
        
if first_num:
    result_str = first_num+second_num
else:
    result_str = fir_sec_num


result_list = []
plate = ['가', '나', '다', '라', '마', '거', '너', '더', '러', '머', '버', '서', '어', '저', '고', '노', '도', '로', '모', '보', '소', '오', '조', '구', '누', '두', '루', '무', '부', '수', '우', '주', '허', '하', '호', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# -------------------한글 & 숫자 추출-------------------

for i in result_str :
  for j in i[1] :
    for str in plate :
      if j == str :
        result_list.append(j)


first_num = ''
second_num = ''

for n in result_list :
  if '가'<=n<='힣' :
    first_num=result_list[:result_list.index(n)+1]
    second_num=result_list[result_list.index(n)+1:]
    if 3<=len(first_num)<=4 :
      first_num = ''.join(first_num)
    else :
      first_num = 'error'
    if len(second_num) == 4 :
      second_num = ''.join(second_num)
    else :
      result_list2 = [n for n in second_num if '0'<=n<='9' in second_num]
      second_num = ''.join(result_list2[-4:])

  else :
    # result_list2 = [n for n in second_num if '0'<=n<='9' in second_num]
    second_num = ''.join(result_list[-4:])

print(#'클래스 번호:', class_num,
      # '\n클래스 이름: ', class_name,
      '\n차량번호 앞자리: ', first_num,
      '\n차량번호 뒷자리: ', second_num)
# -------차량 번호판 데이터 출력
print(result_list)