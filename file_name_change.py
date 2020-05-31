# file_name_change.py
import os

def main():
    file_path = "/Users/younghoonji/Documents/Ebook/알고리즘문제해결전략/"

    file_list = []
    file_name_head = "chapter"
    index_begin = 4

    file_list = os.listdir(file_path)
    file_list.sort()

    for file_target in file_list:
        if(file_target == ".DS_Store"):
            continue
        
        file_name_before = file_path + file_target
        file_name_after = file_path + file_name_head + str(index_begin) + ".pdf"
        os.rename(file_name_before, file_name_after)
        print("Filename %s changed to %s" %(file_target, file_name_after))
        index_begin += 1


if __name__=="__main__":
    main()