# Progress Timer
* Serialize any python datatypes and executes redis commands using redis-py
* When loading, it auutomatically converts serialized data into original data types 

# Install
`pip install direct-redis`

# Supporting Data Types
* Native
    * string
    * number(int, float)
    * dictionary
    * list
    * tuple
    * etc
* Non-native
    * pandas
    * numpy
  
# Supporting Redis Commands
* SET
* HSET
* HMSET
* GET
* HGET
* HMGET
* HGETALL
 
# Usage

## Instantiate 
```
from direct_redis import DirectRedis
r = DirectRedis(host='localhost', port=6379)
```

## Example
