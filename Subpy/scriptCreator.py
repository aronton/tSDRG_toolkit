import re
import os
import average

class paraList1:
    def __init__(self, L_dic, J_dic, D_dic, S_dic):
        # print(L_dic)
        self.set_L(L_dic)
        # print(J_dic)
        self.set_J(J_dic)
        # print(D_dic)
        self.set_D(D_dic)
        # print(S_dic)
        self.set_S(S_dic)
        
    def set_L(self,dic):
        if dic["L1"] == "skip":
            for i in dic:
                dic[i] = "skip" 
            return
        L_dic = {}
        for key,value in dic.items():
            L_dic.update([(key,int(value))])
        if dic["L1"] == dic["L2"] or dic["dL"] == 0:
            self.L_num = [L_dic["L1"]]
            self.L_str = ["L" + str(self.L_num[0])]
            self.L_p_num = [L_dic["L1"],L_dic["L2"],0]
            self.L_p_str = ["L" + str(self.L_num[0]),"L" + str(self.L_num[0]),"L000"]
            return
        self.L_num = [l for l in range(L_dic["L1"], L_dic["L2"]+1, L_dic["dL"])]
        self.L_str = ["L" + str(l) for l in range(L_dic["L1"], L_dic["L2"]+1, L_dic["dL"])]
        self.L_p_str = ["L" + str(L_dic["L1"]), "L" + str(L_dic["L2"]), "L" + str(L_dic["dL"])]
        self.L_p_num = list(L_dic.values())
    def set_J(self,dic):
        if dic["J1"] == "skip":
            for i in dic:
                dic[i] = "skip" 
            return
        # if dic["J1"] == "":
        #     return
        J_dic = {}
        for key,value in dic.items():
            J_dic.update([(key,float(value))])
        if dic["J1"] == dic["J2"] or dic["dJ"] == 0:
            self.J_num = [J_dic["J1"]]
            self.J_s100 = [str(J_dic["J1"])]
            while len(self.J_s100[0]) < 4:
                self.J_s100[0] = self.J_s100[0] + "0"
                # self.J_s100[1] = self.J_s100[1] + "0"
            self.J_s100[0] = self.J_s100[0].replace('.', '')
            # self.J_s100[1] = self.J_s100[1].replace('.', '')
            self.J_str = ["Jdis" + self.J_s100[0]]
            self.J_p_num = [J_dic["J1"],J_dic["J2"],0]
            self.J_p_s100 = self.J_s100.copy()
            self.J_p_str = [str(J_dic["J1"]),str(J_dic["J2"]),"000"]
            return
        self.J_num = [round(n*J_dic["dJ"] + J_dic["J1"],2) for n in range(int((100*J_dic["J2"]-100*J_dic["J1"])/(100*J_dic["dJ"]))+1)]
        # self.J_list = [j for j in range(J_dic["L1"], J_dic["L2"]+1, J_dic["dL"])]
        self.J_s100 = [(str(n) + "0").replace('.', '') if len(str(n)) < 4 else str(n).replace('.', '') for n in self.J_num]
        self.J_str = [ "Jdis" + (str(n) + "0").replace('.', '') if len(str(n)) < 4 else "Jdis" + str(n).replace('.', '') for n in self.J_num]
        
        self.J_p_num =list(J_dic)
        self.J_p_s100 = [ self.J_s100[0], self.J_s100[-1], str(int(100*J_dic["dJ"])) ]
        self.J_p_str = ["Jdis" + n  for n in self.J_s100]
    def set_D(self,dic):
        if dic["D1"] == "skip":
            for i in dic:
                dic[i] = "skip" 
            return
        # if dic["D1"] == "":
        #     return
        D_dic = {}
        for key,value in dic.items():
            D_dic.update([(key,float(value))])
        if dic["D1"] == dic["D2"] or dic["dD"] == 0:
            self.D_num = [D_dic["D1"]]
            self.D_s100 = [str(D_dic["D1"])]
            while len(self.D_s100[0]) < 4:
                self.D_s100[0] = self.D_s100[0] + "0"
                # self.D_s100[1] = self.D_s100[1] + "0"
            self.D_s100[0] = self.D_s100[0].replace('.', '')
            # self.D_s100[1] = self.D_s100[1].replace('.', '')
            self.D_str = ["Dim" + self.D_s100[0]]
            self.D_p_num = [D_dic["D1"],D_dic["D2"],0]
            self.D_p_s100 = [str(D_dic["D1"]),str(D_dic["D2"]),"000"]
            self.D_p_str = ["Dim" + self.D_s100[0],"Dim" + self.D_s100[0],"Dim000"]
            return
        self.D_num = [round(n*D_dic["dD"] + D_dic["D1"],2) for n in range(int((100*D_dic["D2"]-100*D_dic["D1"])/(100*D_dic["dD"]))+1)]
        # self.J_list = [j for j in range(J_dic["L1"], J_dic["L2"]+1, J_dic["dL"])]
        self.D_s100 = [(str(n) + "0").replace('.', '') if len(str(n)) < 4 else str(n).replace('.', '') for n in self.D_num]
        self.D_str = [ "Dim" + (str(n) + "0").replace('.', '') if len(str(n)) < 4 else "Dim" + str(n).replace('.', '') for n in self.D_num]
        
        self.D_p_num =list(D_dic)
        self.D_p_s100 = [ self.D_s100[0], self.D_s100[1], str(int(100*D_dic["dD"])) ]
        self.D_p_str = ["Dim" + n for n in self.D_s100]
    def set_S(self,dic):
        if dic["S1"] == "skip":
            for i in dic:
                dic[i] = "skip" 
            return
        # if dic["S1"] == "":
        #     return
        S_dic = {}
        for key,value in dic.items():
            print(f"value{value}")
            S_dic.update([(key,int(value))])
        if dic["S1"] == dic["S2"]:
            self.S_num = [[dic["S1"],dic["S2"]]]
            self.S_str = [["seed1=" + str(dic["S1"]), "seed2=" + str(dic["S2"])]]
            return
        self.S_num1 = [S_dic["S1"] + n*S_dic["dS"] for n in range(int((S_dic["S2"]-S_dic["S1"]+1)/(S_dic["dS"])))]
        self.S_num2 = [S_dic["S1"]-1 + (n+1)*S_dic["dS"] for n in range(int((S_dic["S2"]-S_dic["S1"]+1)/(S_dic["dS"])))]
        self.S_num = [[self.S_num1[i], self.S_num2[i]] for i in range(len(self.S_num1))]
        self.S_str = [["seed1=" + str(self.S_num1[i]), "seed2=" + str(self.S_num2[i])] for i in range(len(self.S_num1))]
        
class para:
    def __init__(self,task,partitionlsit):
        self.partitionlsit = partitionlsit
        if task == "submit":
            self.para = {"Spin":None,"L":{"L1":None,"L2":None,"dL":None},"J":{"J1":None,"J2":None,"dJ":None},\
                 "D":{"D1":None,"D2":None,"dD":None},"S":{"S1":None,"S2":None,"dS":None},\
                 "BC":None,"Pdis":None,"chi":None,"check_Or_Not":None,"Ncore":None,"partition1":None,"task":"submit"}

        elif task == "show":
            self.para = {"Spin":None,"L":{"L1":None,"L2":None,"dL":None},"J":{"J1":None,"J2":None,"dJ":None},\
                 "D":{"D1":None,"D2":None,"dD":None},"S":{"S1":None,"S2":None,"dS":None},\
                 "BC":None,"Pdis":None,"chi":None,"status":None,"Ncore":None,"partition1":None,"task":"show"}

        elif task == "cancel":
            self.para = {"Spin":None,"L":{"L1":None,"L2":None,"dL":None},"J":{"J1":None,"J2":None,"dJ":None},\
                 "D":{"D1":None,"D2":None,"dD":None},"S":{"S1":None,"S2":None,"dS":None},\
                 "BC":None,"Pdis":None,"chi":None,"status":None,"Ncore":None,"partition1":None,"task":"cancel"}

        elif task == "change":
            self.para = {"Spin":None,"L":{"L1":None,"L2":None,"dL":None},"J":{"J1":None,"J2":None,"dJ":None},\
                 "D":{"D1":None,"D2":None,"dD":None},"S":{"S1":None,"S2":None,"dS":None},\
                 "BC":None,"Pdis":None,"chi":None,"check_Or_Not":None,"status":None,"Ncore":None,"partition1":None,"partition2":None}
            
            self.cancel = {"Spin":None,"L":{"L1":None,"L2":None,"dL":None},"J":{"J1":None,"J2":None,"dJ":None},\
                 "D":{"D1":None,"D2":None,"dD":None},"S":{"S1":None,"S2":None,"dS":None},\
                 "BC":None,"Pdis":None,"chi":None,"status":None,"Ncore":None,"partition1":None,"task":"cancel"}
            self.resubmit = {"Spin":None,"L":{"L1":None,"L2":None,"dL":None},"J":{"J1":None,"J2":None,"dJ":None},\
                 "D":{"D1":None,"D2":None,"dD":None},"S":{"S1":None,"S2":None,"dS":None},\
                 "BC":None,"Pdis":None,"chi":None,"check_Or_Not":None,"Ncore":None,"partition1":None,"task":"resubmit"}
            
        elif task == "dis":
            self.para = {"Spin":None,"L":{"L1":None,"L2":None,"dL":None},"J":{"J1":None,"J2":None,"dJ":None},\
                 "D":{"D1":None,"D2":None,"dD":None},"S":{"S1":None,"S2":None,"dS":None},\
                 "BC":None,"Pdis":None,"chi":None,"status":None,"Ncore":None,"partition1":None,"task":"dis"}
        elif task == "collect":
            self.para = {"Spin":None,"L":{"L1":None,"L2":None,"dL":None},"J":{"J1":None,"J2":None,"dJ":None},\
                 "D":{"D1":None,"D2":None,"dD":None},"S":{"S1":None,"S2":None,"dS":None},\
                 "BC":None,"Pdis":None,"chi":None,"status":None,"Ncore":None,"partition1":None,"task":"collect"}
    def keyin(self):
        for key in self.para.keys():
            eval("self.set_" + key + "()")
    def set_task(self):
        pass
    def set_Spin(self):
        try:
            S = input("key in spin :\n")
            if "." in S:
                S=int(10*float(S))
            else:
                S=int(S)
        except ValueError:
            if S == "":
                self.para["Spin"] = "skip"
                return
            else:
                print("should be interger or enter to skip")
                self.set_Spin()
        self.para["Spin"] = S
    def set_L(self):
        L_dic = self.check_L()
        self.para["L"] = L_dic
        # self.para["L"]["L1"] = L[0]
        # self.para["L"]["L2"] = L[1]
        # self.para["L"]["dL"] = L[2]
    def check_L(self):
        L_list = {"L1":None,"L2":None,"dL":None}
        for key, value in L_list.items():
        # while(len(L_list) < 3):
            try:
                L = input(key+ " : \n")
                L = int(L)
            except ValueError: 
                if L == "":
                   L_list = {"L1":"skip","L2":"skip","dL":"skip"}
                   return L_list
                else:
                    print("should be interger or enter to skip")
                    self.set_L()
            L_list[key] = L
        if L_list["L1"] == L_list["L2"]:
            if L_list["dL"] != 0:
                print("set 3rd to 0 automaticallly")
                L_list["dL"] = 0
            return L_list
        if ((L_list["L2"] - L_list["L1"]) % L_list["dL"]) != 0:
            print("key in error, rekey ")
            self.set_L()
        return L_list
    def set_S(self):
        S_dic = self.check_S()
        self.para["S"] = S_dic
    def check_S(self):
        S_dic = {"S1":None,"S2":None,"dS":None}
        for key, value in S_dic.items():
        # while(len(S_list) < 3):
            try:
                average.showPartition()
                S = input(key + " : \n")
                S = int(S)
            except ValueError: 
                if S == "":
                   S_dic = {"S1":"skip","S2":"skip","dS":"skip"}
                   return S_dic
                else:
                    self.set_S()
                    print("should be interger or enter to skip")
            S_dic[key] = S
        if S_dic["S1"] % 10 != 1:
            print("1st should be XX1")
            self.check_S()
        if S_dic["S1"] == S_dic["S2"]:
            if S_dic["dS"] != 0:
                print("set 3rd to 0 automaticallly?")
                S_dic["dS"] = 0
            return S_dic
        if ((S_dic["S2"] - S_dic["S1"] + 1) % S_dic["dS"]) != 0:
            print("key in error, rekey ")
            self.set_S()
        return S_dic
    def set_J(self):
        J_dic = self.check_J()
        self.para["J"] = J_dic
        # self.para["J"]["J1"] = J[0]
        # self.para["J"]["J2"] = J[1]
        # self.para["J"]["dJ"] = J[2]
    def check_J(self):
        J_dic = {"J1":None,"J2":None,"dJ":None}
        for key, value in J_dic.items():        
            # while(len(J_list) < 3):
            try:
                J = input(key + " : \n")
                J = float(J)
            except ValueError: 
                if J == "":
                   J_dic = {"J1":"skip","J2":"skip","dJ":"skip"}
                   return J_dic
                else:
                    para.set_J()
                    print("should be interger or enter to skip")
            J_dic[key] = J
        if J_dic["J1"] == J_dic["J2"]:
            if J_dic["dJ"] != 0:
                print("set 3rd to 0 automaticallly")
                J_dic["dJ"] = 0
            return J_dic
        if ((int(100*J_dic["J2"]) - int(100*J_dic["J1"])) % int(100*J_dic["dJ"])) != 0:
            print("key in error, rekey ")
            self.set_J()
        return J_dic
    def set_D(self):
        D_dic = self.check_D()
        self.para["D"] = D_dic

        # self.para["D"]["D1"] = D[0]
        # self.para["D"]["D2"] = D[1]
        # self.para["D"]["dD"] = D[2]
    def check_D(self):
        D_dic = {"D1":None,"D2":None,"dD":None}
        for key, value in D_dic.items():
        # while(len(D_list) < 3):
            try:
                D = input(key + " : \n")
                D = float(D)
            except ValueError: 
                if D == "":
                   D_dic = {"D1":"skip","D2":"skip","dD":"skip"}
                   return D_dic
                else:
                    print("should be float or enter to skip")
                    self.set_D()
            D_dic[key] = D
        if D_dic["D1"] == D_dic["D2"]:
            if D_dic["dD"] != 0:
                print("set 3rd to 0 automaticallly")
                D_dic["dD"] = 0
            return D_dic
        if ((int(100*D_dic["D1"]) - int(100*D_dic["D2"])) % int(100*D_dic["dD"])) != 0:
            print("key in error, rekey ")
            self.set_D()
        return D_dic
    def set_BC(self):
        BC = ""
        while(BC not in {"PBC","OBC"}):
            BC = input("BC? PBC or OBC :\n")
            if BC == "":
                self.para["BC"] = "skip"
                return
        self.para["BC"] = BC
    def set_Pdis(self):
        Pdis = 0    
        while(Pdis not in {"10","20","30"}):
            Pdis = input("distribution 10,20,30 :\n")    
            if Pdis == "":
                self.para["Pdis"] = "skip"
                return
        self.para["Pdis"] = Pdis
    def set_chi(self):
        try:
            chi = input("chi? : \n")
            chi = int(chi)
        except ValueError: 
            if chi == "":
                self.para["chi"] = "skip"
                return
            else:
                print("only int")
                self.set_chi()
        self.para["chi"] = chi
    def set_check_Or_Not(self):        
        check = ""
        while(check not in {"Y","N"}):
            check = input("check? Y or N : \n")
        self.para["check_Or_Not"] = check     
    def set_status(self):        
        status = ""
        while(status not in {"P","R"}):
            status = input("status? R or P : \n")
            if status == "":
                self.para["status"] = "skip"
                return
        self.para["status"] = status  
    def set_Ncore(self):
        status = ""
        try:
            Ncore = input("Ncore? : \n")
            Ncore = int(Ncore)
        except ValueError: 
            if status == "":
                self.para["Ncore"] = "skip"
                return
            print("only int") 
        self.para["Ncore"] = Ncore
    def set_partition1(self):
        # print(self.partitionlsit)
        numOfpartitionlist = [int(v[0]) for v in self.partitionlsit]
        # print(numOfpartitionlist)
        partition1 = 10000      
        while(int(partition1) not in numOfpartitionlist):
            average.showPartition()
            partition1 = input("partition1 : \n")    
            # partition1 = int(partition1)
            if partition1 == "":
                self.para["partition1"] = "skip"
                return
        self.para["partition1"] = self.partitionlsit[int(partition1)][1]
    def set_partition2(self):
        
        numOfpartitionlist = [int(v[0]) for v in self.partitionlsit]
        partition2 = 10000    
        while(partition2 not in numOfpartitionlist):
            average.showPartition()
            partition2 = input("partition2 : \n")    
            # partition2 = int(partition2)
            if partition2 == "":
                self.para["partition2"] = "skip"
                return
        self.para["partition2"] = self.partitionlsit[int(partition2)][1]
    def release(self):
        self.new_dic = {}
        for key,value in self.para.items():
            if type(value) != dict:
                self.new_dic.update([(key, str(value))])
            else:
                for key1,value1 in value.items():
                    self.new_dic.update([(key1, str(value1))])


################################################### not used ############################################

                    
class paraList:
    def __init__(self,title,inlist):
        # self._numlist = list(numlist.values())
        if ("." in list(inlist.values())[0]) or ("." in list(inlist.values())[1]) or ("." in list(inlist.values())[2]): 
            self.intOrnot = "N"
        else:
            self.intOrnot = "Y"
        self.p_s100_list = [] # ex 050,150,050
        self.set_p_s100_list(title,list(inlist.values()))
        # self.p_list = list(inlist.values())
        self.p_num_list = [] # ex 0.5,1.5,0.5
        self.set_p_num_list(title,list(inlist.values()))
        self.p_str_list = [] # ex Jdis050,Jdis150,Jdis050
        self.set_p_str_list(title,self.p_s100_list.copy())

        self.s100_list = [] # ex 050,100,150...
        self.set_s100_list(title,self.p_s100_list.copy())
        self.num_list = [] # ex 0.5,1,1.5...
        self.set_num_list(title,self.s100_list.copy())
        self.str_list = [] # ex Jdis050,Jdis100,Jdis150...
        self.set_str_list(title,self.s100_list.copy())
        
    def set_p_s100_list(self,title,inlist):
        # if self.intOrnot == "N":
        if inlist[0] == inlist[1]:
            s = str(float(inlist[0]))
            s = inlist[0]
            slen = len(s)
            l=re.sub("[^0-9]", "", s)

            if self.intOrnot == "N":
                while len(l) < 3:
                    l = l + "0"                
            self.p_s100_list = [l,l,"000"]
        else:
            p1=re.sub("[^0-9]", "", inlist[0])
            if self.intOrnot == "N":
                while len(p1) < 3:
                    p1 = p1 + "0"            
            p2=re.sub("[^0-9]", "", inlist[1])
            if self.intOrnot == "N":
                while len(p2) < 3:
                    p2 = p2 + "0"
            dp=re.sub("[^0-9]", "", inlist[2])
            if self.intOrnot == "N":
                while len(dp) < 3:
                    dp = dp + "0"      
            self.p_s100_list = [p1,p2,dp]    
        # else:
        #     if inlist[0] == inlist[1]:
        #         slen = len(inlist[0])
        #         l=re.sub("[^0-9]", "", inlist[0])
        #         while len(l) < slen:
        #             l = l + "0"
        #         self.p_s100_list = [l,l,"000"]
        #     else:
        #         p1=re.sub("[^0-9]", "", inlist[0])
        #         if self.intOrnot == "N":
        #             while len(p1) < 3:
        #                 p1 = p1 + "0"            
        #         p2=re.sub("[^0-9]", "", inlist[1])
        #         if self.intOrnot == "N":
        #             while len(p2) < 3:
        #                 p2 = p2 + "0"
        #         dp=re.sub("[^0-9]", "", inlist[2])
        #         if self.intOrnot == "N":
        #             while len(dp) < 3:
        #                 dp = dp + "0"      
        #         self.p_s100_list = [p1,p2,dp]    
    def set_p_num_list(self,title,inlist):
        if inlist[0] == inlist[1]:
            inlist[2] = "0"
        l_num = []
        for s in inlist:
            l = [c for c in s if c.isdigit()]
            if "." in s:
                l.insert(1,".")
                x = "".join(l)
                num = float("".join(x))
            else:
                x = "".join(l)
                num = int("".join(x))
            l_num.append(num)
        self.p_num_list = l_num
    def set_p_str_list(self,title,inlist):
        self.p_str_list = []
        for s in inlist:
            self.p_str_list.append(title + s)
    def set_s100_list(self,title,inlist):
        if self.intOrnot == "N":
            if inlist[0] == inlist[1]:
                l = []
                l.append(inlist[0])
            else:
                n = int((int(inlist[1]) - int(inlist[0]))/int(inlist[2]))
                l = []
                for i in range(n+1):
                    if len(str(int(inlist[0]) + i*int(inlist[2])))==2:
                        l.append("0"+str(int(inlist[0]) + i*int(inlist[2])))
                    elif len(str(int(inlist[0]) + i*int(inlist[2])))==1:
                        l.append("00"+str(int(inlist[0]) + i*int(inlist[2])))
                    else:
                        l.append(str(int(inlist[0]) + i*int(inlist[2])))
            self.s100_list = list(l)
        else:
            if inlist[0] == inlist[1]:
                l = []
                l.append(str(int(inlist[0])))
            else:
                n = int((int(inlist[1]) - int(inlist[0]))/int(inlist[2]))
                l = []
                for i in range(n+1):
                    if len(str(int(inlist[0]) + i*int(inlist[2])))==2:
                        l.append(str(int(inlist[0]) + i*int(inlist[2])))
                    elif len(str(int(inlist[0]) + i*int(inlist[2])))==1:
                        l.append(str(int(inlist[0]) + i*int(inlist[2])))
                    else:
                        l.append(str(int(inlist[0]) + i*int(inlist[2])))
            self.s100_list = list(l)        
    def set_num_list(self,title,inlist):
        l = []
        if self.intOrnot == "N":
            for s in inlist:
                l.append(float(s[0]+"."+s[1]+s[2]))
        else:
            for s in inlist:
                l.append(int(s))            
        self.num_list = list(l)
    def set_str_list(self,title,inlist):
        l = []
        for s in inlist:
            if self.intOrnot == "N":
                if int(s) == 0:
                    l.append(title + "000")
                else:
                    l.append(title + str(s))
            else:
                if int(s) == 0:
                    l.append(title + "000")
                else:
                    l.append(title + str(s))
        self.str_list = list(l)
        
class Lpara:
    def __init__(self,title,inlist):
        
        self.p_s100_list = [] # ex 050,150,050
        self.set_p_s100_list(title,list(inlist.values()))
        # self.p_list = list(inlist.values())
        self.p_num_list = [] # ex 0.5,1.5,0.5
        self.set_p_num_list(title,list(inlist.values()))
        self.p_str_list = [] # ex Jdis050,Jdis150,Jdis050
        self.set_p_str_list(title,self.p_s100_list.copy())

        self.s100_list = [] # ex 050,100,150...
        self.set_s100_list(title,self.p_s100_list.copy())
        self.num_list = [] # ex 0.5,1,1.5...
        self.set_num_list(title,self.s100_list.copy())
        self.str_list = [] # ex Jdis050,Jdis100,Jdis150...
        self.set_str_list(title,self.s100_list.copy())
        
        # self.p_list = list(inlist.values())
        # self.p_num_list = []
        # self.set_p_num_list(title,list(inlist.values()))
        # self.p_s100_list = []
        # self.set_p_s100_list(title,list(inlist.values()))
        # self.p_str_list = []
        # self.set_p_str_list(title,self.p_s100_list.copy())

        # self.s100_list = []
        # self.set_s100_list(title,self.p_s100_list.copy())
        # self.num_list = []
        # self.set_num_list(title,self.s100_list.copy())
        # self.str_list = []
        # self.set_str_list(title,self.s100_list.copy())
    def set_p_s100_list(self,title,inlist):
        for s in inlist:
            self.p_s100_list.append(str(int(s)))
    def set_p_num_list(self,title,inlist):
        for s in inlist:
            self.p_num_list.append(int(s))
    def set_p_str_list(self,title,inlist):
        for s in inlist:
            self.p_str_list.append(title + str(int(s)))
            
    def set_s100_list(self,title,inlist):
        if inlist[0] == inlist[1]:
            l = []
            l.append(str(int(inlist[0])))
        else:
            n = int((int(inlist[1]) - int(inlist[0]))/int(inlist[2]))
            l = []
            for i in range(n+1):
                # if len(str(int(inlist[0]) + i*int(inlist[2])))==2:
                #     l.append("0"+str(int(inlist[0]) + i*int(inlist[2])))
                # else:
                l.append(str(int(inlist[0]) + i*int(inlist[2])))
        self.s100_list = list(l)
    def set_num_list(self,title,inlist):
        l = []
        for s in inlist:
            l.append(int(s))
        self.num_list = list(l)
    def set_str_list(self,title,inlist):
        l = []
        for s in inlist:
            l.append(title + s)
        self.str_list = list(l)

class Spara:
    def __init__(self,title,numlist):
        numlist = list(numlist.values())
        self.x1 = int(numlist[0])
        self.x2 = int(numlist[1])
        self.dx = int(numlist[2])
        self.title = title
    def toS(self):
        numSeed = []
        for i in list(range(self.x1 ,self.x2, self.dx)):
            a = [j for j in list(range(i,i+self.dx))]
            numSeed.append(a)
        # print(numSeed)
        # numL = [self.x1 + l*self.dx for l in range(int((self.x2-self.x1)/self.dx) + 1)]
        return list(numSeed)   
    def toStr(self):
        if self.x2>0:
            strSeed = []
            for i in list(range(self.x1 ,self.x2,self.dx)):
                a = [self.title + str(j) for j in list(range(i,i+self.dx))]
                strSeed.append(a)
            # numL = [ self.title + str(self.x1 + l*self.dx) for l in range(int((self.x2-self.x1)/self.dx) + 1)]
        else:
            strSeed = []
            for i in list(range(self.x1 ,self.x2,self.dx)):
                a = [self.title + "N" + str(j) for j in list(range(i,i+self.dx))]
                strSeed.append(a)
            # numL = [ self.title + "N" + str((self.x1 + l*self.dx)*-1) for l in range(int((self.x2-self.x1)/self.dx) + 1)]    
        return list(strSeed)    
    def __repr__(self):
        return f'Point({self.x1}, {self.x2}, {self.dx})'
