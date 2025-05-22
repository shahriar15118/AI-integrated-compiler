from flask import Flask, render_template, request, jsonify
import subprocess
import os
import webbrowser
import threading
import time

app = Flask(__name__,
            template_folder='templates',
            static_folder='static')

def open_browser():
    time.sleep(2)
    webbrowser.open('http://localhost:5000')

def parse_code(code):
    """Execute C++ parser"""
    try:
        # Write input to temporary file
        with open("temp.cpp", "w") as f:
            f.write(code)
        
        # Compile C++ parser
        compile_result = subprocess.run(
            ["g++", "project.cpp", "-o", "parser"],
            capture_output=True,
            text=True
        )
        
        if compile_result.returncode != 0:
            return f"Compilation Error:\n{compile_result.stderr}"
        
        # Run the parser
        run_result = subprocess.run(
            ["./parser", "temp.cpp"],
            capture_output=True,
            text=True
        )
        
        return run_result.stdout
        
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        if os.path.exists("temp.cpp"):
            os.remove("temp.cpp")
        if os.path.exists("parser.exe"):
            os.remove("parser.exe")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    code = data.get('code', '')
    
    try:
        result = parse_code(code)
        return jsonify({'output': result})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    threading.Thread(target=open_browser).start()
    app.run(debug=True, use_reloader=False)