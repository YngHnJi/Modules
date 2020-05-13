import os
import shutil

def file_move(img_dir, output_dir, img_list):
    for img in img_list:
        img_src = img_dir + "/" + img
        img_dst = output_dir + "/" + img

        shutil.copyfile(img_src, img_dst)

def dataset_divider(img_dir, output_dir, st_point, end_point):
    result = []
    if(os.path.exists(img_dir) == False):
        print("Img Dir not exists, Check")

        return 0

    if(os.path.exists(output_dir) == False):
        os.makedirs(output_dir)
        print("Output Dir created")

    item_list = os.listdir(img_dir)
    item_list = item_list[:len(item_list)-3]
    item_list.sort()
    print("Img dir load successfully")

    st_index = (st_point - 1) * 5
    end_index = (end_point * 5)
    result.extend(item_list[st_index:end_index])

    # file move to target directory
    file_move(img_dir, output_dir, result)
    print("Done!")


if __name__=="__main__":
    dataset_divider("C:\\Users\\user\\Documents\\SUBH\\dataset_split\\49_97(ljj)", "C:\\Users\\user\\Documents\\SUBH\\71_97", 22, 48)