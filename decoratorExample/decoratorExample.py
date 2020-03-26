from flask import Flask, request
import requests

import oneagent

# Justin Hagerty and Zach Podbielniak
# Example for comparison with using the decorator for minimalistic "invasive code for the python sdk"

from oneagent.common import DYNATRACE_HTTP_HEADER_NAME

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

# Decorator Definition
def oneagent_incomingTrace(func):
    def incomingTracer(*args, **kwargs):
        tracerObject = sdk.trace_incoming_web_request(
            wappinfo,
            request.base_url,
            request.method,
            remote_address=request.remote_addr,
            headers=dict(request.headers)
            )

        if tracerObject:
            with tracerObject:
                kwargs['incoming_wreq'] = tracerObject
                tracerArgs = func(*args, **kwargs)
                tracerObject.set_status_code(200)
        else:
                tracerArgs = func(*args, **kwargs)
        return tracerArgs
    return incomingTracer

def oneagent_outgoingTracer(func, url, headers):
    def outgoingTracer(*args, **kwargs):
        tracerObject = sdk.trace_outgoing_web_request(url, "GET")
        if tracerObject:
            with tracerObject:
                tag = outGoingTracer.outgoing_dynatrace_string_tag
                headers[DYNATRACE_HTTP_HEADER_NAME] = tag

                kwargs['outgoing_wreq'] = tracerObject
                kwargs['outgoingTracerHeaders'] = headers
                kwargs['url'] = url
                tracerArgs = func(*args, **kwargs)
                tracerObject.set_status_code(200)
        else:
            tracerArgs = func(*args, **kwargs)
        return tracerArgs
    return outgoingTracer



@app.route("/")
@oneagent_incomingTrace
def hello(incoming_wreq):
    # do some things here
    incoming_wreq.set_status_code(200)
    return "Hello World!"


@app.route("/anotherTest")
@oneagent_incomingTrace
def anotherTest(incoming_wreq):
    # do some things here
    incoming_wreq.set_status_code(200)
    return "Hello World!"


@app.route("/outgoingflask")
@oneagent_incomingTrace
def outgoingflask(incoming_wreq):
    # Information already defined for outgoing requests
    headers = {"Test": "things"}
    url = "http://127.0.0.1"

    @oneagent_outgoingTracer(url, headers)
    def outgoingRequest(outgoing_wreq, outgoingTracerHeaders, url):
        response = requests.get(url, headers=outgoingTracerHeaders)
        print(response)
    return "Hello World!"


# Tracer Decorator, allows easy instrumentation of each web request
@app.route('/exampleDecoratorPath')
@oneagent_incomingTrace  # Web Tracer Decorator
def health(incoming_wreq):
    incoming_wreq.set_status_code(200)
    return "Hello world!"

if __name__ == "__main__":
    app.run()