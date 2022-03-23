from running_model.models import model # import model 
from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# <>안에 변수형을 정의하지 않으면 string 
@app.route('/result', methods=['GET'])
def result():

    sentence1 = request.args.get('sentence1')
    sentence2 = request.args.get('sentnece2')
    output = model(sentence1, sentence2)
    # 퍼센트로 나타내기
    output = math.trunc(output*20)

    return render_template('result.html', sentence1 = sentence1, sentence2 = sentence2, output=output)

## 해당 모듈의 __name__이 __main__ 일경우, 즉 모듈의 시작점 일경우에, app을 실행
if __name__ == '__main__' :
    app.run(debug=True)
