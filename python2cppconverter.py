import os
import configparser
import sys
import contextlib

import openai
import random


MAX_SUPPORTED_INPUT_LENGTH = 4096
USE_STREAM_FEATURE = True
SET_TEMPERATURE_NOISE = False
MAX_TOKENS_DEFAULT = 128

STREAM = True
API_KEYS_LOCATION = "./config"
PYTHON_FILE_TO_CONVERT = "simplePythonScript.py"


def create_template_ini_file():
    """
  If the ini file does not exist create it and add the organization_id and
  secret_key
  """
    if not os.path.isfile(API_KEYS_LOCATION):
        with open(API_KEYS_LOCATION, 'w') as f:
            f.write('[openai]\n')
            f.write('organization_id=\n')
            f.write('secret_key=\n')

        print('OpenAI API config file created at {}'.format(API_KEYS_LOCATION))
        print('Please edit it and add your organization ID and secret key')
        print('If you do not yet have an organization ID and secret key, you\n'
              'need to register for OpenAI Codex: \n'
              'https://openai.com/blog/openai-codex/')
        sys.exit(1)


def initialize_openai_api():
    """
  Initialize the OpenAI API
  """
    # Check if file at API_KEYS_LOCATION exists
    create_template_ini_file()
    config = configparser.ConfigParser()
    config.read(API_KEYS_LOCATION)

    openai.organization_id = config['openai']['organization_id'].strip('"').strip("'")
    openai.api_key = config['openai']['secret_key'].strip('"').strip("'")


def create_input_prompt(length=3000):
    inputPrompt = ''
    filename = PYTHON_FILE_TO_CONVERT
    with open(filename) as f:
        inputPrompt += '\n===================\n# ' + filename + ':\n'
        inputPrompt += f.read() + '\n'

    inputPrompt = inputPrompt[:length]
    inputPrompt += '\n\n===================\n# ' + 'C++ Code:' + '\n'
    return inputPrompt


def generate_completion(input_prompt, num_tokens):
    temperature = 0.1
    if SET_TEMPERATURE_NOISE:
        temperature += 0.1 * round(random.uniform(-1, 1), 1)
    print("CODEX: Let me come up with something new ...")
    response = openai.Completion.create(engine='code-davinci-001', prompt=input_prompt, temperature=temperature,
                                        max_tokens=num_tokens, stream=STREAM, stop='===================\n')
    return response


def get_generated_response(response):
    generatedFile = "// C++ Code generated from Python Code: \n"
    while True:
        nextResponse = next(response)
        completion = nextResponse['choices'][0]['text']
        generatedFile = generatedFile + completion
        if nextResponse['choices'][0]['finish_reason'] is not None:
            break
    return generatedFile


def write_cpp_file(textResponse):
    fileName = PYTHON_FILE_TO_CONVERT.split(".")[0] + ".cpp"
    if os.path.exists(fileName):
        os.remove(fileName)
    f = open(fileName, "a")
    f.write(textResponse)
    f.close()


def test_cpp_compilation(cppFile):
    """
  Checks if the generated file is compilable using g++
  """
    exeFile = cppFile.split(".")[0] + ".exe"
    if os.system("g++ " + cppFile + " -o " + exeFile + " &> /dev/null") == 0:
        return True
    else:
        return False


def iterate_for_compilable_solution(prompt, maxIterations):
    print('Iterating for a compilable C++ solution ...')
    print()
    for it in range(maxIterations):
        response = generate_completion(prompt, num_tokens=MAX_TOKENS_DEFAULT)
        textResponse = get_generated_response(response)
        write_cpp_file(textResponse)
        fileName = PYTHON_FILE_TO_CONVERT.split(".")[0]
        with contextlib.redirect_stdout(None):
            isSolutionCompilable = test_cpp_compilation(fileName + ".cpp")
        if isSolutionCompilable:
            print("Found a compilable solution after {} iterations".format(it+1))
            print("C++ File: {}".format(fileName + ".cpp"))
            print("Compiled Executable: {}".format(fileName + ".exe"))
            break
        if it == maxIterations - 1:
            print('Unfortunately CODEX did not find a compilable solution. Still you can find the generated code '
                  'in the file: {}'.format(fileName + ".cpp"))


if __name__ == "__main__":
    initialize_openai_api()
    prompt = create_input_prompt()
    #print(prompt)
    iterate_for_compilable_solution(prompt=prompt, maxIterations=5)


