#coding=utf-8
# 不加上就無法使用中文註解
#網頁後端(html是前端)

from flask import *
app = Flask(__name__)
current_data = {}

@app.route("/")
def index():
    # 回傳首頁畫面 ( 請確保你的html檔是放在名為 templates的資料夾) 
    return render_template('lab10plus.html')

# 設定路由為/set
# 使用 request.form['變數名稱'] 來直接取用表單的輸入資料
# 使用 request.form 來接收前端輸入之資料的資料，接著用to_dict()這個function來轉成python的dict格式，可以做資料的儲存

@app.route('/set',methods = ['POST']) #為什麼一開始是/。輸入店名評分之後網址改成/set????
def root():
    print(current_data) #!!!!!!!!
    while True :
        Store = request.form['string1']
        Score = request.form['string2']
        current_data[Store] = Score #將資料加入字典 
        print(f"stroe name:{Store} , score:{Score}")
        print(f"current dara: {current_data}")
        return render_template('lab10plus.html',current_data_str=current_data)#??!!!!!!!!!!!!!!
        #current_data_str = str(current_data)  

        #return current_data_str #把字典轉成為字串之後再傳到前端
    #用return將東西顯示在網頁裡
   
    #if " http://192.168.137.227:3000/reset/y " 後端清除已存放之資料:
            #break

#http://192.168.137.98:3000/reset/y   
@app.route('/reset/<t>',methods = ['GET'])
def reset(t): #動態路由
    #a = request.args.get('t')
    global current_data
    #if y == 'y' :
    current_data={}
    print(f"current dara: {current_data}")
    #print(current_data) #在後端的terminal檢查字典有沒有清空
    return render_template('Reset.html') #??????render_template?????
    
        #return 'Reset!'#使用 return 來回傳一個回應給前端
#@app.route('/reset',methods = ['POST'])
#def y_n():
    #輸入y清空字典
    #if request.args.get('choice') == 'y' :
        #current_data = {}
    #顯示回前端的超連結
    
    
app.run(host="0.0.0.0", port=3000, debug=True)

#http://192.168.137.98:3000
