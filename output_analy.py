import numpy as np
import pandas as pd
import heapq

def extract_info_csv(file_name):
    df = pd.read_csv(file_name, header=None)
    target_sliced = df[[0,1]]
    
    print("Data extracted")

    return target_sliced
    
def make_confusion_mat(df):
    gt_label = df[0]
    pred_label = df[1]

    # Saving Confusion Matrix in conf_mat.
    conf_mat = np.zeros((51,51))

    for i in range(gt_label.shape[0]):
        gt = int(gt_label[i])
        pred = int(pred_label[i])
        conf_mat[gt][pred] += 1
        
    print("Confusion Mat generated")
    
    return conf_mat

def get_topk_index(confusion_mat, topk=5,print_opt=False):
    output_topk = []
    output_topk = np.array(output_topk)

    for i in range(confusion_mat.shape[0]):
        index_topk = heapq.nlargest(topk, range(len(confusion_mat[i])), confusion_mat[i].take)
        if(print_opt==True):
            print("{} {}".format(i, index_topk))
        output_topk = np.append(output_topk, index_topk)

    output_topk = output_topk.reshape(confusion_mat.shape[0], -1)
    
    print("Topk index returned")

    return output_topk
    
def get_pred_accuracy(confusion_mat, topk_index):
    ### print predicted accuracy for each categories
    for i in range(confusion_mat.shape[0]):
        for j in range(topk_index.shape[1]):
            total = conf_mat[i].sum()
            target = int(topk_index[i][j])
            ratio = (conf_mat[i][target]/total)
            print(ratio)
            
def print_pred_label(topk_index):
    for i in range(topk_index.shape[0]):
        for j in range(topk_index.shape[1]):
            print(topk_index[i][j])
            
if __name__=="__main__":
    base_path = "/home/yhji/Desktop/Research/pytorch-coviar-master/model_csv/hmdb51/trial1/"
    file_name = "hmdb51_residual_split3_trial1.csv"
    
    print("=====> Output Analysis on {}".format(file_name))
    
    target_df = extract_info_csv(base_path+file_name)
    conf_mat = make_confusion_mat(target_df)
    topk_index = get_topk_index(conf_mat, topk=5, print_opt=False)
    print("=====> pred label")
    print_pred_label(topk_index)
    
    print("=====> Pred Accuracy")
    get_pred_accuracy(conf_mat, topk_index)