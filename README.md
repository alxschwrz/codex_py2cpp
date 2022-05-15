<h1 align="center">🦾 codex_py2cpp 🤖 </h1>

<p align="center">
    OpenAI Codex Python to C++ Code Generator
</p>

Your Python Code is too slow? 🐌 
You want to speed it up but forgot how to code in C++? ⌨
Convert your Python script to C++ Code using OpenAI Codex.

## How it works
Reads a Python file and creates an input prompt which is then fed to OpenAI Codex to generate corresponding C++ code. The generated 
code is getting compiled using g++ and if compilation is successful the executable is saved.

To generate your own files you need to get access to the Codex API (https://openai.com/blog/openai-codex/).
## Installation
```bash
git clone https://github.com/alxschwrz/codex_py2cpp.git
cd codex_py2cpp
pip3 install -r requirements.txt
```
## Run example
Reads the file "simpleScript.py", and feeds the corresponding input prompt to OpenAI Codex. Compilable solutions 
are stored in the form of .cpp and .exe files.
```
python3 python2cppconverter.py
```

If the generated C++ code got compiled, test it with
```
./simpleScript.exe
```
You hopefully get the same output as when running
```
python3 simpleScript.py
```
Check how much faster you are now ...
```
time ./simpleScript.exe
time python3 simpleScript.py
```

### Example Code Generation:
Python Snippet:
```python
def add_something(x, y):
    print("casually adding some stuff together")
    z = x + y
    return z


if __name__ == "__main__":
    print('Okay, lets go')
    print(add_something(5, 2))
```
This is how your CODEX conversion may look like:
```cpp
// C++ Code generated from Python Code: 
#include <iostream>
using namespace std;

int add_something(int x, int y) {
    cout << "casually adding some stuff together" << endl;
    int z = x + y;
    return z;
}

int main() {
    cout << "Okay, lets go" << endl;
    cout << add_something(5, 2) << endl;
    return 0;
}
```


Please test your generated code before usage.
## Credits

This project is based on the OpenAI Codex project.
Inspired by https://github.com/tom-doerr
