from flask import Flask, jsonify, request

app = Flask(__name__)

# ----------------- first define ---------------

@app.route("/") # 127.0.0.1
def anasayfa():
    return "Hello, furkan"

@app.route("/wordlist")
def wordlist():
    wordList = [{"turkish": "top", "english": "ball"}, {"turkish": "bardak", "english": "cup"}]
    
    return jsonify({"success": True, "data": wordList})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print("POST İSTEĞİ GELDİ........")
        
        username = request.form.get("username")
        password = request.form.get("password")
        image = request.files.get("image")
        
        
        print(username, password, image)
        
        if username == "furkan" and password == "furkan123":
            return "True"
        else:
            return "False"
    else:
        print("GET İSTEĞİ GELDİ...........")
    










# ------------------ last define ---------------
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")