<h1 align="center">🦾 codex_py2cpp 🤖 </h1>

<p align="center">
    OpenAI Codex Python to C++ Code Generator
</p>

Your Python Code is too slow? 🐌 
You want to speed it up but forgot how to code in C++? ⌨
Convert your Python script to C++ Code using this simple script and OpenAI Codex.

## Installation
```bash
git clone https://github.com/alxschwrz/codex_py2cpp.git
cd codex_py2cpp
pip3 install -r requirements.txt
```
## Run example
```
python3 main.py
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

Inspired by https://github.com/tom-doerr
