import os 

imgdir = os.path.join(os.getcwd(), 'wardrobe')

os.chdir(imgdir)


imglist = os.listdir(imgdir) 

j = 1
for i in imglist:
	os.rename(i, 'wardrobe'+str(j)+'.jpg')
	j += 1
