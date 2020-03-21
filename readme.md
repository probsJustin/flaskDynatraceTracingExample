# Flask Simple Dynatrace Tracing Example

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
