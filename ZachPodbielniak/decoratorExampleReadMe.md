# Decorator Example: 

Using the decorator from python in conjunction with the SDK can cut down on development time and the need for invasive code. 

This is a comparison of "decoratorExample.py" and "baseFlaskDecoratorExample.py"


## Base Flask Incoming Request: 

```
@app.route("/")
def hello():
    return "Hello World!" 
```
## Same Flask Incoming Request With OneAgent SDK Decorator: 
```
@app.route("/")
@oneagent_incomingTrace
def hello(incoming_wreq):
    # do some things here
    incoming_wreq.set_status_code(200)
    return "Hello World!"
```