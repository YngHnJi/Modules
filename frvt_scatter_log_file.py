# frvt_scatter_log_file.py

import os
import numpy as np
import matplotlib.pyplot as plt


def plot_histogram(result_array, label, filename, output_dir="./plot/"):
    for i in range(result_array.shape[0]):
        X = label[i]
        Y = result_array[i]

        # plot 입력
        scatter = plt.scatter(X, Y, s=5, c="gray", label='A')
        
    # 그래프의 타이틀과 x, y축 라벨링
    plt.title(filename, pad=10)
    plt.xlabel('Genuine     Imposter', labelpad=10)
    plt.ylabel('Similarity', labelpad=10)

    # 플롯 출력
    #plt.savefig('./scatter_frvt_report_target_similarity_yhji.png')
    plot_name = output_dir + filename + ".png"
    plt.savefig(plot_name)

def logfile_preprocess(log_file_path, label_file_path):
    labels = np.array([])
    similarity_score = np.array([])
    similarity_label = np.array([])

    f = open(log_file_path)
    lines = f.readlines()

    label_file = open(label_file_path, "r")
    label_lines = label_file.readlines()

    for i in range(1, len(lines[1:])):
        line_split = lines[i].split()
        label = label_lines[i-1]

        similarity_score = np.append(similarity_score, line_split[2])
        labels = np.append(labels, int(label[0]))

    labels = labels.reshape(-1,1)
    labels = labels.astype("int32")
    similarity_score = similarity_score.reshape(-1,1)
    similarity_score = similarity_score.astype("float32")

    similarity_label = np.hstack((similarity_score, labels))
    #similarity_label_sorted = similarity_label[similarity_label[:,0].argsort()]

    # return sim_score, label
    return similarity_label

def main():    
    #target_dir = "/home/yhji/Documents/frvt_debug_201119/frvt/" + "debugged/"
    #target_match_log = target_dir + "match.log"
    
    target_dir = "/home/yhji/Documents/model_output/mxnet/210113/nist/"
    target_match_log = target_dir + "match.log"

    #sim_txt = target_dir + "sim_score.txt"

    frvt_label_file_path = "/home/yhji/Documents/frvt_testset_label.txt"

    similarity_label = logfile_preprocess(target_match_log, frvt_label_file_path)
    plot_histogram(similarity_label[:,0], similarity_label[:,1], "mxnet_result")

    """
    with open(sim_txt, "w") as f:
        for i in similarity_label.shape[0]:
            print(similarity_label[:,i])
            line = similarity_label[:,i]
            f.write()
    """

    print("Done")


if __name__=="__main__":
    main()