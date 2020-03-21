# Flask Simple Dynatrace Tracing Example

Simple tracing example for python for dynatrace python SDK


### Dynatrace documentation: 
https://github.com/Dynatrace/OneAgent-SDK-for-Python

Common concepts of the Dynatrace OneAgent SDK are explained in the Dynatrace [OneAgent SDK repository.](https://github.com/Dynatrace/OneAgent-SDK#apiconcepts)



````buildoutcfg
init_result = oneagent.initialize()
print('OneAgent SDK initialization result' + repr(init_result))
if init_result:
    print('SDK should work (but agent might be inactive).')
else:
    print('SDK will definitely not work (i.e. functions will be no-ops):', init_result)
````
## Other Examples and Documenation: 
https://dynatrace.github.io/OneAgent-SDK-for-Python/docs/index.html

https://dynatrace.github.io/OneAgent-SDK-for-Python/docs/quickstart.html

Blog post about the future of python instrumention: 

https://www.dynatrace.com/news/blog/from-monitoring-to-software-intelligence-for-flask-applications/?_ga=2.53446048.922207973.1584701170-2108488564.1518964828

Flaskr Example From Dynatrace: https://github.com/Dynatrace/snippets/tree/master/technologies/python/flask

## Other Foot Notes and Examples: 
Planned support for flask and django?
https://answers.dynatrace.com/questions/229719/is-it-planned-to-support-python-framworks-like-dja.html
### Auto Instrumentation a possibility?
https://github.com/dlopes7/autodynatrace

Looks like the end result is for dynatrace to have openTelemetry support for python: https://opencensus.io/

Other technologies to look into for python SDK examples: https://cherrypy.org/

### Easter Egg: 
Might be worth looking into python lambda functions
https://stackabuse.com/lambda-functions-in-python/


Separate Example From Zach Podbielniak: https://gitlab.com/zachpodbielniak/RSC/-/blob/master/Src/RSC.py
Also added here in this repo: https://github.com/probsJustin/flaskDynatraceTracingExample/tree/master/ZachPodbielniak
