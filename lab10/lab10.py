from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
dic = {}  #建立一個dic儲存key和value

# web server 路由設定
# 若有get request傳送到 / ，就會執行下面的這個function
@app.route('/',methods=['GET'])
def root() :
    return 'ok' # 回傳 ok

# 設定路由為/set
# 使用 request.form 來接收資料，接著用get()這個function來取得key和value
@app.route('/set',methods=['POST'])
def root1() :
    data = request.form.get('key')
    data1 = request.form.get('value')
    if data in dic:  #假設data已存在dic中，則回傳key exist
        return 'key exist'
    else :
        dic.setdefault(data, data1)  #否則新增key、value到dic中
        return 'set success'  #回傳set success

# 設定路由為/key_list
@app.route('/',methods=['GET'])
def root2() :
    key_list = str(list(dic.keys()))  #取得dic中的key值，並且存成list，最後轉為字串
    return key_list  #回傳所有存在的 key

# 設定路由為/get_value/<key>
@app.route('/get_value/<key>',methods=['GET'])
def root3(key) :
    if key in dic :  #若key在dic中
        a = dic.get(key)  #取出key值
        return a   #回傳key值
    else :   #若key不存在
        return 'key not found'  #則回傳key not found

# 設定路由為/update_value
@app.route('/update_value',methods=['POST'])
def root4() :
    data = request.form.get('key')
    data1 = request.form.get('value')
    if data in dic :  #若key在dic中
        dic[data] = data1  #將data1 update 為data的value
        return 'update success'   #回傳update success
    else :   #若key不存在dic中
        return 'key does not exist'  #則回傳key does not exist

# 設定路由為/delete/<key>
@app.route('/delete/<key>',methods=['GET'])
def root5(key) :
    if key in dic :  #若key在dic中
        del dic[key]  #將對應的key和value刪除
        return 'delete success'   #回傳update success
    else :   #若key不存在dic中
        return 'key does not exist'  #則回傳key does not exist

# 將webserver執行，監聽任意來源ip，port開在3000，開啟debug模式
# debug模式代表，每次檔案更新後，webserver會自動重啟，不需要手動重啟
app.run(host="0.0.0.0", port=3000, debug=True)