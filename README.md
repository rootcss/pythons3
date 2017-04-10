# pythons3

Fastest & Easiest way to upload data on AWS S3.

### Usage:
Define AWS_ACCESS_KEY_ID & AWS_SECRET_ACCESS_KEY within the code or environmental variables and execute the following code:
```
from pythons3 import PythonS3
PythonS3().upload('my_file.csv')
```
or, because humans do typos!
```
from pythons3 import Pythons3
Pythons3().upload('my_file.csv')
```
or, because some people have multiple use cases:
```python
from pythons3 import PythonS3
PythonS3(bucket_name="my-bucket-name").upload('my_file.csv')
# OR
PythonS3(bucket_name="my-bucket-name", key="myfilename.csv").upload('my_file.csv')
# OR
PythonS3(bucket_name="my-bucket-name", path="directory/myfilename.csv").upload('my_file.csv') # This line will copy the file "my_file.csv" to "my-bucket-name/directory/myfilename.csv" in S3
```
Note: `key` and `path` parameters are aliases.

### Installation:
`git clone https://github.com/rootcss/pythons3`
<br>
`python setup.py install`

### Uninstallation:
`pip uninstall pythons3`

### TODO:
<ul>
<li>Multithreading support for multiple files.</li>
<li>Determine file size before uploading.</li>
</ul>
