# img_dir_resize.py

import os
import cv2

"""
src data Tree
man(0000-2000)
				├── 00000
					 ├── 000001.jpg
					 ├── 000002.jpg
					 ├── 000003.jpg
					 ├── 000004.jpg
					 ├── 000005.jpg
"""

def main():
    src_path = "/mnt/hdd/XP_DB/ch/man"
    dst_path = "/mnt/hdd/XP_DB_resized/ch/man"

    supported_ext = [".jpg", ".jpeg", "png"]

    resize = (512,512)

    if(os.path.exists(dst_path) == False):
        print("Dst dir not exist")
        os.mkdir(dst_path)

    sub_dir_list = os.listdir(src_path)

    for sub_dir in sub_dir_list:
        sub_dir_dst_path = dst_path + "/" + sub_dir
        if(os.path.exists(sub_dir_dst_path) == False):
            os.mkdir(sub_dir_dst_path)

    for sub_dir in sub_dir_list:
        sub_dir_src_path = src_path + "/" + sub_dir
        sub_dir_dst_path = dst_path + "/" + sub_dir

        img_list = os.listdir(sub_dir_src_path)
        for img in img_list:
            img_ext = os.path.splitext(img)
            if ((img_ext[1] in supported_ext) == False):
                continue

            img_src_path = sub_dir_src_path + "/" + img
            img_dst_path = sub_dir_dst_path + "/" + img

            src_img = cv2.imread(img_src_path)
            if(src_img is None):
                continue
            resized_img = cv2.resize(src_img, resize)
            cv2.imwrite(img_dst_path, resized_img)




if __name__=="__main__":
    main()
    print("done!")
