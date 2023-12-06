#coding=utf-8
# 不加上就無法使用中文註解
#網頁後端(html是前端)

from flask import *
import random
app = Flask(__name__)


# 設定根目錄(通常代表首頁)之路由
# 使用render_template函式讓首頁的路由能夠回傳html檔(簡單架構)給前端，來顯示首頁畫面，而不是僅用return文字的方式
@app.route("/")
def index():
    # 回傳首頁畫面 ( 請確保你的html檔是放在名為 templates的資料夾) 
    return render_template('lab10.html')
#不行lab10template？

# 設定路由為/set

# 使用 request.form['變數名稱'] 來直接取用表單的輸入資料
# 
# 使用 request.form 來接收前端輸入之資料的資料，接著用to_dict()這個function來轉成python的dict格式，可以做資料的儲存


@app.route('/set',methods = ['POST'])
def root():
    Name = request.form['string1']
    ID = request.form['string2']
    data = request.form.to_dict()
    print(f'name : {Name}') 
    print(f'student_ID : {ID}')#use print to print result(input) at cmd
    return 'ok ! your name is : '+ Name + 'your ID is : '+ ID # 發送response為 ok + 傳送的文字內容

#開始和後端玩
@app.route('/rsp',methods = ['GET'])
def rsp():
    #先寫我出拳
    user = request.args.get('choice') #" :  http://192.168.137.98:3000/rsp?choice=r  "

    # server出拳
    choose_from = ['r','s','p']
    pi = random.choice(choose_from)
    
    print(f'computer : {pi} player : {user} ')

    if user == 'r' and pi == 's' :
        return 'You win!'
    
    elif user == 'p' and pi == 'r' :
        return 'You win!'
    
    elif user == 's' and pi == 'p' :
        return 'You win!'
    
    elif user == 's' and pi == 'r' :
        return 'You lose!'
    
    elif user == 'p' and pi == 'r' :
        return 'You lose!'
    
    elif user == 's' and pi == 'p' :
        return 'You lose!'
    
    elif user == 's' and pi == 's' :
        return 'Tie!'
    
    elif user == 'r' and pi == 'r' :
        return 'Tie!'
    
    elif user == 'p' and pi == 'p' :
        return 'Tie!'
    elif user != 'r' or user != 's' or user != 'p' :
        return " Wrong input ! try again " 
        

    
app.run(host="0.0.0.0", port=3000, debug=True)

#Running on http://127.0.0.1:3000
#Running on http://192.168.137.98:3000 copy this and paste on google 