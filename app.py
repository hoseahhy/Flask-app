from flask import Flask
app = Flask(__name__)  #__name__ 代表目前執行的模組

@app.route("/")  #函式的裝飾 (Decorator):已函式為基礎，提供附加的功能
def home():
    return 'Home Flask  page'

@app.route("/test")  #加一個跟目錄
def test():
    return 'This is a test page'

if __name__ == "__main__":  #如果以主程式執行
    app.run()  #啟動伺服器
