# scatter_log_file.py

import os
import numpy as np
import matplotlib.pyplot as plt


def plot_histogram(result_array, label, filename, output_dir="./plot/"):
    for i in range(20):
        X = label[i]
        Y = result_array[i]

        # plot 입력
        scatter = plt.scatter(X, Y, s=10, c="gray", label='A')
        
    # 그래프의 타이틀과 x, y축 라벨링
    plt.title(filename, pad=10)
    plt.xlabel('Genuine     Imposter', labelpad=10)
    plt.ylabel('Similarity', labelpad=10)

    # 플롯 출력
    #plt.savefig('./scatter_frvt_report_target_similarity_yhji.png')
    plot_name = output_dir + filename + ".png"
    plt.savefig(plot_name)
    
# Function for extract sim_score from match.log
def logfile_preprocess(log_file_path, num_of_genuine):
    label = np.array([])
    similarity_score = np.array([])
    similarity_label = np.array([])

    f = open(log_file_path)
    lines = f.readlines()

    cnt = 0
    for line in lines[1:]:
        line_split = line.split()
        if(cnt<num_of_genuine):
            #print(0, line_split[2])
            label = np.append(label, 0)
            similarity_score = np.append(similarity_score, line_split[2])
        else:
            #print(1, line_split[2])
            label = np.append(label, 1)
            similarity_score = np.append(similarity_score, line_split[2])

        cnt += 1 

    label = label.reshape(-1,1)
    label = label.astype("int32")
    similarity_score = similarity_score.reshape(-1,1)
    similarity_score = similarity_score.astype("float32")

    similarity_label = np.hstack((similarity_score, label))
    #similarity_label_sorted = similarity_label[similarity_label[:,0].argsort()]

    # return sim_score, label
    return similarity_label

def logfile_preprocess_no_sort(log_file_path, num_of_genuine):
    label = np.array([])
    similarity_score = np.array([])
    similarity_label = np.array([])

    f = open(log_file_path)
    lines = f.readlines()

    cnt = 0
    for line in lines[1:]:
        line_split = line.split()
        if(cnt<num_of_genuine):
            #print(0, line_split[2])
            label = np.append(label, 0)
            similarity_score = np.append(similarity_score, line_split[2])
        else:
            #print(1, line_split[2])
            label = np.append(label, 1)
            similarity_score = np.append(similarity_score, line_split[2])

        cnt += 1 

    label = label.reshape(-1,1)
    similarity_score = similarity_score.reshape(-1,1)

    similarity_label = np.hstack((similarity_score, label))
    #similarity_label_sorted = similarity_label[similarity_label[:,0].argsort()]

    return similarity_label


def main():
    base_path = "/home/yhji/Documents/frvt_log/resize_test/"
    
    target_320x320_dir = "320x320_submission/"
    target_720x720_dir = "720x720/"
    target_no_resize_dir = "no_resize/"

    target_320x320 = base_path + target_320x320_dir + "match.log"
    target_720x720 = base_path + target_720x720_dir + "match.log"
    target_no_resize = base_path + target_no_resize_dir + "match.log"

    #similarity_label_320 = logfile_preprocess(target_320x320, 12)
    #similarity_label_720 = logfile_preprocess(target_720x720, 12)
    similarity_label_no_resize = logfile_preprocess(target_no_resize, 12)

    print("720_720")
    #plot_histogram(similarity_label_320[:,0], similarity_label_320[:,1])
    #plot_histogram(similarity_label_720[:,0], similarity_label_720[:,1])
    plot_histogram(similarity_label_no_resize[:,0], similarity_label_no_resize[:,1], "temp")


def main2():
    # base_path = "/home/yhji/Documents/nist_20_close2target/"
    # target_dir = "201106_2/"
    # target_match_log = base_path + target_dir + "match.log"
    
    #target_dir = "/home/yhji/Documents/frvt_debug_201119/nist/debugged/"
    target_dir = "/home/yhji/Documents/model_output/mxnet/210113/nist/"
    target_match_log = target_dir + "match.log"
    sim_txt = target_dir + "sim_score.txt"

    similarity_label = logfile_preprocess(target_match_log, 12)
    plot_histogram(similarity_label[:,0], similarity_label[:,1], "mxnet_210113")

    """
    with open(sim_txt, "w") as f:
        for i in similarity_label.shape[0]:
            print(similarity_label[:,i])
            line = similarity_label[:,i]
            f.write()
    """

    print("Done")



if __name__=="__main__":
    main2()