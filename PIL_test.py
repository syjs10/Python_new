import Image, ImageFilter
im = Image.open('./test.jpg')
im = im.filter(ImageFilter.EMBOSS)
im.save('./test1.jpg', 'jpeg')