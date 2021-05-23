from stegano import lsb
print("hide data [1]    show data [2]")
ask=input("choose the options :")
if ask=="1":
  img=input("enter the image name :")
  new_img_name=input("enter the new image name : ")
  data=input("enter the data : ")
  lsb.hide(img,message=data).save(new_img_name)
if ask=="2":
  img=lsb.reveal(input("enter the image name :"))
  print("The data is : "+img)
