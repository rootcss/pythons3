#!/usr/bin/env python

import sys
import boto
import boto.s3
from socket import gethostname
from boto.s3.key import Key
import re
import os

def percent_cb(complete, total):
  sys.stdout.write('.')
  sys.stdout.flush()

class PythonS3(object):
  bucket_name = re.sub('[^A-Za-z0-9]+', '-', gethostname())
  key = 'pythons3'
  conn = None
  bucket = None

  def __init__(self, bucket_name=None, key=None):
    if bucket_name is not None:
      self.bucket_name = bucket_name
    self.__connect()

  def upload(self, file):
    self.set_bucket()
    print 'Uploading %s in bucket %s' % (file, self.bucket_name)
    k = Key(self.bucket)
    k.key = file
    k.set_contents_from_filename(file, cb=percent_cb, num_cb=10)

  def set_bucket(self):
    bucket = self.conn.lookup(self.bucket_name)
    if bucket is None:
      bucket = self.conn.create_bucket(self.bucket_name, location=boto.s3.connection.Location.DEFAULT)
    self.bucket = bucket

  def __connect(self):
    self.conn = boto.connect_s3(*self.__aws_access_keys())

  def __aws_access_keys(self):
    try:
      aws_access_key_id = AWS_ACCESS_KEY_ID
      aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    except:
      aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
      aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
    finally:
      if aws_secret_access_key is None or aws_secret_access_key is None \
        or aws_secret_access_key is '' or aws_secret_access_key is '':
        raise Exception("AWS Access keys are not provided.")
      return aws_access_key_id, aws_secret_access_key