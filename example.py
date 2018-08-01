from ThaiTextUtility import ThaiTextUtility

thai_text_util = ThaiTextUtility()

test_phrase1 = 'ผมก็เออออกับเขาไปเรื่อย'
test_phrase2 = 'ไปเที่ยวสนุกมากกกกกกกกกกกกกกกกก'

print('###########################')
thai_text_util.lemmatize(test_phrase1)
print('###########################')
thai_text_util.lemmatize(test_phrase2)
print('###########################')