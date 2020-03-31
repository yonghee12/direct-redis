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
### String
* Originally redis stores string into bytes.
```
>>> s = "This is a String. \n스트링입니다."
>>> print(s)
This is a String.
스트링입니다.   

>>> r.set('s', s)   

>>> r.get('s')   
'This is a String. \n스트링입니다.'    

>>> type(r.get('s'))
<class 'str'>
```

### Numbers
```
>>> mapping = {
...     'a': 29,
...     'b': 0.5335113,
...     'c': np.float64(0.243623466363223),
... }   

>>> r.hmset('nums', mapping)   

>>> r.hmget('nums', *mapping.keys())   
[29, 0.5335113, 0.243623466363223]    

>>> list(mapping.values()) == r.hmget('nums', *mapping.keys())
True
```

### Nested Dictionaries and Lists
```
>>> l = [1,2,3]
>>> d = {'a': 1, 'b': 2, 'c': 3}   

>>> r.hmset('list and dictionary', {'list': l, 'dict': d})   

>>> r.hgetall("list and dictionary")
{'list': [1, 2, 3], 'dict': {'a': 1, 'b': 2, 'c': 3}}

>>> type(r.hgetall("list and dictionary")['list'])
<class 'list'>   

>>> type(r.hgetall("list and dictionary")['dict'])
<class 'dict'>
```

### Pandas DataFrame
```
>>> df =  pd.DataFrame([[1,2,3,'235', '@$$#@'], 
                       ['a', 'b', 'c', 'd', 'e']])
>>> print(df)
   0  1  2    3      4
0  1  2  3  235  @$$#@
1  a  b  c    d      e   

>>> r.set('df', df)   

>>> r.get('df')
   0  1  2    3      4
0  1  2  3  235  @$$#@
1  a  b  c    d      e   

>>> type(r.get('df'))
<class 'pandas.core.frame.DataFrame'>
```


### Numpy Array
```
>>> arr = np.random.rand(10).reshape(5, 2)
>>> print(arr)
[[0.25873887 0.00937433]
 [0.0472811  0.94004351]
 [0.92743943 0.93898677]
 [0.87706341 0.85135288]
 [0.06390652 0.86362001]]   

>>> r.set('a', arr)   

>>> r.get('a')   
array([[0.25873887, 0.00937433],
       [0.0472811 , 0.94004351],
       [0.92743943, 0.93898677],
       [0.87706341, 0.85135288],
       [0.06390652, 0.86362001]])   

>>> type(r.get('a'))
<class 'numpy.ndarray'>
```