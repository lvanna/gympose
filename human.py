import math
import numpy as np

class Human:
    def __init__(self, keypoints):
        #{0,  "Nose"},
        self.Nose = keypoints[0][0]
        #{1,  "Neck"},
        self.Neck = keypoints[0][1]
        #{2,  "RShoulder"},!!
        self.RS = keypoints[0][2]
        #{3,  "RElbow"},
        self.RE = keypoints[0][3]
        #{4,  "RWrist"},
        self.RW = keypoints[0][4]
        #{5,  "LShoulder"},!!
        self.LS = keypoints[0][5]
        #{6,  "LElbow"},
        self.LE = keypoints[0][6]
        #{7,  "LWrist"},
        self.LW = keypoints[0][7]
        #{8,  "MidHip"},
        self.MH = keypoints[0][8]
        #{9,  "RHip"},
        self.RH = keypoints[0][9]
        #{10, "RKnee"},
        self.RK = keypoints[0][10]
        #{11, "RAnkle"},!!
        self.RA = keypoints[0][11]
        #{12, "LHip"},
        self.LH = keypoints[0][12]
        #{13, "LKnee"},
        self.LK = keypoints[0][13]
        #{14, "LAnkle"},!!
        self.LA = keypoints[0][14]


    def getTArch(self):
        return np.array([self.Neck, self.RS, self.LS, self.MH])

    def measureTArch(self, tarch):
        difArch = np.absolute(self.getTArch()-tarch)
        print('mTA_getTArch()', self.getTArch())
        print('mTA_tarch', tarch)
        print('mTA_difArch', difArch)
        if difArch[0][1]<5 or difArch[3][1]<5:
            return 1
        return 0

    def getBArch(self):
        return np.array([self.Neck, self.MH, self.LK])

    def measureBArch(self, barch):
        difArch = np.absolute(self.getBArch()-barch)
        print('mBA_getBArch()', self.getBArch())
        print('mBA_barch', barch)
        print('mBA_difArch', difArch)
        if difArch[0].any()<5 and difArch[1].any()<15 and difArch[2][0]<25 and difArch[2][1]>10:
            return 1
        return 0

    def measureWristsAndAnkles(self):
        hwidth = abs(self.RW[0]-self.LW[0])
        fwidth = abs(self.RA[0]-self.LA[0])
        if hwidth > fwidth:
            return 1
        return 0

    def measureShouldersAndAnleesParallel(self):
        soulder_ans = self.LS-self.RS
        soulder_result = float(soulder_ans[1])/float(soulder_ans[0])
        anless_ans = self.LA-self.RA
        anless_result = float(anless_ans[1])/float(anless_ans[0])
        print(abs(soulder_result-anless_result))
        if abs(soulder_result-anless_result)<0.1:
            return 1
        return 0

    def measureShouldersAndAnkles(self):
        soulder_x = math.pow((self.RS[0]-self.LS[0]), 2)
        soulder_y = math.pow((self.RS[1]-self.LS[1]), 2)
        soulder_dis = math.sqrt(soulder_x+soulder_y)

        ankle_x = math.pow((self.RA[0]-self.LA[0]), 2)
        ankle_y = math.pow((self.RA[1]-self.LA[1]), 2)
        ankle_dis = math.sqrt(ankle_x+ankle_y)
        if ankle_dis >= soulder_dis:
            return 1
        return 0

    def measureHandAndKnee(self):
        a=self.LW[1]-self.LS[1]
        b=self.LS[0]-self.LW[0]
        c=(self.LW[0]*self.LS[1])-(self.LS[0]*self.LW[1])
        e=math.sqrt((a*a)+(b*b))
        d=abs((a*self.LK[0])+(b*self.LK[1])+c)/e
        if self.LS[1] < self.LK[1] and self.LW[1] > self.LK[1]:
            if self.LS[0] > self.LK[0] and self.LW[0] > self.LK[0]:
                if d>0:
                    return 1
        return 0

    def measureArmAndBent(self):
        difSE = np.absolute(np.around(self.LS)-np.around(self.LE))
        SE_results = float(difSE[0])/float(difSE[1])
        difEW = np.absolute(np.around(self.LE)-np.around(self.LW))
        EW_results = float(difSE[0])/float(difEW[1])
        if abs(SE_results-EW_results)<0.2:
            return 1
        return 0

    def measureHipAndKnee(self):
        mh = self.MH[1]
        lk = self.LK[1]

        if (abs(mh-lk)<28):
            return 1
        return 0

    # def getinitBack(self):
    #     print('gIB_Neck', self.Neck)
    #     print('gIB_MH', self.MH)
    #     bh=math.pow((self.Neck[0]-self.MH[0]), 2)
    #     bw=math.pow((self.Neck[1]-self.MH[1]), 2)
    #     print("gIB_bh", bh)
    #     print("gIB_bw", bw)
    #     ib=math.sqrt(bh+bw)
    #     print("gIB_ib", ib)
    #     return np.array([[ib], self.Neck, self.MH, self.LK])

    #measure Back
    # def measureBack(self, ib):

    #     #Threshold
    #     th=10

    #     nbh=math.pow((self.Neck[0]-self.MH[0]), 2)
    #     nbw=math.pow((self.Neck[1]-self.MH[1]), 2)
    #     nb=math.sqrt(nbh+nbw)

    #     print("ib", ib)
    #     diff=abs(ib-nb)
    #     print("diff", diff)

    #     if diff<th:
    #         return 1
    #     else:
    #         return 0

    def measureNeckAndBottom(self, tarch_s, tarch_e):
        difArch = np.absolute(tarch_e-tarch_s)
        print
        if difArch[0][1]<3 and difArch[1][1]<3 and difArch[2][1]<4 and difArch[3][1]<3:
           return 1
        return 0
