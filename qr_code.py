import qrcode
from qrcode.image.pil import PilImage
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import ImageColor  # helps convert color names/hex to RGB
import os

# class CustomImage(qrcode.image.pil.PilImage):
#     def drawrect(self,row,col):
#         x=(col*self.box_size)+self.box_size/2
#         y=(row*self.box_size)+self.box_size/2
#         r=self.box_size/2 #radius of the circle

#         draw=ImageDraw.Draw(self._img)
#         draw.ellipse((x-r,y-r,x+r,y+r),fill=self.fill_color)

# class CustomImage(qrcode.image.pil.PilImage):
#     def drawrect(self, row, col):
#         # Calculate the coordinates for the circle
#         # The rect method gives the top-left and bottom-right corners of the square module
#         x = (col * self.box_size) + self.box_size / 2
#         y = (row * self.box_size) + self.box_size / 2
#         r = self.box_size / 2  # radius of the circle /4 for diamand
        


#         # Draw the circle using the ImageDraw module
#         draw = ImageDraw.Draw(self._img)
        
#         draw.ellipse([x - r, y - r, x + r, y + r], fill=self.fill_color)      

website_link=input("Enter your desired link:: ")
version=input("Enter version:: ")
box_size=input("Enter box size:: ")
border=input("Enter border size:: ")
choice=input("Do you want circle or rectangle shaped pixels?? ")
#to make the qrcode 

qr=qrcode.QRCode(version=version,box_size=box_size,border=border)
qr.add_data(website_link)
qr.make()

#to beautify the code!
fcolor=input("Enter the fill color(can provide hexcodes also):: ")
bcolor=input("Enter the back color(can provide hexcodes also):: ")
fcolor_rgb = ImageColor.getrgb(fcolor)
bcolor_rgb = ImageColor.getrgb(bcolor)
if choice=="circle":
    img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=RoundedModuleDrawer(),
    color_mask=SolidFillColorMask(
        front_color=fcolor_rgb,   # foreground color
        back_color=bcolor_rgb     # background color
    )
)

else:
    img=qr.make_image(fill_color=fcolor,back_color=bcolor)
    
#to save the qrcode
name=input("Enter the name of the downloaded file along with its extension(.png or .jpeg or .jpg):: ")
fullpath=os.path.join('YOUR FILEPATH HERE',name) #EDIT YOUR FILE PATH HERE
img.save(fullpath)

