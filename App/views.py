from django.shortcuts import render
from .models import images
import cv2
# from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
from rembg import remove
import numpy as np
# Create your views here.

def index(request):
    return render(request,'index.html')
  # print("Request",request.FILES['image'])
   # print('image123' , image[pic])
    # print('image12323' ,images,"dff" , image ,"efeeff", image.objects, pic)
    # print('image1232333434' , images[pic] )

    # images = images.objects.all()
    # rgb_image = cv2.imread( image)
    # print('image2' , "../media[request.FILES['image']]");
    # print('image2' , image[request.FILES["image"]])
    # print('image2' , image)

    # c = 'C:\Users\hp\Desktop\Read_Image\media\Images\',pic
    # rgb_image = cv2.imread(images.objects[pic])
    # print('../media/Images/',str(pic))
    # print("% media 'Images/'%",str(pic))
    # rgb_image = cv2.imread("./../media/Images/%s"%(str(pic)))
        # plt.show()
    # output = plt.show()
    

def upload(request):
  
    # print(request.FILES != {},request)
    if(request.FILES != {}):
        pic = request.FILES['image'];
        image = images(image=pic);
        # print('image1' , image,type(pic),"rffs",str(pic))
        # print('image2' ,str(pic))
        image.save();
        image = images.objects.last()
        # for i in range(1,200):
        #     print("")
        rgb_image = cv2.imread( r"C:\Users\hp\Desktop\Read_Image\media\Images\%s" % (str(pic)))
        # try :
        #     rgb_image = cv2.imread( r"C:\Users\hp\Desktop\Read_Image\media\Images\%s" % (str(pic)))
        # except:
        #     continue
        # try:
        rgb_image_size = cv2.resize(rgb_image, (500, 500),interpolation = cv2.INTER_AREA) 
        # print(rgb_image_size ,"jjhjhjhjh") 

        # rgb_image_size_plot = cv2.cvtColor(rgb_image_size, cv2.COLOR_BGR2RGB)
        # plt.hist(rgb_image_size_plot.flat, bins=255 , range=(0,255))

        # plt.savefig( r"C:\Users\hp\Desktop\Read_Image\media\Images\hist%s" % (str(pic)))


        img = cv2.imread( r"C:\Users\hp\Desktop\Read_Image\media\Images\%s" % (str(pic)))
        img1 = remove(img)
        # cv2.imshow('Original Image', img1)
        # img1.save()
        # print(img1,"fdfdsfd")
        cv2.imwrite(r"C:\Users\hp\Desktop\Read_Image\media\Images\remove%s" % (str(pic)), img1)
        # cv2.imwrite('pills_thresh.jpg', img1)



        gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) 
        cv2.imwrite(r"C:\Users\hp\Desktop\Read_Image\media\Images\gray%s" % (str(pic)), gray)

        plt.hist(gray.flat, bins=255 , range=(0,255))

        plt.savefig( r"C:\Users\hp\Desktop\Read_Image\media\Images\grayhist%s" % (str(pic)))

        equ = cv2.equalizeHist(gray)

        cv2.imwrite(r"C:\Users\hp\Desktop\Read_Image\media\Images\equ%s" % (str(pic)), equ)

        plt.hist(equ.flat, bins=255 , range=(0,255))

        plt.savefig( r"C:\Users\hp\Desktop\Read_Image\media\Images\equhist%s" % (str(pic)))
        
        # print(gray)
        # plt.plot(gray.flat,bins=200,range=(0,200))
        # print(plt,"rfgrfrrfg",gray)
        # cv2.imwrite(r"C:\Users\hp\Desktop\Read_Image\media\Images\hist%s" % (str(pic)), gray)

        # plt.savefig( r"C:\Users\hp\Desktop\Read_Image\media\Images\hist%s" % (str(pic)))


        # equ = cv2.equalizeHist(gray)
        # plt.plot(equ.flat,bins=256,range=(0,256))
        binary = cv2.threshold(gray,170, 255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
        cv2.imwrite(r"C:\Users\hp\Desktop\Read_Image\media\Images\binary%s" % (str(pic)), binary)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        MORPH_close = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
        cv2.imwrite(r"C:\Users\hp\Desktop\Read_Image\media\Images\MORPH%s" % (str(pic)), MORPH_close)

        contours, _ = cv2.findContours(MORPH_close, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE);
        image_copy = rgb_image.copy()
        spot_on_org_img = cv2.drawContours(image_copy, contours, -1, (0, 255, 0), thickness=3)
        cv2.imwrite(r"C:\Users\hp\Desktop\Read_Image\media\Images\contours%s" % (str(pic)), spot_on_org_img)

        # contours, _ = cv2.findContours(morph, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) ;
        # image_copy = image.copy()
        # spot_on_org_img = cv2.drawContours(image_copy, contours, -1, (0, 255, 0), thickness=3)
        black_img = np.zeros(rgb_image.shape)
        drawContour = cv2.drawContours(black_img, contours, -1, (0,255,0), 3)

        cv2.imwrite(r"C:\Users\hp\Desktop\Read_Image\media\Images\drawContour%s" % (str(pic)), drawContour)






        # except:
        #     print("Error")

    # output = "/media/Images/hist%s" %(str(pic)) 

        return render(request,'process.html',{'images' : image , "output" : str(pic),'remove'  :img1})
        # return render(request,'process.html',{'images' : image , "output" : str(pic),'remove'  :img1})
    else:
        return render(request,'Error.html',{"message"  :"Not Found"})

    # return render(request,'process.html',{'images' : image , "output" : output})
