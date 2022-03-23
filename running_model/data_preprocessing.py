import re
import string

def normalize_answer(s):
    def remove_(text):
        ''' 불필요한 기호 제거 '''
        text = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', ' ', text)
        return text

    def white_space_fix(text):  #공백을 하나로 줄이는 코드
        return ' '.join(text.split())

    def remove_punc(text): # 반점 제거
        exclude = set(string.punctuation)
        return ''.join(ch for ch in text if ch not in exclude)

    def lower(text): # 소문자로 변경
        return text.lower()

    return white_space_fix(remove_punc(lower(remove_(s))))

def preprocess(sen):
  sen =  re.sub("((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*", "",sen)
  sen = normalize_answer(sen)
  
  return sen