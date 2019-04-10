import urllib.parse
import base64


def convert_unicode(raw_text):
    res = urllib.parse.quote(raw_text, safe='')
    res = bytes(res, encoding="utf8")
    return res


def base64_encode(percent_text):
    res = base64.b64encode(percent_text)
    return res


def pcstore_input_text_convert(raw_text):
    res = base64_encode(convert_unicode(raw_text))
    res = str(res, encoding="utf8")
    return res

# print(pcstore_input_text_convert("爬"))
