# 전처리 모듈 import 
from running_model.data_preprocessing import preprocess
import torch
from transformers import ElectraForSequenceClassification, ElectraTokenizer

def model(sentence1, sentence2):
    '''
    두개의 문장을 입력받고, 유사도를 구하는 함수
    input : sentence1, sentence2
    output : 유사도(0~5사이의 float)
    '''
    tokenizer = ElectraTokenizer.from_pretrained("monologg/koelectra-base-v3-discriminator")
    model = ElectraForSequenceClassification.from_pretrained("running_model/best_model", num_labels = 1)
    max_length = 128

    sentence1 = preprocess(sentence1)
    sentence2 = preprocess(sentence2)

    input = tokenizer.encode(text = sentence1,
                    text_pair = sentence2,
                    padding="max_length",
                    truncation=True,
                    add_special_tokens=True,
                    max_length=max_length,
                    return_tensors='pt'
                    )
    with torch.no_grad():
            output = model(input)
    return output[0].item()
