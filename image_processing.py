from PIL import Image, ImageFilter

img = Image.open('../PythonProject1/pics_poka/cat2.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
filtered_img = img.convert('L')
resize = filtered_img.resize((300, 300)) #resize image
resize.save('grey.png', 'png')

# crop images
# box = (100, 100, 400, 400)
# region = filtered_img.crop(box)
# region.save('grey.png', 'png')

img.thumbnail((400, 400))
img.save('thumbnail.jpg')
print(img.size)