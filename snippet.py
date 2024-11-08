import json
import threading
import keyboard
import os
import subprocess

f = open("snippets.json", "r")
snippets = json.loads(f.read())

f = open("temp.py", "r")
template = f.read()

binding = {}

def runCode(code):
    print("Here!\n")
    f = open("temp.file.py", "w")
    f.write(code)
    f.close()
    subprocess.run(["python", "temp.file.py"])
    # process.wait()
    os.remove("temp.file.py")

def runSnippet(*args):
    # print(args)
    # code = "".join(args)
    code = args[0]
    code = template + "\n" + f"hotkeyId = {args[1]}" + "\n" + code
    runCode(code)

def initSnippetByName(name):
    snippetFileName = snippets[name]["name"]
    snippetHotKey = snippets[name]["hotkey"]
    f = open(snippetFileName, "r")
    snippetFile = f.read()
    for key, value in snippetHotKey.items():
        binding[key] = [snippetFile, value]

if __name__ == "__main__":
    for key in snippets:
        initSnippetByName(key)
    
    for key, value in binding.items():
        # print(type(value))
        keyboard.add_hotkey(key, callback=runSnippet, args=(value))
    
    keyboard.wait("esc")
