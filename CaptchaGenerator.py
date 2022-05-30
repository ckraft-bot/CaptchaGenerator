#####Generate Captcha image
#CAPTCHA =  complete automate public turing tst to tell computers and humans apart
#pip install captcha
from cgitb import text
from captcha.image import ImageCaptcha
image = ImageCaptcha(width = 200, height = 90)
text = 'NotSomeRobot'
data = image.generate(text)
image.write(text, "path\{picture_name.picture_extension}")
