#coding=utf8
import copy
def disposition(seq,split_e=""):
    #如果序列非列表就转成列表
    if not isinstance(seq,list):
        if isinstance(seq,str) and split_e !="":
            seq=seq.split(split_e)
        else: 
            seq=[i for i in seq]
    #定义要返回的序列
    ret_seq=[]
    #递归出口，如果未排列序列只有一个元素，就把未排列序列加入返回序列
    copy_seq=copy.deepcopy(seq)
    if len(seq)==1:
        ret_seq.append(copy_seq)
        return ret_seq
    '''
    递归主逻辑
    1.每个元素都循环一次，作为第一元素
    2.将第一元素插入剩余全排列列表的首位，作为一组排列
    3.把每组排列都加入ret_seq
    4.最后返回ret_seq'''
    for i in range(len(seq)):
        copy2_seq=copy.deepcopy(seq)
        first_arg=copy2_seq.pop(i)
        for j in disposition(copy2_seq):
            j.insert(0,first_arg)
            ret_seq.append(j)
    return ret_seq

if __name__ =="__main__":
    g=disposition([1,2,3,4])
    print(g)
    k=disposition("abef")
    print(k)
    j=disposition("a,b,c",split_e=",")
    print(j)
