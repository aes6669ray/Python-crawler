import pandas as pd
import random
from datetime import datetime, timedelta

from urllib.parse import unquote

url = "https://cos.uch.edu.tw/course_info/JS/CourseDetail.aspx?smtr=1121&cos_id=ET0175%20%20&class=%u7532"
decoded_url = unquote(url)

print(decoded_url)


