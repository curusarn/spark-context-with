# spark-context-with
Python guard/wrapper for SparkContext from pyspark.
Allows you to use python `with` operator with SparkContext
Useful for throwing exceptions, prematurely exiting functions, etc.

## Example

```
from sparkContextWith import SparkContextWith

myAwesomeFunction(sc, whatever):
  #NOTE: use sc exactly as regular SparkContext ... eg:
  data = sc.sequenceFile("path")
  #TODO: whatever you want
  #NOTE: it is safe to throw exceptions from here
  return true

sparkconf = SparkConf().setMaster("yarn-client").setAppName("My awesome app")

with SparkContextWith(sparkconf) as sc:
  myAwesomeFunction(sc, whatever)

#NOTE: no need to sc.stop() - SparkContextWith does that for you
```
