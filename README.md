<h1 align="center">🦾 codex_py2cpp 🤖 </h1>

<p align="center">
    OpenAI Codex Python to C++ Code Generator
</p>

Your Python Code is too slow? 🐌 
You want to speed it up but forgot how to code in C++? ⌨
Convert your Python script to C++ Code using this simple script and OpenAI Codex.

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
Reads the file "simplePythonScript.py", and feeds the corresponding input prompt to OpenAI Codex. Compilable solutions 
are stored in the form of .cpp and .exe files.
```
python3 python2cppconverter.py
```
### Example Code Generation:
Python Snippet
```python
def print_something():
    print("Hello Cpp file")


if __name__ == "__main__":
    print_something()
```
Converted by Codex to:
```cpp
// C++ Code generated from Python Code: 
#include <iostream>
#include <string>

using namespace std;

void print_something() {
    cout << "Hello Cpp file" << endl;
}

int main() {
    print_something();
    return 0;
}
```
