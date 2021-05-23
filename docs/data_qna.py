qna_data = []

    # 1번 Q&A
qna_data.append(
    {'q':'말하는 걸 좋아하나요?',
     'a':[
         ('전 투머치토커에요!',{'type1': 0, 'type2': 0, 'type3': 0, 'type4' : 0, 'type5' : 0, 'type6' : 5, 'type7' : 7, 'type8' : 0}),
         ('전 말이 없어요.',{'type1' : 8, 'type2' : 0, 'type3' : 0, 'type4' : 0, 'type5' : 5, 'type6' : 0, 'type7' : 0, 'type8' : 0}),
         ]
     })

    # 2번 Q&A
qna_data.append(
    {'q': '당신을 대단하다고 생각하나요?',
     'a': [
         ('네! 매우 대단합니다!', {'type1' : 5, 'type2' : 8, 'type3' :0, 'type4' :0, 'type5' :3, 'type6' :0, 'type7' :0, 'type8' :0}),
         ('아뇨.. 저보다 뛰어난 사람이 많죠..', {'type1' :0, 'type2' :0, 'type3' :0, 'type4' :5, 'type5' :0, 'type6' :0, 'type7' :0, 'type8' :0}),
     ]
     })
    # 3번 Q&A
qna_data.append(
    {'q': '음식이 한 조각 남았을 때',
     'a': [
         ('다른 분에게 양보합니다!', {'type1' :0, 'type2' :0, 'type3' :7, 'type4' :4, 'type5' :0, 'type6' :0, 'type7' :0, 'type8' :0}),
         ('제가 먹어요.', {'type1' :0, 'type2' :5, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :3, 'type7' :0, 'type8' :0}),
     ]
     })
    # 4번 Q&A
qna_data.append(
    {'q': '말을 할때면',
     'a': [
         ('상대방을 배려해 말합니다!', {'type1' :0, 'type2' :0, 'type3' :0, 'type4' :7, 'type5' :4, 'type6' :0, 'type7' :0, 'type8' :0}),
         ('직설적으로 말합니다!', {'type1' :4, 'type2' :3, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :3, 'type7' :0, 'type8' :0}),
     ]
     })
    # 5번 Q&A
qna_data.append(
    {'q': '처음 보는 사람과',
     'a': [
         ('누구든지 친구로 만들어요!', {'type1' :0, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :0, 'type7' :0, 'type8' :5}),
         ('낯선 사람 무서워요..', {'type1' :0, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :7, 'type6' :0, 'type7' :0, 'type8' :0}),
     ]
     })
    # 6번 Q&A
qna_data.append(
    {'q': '근검절약은',
     'a': [
         ('매우 중요해요! 전 뭐든지 절약하죠.', {'type1' :0, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :7, 'type7' :0, 'type8' :0}),
         ('그냥 사고 싶거나 먹고 싶은거 flex', {'type1' :0, 'type2' :0, 'type3' :0, 'type4' :4, 'type5' :0, 'type6' :0, 'type7' :2, 'type8' :10}),
     ]
     })
    # 7번 Q&A
qna_data.append(
    {'q': '잘못된 점이 있다면',
     'a': [
         ('어떤 방법을 써서라도 바로잡아야죠!', {'type1' :0, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :0, 'type7' :6, 'type8' :0}),
         ("언젠가 치워야지 하는 생각을 합니다", {'type1' :0, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :0, 'type7' :0, 'type8' :2}),
     ]
     })

    # 8번 Q&A
qna_data.append(
    {'q': '흥이 많나요?',
     'a': [
         ('그럼요! 흥이 넘치죠!', {'type1' :0, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :0, 'type6' :0, 'type7' :4, 'type8' :7}),
         ('아니요.. 흥이 많지 않아요.', {'type1' :4, 'type2' :0, 'type3' :0, 'type4' :0, 'type5' :3, 'type6' :3, 'type7' :0, 'type8' :0}),
     ]
     })


result_data = {}

# type1 데이터 입력:
result_data['type1'] = ['조용하고 식사는 간단히 하는,','미국인, American','당신은 말이 많지 않고 조용하며, 식사를 간단히 하시는 분이시네요!','당신의 다음 생 국적', 'God Bless America (미국에 신의 축복을)','United States of America','미국','https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Flag_of_the_United_States.svg/285px-Flag_of_the_United_States.svg.png','https://ko.wikipedia.org/wiki/%EB%AF%B8%EA%B5%AD']
# type2 데이터 입력:
result_data['type2'] = ['자부심이 높은,','중국인, 中國人','당신은 자신에 대한 자부심이 높군요! 자부심을 가지는 건 좋은 거라 생각해요!','당신의 다음 생 국적','即使容颜已改，愿你始终如一 (변화는 있어도, 변함은 없기를)','China','중국','https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Flag_of_the_People%27s_Republic_of_China.svg/150px-Flag_of_the_People%27s_Republic_of_China.svg.png','https://ko.wikipedia.org/wiki/%EC%A4%91%EA%B5%AD']
# type3 데이터 입력:
result_data['type3'] = ['양보하는,','러시아인, Russian','날씨는 추울지 몰라도 마음만큼은 따뜻한 분이시군요!','당신의 다음 생 국적','верный друг лучше сотни слуг (진정한 친구가 100명의 부하보다 낫다)','Russia','러시아','https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Flag_of_Russia.svg/150px-Flag_of_Russia.svg.png','https://ko.wikipedia.org/wiki/%EB%9F%AC%EC%8B%9C%EC%95%84']
# type4 데이터 입력:
result_data['type4'] = ['친절함을 겸비한,','일본인, 日本人','당신은 상대방을 배려하며 말하는 신사와 같은 사람이군요!','당신의 다음 생 국적','負けたら終わりじゃなくて。やめたら終わりなんだよね。(당신이 진다고 끝나는게 아니고, 당신이 관둘 때 끝나는것이다.)','Japan','일본','https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Flag_of_Japan.svg/150px-Flag_of_Japan.svg.png','https://ko.wikipedia.org/wiki/%EC%9D%BC%EB%B3%B8']
# type5 데이터 입력:
result_data['type5'] = ['신사적인,','영국인, British','당신은 신사적인 이미지를 가지고 있는 사람이군요!','당신의 다음 생 국적','A gift in season is a double favor to the needy (필요할 때 주는 것은 필요한 자에게 두배의 은혜가 된다)','United Kingdom','영국','https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Flag_of_the_United_Kingdom.svg/150px-Flag_of_the_United_Kingdom.svg.png', 'https://ko.wikipedia.org/wiki/%EC%98%81%EA%B5%AD']
# type6 데이터 입력:
result_data['type6'] = ['절약정신을 가진,', '독일인, Deutsche', '당신은 절약왕이네요! 절약은 아주 좋은 습관이죠!','당신의 다음 생 국적','Der Zweck des Lebens ist das Leben selbst. (인생의 목적은 인생 그 자체이다.)','Germany','독일','https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Flag_of_Germany.svg/150px-Flag_of_Germany.svg.png','https://ko.wikipedia.org/wiki/%EB%8F%85%EC%9D%BC']
# type7 데이터 입력:
result_data['type7'] = ['먹는 것을 좋아하고 잘못된 것을 못 참는,','프랑스인, francais','먹는 걸 좋아하고 잘못된 점을 고치는, 프랑스인과 비슷하네요!','당신의 다음 생 국적',"La vie est belle (인생은 아름다워)","France",'프랑스','https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Flag_of_France.svg/150px-Flag_of_France.svg.png','https://ko.wikipedia.org/wiki/%ED%94%84%EB%9E%91%EC%8A%A4']
# type8 데이터 입력:
result_data['type8'] = ['흥이 많다 못해 흘러넘치는,','멕시코인, mexicano','당신은 흥이 흘러넘치다 못해 증발까지 할 것 같은 엄청난 흥부자이군요!','당신의 다음 생 국적','Vivir no es una bendición, pero saber cómo vivir es una bendición. (살아간다는 것은 축복이 아니라, 어떻게 살아갈지 아는 것이 축복이다.)','Mexico','멕시코','https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Flag_of_Mexico.svg/150px-Flag_of_Mexico.svg.png','https://ko.wikipedia.org/wiki/%EB%A9%95%EC%8B%9C%EC%BD%94']
