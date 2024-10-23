## Trace parser component

This component is directly embedded in the IMA component. Please see the details in the dedicated folder. 


## Requirements

As the XES traces are expressed in XML format, we make use of [ElementTree](https://docs.python.org/3/library/xml.etree.elementtree.html) Python library. 

## Explanatory output 

Once run the function as described in the Trace parser component (configuration type 1), you should obtain something similar to this: 

 ```bash
event	BehaviorSpecification nodes ADD
event	Stimulus name SET
event	BehaviorSpecification nodes ADD
event	Display name SET
event	BehaviorSpecification nodes ADD
event	StructuredNode name SET
event	StructuredNode name SET
event	StructuredNode ports ADD
event	StructuredNode ports ADD
event	Stimulus ports ADD
```  


