import os
import math
import time
import sys
import multiprocessing 
import datetime
import scriptCreator
tSDRG_path="/dicos_ui_home/aronton/tSDRG_random"

# create namelist of task
def submitPara(parameterlist, tSDRG_path):

    p = parameterlist
    Spin = parameterlist["Spin"]
    Ncore = parameterlist["Ncore"]
    partition = parameterlist["partition1"]
    task = parameterlist["task"]
    para=scriptCreator.paraList1(parameterlist["L"],parameterlist["J"],parameterlist["D"],parameterlist["S"])
    L_num = para.L_num
    L_p_num = para.L_p_num
    L_str = para.L_str
    L_p_str = para.L_p_str
    

    
    print("L_num:",L_num)
    print("L_p_num:",L_p_num)
    print("L_str:",L_str)
    print("L_p_str:",L_p_str)

    S_num = para.S_num
    S_str = para.S_str
    s1 = parameterlist["S"]["S1"]
    s2 = parameterlist["S"]["S2"]
    ds = parameterlist["S"]["dS"]
    print("S_num:",S_num)
    print("S_str:",S_str)

    J_num = para.J_num
    J_p_num = para.J_p_num
    J_str = para.J_str
    J_p_str = para.J_p_str
    J_s100 = para.J_s100
    J_p_s100 = para.J_p_s100


    print("J_num",J_num)
    print("J_p_num",J_p_num)
    print("J_str:",J_str)
    print("J_p_str:",J_p_str)
    print("J_s100:",J_s100)
    print("J_p_s100:",J_p_s100)
    
    D_num = para.D_num
    D_p_num = para.D_p_num
    D_str = para.D_str
    D_p_str = para.D_p_str
    D_s100 = para.D_s100
    D_p_s100 = para.D_p_s100

    print("D_num:",D_num)
    print("D_p_num:",D_p_num)
    print("D_str:",D_str)
    print("D_p_str:",D_p_str)
    print("D_s100:",D_s100)
    print("D_p_s100:",D_p_s100)
    Spin=parameterlist["Spin"]
    Pdis=parameterlist["Pdis"]
    chi=parameterlist["chi"]
    BC=parameterlist["BC"]
    try:
        check_Or_Not=parameterlist["check_Or_Not"]
    except KeyError as e:
        print(e)
    # with open("./", "r") as file:
    #     template = file.readlines()
    
    os.system( "cd " + tSDRG_path + "/tSDRG/Main_" + str(Spin))
    script_path_tot = "" 
    submitlsit = []
    argvlist = []
    # for l,L in enumerate(L_num):
    #     for j,J in enumerate(J_num):
    #         for d,D in enumerate(D_num):
    #             # for s_i in range(len(S_num)):
    #             #     s = S_num[s_i]
    #             if parameterlist["task"] == "submit"
    #                 argvlist.append([str(Spin),L,J,D,Pdis,chi,task,check_Or_Not])
                # argvlist.append([str(Spin),L,J,D,Pdis,bondDim,str(s[0]),str(s[-1]),check_Or_Not])
    for l,L in enumerate(L_str):
        for j,J in enumerate(J_str):
            for d,D in enumerate(D_str):
                # for s_i in range(len(S_num)):
                #     s = S_num[s_i]
                name = ["Spin"+str(Spin),L,J,D,"P"+str(Pdis),"BC="+BC,"chi"+str(chi),"partition="+str(partition),"seed1="+str(s1),"seed2="+str(s2),"ds="+str(ds),"task="+task]
                name = "_".join(name)
                submitlsit.append(name)
    return (submitlsit, argvlist)           

# edit & submit task
def EditandSub(paraPath,script_path,output_path,jobName):
    task = ""
    with open(paraPath,"r") as file:
        elementlist = file.readlines()
        print(elementlist)
        for element in elementlist:
            if "partition" in element:
                partition = str(element.split(":")[1].replace("\n",""))
                # partition = str(element.replace("",":"))
            elif "ds" in element:
                ds = str(element.split(":")[1].replace("\n",""))
            elif "seed1" in element:
                s1 = str(element.split(":")[1].replace("\n",""))
            elif "seed2" in element:
                s2 =str(element.split(":")[1].replace("\n",""))
            elif "task" in element:
                task =str(element.split(":")[1].replace("\n",""))
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    output_path += f"/{jobName}.txt"
    
    replacements = {
        "replace1": jobName,
        "replace2": "10",
        "replace3": str(partition),
        "replace4": output_path
    }
    print(task)
    if task == "submit":
        with open("run1.sh", 'r') as file:
            content = file.read()
    if task == "collect":
        with open("runCollect.sh", 'r') as file:
            content = file.read()
    # 依據 replacements 替換文字
    for old_text, new_text in replacements.items():
        content = content.replace(old_text, new_text)
    print(content)
    if not os.path.exists(script_path):
        os.makedirs(script_path)
    script_path += f"/{jobName}.sh"
    # 將結果寫入新檔案
    with open(script_path, 'w') as file:
        file.write(content)

    print(f"替換完成，結果已儲存至 {script_path}")

    # with open(script_path, "w") as file:
    #     context = file.read()
    #     context[1] = context[1].replace("replace1", "scopion" + str(partition))
    #     context[3] = context[3].replace("replace2", jobName)
    #     context[4] = context[4].replace("replace3", str(Ncore))
    #     # taskdescription = ""
    #     # # for 
    #     # #     taskdescription = taskdescription + f"./Spin{Spin}.exe" 
    #     context[5] = context[5].replace("replace4", output_path)
    #     file.writelines(context)
        
    # submit_cmd_list = ["nohup sbatch ",script_path, output_path, ">/dev/null 2>& 1&"]

    
    # submit_cmd_list = ["nohup sbatch ",script_path, str(Spin),str(L),str(J),str(D)\
    # ,str(BC),str(bondDim),str(Pdis),str(s1),str(s2),check_Or_Not,str(Ncore),tSDRG_path,output_path, ">/dev/null 2>& 1&"]

    submit_cmd = f"sbatch --ntasks={ds} {script_path} {paraPath} {output_path}"
    os.system(submit_cmd)    

# organize task and parameter name into scriptpath
def submit(parameterlist, tSDRG_path, tasklist):
    print(parameterlist)
    p = parameterlist
    Ncore = parameterlist["Ncore"]
    partition = parameterlist["partition1"]
    Spin=parameterlist["Spin"]
    Pdis=parameterlist["Pdis"]
    chi=parameterlist["chi"]
    BC=parameterlist["BC"]
    if parameterlist["task"] == "submit":
        check_Or_Not=parameterlist["check_Or_Not"]
    ds=parameterlist["S"]["dS"]

    record_dir = tSDRG_path + "/tSDRG" + "/Main_" + str(Spin) + "/jobRecord" 
    if parameterlist["task"] == "collect":
    # record_dir = tSDRG_path + "/tSDRG" + "/Main_" + str(Spin) + "/jobRecord" 
        script_dir = record_dir + "/collect_script" + "/" + str(BC) + "/B" + str(chi)
        output_dir = record_dir + "/collect_slurmOutput" + "/" + str(BC) + "/B" + str(chi)
    else:
        script_dir = record_dir + "/script" + "/" + str(BC) + "/B" + str(chi)
        output_dir = record_dir + "/slurmOutput" + "/" + str(BC) + "/B" + str(chi)
    nt=datetime.datetime.now()
    now_year = str(nt.year)
    now_date = str(nt.year) + "_" + str(nt.month) + "_" + str(nt.day)
    now_time = "H" + str(nt.hour) + "_M" + str(nt.minute) + "_S" + str(nt.second)

    # with open("/".join([tSDRG_path,"parameterRead",now_year,now_date])) as file:
        


    # with open("run.sh", "r") as file:
    #     template = file.readlines()

    
    os.system( "cd " + tSDRG_path + "/tSDRG/Main_" + str(Spin))
    # script_path_tot = "" 
    print(tasklist[1])
    for i,jobName in enumerate(tasklist[0]):
        print(jobName)
        elementlist = jobName.split("_")
        
        L = elementlist[1]
        J = elementlist[2]
        D = elementlist[3]
        
        script_path = script_dir + "/" + L + "/" + J + "/" + D  
        output_path = output_dir + "/" + L + "/" + J + "/" + D

        if parameterlist["task"]=="submit":
            if not os.path.exists("/".join([tSDRG_path,"Subpy","parameterRead",now_year,now_date])):
                os.makedirs("/".join([tSDRG_path,"Subpy","parameterRead",now_year,now_date]))
            paraPath = "/".join([tSDRG_path,"Subpy","parameterRead",now_year,now_date,"_".join([jobName,f"{now_time}.txt"])])

        if parameterlist["task"]=="collect":
            if not os.path.exists("/".join([tSDRG_path,"Subpy","collectPara",now_year,now_date])):
                os.makedirs("/".join([tSDRG_path,"Subpy","collectPara",now_year,now_date]))
            paraPath = "/".join([tSDRG_path,"Subpy","collectPara",now_year,now_date,"_".join([jobName,f"{now_time}.txt"])])
            
        # os.makedirs("/".join([tSDRG_path,"parameterRead",now_year,now_date,"_".join([jobName,f"{now_time}.txt"])]). exist_ok=True)
        with open(paraPath,"w") as file:
            for element in elementlist:
                if "D" in element:
                    s = str(element.replace("Dim",""))
                    file.writelines("D:" + s[0] + "." + s[1] + s[2] + "\n")
                elif "J" in element:
                    s = str(element.replace("Jdis",""))
                    file.writelines("J:"+ s[0] + "." + s[1] + s[2] + "\n")
                elif "L" in element:
                    s = str(element.replace("L",""))
                    file.writelines("L:"+ s + "\n")
                elif "BC" in element:
                    file.writelines(element.replace("=",":") + "\n")
                elif "partition" in element:
                    file.writelines("partition:" + partition + "\n")
                elif "P" in element:
                    s = str(element.replace("P",""))
                    file.writelines("Pdis:" + s[0] + s[1] + "\n")
                elif "chi" in element:
                    s = str(element.replace("chi",""))
                    file.writelines("chi:" +s[0] + s[1] + "\n")
                elif "seed1" in element:
                    s = str(element.replace("=",":").replace("seed","s"))
                    file.writelines(s + "\n")
                elif "seed2" in element:
                    s = str(element.replace("=",":").replace("seed","s"))
                    file.writelines(s + "\n")
                elif "check" in element:
                    file.writelines(element + "\n")
                elif "task" in element:
                    s = str(element.replace("=",":"))
                    file.writelines(s + "\n")
            file.writelines("ds:"+str(ds) + "\n")
        EditandSub(paraPath, script_path, output_path, jobName)
                # print(element)
    #     if os.path.exists(script_path):
    #         pass
    #         # print("exist : ", script_path)
    #     else:
    #         # print("not exist : ", script_path)
    #         os.makedirs(script_path)
            
    #     if os.path.exists(output_path):
    #         pass
    #         # print("exist : ", output_path)
    #     else:
    #         # print("not exist : ", output_path)
    #         os.makedirs(output_path)
            
    #     script_name = jobName + "_" + now_date + "_" + now_time
    #     script_path = script_path + "/" + script_name + "_random.sh"
    #     output_path = output_path + "/" + script_name + "_random.out"
    #     context = template.copy()
    #     script_path_tot = script_path_tot + script_path + "\n"
    #     EditandSub(parameterlist,script_path,output_path,jobName,context)
        
    # print(script_path_tot)


def find(parameterlist):
    print("find")
    p = parameterlist
    # flag = input("Job_state R/P")
    if p["status"] == "R":
        Job_state = "RUNNING"
    elif p["status"] == "P":
        Job_state = "PENDING"
    elif p["status"] == "skip" :
        Job_state = "skip"

    Ncore = p["Ncore"]
    partition = p["partition1"]      
    
    if partition != "skip":
        job_list = os.popen("squeue " + "-u aronton " + "-p " + str(partition) + " -o \"%%10i %%30P %%130j %%15T\"")
    else:
        job_list = os.popen("squeue " + "-u aronton " + " -o \"%%10i %%30P %%130j %%15T\"")
    job_list = list(job_list)

    del job_list[0]
    for i in range(len(job_list)):
        job_list[i] = job_list[i].split()    

    para = scriptCreator.paraList1(p["L"],p["J"],p["D"],p["S"])

    if (p["L"]["L1"] != "skip") and (p["L"]["L2"] != "skip") and (p["L"]["dL"] != "skip"): 
        L_num = para.L_num
        L_p_num = para.L_p_num
        L_str = para.L_str
        L_p_str = para.L_p_str       
        temp = []
        for l in L_str:
            for e in job_list:
                if l in e[2]:
                    temp.append(e)
        job_list = temp

            
    if (p["J"]["J1"] != "skip") and (p["J"]["J2"] != "skip") and (p["J"]["dJ"] != "skip"): 
        J_num = para.J_num
        J_p_num = para.J_p_num
        J_str = para.J_str
        J_p_str = para.J_p_str
        J_s100 = para.J_s100
        J_p_s100 = para.J_p_s100
        temp = []
        for j in J_str:
            for e in job_list:
                if j in e[2]:
                    temp.append(e)
        job_list = temp




    if (p["D"]["D1"] != "skip") and (p["D"]["D2"] != "skip") and (p["D"]["dD"] != "skip"): 
        D_num = para.D_num
        D_p_num = para.D_p_num
        D_str = para.D_str
        D_p_str = para.D_p_str
        D_s100 = para.D_s100
        D_p_s100 = para.D_p_s100
        temp = []
        for d in D_str:
            for e in job_list:
                if d in e[2]:
                    temp.append(e)
            # if i in job_list
        job_list = temp
        
    Pdis=p["Pdis"]
    chi=p["chi"]
    BC=p["BC"]
        
    if (p["Spin"] != "skip"): 
        Spin=str(p["Spin"])
        job_list = list(filter(lambda n: Spin in n[2],job_list))
    if (p["Pdis"] != "skip"): 
        Pdis=str(p["Pdis"])
        job_list = list(filter(lambda n: Pdis in n[2],job_list))        
    if (p["chi"] != "skip"): 
        chi=str(p["chi"])
        job_list = list(filter(lambda n: chi in n[2],job_list))   
    if (p["BC"] != "skip"): 
        BC=str(p["BC"])
        job_list = list(filter(lambda n: BC in n[2],job_list))    
    if (Job_state != "skip"): 
        job_list = list(filter(lambda n: Job_state in n[3],job_list))     
     
    return job_list

def cancel(parameterlist):

    job_list = find(parameterlist)

    print("Cancel : \n\n")
    print("------------------------------------------------- \n\n")
    
    for i in range(len(job_list)):
        print(job_list[i][2])    
    yes = input(f"These {len(job_list)} jobs are found, are you going to cancel them ?(Y or y to delete)")
    if yes == "y" or yes == "Y":
        for i in range(len(job_list)):
            cmd = "scancel " + job_list[i][0]
            print(cmd + " : " + job_list[i][2])    
            os.system(cmd)        
    else:
        return
def get(parameterlist):
    
    job_list = find(parameterlist)
    task_list = []
    for job in job_list:
        task_list.append(job[2])
        
    return task_list


def show(parameterlist):
        
    job_list = find(parameterlist)

    print("show\n\n")
    print("------------------------------------------------------\n\n")

    for i in range(len(job_list)):
        print(job_list[i])

def Distribution(parameterlist):
        
    job_list = find(parameterlist)

    print("Distribution\n\n")
    print("------------------------------------------------------\n\n")
    print("tot:")
    tot=len(job_list)
    print(tot)
    print("Running:")
    job_list = list(filter(lambda n: "RUNNING" in n[3],job_list)) 
    run=len(job_list)
    print(run)
    print("Pending:")  
    print(tot-run)      

def collect(parameterlist, tSDRG_path):

    p = parameterlist
    Spin = parameterlist["Spin"]
    Ncore = parameterlist["Ncore"]
    partition = parameterlist["partition1"]
    para=scriptCreator.paraList1(parameterlist["L"],parameterlist["J"],parameterlist["D"],parameterlist["S"])
    L_num = para.L_num
    L_p_num = para.L_p_num
    L_str = para.L_str
    L_p_str = para.L_p_str
    

    
    print("L_num:",L_num)
    print("L_p_num:",L_p_num)
    print("L_str:",L_str)
    print("L_p_str:",L_p_str)

    # S_num = para.S_num
    # S_str = para.S_str
    # s1 = parameterlist["S"]["S1"]
    # s2 = parameterlist["S"]["S2"]
    # print("S_num:",S_num)
    # print("S_str:",S_str)

    J_num = para.J_num
    J_p_num = para.J_p_num
    J_str = para.J_str
    J_p_str = para.J_p_str
    J_s100 = para.J_s100
    J_p_s100 = para.J_p_s100


    print("J_num",J_num)
    print("J_p_num",J_p_num)
    print("J_str:",J_str)
    print("J_p_str:",J_p_str)
    print("J_s100:",J_s100)
    print("J_p_s100:",J_p_s100)
    
    D_num = para.D_num
    D_p_num = para.D_p_num
    D_str = para.D_str
    D_p_str = para.D_p_str
    D_s100 = para.D_s100
    D_p_s100 = para.D_p_s100

    print("D_num:",D_num)
    print("D_p_num:",D_p_num)
    print("D_str:",D_str)
    print("D_p_str:",D_p_str)
    print("D_s100:",D_s100)
    print("D_p_s100:",D_p_s100)

    Spin=parameterlist["Spin"]
    Pdis=parameterlist["Pdis"]
    chi=parameterlist["chi"]
    BC=parameterlist["BC"]
    runlist = []
    for L in L_str:
        for J in J_str:
            for D in D_str:
                runlist.append((BC,J,D,L,Pdis,chi,"ZL"))

    with multiprocessing.Pool(processes=int(Ncore)) as pool:
        results = pool.starmap(collectData, runlist)
    print(results)

def collectData(parameterlist):
    para=scriptCreator.paraList1(parameterlist["L"],parameterlist["J"],parameterlist["D"],parameterlist["S"])
    BC = parameterlist["BC"]
    Pdis = parameterlist["Pdis"]
    chi = "m" + str(parameterlist["chi"])
    s1 = int(parameterlist["S"]["S1"])
    s2 = int(parameterlist["S"]["S2"])
    for s in ["ZL","corr1","corr2","string","J_list","energy","dimerization","w_loc","seed"]:
        for L in para.L_str:
            for J in para.J_str:
                    arg.append((BC, J, para.D_str[0], L, f"P{Pdis}", f"{chi}", s, s1, s2))
    print(arg)         
    print("---------------------col--------------------\n")
    with multiprocessing.Pool(processes=len(s)*len(para.L_str)*len(para.J_str)) as pool:
        results1 = pool.starmap(combine.Combine, arg)
def collectDatatemp(BC, J, D, L, P, m, phys):
    
    sourcePathBase = tSDRG_path + "/tSDRG/Main_15/data_random/BC_re/J_re/D_re/L_re_P_re_m_re_s_re"
    targetPathBase = tSDRG_path + "/tSDRG/Main_15/data_random/BC_re/J_re/D_re/target"

    sourcePath = sourcePathBase.replace("BC_re", BC)
    sourcePath = sourcePath.replace("J_re", J)
    sourcePath = sourcePath.replace("D_re", D)

    targetPath = targetPathBase.replace("BC_re", BC)
    targetPath = targetPath.replace("J_re", J)
    targetPath = targetPath.replace("D_re", D)

    sourcePath = sourcePath.replace("L_re", L)
    sourcePath = sourcePath.replace("P_re", f"P{P}")
    sourcePath = sourcePath.replace("m_re", f"m{m}")
    
    if phys == "ZL":
        quantity = "ZL"
    elif phys == "energy":
        quantity = "energy"
    elif phys == "J_list":
        quantity = "J_list.csv"
    elif phys == "D_list":
        quantity = "J_list.csv"
    else:
        quantity = "string.csv"
        
    targetName = "_".join([quantity, J, D, L, f"P{P}", f"m{m}", BC]) + ".txt"
    targetPath = targetPath.replace("target", targetName)
    
    record = 0
    err = 1
    # 產生 seed 陣列
    seedArray = [i for i in range(20000)]
    print(f"targetPath:{targetPath}")
    # 開啟輸出檔案
    with open(targetPath, 'w') as fTargert:
        line = "{quantity}\n"
        for seed in seedArray:
            newPath = os.path.join(sourcePath.replace("s_re", f"{seed+1}"), f"{quantity}.csv")
            if seed == seedArray[0]:
                print(newPath)

            
            # 嘗試開啟檔案
            try:
                with open(newPath, 'r') as fSource:
                    data = fSource.readlines()
                    value = data[-1].strip()  # 去除換行符號並轉 float
                    print(f"original {quantity}:{value}")
                    line = line + str(seed+1) + ",  " + quantity + "\n"
                    # 寫入結果到 ZL.txt
                    record = seed+1
                    # 存入陣列
                    # a[seed] = ZL
            except FileNotFoundError:
                if err == 1:
                    err = seed+1

                print(f"檔案不存在: {newPath}")
            if seed == seedArray[-1]:
                print(newPath)
        fTargert.write(line)
    return (record, err)

def checkAndDelete(BC, J, D, L, P, m, phys):
    sourcePathBase = tSDRG_path + "/tSDRG/Main_15/data_random/BC_re/J_re/D_re/L_re_P_re_m_re_s_re"
    targetPathBase = tSDRG_path + "/tSDRG/Main_15/data_random/BC_re/J_re/D_re/target"

    sourcePath = sourcePathBase.replace("BC_re", BC)
    sourcePath = sourcePath.replace("J_re", J)
    sourcePath = sourcePath.replace("D_re", D)

    targetPath = targetPathBase.replace("BC_re", BC)
    targetPath = targetPath.replace("J_re", J)
    targetPath = targetPath.replace("D_re", D)

    sourcePath = sourcePath.replace("L_re", L)
    sourcePath = sourcePath.replace("P_re", f"P{P}")
    sourcePath = sourcePath.replace("m_re", f"m{m}")
    quantity = phys
    targetName = "_".join([quantity, J, D, L, f"P{P}", f"m{m}", BC]) + ".txt"
    targetPath = targetPath.replace("target", targetName)    
    with open(targetPath, 'w') as fTargert:
        line = "{quantity}\n"
        for seed in seedArray:
            newPath = os.path.join(sourcePath.replace("s_re", f"{seed+1}"), f"{quantity}.csv")
            if seed == seedArray[0]:
                print(newPath)

            
            # 嘗試開啟檔案
            try:
                with open(newPath, 'r') as fSource:
                    data = fSource.readlines()
                    value = data[-1].strip()  # 去除換行符號並轉 float
                    print(f"original {quantity}:{value}")
                    line = line + str(seed+1) + ",  " + quantity + "\n"
                    # 寫入結果到 ZL.txt
                    record = seed+1
                    # 存入陣列
                    # a[seed] = ZL
            except FileNotFoundError:
                if err == 1:
                    err = seed+1

                print(f"檔案不存在: {newPath}")
            if seed == seedArray[-1]:
                print(newPath)
        fTargert.write(line)    
    return

def showPartition():
    # os.system('sinfo -o "%P %C"')
    partitionlsit = os.popen('sinfo -o "%P %C"')
    partitionlsit = list(partitionlsit)
    del partitionlsit[0]
    partitionlsit = [str(v.replace("\n","")) for v in partitionlsit]

    partitionlsit = [v.split(" ") for v in partitionlsit]
    partitionlsit = [(str(i),v[0],int(v[1].split("/")[1])) for i,v in enumerate(partitionlsit)]
    
    partitionlsit = [v for v in partitionlsit if "v100" not in v[0]]
    partitionlsit = [v for v in partitionlsit if "a100" not in v[0]]
    # [print(v[0]) for v in partitionlsit]
    return partitionlsit

def main():
    
    tasks = ["submit","show","cancel","change","dis","check","collect","a","b","c","d","e","f","g"]
    task = ""

    while task not in tasks:
        task = input("What is the task? (a)submit, (b)show, (c)cancel Jobs, (d)change (e)distribution: (f)check: (g)collect: \n")
        if task == "a":
            task = "submit"
        elif task == "b":
            task = "show"
        elif task == "c":
            task = "cancel"
        elif task == "d":
            task = "change"
        elif task == "e":
            task = "dis"    
        elif task == "f":
            task = "check"    
        elif task == "g":
            task = "collect"    

    os.system("sinfo")

    nt=datetime.datetime.now()

    print("---------------------------"+str(nt.now())+"---------------------------")

    print("key in parameter in the following format : \n\
    ex : Spin, L1, L2, delta_L, J1, J2, delta_J, D1, D2, delta_D, Pdis, chi, initialSampleNumber, finalSampleNumber, sampleDelta, check_Or_Not\n\
    ex : 15(Spin) 64(L) 1.1(J) 0.1(D) 10(Pdis) 40(chi) 1(initialSampleNumber) 20(finalSampleNumber) 5(sampleDelta), Y(check_Or_Not)\n")

    # task = sys.argv[1]
    partitionlsit = showPartition()
    [print(v) for v in partitionlsit]
    a = scriptCreator.para(task,partitionlsit)
    
    a.keyin()
    parameterlist = a.para
    print(parameterlist)
    
    # i = 2
    # for key1,value1 in parameterlist.items():
    #     if type(value1) != dict:
    #         try:
    #             if sys.argv[i] == "skip":
    #                 parameterlist[key1] = ""
    #             else:
    #                 parameterlist[key1]=sys.argv[i]
    #         except IndexError:
    #             parameterlist[key1]=""
    #         i = i + 1
    #     else:
    #         for key2,value2 in value1.items():
    #             try:
    #                 if sys.argv[i] == "skip":
    #                     parameterlist[key1][key2] = ""
    #                 else:
    #                     parameterlist[key1][key2]=sys.argv[i]
    #             except IndexError:
    #                 parameterlist[key1][key2]=""
    #             i = i + 1
                
    if task == "change":
        psubmit = a.resubmit
        pcancel = a.cancel

    print(parameterlist,"\n")
    for s in parameterlist:
        print(s," : ",parameterlist[s])

    if task == "submit" or task == "a":
        tasklist = submitPara(parameterlist, tSDRG_path)
        submit(parameterlist, tSDRG_path, tasklist)
    elif task == "show" or task == "b":
        show(parameterlist)
        Distribution(parameterlist)
    elif task == "cancel" or task == "c":
        cancel(parameterlist)
    elif task == "change" or task == "d":
        for key,value in parameterlist.items():
            if key in psubmit and key != "partition1":
                psubmit[key] = value
            if key in pcancel and key != "partition1":
                pcancel[key] = value
        print(parameterlist)
        pcancel["partition1"] = parameterlist["partition1"] 
        psubmit["partition1"] = parameterlist["partition2"]
        tasklist=get(pcancel)
        cancel(pcancel)
        submit(psubmit, tSDRG_path, tasklist)
    elif task == "dis" or task == "e":
        Distribution(parameterlist)
    elif task == "check" or task == "f":
        Distribution(parameterlist)
    elif task == "collect" or task == "g":
        tasklist = submitPara(parameterlist, tSDRG_path)
        submit(parameterlist, tSDRG_path, tasklist)
    return

if __name__ == '__main__' :
    main()

