from tempfile import NamedTemporaryFile, _TemporaryFileWrapper
import binascii


def string_to_file(utf8_decoded: str) -> _TemporaryFileWrapper:
  # Re-encode to bytes
  as_bytes = utf8_decoded.encode('utf-8')
  as_ascii = binascii.a2b_base64(as_bytes)
  with NamedTemporaryFile('wb', suffix='.odt', delete=False) as temp_source_file:
    temp_source_file.write(as_ascii)
  return temp_source_file

def file_to_string(file: _TemporaryFileWrapper) -> str:
  # Re-encode to bytes
  with open(file, 'rb') as f:
    as_bytes = f.read()
  as_base64 = binascii.b2a_base64(as_bytes)
  return as_base64.decode('utf-8')