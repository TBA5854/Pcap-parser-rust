from striprtf.striprtf import rtf_to_text

with open('/home/tba/Downloads/Sample_configs_Prob 2/Sample_configs/conf_2034.rtf', 'r') as file:
    rtf_content = file.read()

    text = rtf_to_text(rtf_content)

text = [i.strip(" !\t") for i in text.split("\n")]
text = [i for i in text if i != ""]
for i in text:
    print(i)

def user_count(text):
    count = 0
    for i in text:
        if i.startswith("user"):
            count += 1
    return count
def insecure_protocol(text):
    count = 0
    for i in text:
        if i.startswith("tftp-server") or (i.startwith("ip") and i.split(" ")[1] == "http") or (i.split(" ")[1] == "ftp" and (i.split(" ")[2] == "username" or (i.split(" ")[2] == "password" and (i.split(" ")[3] == "0" or len(i.split(" ")) == 3)))):
            count += 1
    return count
def snmp(text):
    count = 0
    for i in text:
        if i.startswith("snmp-server"):
            if i.split(" ")[1]=="group" and i.split(" ")[-1] in ["noauth","v1","v2c"]:
                count += 1
    return count
def pswd(text):
    count = 0
    for i in text:
        if i.startswith("enable password"):
            if len(i.split(" ")) == 3 or i.split(" ")[2] == "0" :
                count += 1
            count += 1
    return count
