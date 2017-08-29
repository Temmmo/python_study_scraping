import cookielib, urllib2, pprint
import login
from io import BytesIO
import lxml.html
from PIL import Image
import pytesseract
REGISTER_URL = 'http://example.webscraping.com/places/default/user/register?_next=/places/default/index'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
html = opener.open(REGISTER_URL).read()
form = login.parse_form(html)
#pprint.pprint(form)
tree = lxml.html.fromstring(html)
img_data = tree.cssselect('div#recaptcha img')[0].get('src')
img_data = img_data.partition(',')[-1]
binary_img_data = img_data.decode('base64')
file_like = BytesIO(binary_img_data)
img = Image.open(file_like)
img.save('captcha_original.png')
gray = img.convert('L')
gray.save('captcha_gray.png')
bw = gray.point(lambda x: 0 if x < 1 else 255, '1')
bw.save('captcha_thresholded.png')
pytesseract.image_to_string(img)







