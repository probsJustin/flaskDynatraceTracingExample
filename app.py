from flask import Flask
app = Flask(__name__)

#import the one agent sdk

import oneagent

# Justin Hagerty
# only did the hello world because I really only need to be able to trace this request. This is an example someone brought in - not sure if it works yet - will need to fix it likely

init_result = oneagent.initialize()
print('OneAgent SDK initialization result' + repr(init_result))
if init_result:
    print('SDK should work (but agent might be inactive).')
else:
    print('SDK will definitely not work (i.e. functions will be no-ops):', init_result)

@app.route('/')
def hello_world():
    return 'Hello, World!'