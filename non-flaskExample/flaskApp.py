from flask import Flask, request
import oneagent

# Justin Hagerty
# Short minimalistic example of tracing flask with Dynatrace

app = Flask(__name__)

init_result = oneagent.initialize()
print('OneAgent SDK initialization result' + repr(init_result))
if init_result:
    print('SDK should work (but agent might be inactive).')
else:
    print('SDK will definitely not work (i.e. functions will be no-ops):', init_result)

sdk = oneagent.get_sdk()

wappinfo = sdk.create_web_application_info(
    virtual_host='testDevice',  # this will be your servers name in the metadata for the request "Server name = testDevice"
    application_id='Example SDK Info',  # Name of the service
    context_root='/'  # note if you put anything other than '/' this will show up in the service name as "(/yourService)"
)

@app.route("/")
def hello():
    traceRequest = sdk.trace_incoming_web_request(wappinfo, request.base_url, request.method, dict(request.headers))
    with traceRequest:
        # do things here
        # the status code if you want
        traceRequest.set_status_code(200)
        return "Hello World!"

@app.route("/anotherTest")
def anotherTest():
    traceRequest = sdk.trace_incoming_web_request(wappinfo, request.base_url, request.method, dict(request.headers))
    with traceRequest:
        # do things here
        # the status code if you want
        traceRequest.set_status_code(200)
        return "Hello World!"


if __name__ == "__main__":
    app.run()