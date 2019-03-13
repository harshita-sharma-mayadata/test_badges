from PIL import Image, ImageDraw, ImageFont
from coverage import coverage

cov = coverage()
cov.load()
total = cov.report()

# total = 79.0

im = Image.new("RGB", (120, 20))
fnt = ImageFont.load_default()
d = ImageDraw.Draw(im)

d.text((10, 5), "coverage:", fill=(255, 255, 255), font=fnt)
d.rectangle([(80, 0), (150, 20)], fill=(220, 0, 0))
d.text((90, 5), "{:.0f}%".format(total), fill=(0, 0, 0), font=fnt)
