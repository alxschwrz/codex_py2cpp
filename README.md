# codex_py2cpp 🤖
Your Python Code is too slow? 🐌 
You wanna speed it up but don't wanna learn C++
Convert your Python script to C++ Code using this simple script and OpenAI Codex.

## Installation
```bash
git clone xxx
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
