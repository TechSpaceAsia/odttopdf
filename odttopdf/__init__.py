from typing import Type
from celery import shared_task
import subprocess
import binascii
from tempfile import _TemporaryFileWrapper

from odttopdf.conversion import string_to_file

@shared_task
def convert_odt_to_pdf(utf8_decoded: str):
  temp_source_file = string_to_file(utf8_decoded)
  
  temp_source_file.delete()
  
  
