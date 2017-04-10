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
```
from pythons3 import PythonS3
PythonS3(bucket_name="my-bucket-name", key="my_key").upload('my_file.csv')
```

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
