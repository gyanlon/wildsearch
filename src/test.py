import re

line = "13_Isopropylpodocarpa_7,13_dien_15_oic acid; Abietadien_18_oic acid, 7,13_; Abietate; EINECS 208_178_3; NSC 25149"
# line = line.decode("utf8")
string = re.sub("[+——！，。？?、~@#￥%……&*（）;，]+", " ", line)


print(string)      