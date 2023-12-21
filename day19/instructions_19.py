
def NSZ(metal):
	if(metal["x"]>1625):
		return "R"
	else:
		return "R"

def LDX(metal):
	if(metal["s"]>3581):
		return "R"

	if(metal["s"]<3393):
		return "A"

	if(metal["x"]<1640):
		return "A"
	else:
		return "A"

def PZ(metal):
	if(metal["x"]<645):
		return "A"
	else:
		return "A"

def PJC(metal):
	if(metal["x"]>3650):
		return "A"

	if(metal["m"]<1853):
		return KX(metal)
	else:
		return CPB(metal)
def SFJ(metal):
	if(metal["x"]>2325):
		return "R"

	if(metal["m"]<1913):
		return "A"

	if(metal["s"]<1268):
		return "R"
	else:
		return "R"

def JX(metal):
	if(metal["m"]>963):
		return HF(metal)

	if(metal["m"]<581):
		return BRR(metal)

	if(metal["a"]>990):
		return SD(metal)
	else:
		return BT(metal)
def SCR(metal):
	if(metal["m"]<3108):
		return "A"

	if(metal["a"]<171):
		return "R"
	else:
		return "R"

def XVC(metal):
	if(metal["m"]<2497):
		return NKQ(metal)
	else:
		return "R"

def TQK(metal):
	if(metal["a"]<3529):
		return "R"
	else:
		return "R"

def CS(metal):
	if(metal["s"]>2943):
		return "R"

	if(metal["s"]>2799):
		return "R"

	if(metal["a"]>2999):
		return "A"
	else:
		return "R"

def TGG(metal):
	if(metal["m"]>923):
		return BVD(metal)
	else:
		return PPZ(metal)
def QBP(metal):
	if(metal["m"]>3259):
		return ZK(metal)

	if(metal["x"]<776):
		return "R"
	else:
		return "A"

def SBV(metal):
	if(metal["m"]<2517):
		return XVC(metal)

	if(metal["a"]<1226):
		return JCS(metal)

	if(metal["x"]<1907):
		return JS(metal)
	else:
		return PKH(metal)
def SJK(metal):
	if(metal["s"]>846):
		return NFV(metal)
	else:
		return XFM(metal)
def VM(metal):
	if(metal["m"]<2459):
		return "A"

	if(metal["x"]<2610):
		return "R"
	else:
		return "A"

def BPT(metal):
	if(metal["x"]>1809):
		return "A"

	if(metal["s"]<1043):
		return "A"

	if(metal["m"]>1649):
		return "R"
	else:
		return "A"

def DGD(metal):
	if(metal["a"]>3408):
		return RCS(metal)
	else:
		return BDV(metal)
def XFM(metal):
	if(metal["s"]<730):
		return "R"

	if(metal["x"]>184):
		return "R"
	else:
		return "A"

def VBC(metal):
	if(metal["a"]>3030):
		return FZT(metal)
	else:
		return FFT(metal)
def LGX(metal):
	if(metal["s"]>3059):
		return "A"
	else:
		return "A"

def GJF(metal):
	if(metal["a"]>1338):
		return "R"
	else:
		return "A"

def RGB(metal):
	if(metal["s"]<29):
		return "A"

	if(metal["x"]<849):
		return "A"
	else:
		return "A"

def KHC(metal):
	if(metal["s"]<458):
		return "R"

	if(metal["x"]<2962):
		return "R"
	else:
		return FDL(metal)
def SST(metal):
	if(metal["s"]>1367):
		return NZL(metal)

	if(metal["x"]>678):
		return NBM(metal)

	if(metal["a"]>3313):
		return TL(metal)
	else:
		return HBL(metal)
def RG(metal):
	if(metal["s"]<355):
		return "R"

	if(metal["a"]>3711):
		return "R"
	else:
		return "R"

def NBM(metal):
	if(metal["s"]<876):
		return HXH(metal)

	if(metal["m"]<1260):
		return RT(metal)
	else:
		return KZQ(metal)
def VBQ(metal):
	if(metal["a"]>1476):
		return "R"

	if(metal["a"]<1042):
		return MT(metal)

	if(metal["x"]>1740):
		return "R"
	else:
		return MQ(metal)
def CC(metal):
	if(metal["a"]>1194):
		return "A"

	if(metal["s"]>3579):
		return "R"
	else:
		return "A"

def HJ(metal):
	if(metal["s"]>1509):
		return "A"

	if(metal["s"]<979):
		return "R"
	else:
		return "R"

def XG(metal):
	if(metal["m"]>1602):
		return SMN(metal)

	if(metal["a"]<3522):
		return SJZ(metal)

	if(metal["m"]<1438):
		return "A"
	else:
		return "A"

def XD(metal):
	if(metal["x"]<3238):
		return "A"

	if(metal["m"]<1833):
		return DCK(metal)
	else:
		return CFH(metal)
def IN(metal):
	if(metal["m"]<2319):
		return HQN(metal)
	else:
		return GCX(metal)
def FMD(metal):
	if(metal["x"]<359):
		return "A"

	if(metal["a"]<3041):
		return "R"
	else:
		return "R"

def DHX(metal):
	if(metal["x"]<107):
		return "R"

	if(metal["x"]>191):
		return "R"
	else:
		return "R"

def LHL(metal):
	if(metal["m"]<837):
		return HNP(metal)
	else:
		return KBF(metal)
def RCS(metal):
	if(metal["s"]>359):
		return "A"

	if(metal["m"]<1653):
		return NVH(metal)
	else:
		return VR(metal)
def TV(metal):
	if(metal["s"]<2555):
		return "R"
	else:
		return "A"

def PBB(metal):
	if(metal["s"]>2718):
		return DH(metal)

	if(metal["a"]<2787):
		return HX(metal)

	if(metal["s"]>2206):
		return FT(metal)
	else:
		return HGN(metal)
def JH(metal):
	if(metal["s"]<2561):
		return GQ(metal)

	if(metal["x"]>1586):
		return BZ(metal)
	else:
		return ZBP(metal)
def VPM(metal):
	if(metal["m"]>343):
		return "R"

	if(metal["m"]>142):
		return "A"

	if(metal["x"]<855):
		return "A"
	else:
		return "R"

def JG(metal):
	if(metal["a"]<3444):
		return "A"

	if(metal["s"]<2055):
		return "R"
	else:
		return "R"

def ZH(metal):
	if(metal["x"]<2198):
		return "A"

	if(metal["s"]>3185):
		return "A"
	else:
		return "A"

def DJ(metal):
	if(metal["x"]>3152):
		return XDQ(metal)

	if(metal["a"]<3437):
		return "A"

	if(metal["s"]<2026):
		return "A"
	else:
		return "A"

def RKG(metal):
	if(metal["m"]<1540):
		return NCR(metal)

	if(metal["a"]<2987):
		return NSZ(metal)
	else:
		return "R"

def HX(metal):
	if(metal["s"]<2253):
		return "R"

	if(metal["s"]<2549):
		return XB(metal)

	if(metal["s"]>2630):
		return "A"
	else:
		return TM(metal)
def ZT(metal):
	if(metal["m"]<2724):
		return SFZ(metal)

	if(metal["a"]<1257):
		return JC(metal)

	if(metal["m"]<2807):
		return GJ(metal)
	else:
		return NM(metal)
def MSZ(metal):
	if(metal["x"]<108):
		return "R"

	if(metal["m"]>106):
		return "A"
	else:
		return "R"

def FZT(metal):
	if(metal["x"]>2661):
		return FD(metal)

	if(metal["m"]<910):
		return PR(metal)
	else:
		return CLJ(metal)
def PVR(metal):
	if(metal["s"]>622):
		return "A"
	else:
		return "A"

def JB(metal):
	if(metal["m"]<1468):
		return "A"
	else:
		return VP(metal)
def MC(metal):
	if(metal["x"]<908):
		return LV(metal)

	if(metal["m"]>2609):
		return "A"

	if(metal["s"]<1191):
		return ZG(metal)
	else:
		return "A"

def MN(metal):
	if(metal["a"]<2864):
		return "A"
	else:
		return FMD(metal)
def RMF(metal):
	if(metal["x"]>951):
		return ZX(metal)

	if(metal["s"]<1352):
		return LXF(metal)

	if(metal["s"]<1561):
		return HQZ(metal)
	else:
		return PMD(metal)
def SC(metal):
	if(metal["a"]>1183):
		return "R"

	if(metal["x"]>2364):
		return "R"

	if(metal["m"]>884):
		return "R"
	else:
		return "A"

def VNM(metal):
	if(metal["s"]>1099):
		return "R"

	if(metal["a"]<3335):
		return "R"
	else:
		return "A"

def VSQ(metal):
	if(metal["s"]>2505):
		return CK(metal)
	else:
		return LNG(metal)
def RFC(metal):
	if(metal["s"]<3370):
		return KVS(metal)
	else:
		return QFK(metal)
def GF(metal):
	if(metal["x"]<3502):
		return "A"

	if(metal["x"]<3768):
		return "R"
	else:
		return "R"

def SKN(metal):
	if(metal["a"]>765):
		return CJM(metal)

	if(metal["x"]<1158):
		return MK(metal)
	else:
		return "A"

def JQ(metal):
	if(metal["a"]<3441):
		return "R"

	if(metal["s"]>1088):
		return "A"

	if(metal["a"]>3715):
		return "R"
	else:
		return "A"

def CFH(metal):
	if(metal["x"]<3582):
		return "R"
	else:
		return "A"

def JFH(metal):
	if(metal["a"]<3373):
		return "R"

	if(metal["a"]>3503):
		return "A"

	if(metal["a"]<3418):
		return "A"
	else:
		return "R"

def DCK(metal):
	if(metal["a"]<697):
		return "A"

	if(metal["x"]<3704):
		return "R"

	if(metal["m"]>1602):
		return "A"
	else:
		return "A"

def QM(metal):
	if(metal["a"]<2966):
		return "A"

	if(metal["a"]>3156):
		return "R"

	if(metal["m"]>1113):
		return "A"
	else:
		return "A"

def RRZ(metal):
	if(metal["x"]<2839):
		return "R"
	else:
		return RRG(metal)
def HC(metal):
	if(metal["m"]<3403):
		return PTL(metal)

	if(metal["a"]<1344):
		return ZKR(metal)
	else:
		return QT(metal)
def NZF(metal):
	if(metal["m"]<2399):
		return "A"

	if(metal["x"]>2689):
		return "R"
	else:
		return "A"

def FP(metal):
	if(metal["a"]<3805):
		return "R"
	else:
		return "A"

def LZN(metal):
	if(metal["x"]>836):
		return SBC(metal)
	else:
		return QBP(metal)
def SF(metal):
	if(metal["m"]<2848):
		return "A"
	else:
		return "A"

def NGF(metal):
	if(metal["m"]<2674):
		return QN(metal)

	if(metal["s"]<505):
		return "R"

	if(metal["m"]>2863):
		return "A"
	else:
		return "R"

def VVN(metal):
	if(metal["a"]>3592):
		return "R"
	else:
		return "A"

def RQK(metal):
	if(metal["x"]>1812):
		return "A"

	if(metal["s"]>1402):
		return "A"

	if(metal["x"]<1809):
		return "A"
	else:
		return "A"

def MNB(metal):
	if(metal["s"]<461):
		return "A"
	else:
		return "R"

def BJ(metal):
	if(metal["m"]>3160):
		return JDL(metal)

	if(metal["x"]<3494):
		return XPR(metal)

	if(metal["x"]>3747):
		return "A"
	else:
		return LX(metal)
def LMZ(metal):
	if(metal["x"]>875):
		return "R"

	if(metal["a"]<2901):
		return "R"
	else:
		return "R"

def QP(metal):
	if(metal["m"]>418):
		return "A"

	if(metal["a"]<3417):
		return GLV(metal)

	if(metal["s"]<3513):
		return "A"
	else:
		return KG(metal)
def KNR(metal):
	if(metal["a"]<1878):
		return TVD(metal)

	if(metal["m"]<2897):
		return MF(metal)

	if(metal["m"]<3632):
		return BPJ(metal)
	else:
		return SL(metal)
def MQH(metal):
	if(metal["m"]<852):
		return "A"
	else:
		return "A"

def HTS(metal):
	if(metal["s"]>3442):
		return "R"
	else:
		return "R"

def RZT(metal):
	if(metal["x"]<2971):
		return QNK(metal)

	if(metal["s"]>1118):
		return GF(metal)
	else:
		return LVG(metal)
def SQN(metal):
	if(metal["m"]<2389):
		return "R"

	if(metal["a"]>833):
		return "A"

	if(metal["s"]<2656):
		return "R"
	else:
		return "A"

def DT(metal):
	if(metal["x"]<414):
		return "R"
	else:
		return "R"

def XM(metal):
	if(metal["m"]<2040):
		return KNT(metal)

	if(metal["x"]<1954):
		return QTX(metal)
	else:
		return SX(metal)
def XV(metal):
	if(metal["x"]>248):
		return DT(metal)

	if(metal["m"]>280):
		return DHX(metal)
	else:
		return MSZ(metal)
def BK(metal):
	if(metal["s"]<1602):
		return "R"

	if(metal["x"]<2734):
		return "R"

	if(metal["a"]>2930):
		return XKR(metal)
	else:
		return "A"

def FZZ(metal):
	if(metal["a"]<3356):
		return "A"
	else:
		return "A"

def NP(metal):
	if(metal["x"]<1911):
		return "R"

	if(metal["a"]>3851):
		return "R"

	if(metal["m"]>3371):
		return "R"
	else:
		return "A"

def XHN(metal):
	if(metal["x"]<758):
		return "A"

	if(metal["m"]<2051):
		return "A"
	else:
		return "R"

def VDJ(metal):
	if(metal["s"]<1196):
		return "R"

	if(metal["x"]<1321):
		return "R"

	if(metal["x"]>1643):
		return "R"
	else:
		return "R"

def CH(metal):
	if(metal["a"]>3507):
		return "R"
	else:
		return "R"

def QBZ(metal):
	if(metal["x"]<722):
		return "A"
	else:
		return "R"

def BL(metal):
	if(metal["x"]>2199):
		return "A"
	else:
		return "R"

def NT(metal):
	if(metal["m"]>3190):
		return QQP(metal)

	if(metal["m"]<2739):
		return CVB(metal)

	if(metal["x"]<2565):
		return CMT(metal)
	else:
		return "A"

def FF(metal):
	if(metal["s"]<331):
		return "A"
	else:
		return "R"

def KXR(metal):
	if(metal["m"]<616):
		return "R"
	else:
		return "A"

def JL(metal):
	if(metal["s"]<2470):
		return "R"
	else:
		return "A"

def HQZ(metal):
	if(metal["m"]>2670):
		return "R"

	if(metal["x"]>547):
		return "R"
	else:
		return "R"

def LH(metal):
	if(metal["s"]>3172):
		return "A"

	if(metal["x"]>2127):
		return "A"

	if(metal["m"]<847):
		return "R"
	else:
		return "A"

def CLJ(metal):
	if(metal["m"]<1711):
		return VVN(metal)

	if(metal["s"]>2667):
		return TQK(metal)

	if(metal["x"]<2452):
		return BPN(metal)
	else:
		return QRK(metal)
def SQQ(metal):
	if(metal["m"]>2881):
		return VMJ(metal)
	else:
		return MNS(metal)
def SK(metal):
	if(metal["m"]<2412):
		return GC(metal)

	if(metal["m"]>2486):
		return SBV(metal)

	if(metal["s"]<2720):
		return LDS(metal)
	else:
		return RN(metal)
def NSJ(metal):
	if(metal["a"]<3342):
		return RH(metal)

	if(metal["m"]<640):
		return QKD(metal)
	else:
		return PPF(metal)
def FCM(metal):
	if(metal["s"]>2549):
		return "A"

	if(metal["m"]>2349):
		return "R"

	if(metal["x"]>2427):
		return "R"
	else:
		return "A"

def PC(metal):
	if(metal["m"]<3086):
		return "A"
	else:
		return "A"

def TDG(metal):
	if(metal["x"]>2849):
		return DXS(metal)
	else:
		return GGQ(metal)
def QK(metal):
	if(metal["s"]>2756):
		return NDX(metal)

	if(metal["a"]<773):
		return XQ(metal)
	else:
		return VBQ(metal)
def RRG(metal):
	if(metal["s"]>450):
		return "R"

	if(metal["m"]>531):
		return "R"

	if(metal["s"]<234):
		return "R"
	else:
		return "A"

def MT(metal):
	if(metal["x"]>2069):
		return "A"
	else:
		return "A"

def TX(metal):
	if(metal["m"]>2891):
		return CMB(metal)

	if(metal["a"]<2054):
		return "A"

	if(metal["a"]>3101):
		return "R"
	else:
		return SDM(metal)
def RN(metal):
	if(metal["x"]>2287):
		return HNB(metal)
	else:
		return JJK(metal)
def NVH(metal):
	if(metal["s"]<144):
		return "A"

	if(metal["x"]>2909):
		return "R"

	if(metal["a"]>3613):
		return "A"
	else:
		return "R"

def PL(metal):
	if(metal["a"]>2552):
		return "R"
	else:
		return "R"

def DKP(metal):
	if(metal["s"]<2186):
		return "A"
	else:
		return "A"

def CPH(metal):
	if(metal["m"]>467):
		return "A"

	if(metal["s"]>728):
		return CH(metal)

	if(metal["s"]>596):
		return "R"
	else:
		return RQ(metal)
def LKL(metal):
	if(metal["x"]>3811):
		return "A"

	if(metal["m"]<1766):
		return "R"

	if(metal["x"]>3645):
		return "A"
	else:
		return "R"

def QRK(metal):
	if(metal["a"]>3612):
		return "R"
	else:
		return "R"

def ZX(metal):
	if(metal["x"]<1189):
		return "R"
	else:
		return "A"

def CFT(metal):
	if(metal["x"]<1736):
		return RJV(metal)

	if(metal["m"]<515):
		return NH(metal)

	if(metal["x"]>1804):
		return SV(metal)
	else:
		return JGT(metal)
def SPB(metal):
	if(metal["s"]<1106):
		return "A"
	else:
		return "A"

def MQ(metal):
	if(metal["x"]>621):
		return "R"

	if(metal["s"]>2375):
		return "R"

	if(metal["a"]>1192):
		return "R"
	else:
		return "A"

def QFK(metal):
	if(metal["x"]<2170):
		return "A"

	if(metal["s"]<3790):
		return "R"

	if(metal["m"]<2700):
		return XZK(metal)
	else:
		return "A"

def KZQ(metal):
	if(metal["m"]<1627):
		return VNM(metal)

	if(metal["x"]>1174):
		return QC(metal)
	else:
		return FND(metal)
def TB(metal):
	if(metal["a"]>2838):
		return "R"
	else:
		return "R"

def ZTB(metal):
	if(metal["a"]>878):
		return "R"

	if(metal["a"]>389):
		return "A"
	else:
		return "A"

def XPR(metal):
	if(metal["s"]<1623):
		return "A"

	if(metal["m"]>2860):
		return "A"
	else:
		return "A"

def SJZ(metal):
	if(metal["x"]>1759):
		return "A"
	else:
		return "A"

def BR(metal):
	if(metal["a"]>2698):
		return "A"
	else:
		return KKR(metal)
def XK(metal):
	if(metal["s"]>1574):
		return "A"

	if(metal["a"]>2857):
		return "A"

	if(metal["x"]<2304):
		return ZSL(metal)
	else:
		return "A"

def PMN(metal):
	if(metal["a"]<2987):
		return "A"
	else:
		return NQD(metal)
def CPB(metal):
	if(metal["s"]<2494):
		return "R"

	if(metal["s"]>3056):
		return "R"

	if(metal["s"]<2772):
		return "A"
	else:
		return "A"

def DBD(metal):
	if(metal["s"]>491):
		return ZR(metal)
	else:
		return NGX(metal)
def BXZ(metal):
	if(metal["a"]>2680):
		return QX(metal)

	if(metal["m"]<561):
		return CVM(metal)

	if(metal["m"]<746):
		return RK(metal)
	else:
		return HHJ(metal)
def QX(metal):
	if(metal["a"]>2954):
		return "R"

	if(metal["s"]>409):
		return "A"

	if(metal["a"]<2841):
		return GHG(metal)
	else:
		return ST(metal)
def RL(metal):
	if(metal["s"]<2957):
		return MRD(metal)

	if(metal["m"]<3104):
		return RFC(metal)
	else:
		return MFS(metal)
def MV(metal):
	if(metal["m"]<1137):
		return "A"

	if(metal["m"]>1179):
		return "R"

	if(metal["m"]>1151):
		return "R"
	else:
		return "A"

def TQR(metal):
	if(metal["x"]<3007):
		return DC(metal)
	else:
		return QD(metal)
def NGX(metal):
	if(metal["s"]>251):
		return GXL(metal)

	if(metal["a"]<1663):
		return SKN(metal)

	if(metal["s"]>105):
		return VCR(metal)
	else:
		return FTG(metal)
def RLH(metal):
	if(metal["x"]<1346):
		return "R"

	if(metal["s"]<3709):
		return "R"

	if(metal["m"]>3186):
		return "A"
	else:
		return "A"

def NDX(metal):
	if(metal["m"]>3460):
		return "R"
	else:
		return ZTB(metal)
def GQM(metal):
	if(metal["m"]>1694):
		return SPB(metal)
	else:
		return "A"

def TC(metal):
	if(metal["a"]<518):
		return "R"

	if(metal["s"]>3724):
		return "R"
	else:
		return "R"

def BHR(metal):
	if(metal["x"]>1170):
		return "R"
	else:
		return "R"

def KXB(metal):
	if(metal["a"]<1543):
		return VDJ(metal)

	if(metal["s"]<1033):
		return SJ(metal)
	else:
		return ZHZ(metal)
def FM(metal):
	if(metal["s"]<2431):
		return "R"
	else:
		return "R"

def GMF(metal):
	if(metal["m"]>2461):
		return "A"
	else:
		return "A"

def BJM(metal):
	if(metal["s"]>2014):
		return GX(metal)
	else:
		return TP(metal)
def KLG(metal):
	if(metal["x"]>1693):
		return "A"

	if(metal["x"]<1677):
		return "R"

	if(metal["m"]<666):
		return "A"
	else:
		return "R"

def BVS(metal):
	if(metal["m"]<2466):
		return "A"

	if(metal["m"]>2479):
		return "R"
	else:
		return "R"

def MJ(metal):
	if(metal["s"]<411):
		return DQT(metal)

	if(metal["x"]>404):
		return KHJ(metal)
	else:
		return FS(metal)
def SG(metal):
	if(metal["a"]>3654):
		return "A"

	if(metal["m"]<1608):
		return KC(metal)

	if(metal["x"]>321):
		return DB(metal)
	else:
		return GBG(metal)
def QQL(metal):
	if(metal["x"]<1435):
		return SST(metal)

	if(metal["m"]>1318):
		return QZS(metal)
	else:
		return LHX(metal)
def TS(metal):
	if(metal["m"]>1928):
		return "A"

	if(metal["x"]<1810):
		return "R"
	else:
		return "R"

def NB(metal):
	if(metal["x"]>3081):
		return "R"
	else:
		return "R"

def DQT(metal):
	if(metal["s"]>183):
		return "A"

	if(metal["a"]<2137):
		return LR(metal)

	if(metal["x"]>407):
		return NVM(metal)
	else:
		return "A"

def QH(metal):
	if(metal["x"]>1385):
		return "R"

	if(metal["x"]<760):
		return "A"

	if(metal["x"]<987):
		return "R"
	else:
		return "R"

def SGF(metal):
	if(metal["s"]>472):
		return BQ(metal)

	if(metal["s"]>210):
		return QH(metal)

	if(metal["a"]<937):
		return "R"
	else:
		return "R"

def ST(metal):
	if(metal["m"]>313):
		return "A"

	if(metal["a"]<2915):
		return "A"
	else:
		return "R"

def ZNR(metal):
	if(metal["m"]<1210):
		return "A"

	if(metal["a"]>630):
		return "R"
	else:
		return "A"

def RTC(metal):
	if(metal["a"]<3690):
		return "R"
	else:
		return NP(metal)
def XKR(metal):
	if(metal["s"]<1717):
		return "A"

	if(metal["x"]>2917):
		return "R"
	else:
		return "R"

def PTL(metal):
	if(metal["s"]>1375):
		return "A"
	else:
		return "A"

def XX(metal):
	if(metal["a"]>1588):
		return "R"

	if(metal["m"]<2541):
		return "R"

	if(metal["m"]<2556):
		return "R"
	else:
		return "A"

def QT(metal):
	if(metal["s"]>1320):
		return "R"

	if(metal["x"]>1624):
		return "R"
	else:
		return "R"

def CK(metal):
	if(metal["s"]<2668):
		return "R"

	if(metal["s"]>2798):
		return "A"
	else:
		return "R"

def LV(metal):
	if(metal["x"]>342):
		return "A"

	if(metal["m"]>2531):
		return "R"

	if(metal["s"]>1185):
		return "R"
	else:
		return "R"

def FQH(metal):
	if(metal["s"]>2528):
		return "R"
	else:
		return "A"

def QGX(metal):
	if(metal["x"]<417):
		return RGZ(metal)

	if(metal["x"]>709):
		return JM(metal)
	else:
		return "A"

def LDS(metal):
	if(metal["a"]<935):
		return ZC(metal)

	if(metal["a"]>1524):
		return KJH(metal)

	if(metal["a"]<1285):
		return ZDG(metal)
	else:
		return FVN(metal)
def PRS(metal):
	if(metal["a"]>1688):
		return GXZ(metal)
	else:
		return VHG(metal)
def RDL(metal):
	if(metal["m"]>530):
		return "R"

	if(metal["m"]>318):
		return "A"

	if(metal["a"]>3507):
		return "A"
	else:
		return "A"

def RGZ(metal):
	if(metal["s"]<798):
		return "R"

	if(metal["x"]>183):
		return "A"
	else:
		return "R"

def GL(metal):
	if(metal["m"]>555):
		return "A"

	if(metal["x"]<3803):
		return "A"

	if(metal["x"]>3911):
		return "A"
	else:
		return "R"

def CF(metal):
	if(metal["s"]>869):
		return "A"

	if(metal["x"]<3686):
		return "R"
	else:
		return "R"

def SN(metal):
	if(metal["x"]>193):
		return "R"

	if(metal["x"]>175):
		return JP(metal)
	else:
		return MCX(metal)
def KX(metal):
	if(metal["a"]>3621):
		return "R"

	if(metal["x"]<3580):
		return "R"

	if(metal["a"]>3389):
		return "R"
	else:
		return "A"

def ZGG(metal):
	if(metal["s"]>844):
		return "R"

	if(metal["x"]<948):
		return "A"
	else:
		return "A"

def XP(metal):
	if(metal["x"]>3232):
		return RD(metal)

	if(metal["x"]>2875):
		return JTM(metal)
	else:
		return DJX(metal)
def VSX(metal):
	if(metal["a"]>480):
		return "A"
	else:
		return "A"

def SV(metal):
	if(metal["x"]<1825):
		return RQK(metal)

	if(metal["s"]<1909):
		return "R"
	else:
		return "R"

def HGN(metal):
	if(metal["a"]<3015):
		return JNS(metal)

	if(metal["m"]<778):
		return "A"

	if(metal["x"]<3533):
		return "A"
	else:
		return LKL(metal)
def BD(metal):
	if(metal["a"]>3007):
		return "A"
	else:
		return "R"

def SBC(metal):
	if(metal["x"]<905):
		return SPJ(metal)

	if(metal["m"]>2991):
		return DCH(metal)

	if(metal["x"]<929):
		return "R"
	else:
		return ZGG(metal)
def LD(metal):
	if(metal["m"]>2468):
		return "A"

	if(metal["a"]<1961):
		return "A"
	else:
		return "A"

def QZ(metal):
	if(metal["a"]<1538):
		return "A"

	if(metal["x"]<587):
		return VHP(metal)

	if(metal["s"]<463):
		return FNT(metal)
	else:
		return "R"

def KG(metal):
	if(metal["s"]<3708):
		return "R"

	if(metal["x"]<3794):
		return "A"
	else:
		return "R"

def ZL(metal):
	if(metal["a"]>845):
		return RLH(metal)

	if(metal["m"]<3174):
		return "R"
	else:
		return TC(metal)
def MF(metal):
	if(metal["s"]<660):
		return "R"

	if(metal["m"]<2546):
		return "R"

	if(metal["m"]>2749):
		return "A"
	else:
		return "R"

def SFS(metal):
	if(metal["a"]>3403):
		return "A"

	if(metal["m"]>1875):
		return "R"

	if(metal["s"]>3228):
		return "A"
	else:
		return "A"

def GXL(metal):
	if(metal["s"]<365):
		return VXK(metal)

	if(metal["s"]<418):
		return "R"
	else:
		return "A"

def VT(metal):
	if(metal["s"]>1493):
		return CG(metal)
	else:
		return "A"

def PP(metal):
	if(metal["a"]>3414):
		return "R"

	if(metal["x"]<3505):
		return "R"
	else:
		return "R"

def CL(metal):
	if(metal["a"]<2823):
		return "R"

	if(metal["s"]>62):
		return "A"
	else:
		return "A"

def XF(metal):
	if(metal["a"]>3642):
		return XN(metal)
	else:
		return ZH(metal)
def CVM(metal):
	if(metal["x"]>3538):
		return XKM(metal)

	if(metal["x"]>3370):
		return XST(metal)
	else:
		return GXQ(metal)
def TP(metal):
	if(metal["m"]<1208):
		return FX(metal)

	if(metal["x"]>1999):
		return NLR(metal)

	if(metal["x"]<927):
		return PZQ(metal)
	else:
		return BPD(metal)
def DM(metal):
	if(metal["x"]>370):
		return "R"

	if(metal["x"]>136):
		return XZ(metal)

	if(metal["s"]>180):
		return HXS(metal)
	else:
		return GB(metal)
def LDK(metal):
	if(metal["a"]<3430):
		return FZZ(metal)

	if(metal["a"]>3524):
		return "A"
	else:
		return LGX(metal)
def KTV(metal):
	if(metal["a"]>3015):
		return "A"
	else:
		return "R"

def FS(metal):
	if(metal["a"]<1565):
		return DCG(metal)
	else:
		return "A"

def CJM(metal):
	if(metal["s"]>145):
		return "R"

	if(metal["s"]>52):
		return "R"

	if(metal["a"]>1326):
		return "A"
	else:
		return "R"

def VHG(metal):
	if(metal["m"]>3219):
		return "A"
	else:
		return PRD(metal)
def KP(metal):
	if(metal["a"]<2689):
		return VQJ(metal)

	if(metal["a"]<3052):
		return BBK(metal)
	else:
		return HTS(metal)
def RDZ(metal):
	if(metal["m"]<3223):
		return TZ(metal)

	if(metal["x"]<224):
		return LTG(metal)
	else:
		return MJ(metal)
def XKM(metal):
	if(metal["m"]>294):
		return "R"
	else:
		return "A"

def DXS(metal):
	if(metal["m"]<2735):
		return "R"
	else:
		return SF(metal)
def ZXR(metal):
	if(metal["x"]<2226):
		return "R"
	else:
		return "R"

def RK(metal):
	if(metal["x"]<3654):
		return PVR(metal)

	if(metal["a"]<2590):
		return LFQ(metal)

	if(metal["m"]>680):
		return "R"
	else:
		return KXR(metal)
def HNB(metal):
	if(metal["m"]<2440):
		return GJF(metal)
	else:
		return "A"

def XMJ(metal):
	if(metal["a"]>2809):
		return "R"

	if(metal["a"]<2710):
		return "R"
	else:
		return "A"

def ZHZ(metal):
	if(metal["x"]>1335):
		return "R"
	else:
		return "A"

def RM(metal):
	if(metal["s"]<2906):
		return "A"

	if(metal["a"]<1097):
		return "A"
	else:
		return "A"

def GS(metal):
	if(metal["s"]>618):
		return "R"

	if(metal["a"]>1306):
		return "A"
	else:
		return FFG(metal)
def PR(metal):
	if(metal["m"]>597):
		return "A"
	else:
		return "A"

def CG(metal):
	if(metal["a"]<1668):
		return "A"

	if(metal["m"]<2602):
		return "A"

	if(metal["m"]>2753):
		return "A"
	else:
		return "R"

def KJH(metal):
	if(metal["a"]<1795):
		return TNS(metal)

	if(metal["m"]<2454):
		return "R"

	if(metal["a"]<1894):
		return MMP(metal)
	else:
		return LD(metal)
def VMJ(metal):
	if(metal["a"]>911):
		return HC(metal)

	if(metal["x"]<1742):
		return PX(metal)

	if(metal["a"]<468):
		return LFH(metal)
	else:
		return CTP(metal)
def JR(metal):
	if(metal["s"]>1089):
		return DNN(metal)
	else:
		return SVD(metal)
def SL(metal):
	if(metal["m"]<3860):
		return QJ(metal)

	if(metal["s"]>533):
		return "R"
	else:
		return "A"

def DG(metal):
	if(metal["m"]>480):
		return "A"
	else:
		return "R"

def VHP(metal):
	if(metal["a"]>1986):
		return "R"

	if(metal["m"]>2260):
		return "A"

	if(metal["x"]<207):
		return "A"
	else:
		return "A"

def BPN(metal):
	if(metal["s"]>2180):
		return "A"
	else:
		return "R"

def GP(metal):
	if(metal["a"]<3007):
		return FM(metal)
	else:
		return FQH(metal)
def HSN(metal):
	if(metal["m"]>233):
		return "R"
	else:
		return "A"

def CFR(metal):
	if(metal["a"]>3816):
		return "A"

	if(metal["x"]<3746):
		return "R"
	else:
		return "R"

def VR(metal):
	if(metal["s"]<208):
		return "R"

	if(metal["x"]>3073):
		return "R"

	if(metal["a"]>3675):
		return "A"
	else:
		return "A"

def HJQ(metal):
	if(metal["x"]<2261):
		return ZT(metal)
	else:
		return TDG(metal)
def XS(metal):
	if(metal["a"]<2789):
		return "A"
	else:
		return "A"

def BV(metal):
	if(metal["x"]<1363):
		return "A"

	if(metal["m"]<3020):
		return "R"

	if(metal["s"]>2415):
		return "A"
	else:
		return "A"

def JS(metal):
	if(metal["s"]>3075):
		return "R"

	if(metal["s"]>2295):
		return XT(metal)
	else:
		return XX(metal)
def BJF(metal):
	if(metal["a"]<3063):
		return "R"

	if(metal["x"]<1285):
		return "A"

	if(metal["s"]<781):
		return "R"
	else:
		return "R"

def DCH(metal):
	if(metal["s"]<768):
		return "R"

	if(metal["m"]<3474):
		return "A"

	if(metal["a"]>1745):
		return "R"
	else:
		return "R"

def XN(metal):
	if(metal["x"]<1811):
		return "A"

	if(metal["a"]<3781):
		return "A"

	if(metal["x"]>3212):
		return "R"
	else:
		return "R"

def MCZ(metal):
	if(metal["x"]<2047):
		return QQ(metal)

	if(metal["x"]>3098):
		return BJ(metal)

	if(metal["x"]<2483):
		return XK(metal)
	else:
		return BK(metal)
def MJB(metal):
	if(metal["m"]>3716):
		return "R"

	if(metal["a"]<1749):
		return "A"

	if(metal["s"]>378):
		return "A"
	else:
		return "A"

def BH(metal):
	if(metal["a"]>2047):
		return RL(metal)

	if(metal["m"]>2924):
		return HL(metal)

	if(metal["m"]>2577):
		return HJQ(metal)
	else:
		return SK(metal)
def CXF(metal):
	if(metal["s"]>1991):
		return "R"
	else:
		return "A"

def MMX(metal):
	if(metal["a"]<700):
		return "R"

	if(metal["s"]<3690):
		return "A"
	else:
		return "A"

def PHT(metal):
	if(metal["m"]>2343):
		return FCM(metal)

	if(metal["a"]<1565):
		return QZD(metal)

	if(metal["s"]<3225):
		return SLS(metal)
	else:
		return "R"

def NM(metal):
	if(metal["s"]>3143):
		return "R"
	else:
		return TSH(metal)
def TR(metal):
	if(metal["m"]>1907):
		return LF(metal)

	if(metal["m"]>1572):
		return "R"

	if(metal["x"]>3149):
		return "R"
	else:
		return "R"

def KM(metal):
	if(metal["a"]<551):
		return "A"

	if(metal["x"]>2529):
		return "A"
	else:
		return "R"

def GB(metal):
	if(metal["x"]<91):
		return "R"

	if(metal["x"]>109):
		return "A"
	else:
		return "A"

def TCJ(metal):
	if(metal["x"]>1369):
		return "R"

	if(metal["x"]>1299):
		return "R"

	if(metal["x"]<1273):
		return "A"
	else:
		return "A"

def VSM(metal):
	if(metal["a"]>1248):
		return "A"
	else:
		return "A"

def LRG(metal):
	if(metal["s"]>3071):
		return CC(metal)
	else:
		return SC(metal)
def ZSL(metal):
	if(metal["m"]<3319):
		return "A"
	else:
		return "R"

def RLP(metal):
	if(metal["x"]>1447):
		return FQ(metal)

	if(metal["x"]<664):
		return RDZ(metal)

	if(metal["x"]>969):
		return DBD(metal)
	else:
		return HDH(metal)
def SDM(metal):
	if(metal["x"]>400):
		return "R"

	if(metal["s"]<405):
		return "R"

	if(metal["m"]>2635):
		return "A"
	else:
		return "A"

def GLV(metal):
	if(metal["x"]<3730):
		return "A"
	else:
		return "R"

def LJ(metal):
	if(metal["s"]<1546):
		return "A"

	if(metal["s"]>1676):
		return "A"

	if(metal["m"]>3698):
		return "A"
	else:
		return "R"

def MH(metal):
	if(metal["a"]<918):
		return "R"
	else:
		return "A"

def RBQ(metal):
	if(metal["s"]>3266):
		return "A"

	if(metal["a"]<3014):
		return "A"
	else:
		return "A"

def LR(metal):
	if(metal["s"]>83):
		return "A"
	else:
		return "A"

def ZTG(metal):
	if(metal["m"]>2791):
		return "R"
	else:
		return "R"

def HDH(metal):
	if(metal["s"]<584):
		return ZQ(metal)
	else:
		return LZN(metal)
def ZQ(metal):
	if(metal["x"]<782):
		return MZS(metal)

	if(metal["s"]>227):
		return GBM(metal)

	if(metal["s"]<118):
		return ZPM(metal)
	else:
		return GLB(metal)
def PRD(metal):
	if(metal["a"]>600):
		return "R"
	else:
		return "A"

def FFC(metal):
	if(metal["m"]>2132):
		return "A"
	else:
		return "A"

def NK(metal):
	if(metal["s"]>3514):
		return "A"

	if(metal["x"]<3755):
		return "A"
	else:
		return "A"

def GCX(metal):
	if(metal["s"]>1810):
		return BH(metal)

	if(metal["s"]>1023):
		return LM(metal)
	else:
		return RLP(metal)
def ZR(metal):
	if(metal["a"]<2128):
		return DQP(metal)
	else:
		return BJF(metal)
def GJ(metal):
	if(metal["m"]<2772):
		return ZHM(metal)

	if(metal["s"]<2706):
		return ZTG(metal)
	else:
		return "A"

def PMD(metal):
	if(metal["s"]<1687):
		return "A"

	if(metal["m"]>2527):
		return "A"

	if(metal["a"]>555):
		return "A"
	else:
		return "R"

def JJK(metal):
	if(metal["m"]>2443):
		return BVS(metal)
	else:
		return "A"

def SPJ(metal):
	if(metal["m"]<3148):
		return "A"
	else:
		return "A"

def QB(metal):
	if(metal["s"]<370):
		return "R"

	if(metal["x"]>709):
		return "R"
	else:
		return "A"

def DBR(metal):
	if(metal["x"]<2064):
		return "R"
	else:
		return CKL(metal)
def GMT(metal):
	if(metal["x"]<70):
		return "R"
	else:
		return MJB(metal)
def NNH(metal):
	if(metal["s"]<3292):
		return "A"

	if(metal["x"]>3387):
		return "R"
	else:
		return "R"

def TD(metal):
	if(metal["x"]>3056):
		return "R"

	if(metal["x"]>2710):
		return "A"
	else:
		return "R"

def DZ(metal):
	if(metal["a"]<3652):
		return "R"

	if(metal["m"]<202):
		return "R"

	if(metal["a"]<3832):
		return "R"
	else:
		return "R"

def DX(metal):
	if(metal["x"]>2870):
		return "R"

	if(metal["m"]<2531):
		return "A"

	if(metal["x"]<2399):
		return "R"
	else:
		return "R"

def TT(metal):
	if(metal["s"]>100):
		return "R"

	if(metal["m"]<1645):
		return "R"
	else:
		return "A"

def JZ(metal):
	if(metal["s"]<214):
		return "A"

	if(metal["s"]<237):
		return "A"

	if(metal["x"]>1271):
		return "A"
	else:
		return "A"

def CMT(metal):
	if(metal["s"]>1258):
		return "A"

	if(metal["s"]>1245):
		return "R"
	else:
		return "R"

def KVS(metal):
	if(metal["m"]<2760):
		return ZXR(metal)

	if(metal["s"]<3201):
		return "A"

	if(metal["x"]>2030):
		return NKZ(metal)
	else:
		return RBQ(metal)
def HKV(metal):
	if(metal["m"]<2706):
		return JSN(metal)

	if(metal["x"]<186):
		return "R"
	else:
		return "A"

def RQ(metal):
	if(metal["a"]>3646):
		return "A"
	else:
		return "A"

def XZ(metal):
	if(metal["a"]>3868):
		return "A"

	if(metal["m"]>454):
		return "R"
	else:
		return "A"

def MFS(metal):
	if(metal["a"]<3298):
		return KP(metal)

	if(metal["s"]<3437):
		return XF(metal)
	else:
		return BBP(metal)
def BBP(metal):
	if(metal["x"]<1840):
		return "A"

	if(metal["x"]>2935):
		return "R"
	else:
		return SBJ(metal)
def HLN(metal):
	if(metal["m"]>2906):
		return BV(metal)

	if(metal["s"]<2210):
		return SHV(metal)

	if(metal["s"]<2488):
		return BD(metal)
	else:
		return "A"

def MRD(metal):
	if(metal["m"]>3208):
		return VSQ(metal)

	if(metal["m"]>2743):
		return HLN(metal)
	else:
		return GP(metal)
def TQB(metal):
	if(metal["a"]>3812):
		return "A"

	if(metal["a"]<3705):
		return "A"
	else:
		return "A"

def RD(metal):
	if(metal["s"]>2949):
		return "R"

	if(metal["a"]<952):
		return RJ(metal)

	if(metal["m"]>1000):
		return "A"
	else:
		return "A"

def SJ(metal):
	if(metal["x"]<1391):
		return "A"

	if(metal["s"]>531):
		return "R"

	if(metal["m"]<1991):
		return "A"
	else:
		return "A"

def BZ(metal):
	if(metal["m"]<856):
		return "A"

	if(metal["s"]>3162):
		return "R"

	if(metal["x"]>1637):
		return "R"
	else:
		return CS(metal)
def FR(metal):
	if(metal["m"]<488):
		return DZ(metal)

	if(metal["m"]>688):
		return MQH(metal)
	else:
		return GL(metal)
def SFZ(metal):
	if(metal["s"]<3265):
		return BX(metal)
	else:
		return MMX(metal)
def SX(metal):
	if(metal["a"]>3250):
		return LP(metal)
	else:
		return "A"

def QKD(metal):
	if(metal["m"]>502):
		return "A"

	if(metal["m"]>465):
		return "A"
	else:
		return "A"

def FFT(metal):
	if(metal["m"]<1448):
		return BR(metal)
	else:
		return VNQ(metal)
def LTH(metal):
	if(metal["x"]>1414):
		return "R"

	if(metal["a"]<200):
		return "R"

	if(metal["x"]>656):
		return "A"
	else:
		return "R"

def PPZ(metal):
	if(metal["s"]>1019):
		return DF(metal)

	if(metal["a"]>3107):
		return SQ(metal)

	if(metal["x"]<3125):
		return TCC(metal)
	else:
		return BXZ(metal)
def JDL(metal):
	if(metal["a"]>3100):
		return "A"
	else:
		return "R"

def NZ(metal):
	if(metal["x"]<1802):
		return CVV(metal)

	if(metal["x"]<2151):
		return HZ(metal)
	else:
		return LRG(metal)
def SQ(metal):
	if(metal["s"]>487):
		return CPH(metal)

	if(metal["s"]<208):
		return QQQ(metal)
	else:
		return LQZ(metal)
def RH(metal):
	if(metal["a"]>2988):
		return "A"

	if(metal["a"]>2717):
		return "A"
	else:
		return "A"

def QC(metal):
	if(metal["x"]>1297):
		return "A"

	if(metal["x"]>1237):
		return "R"

	if(metal["m"]>2052):
		return "R"
	else:
		return "R"

def GQ(metal):
	if(metal["a"]<3385):
		return HJ(metal)

	if(metal["a"]<3653):
		return DG(metal)
	else:
		return "R"

def VCR(metal):
	if(metal["s"]<164):
		return DFN(metal)

	if(metal["a"]>3066):
		return JZ(metal)

	if(metal["a"]<2547):
		return RX(metal)
	else:
		return XMJ(metal)
def CBZ(metal):
	if(metal["s"]<2435):
		return "A"

	if(metal["a"]<1101):
		return "R"
	else:
		return "R"

def CKL(metal):
	if(metal["x"]<2164):
		return "R"

	if(metal["x"]>2223):
		return "A"

	if(metal["a"]<2867):
		return "A"
	else:
		return "R"

def KC(metal):
	if(metal["m"]<1226):
		return "R"

	if(metal["m"]<1417):
		return "A"

	if(metal["s"]<249):
		return "A"
	else:
		return "A"

def GBG(metal):
	if(metal["m"]>2033):
		return "R"

	if(metal["a"]>3449):
		return "A"
	else:
		return "R"

def NL(metal):
	if(metal["x"]<867):
		return "R"

	if(metal["s"]<95):
		return "A"

	if(metal["x"]>913):
		return "A"
	else:
		return "R"

def JC(metal):
	if(metal["a"]>564):
		return "A"

	if(metal["s"]<3164):
		return LTH(metal)
	else:
		return FK(metal)
def GHG(metal):
	if(metal["x"]>3699):
		return "R"
	else:
		return "R"

def PGX(metal):
	if(metal["m"]<526):
		return HSN(metal)
	else:
		return ZRM(metal)
def LM(metal):
	if(metal["a"]<2173):
		return SQQ(metal)
	else:
		return RC(metal)
def HHJ(metal):
	if(metal["s"]>555):
		return PB(metal)

	if(metal["x"]>3691):
		return "A"

	if(metal["m"]<856):
		return MRK(metal)
	else:
		return PL(metal)
def GK(metal):
	if(metal["a"]<670):
		return "R"

	if(metal["m"]<3301):
		return "R"
	else:
		return "R"

def JGT(metal):
	if(metal["a"]>3287):
		return "R"

	if(metal["s"]>1669):
		return "R"

	if(metal["m"]>787):
		return "A"
	else:
		return "A"

def PG(metal):
	if(metal["a"]<628):
		return "A"
	else:
		return "A"

def GLB(metal):
	if(metal["m"]<3381):
		return "A"
	else:
		return "R"

def FK(metal):
	if(metal["a"]<278):
		return "R"

	if(metal["m"]>2835):
		return "A"

	if(metal["x"]<1081):
		return "A"
	else:
		return "A"

def SMN(metal):
	if(metal["a"]>3531):
		return "R"

	if(metal["x"]>1652):
		return "R"

	if(metal["x"]<1509):
		return "A"
	else:
		return "R"

def MZS(metal):
	if(metal["m"]>3099):
		return "R"

	if(metal["m"]>2652):
		return QBZ(metal)

	if(metal["a"]>1684):
		return XR(metal)
	else:
		return QB(metal)
def ZV(metal):
	if(metal["m"]<1635):
		return "R"
	else:
		return "A"

def KNT(metal):
	if(metal["s"]<2108):
		return TS(metal)

	if(metal["m"]>1912):
		return "A"

	if(metal["x"]<1913):
		return "R"
	else:
		return "A"

def JP(metal):
	if(metal["s"]>234):
		return "A"
	else:
		return "A"

def SXN(metal):
	if(metal["s"]<2354):
		return CXF(metal)
	else:
		return LH(metal)
def DVT(metal):
	if(metal["x"]<3345):
		return HMD(metal)
	else:
		return "A"

def TBN(metal):
	if(metal["x"]>2935):
		return SDP(metal)
	else:
		return VBC(metal)
def FPX(metal):
	if(metal["s"]>1347):
		return SXN(metal)

	if(metal["a"]<3190):
		return DBR(metal)
	else:
		return DPR(metal)
def TNS(metal):
	if(metal["a"]>1653):
		return "A"

	if(metal["a"]<1584):
		return "A"
	else:
		return "A"

def ZKR(metal):
	if(metal["x"]>2512):
		return "R"
	else:
		return "R"

def XL(metal):
	if(metal["x"]<3360):
		return "A"

	if(metal["x"]<3415):
		return "R"
	else:
		return "A"

def RX(metal):
	if(metal["a"]<2102):
		return "R"

	if(metal["s"]>206):
		return "A"

	if(metal["m"]<3036):
		return "R"
	else:
		return "R"

def QTX(metal):
	if(metal["s"]>2342):
		return QJM(metal)

	if(metal["m"]<2175):
		return "A"

	if(metal["s"]<1137):
		return "A"
	else:
		return BP(metal)
def LHX(metal):
	if(metal["x"]>1839):
		return FPX(metal)

	if(metal["x"]>1662):
		return CFT(metal)
	else:
		return JH(metal)
def BX(metal):
	if(metal["m"]<2654):
		return "A"
	else:
		return "R"

def FDL(metal):
	if(metal["m"]>344):
		return "R"
	else:
		return "R"

def JD(metal):
	if(metal["s"]<874):
		return "A"

	if(metal["s"]<1113):
		return QM(metal)

	if(metal["x"]<379):
		return "A"
	else:
		return "R"

def LFH(metal):
	if(metal["m"]>3307):
		return LJ(metal)
	else:
		return SCR(metal)
def HF(metal):
	if(metal["m"]<1439):
		return PZ(metal)

	if(metal["x"]<450):
		return "A"
	else:
		return "R"

def NLR(metal):
	if(metal["a"]>953):
		return KMT(metal)

	if(metal["a"]<561):
		return QV(metal)

	if(metal["x"]>2707):
		return XD(metal)
	else:
		return SFJ(metal)
def VD(metal):
	if(metal["m"]<3322):
		return ZL(metal)

	if(metal["m"]>3700):
		return SZ(metal)
	else:
		return BM(metal)
def JM(metal):
	if(metal["s"]>1234):
		return "R"

	if(metal["a"]>1053):
		return "A"
	else:
		return "A"

def QF(metal):
	if(metal["a"]<2912):
		return "A"

	if(metal["m"]<1484):
		return "A"

	if(metal["s"]>2424):
		return "A"
	else:
		return "A"

def TM(metal):
	if(metal["x"]>3486):
		return "R"
	else:
		return "R"

def DJD(metal):
	if(metal["x"]<2571):
		return "A"

	if(metal["m"]<1931):
		return "A"

	if(metal["m"]>2159):
		return "A"
	else:
		return "A"

def XB(metal):
	if(metal["x"]<3393):
		return "A"

	if(metal["s"]>2359):
		return "A"
	else:
		return "R"

def FFG(metal):
	if(metal["a"]>828):
		return "R"
	else:
		return "R"

def HB(metal):
	if(metal["x"]>513):
		return XHN(metal)
	else:
		return FF(metal)
def TN(metal):
	if(metal["s"]>2834):
		return "R"

	if(metal["m"]>821):
		return "R"

	if(metal["s"]<2377):
		return "R"
	else:
		return "R"

def ZDG(metal):
	if(metal["s"]<2280):
		return "A"
	else:
		return CBZ(metal)
def GGQ(metal):
	if(metal["a"]<725):
		return "R"

	if(metal["x"]>2465):
		return "R"
	else:
		return HHG(metal)
def QQP(metal):
	if(metal["a"]>3755):
		return "R"
	else:
		return "A"

def GN(metal):
	if(metal["a"]<769):
		return "R"

	if(metal["x"]>965):
		return "R"

	if(metal["a"]>861):
		return "R"
	else:
		return "R"

def LNG(metal):
	if(metal["m"]>3597):
		return "R"

	if(metal["m"]<3461):
		return "R"

	if(metal["a"]<3221):
		return "A"
	else:
		return "A"

def LP(metal):
	if(metal["x"]>2196):
		return "R"

	if(metal["s"]>1463):
		return "A"
	else:
		return "A"

def XVL(metal):
	if(metal["s"]>1915):
		return "A"

	if(metal["x"]>1611):
		return BPT(metal)
	else:
		return FP(metal)
def KBF(metal):
	if(metal["s"]>3033):
		return "A"

	if(metal["s"]<2370):
		return "R"

	if(metal["m"]>1333):
		return "R"
	else:
		return "R"

def BM(metal):
	if(metal["a"]>744):
		return MXK(metal)
	else:
		return "A"

def HHG(metal):
	if(metal["x"]<2370):
		return "A"

	if(metal["s"]>2677):
		return "A"

	if(metal["a"]<1282):
		return "R"
	else:
		return "R"

def FTG(metal):
	if(metal["m"]<3403):
		return CL(metal)

	if(metal["a"]<2890):
		return BHR(metal)
	else:
		return KSZ(metal)
def CTP(metal):
	if(metal["s"]>1319):
		return "R"

	if(metal["s"]<1191):
		return "A"
	else:
		return GK(metal)
def HBL(metal):
	if(metal["s"]>497):
		return JD(metal)

	if(metal["s"]>278):
		return GFP(metal)
	else:
		return MN(metal)
def DCG(metal):
	if(metal["s"]>725):
		return "R"
	else:
		return "A"

def PX(metal):
	if(metal["m"]<3557):
		return "A"
	else:
		return LSQ(metal)
def FX(metal):
	if(metal["s"]>948):
		return PGX(metal)

	if(metal["m"]>797):
		return ZZH(metal)

	if(metal["m"]<374):
		return SGF(metal)
	else:
		return GS(metal)
def FD(metal):
	if(metal["x"]<2823):
		return "A"

	if(metal["s"]>2497):
		return "R"
	else:
		return RF(metal)
def LVG(metal):
	if(metal["x"]<3616):
		return "R"

	if(metal["m"]<3033):
		return "R"

	if(metal["s"]>1098):
		return "A"
	else:
		return "A"

def RJ(metal):
	if(metal["a"]<475):
		return "R"

	if(metal["a"]<752):
		return "A"

	if(metal["x"]<3524):
		return "R"
	else:
		return "R"

def DJL(metal):
	if(metal["m"]>2966):
		return "A"

	if(metal["a"]>3785):
		return "A"

	if(metal["x"]>1341):
		return "A"
	else:
		return "R"

def JTM(metal):
	if(metal["m"]<1048):
		return "A"
	else:
		return MH(metal)
def MMP(metal):
	if(metal["m"]>2470):
		return "R"
	else:
		return "A"

def KMT(metal):
	if(metal["a"]>1670):
		return "A"
	else:
		return VSM(metal)
def NPF(metal):
	if(metal["s"]<3688):
		return "R"

	if(metal["a"]>549):
		return "R"
	else:
		return "A"

def PPF(metal):
	if(metal["a"]>3580):
		return "A"

	if(metal["a"]<3436):
		return "A"
	else:
		return "A"

def NDQ(metal):
	if(metal["m"]<588):
		return "A"
	else:
		return "R"

def GC(metal):
	if(metal["m"]>2357):
		return ZJP(metal)

	if(metal["a"]<965):
		return STG(metal)
	else:
		return PHT(metal)
def FQ(metal):
	if(metal["x"]>2971):
		return PRS(metal)
	else:
		return KNR(metal)
def MXK(metal):
	if(metal["m"]<3467):
		return "R"

	if(metal["s"]<3498):
		return "R"
	else:
		return "A"

def QZS(metal):
	if(metal["m"]>1825):
		return XM(metal)
	else:
		return NQP(metal)
def BQ(metal):
	if(metal["a"]>892):
		return "R"
	else:
		return "A"

def QV(metal):
	if(metal["s"]<948):
		return ZV(metal)

	if(metal["m"]<1792):
		return "A"
	else:
		return FFC(metal)
def DJX(metal):
	if(metal["a"]>1069):
		return "R"

	if(metal["s"]<2984):
		return ZNR(metal)
	else:
		return ZLN(metal)
def CMB(metal):
	if(metal["a"]>2171):
		return "R"

	if(metal["s"]>607):
		return "R"
	else:
		return "A"

def QQQ(metal):
	if(metal["s"]<97):
		return "R"

	if(metal["a"]<3554):
		return "A"
	else:
		return "R"

def CJK(metal):
	if(metal["x"]>3311):
		return "R"
	else:
		return "R"

def SHV(metal):
	if(metal["s"]>1975):
		return "A"
	else:
		return "A"

def CR(metal):
	if(metal["a"]<3757):
		return "A"
	else:
		return "A"

def DB(metal):
	if(metal["x"]<467):
		return "A"

	if(metal["a"]>3491):
		return "R"

	if(metal["x"]>603):
		return "R"
	else:
		return "R"

def NVM(metal):
	if(metal["m"]>3599):
		return "R"

	if(metal["s"]<107):
		return "A"
	else:
		return "A"

def LSQ(metal):
	if(metal["x"]<972):
		return "A"

	if(metal["x"]<1326):
		return "R"

	if(metal["m"]>3708):
		return "A"
	else:
		return "R"

def TK(metal):
	if(metal["m"]<1343):
		return JQN(metal)

	if(metal["s"]<3104):
		return TR(metal)

	if(metal["x"]<3129):
		return TQR(metal)
	else:
		return CJK(metal)
def LTG(metal):
	if(metal["x"]<144):
		return GMT(metal)

	if(metal["s"]>648):
		return SJK(metal)
	else:
		return SN(metal)
def VQJ(metal):
	if(metal["a"]<2347):
		return "R"
	else:
		return "A"

def KKR(metal):
	if(metal["s"]<2448):
		return "R"

	if(metal["s"]>2988):
		return "R"

	if(metal["m"]>817):
		return "R"
	else:
		return "R"

def DFN(metal):
	if(metal["m"]<3232):
		return "R"
	else:
		return "R"

def NFV(metal):
	if(metal["m"]<3643):
		return "R"

	if(metal["m"]>3778):
		return "A"

	if(metal["m"]>3695):
		return "A"
	else:
		return "R"

def XDQ(metal):
	if(metal["m"]>966):
		return "R"

	if(metal["s"]>2058):
		return "A"

	if(metal["s"]>1829):
		return "A"
	else:
		return "A"

def SBJ(metal):
	if(metal["s"]>3663):
		return "A"
	else:
		return "R"

def HQN(metal):
	if(metal["a"]<2457):
		return BJM(metal)

	if(metal["x"]<2335):
		return QQL(metal)

	if(metal["s"]>1648):
		return TBN(metal)
	else:
		return TGG(metal)
def PKH(metal):
	if(metal["m"]<2545):
		return DX(metal)
	else:
		return VLH(metal)
def TSH(metal):
	if(metal["a"]<1720):
		return "R"
	else:
		return "R"

def LQZ(metal):
	if(metal["m"]<369):
		return TD(metal)

	if(metal["x"]<3015):
		return "A"

	if(metal["a"]>3642):
		return "R"
	else:
		return PP(metal)
def QD(metal):
	if(metal["s"]>3582):
		return "A"
	else:
		return "R"

def BVD(metal):
	if(metal["s"]<844):
		return DGD(metal)
	else:
		return ZJ(metal)
def VF(metal):
	if(metal["m"]>2442):
		return "A"

	if(metal["a"]<429):
		return "A"

	if(metal["a"]>765):
		return "A"
	else:
		return "R"

def BBK(metal):
	if(metal["a"]>2913):
		return "R"

	if(metal["x"]>1674):
		return "A"

	if(metal["m"]<3478):
		return "A"
	else:
		return "R"

def GFP(metal):
	if(metal["x"]<260):
		return NX(metal)
	else:
		return XS(metal)
def JSN(metal):
	if(metal["s"]<481):
		return "R"

	if(metal["m"]>2509):
		return "A"
	else:
		return "A"

def HM(metal):
	if(metal["m"]<2516):
		return NZF(metal)
	else:
		return NQ(metal)
def QNK(metal):
	if(metal["x"]>2773):
		return "R"

	if(metal["s"]<1113):
		return "R"

	if(metal["m"]<3103):
		return "A"
	else:
		return "A"

def ZJP(metal):
	if(metal["m"]<2387):
		return RM(metal)

	if(metal["m"]>2396):
		return "A"

	if(metal["m"]>2391):
		return "R"
	else:
		return SQN(metal)
def QJM(metal):
	if(metal["a"]>3026):
		return "A"

	if(metal["m"]>2167):
		return "A"
	else:
		return "A"

def GBM(metal):
	if(metal["m"]>3204):
		return RGF(metal)
	else:
		return DR(metal)
def VP(metal):
	if(metal["m"]<1879):
		return "A"

	if(metal["a"]>3733):
		return "R"

	if(metal["m"]<2030):
		return "A"
	else:
		return "A"

def ZJ(metal):
	if(metal["s"]>1327):
		return CM(metal)
	else:
		return GQM(metal)
def ZK(metal):
	if(metal["x"]<774):
		return "A"
	else:
		return "R"

def LX(metal):
	if(metal["s"]<1528):
		return "A"

	if(metal["x"]<3653):
		return "R"
	else:
		return "A"

def ZZH(metal):
	if(metal["m"]<1012):
		return KV(metal)
	else:
		return MV(metal)
def GD(metal):
	if(metal["s"]<1380):
		return "R"

	if(metal["x"]<283):
		return "R"

	if(metal["a"]<1736):
		return "R"
	else:
		return "R"

def JQN(metal):
	if(metal["x"]<3234):
		return TQB(metal)
	else:
		return XL(metal)
def CVV(metal):
	if(metal["x"]<1600):
		return "R"

	if(metal["s"]<2932):
		return "R"
	else:
		return "A"

def HMD(metal):
	if(metal["x"]<2704):
		return "A"
	else:
		return "R"

def XT(metal):
	if(metal["m"]<2557):
		return "R"
	else:
		return "A"

def XZK(metal):
	if(metal["m"]>2542):
		return "R"

	if(metal["s"]>3909):
		return "A"
	else:
		return "A"

def MNS(metal):
	if(metal["x"]>1485):
		return HM(metal)

	if(metal["a"]<1229):
		return RMF(metal)

	if(metal["s"]<1321):
		return MC(metal)
	else:
		return VT(metal)
def TH(metal):
	if(metal["m"]>791):
		return "R"

	if(metal["x"]>2020):
		return "R"

	if(metal["s"]>2503):
		return "R"
	else:
		return "R"

def TXZ(metal):
	if(metal["a"]>1202):
		return "R"
	else:
		return "R"

def LF(metal):
	if(metal["a"]<3790):
		return "R"

	if(metal["s"]<2230):
		return "A"
	else:
		return "R"

def LXF(metal):
	if(metal["x"]>401):
		return "A"

	if(metal["m"]>2570):
		return "R"
	else:
		return "R"

def ZC(metal):
	if(metal["s"]<2223):
		return KM(metal)

	if(metal["s"]>2436):
		return GMF(metal)

	if(metal["s"]>2294):
		return VF(metal)
	else:
		return "R"

def BDV(metal):
	if(metal["s"]>374):
		return "R"

	if(metal["s"]>225):
		return "R"

	if(metal["a"]<2926):
		return TT(metal)
	else:
		return "A"

def ZHM(metal):
	if(metal["a"]<1668):
		return "R"
	else:
		return "A"

def RF(metal):
	if(metal["x"]>2881):
		return "R"

	if(metal["m"]>925):
		return "A"
	else:
		return "A"

def MD(metal):
	if(metal["s"]<2729):
		return DJ(metal)

	if(metal["s"]>3389):
		return LQ(metal)

	if(metal["m"]>1183):
		return FBM(metal)
	else:
		return LDK(metal)
def XQ(metal):
	if(metal["s"]>2140):
		return "A"

	if(metal["s"]>1929):
		return "R"
	else:
		return "R"

def BN(metal):
	if(metal["s"]>112):
		return "A"

	if(metal["a"]<3510):
		return "A"
	else:
		return "R"

def ZRM(metal):
	if(metal["x"]>2201):
		return "A"

	if(metal["a"]>1339):
		return "R"
	else:
		return "A"

def TL(metal):
	if(metal["s"]>494):
		return JB(metal)

	if(metal["m"]>825):
		return SG(metal)

	if(metal["a"]<3751):
		return XV(metal)
	else:
		return DM(metal)
def DR(metal):
	if(metal["m"]>2757):
		return "A"

	if(metal["a"]>1578):
		return "A"
	else:
		return "R"

def SCP(metal):
	if(metal["m"]<1127):
		return "A"
	else:
		return "A"

def QZD(metal):
	if(metal["s"]>2591):
		return "A"

	if(metal["x"]<1477):
		return "A"

	if(metal["m"]<2327):
		return "A"
	else:
		return "A"

def GX(metal):
	if(metal["x"]>2633):
		return XP(metal)

	if(metal["x"]<1288):
		return JX(metal)
	else:
		return NZ(metal)
def PTB(metal):
	if(metal["x"]>570):
		return "A"

	if(metal["a"]<1242):
		return "A"
	else:
		return GD(metal)
def NQ(metal):
	if(metal["s"]>1502):
		return "A"

	if(metal["a"]<1419):
		return "A"

	if(metal["m"]>2710):
		return "A"
	else:
		return "A"

def XRK(metal):
	if(metal["a"]<2748):
		return SCP(metal)
	else:
		return "A"

def FNT(metal):
	if(metal["x"]<783):
		return "R"

	if(metal["m"]<2237):
		return "R"
	else:
		return "R"

def PZQ(metal):
	if(metal["m"]<1923):
		return QGX(metal)

	if(metal["s"]>756):
		return PTB(metal)

	if(metal["m"]>2173):
		return QZ(metal)
	else:
		return HB(metal)
def DQP(metal):
	if(metal["x"]<1260):
		return "R"

	if(metal["s"]<723):
		return TCJ(metal)

	if(metal["a"]<1038):
		return KBR(metal)
	else:
		return "R"

def BPD(metal):
	if(metal["m"]<1625):
		return TXZ(metal)
	else:
		return KXB(metal)
def MK(metal):
	if(metal["m"]<3370):
		return "R"
	else:
		return "R"

def DF(metal):
	if(metal["m"]<432):
		return DVT(metal)
	else:
		return NSJ(metal)
def KBR(metal):
	if(metal["m"]<3355):
		return "R"
	else:
		return "A"

def FT(metal):
	if(metal["a"]>3005):
		return "A"

	if(metal["x"]<3436):
		return QF(metal)
	else:
		return "A"

def SD(metal):
	if(metal["a"]<1555):
		return TN(metal)

	if(metal["x"]>695):
		return HR(metal)
	else:
		return "A"

def JNS(metal):
	if(metal["x"]>3379):
		return "A"
	else:
		return "A"

def RC(metal):
	if(metal["s"]>1303):
		return MCZ(metal)

	if(metal["s"]<1143):
		return JCD(metal)
	else:
		return KSN(metal)
def VNQ(metal):
	if(metal["a"]<2743):
		return "A"

	if(metal["s"]<3065):
		return DJD(metal)
	else:
		return "R"

def NCR(metal):
	if(metal["a"]<2770):
		return "R"
	else:
		return "R"

def NKZ(metal):
	if(metal["x"]<3104):
		return "A"

	if(metal["a"]<2868):
		return "A"
	else:
		return "R"

def QN(metal):
	if(metal["s"]<367):
		return "A"

	if(metal["a"]<2522):
		return "A"

	if(metal["s"]>673):
		return "R"
	else:
		return "A"

def DNN(metal):
	if(metal["a"]<3018):
		return "R"
	else:
		return "A"

def NVX(metal):
	if(metal["x"]>449):
		return "R"

	if(metal["x"]<431):
		return "R"
	else:
		return "A"

def QQ(metal):
	if(metal["x"]<814):
		return "R"

	if(metal["a"]>3379):
		return DJL(metal)

	if(metal["s"]>1570):
		return TB(metal)
	else:
		return "R"

def XR(metal):
	if(metal["a"]<3221):
		return "A"
	else:
		return "A"

def TCC(metal):
	if(metal["a"]>2884):
		return PMN(metal)

	if(metal["a"]<2707):
		return RRZ(metal)

	if(metal["x"]>2744):
		return KHC(metal)
	else:
		return NDQ(metal)
def DC(metal):
	if(metal["x"]<2981):
		return "A"

	if(metal["s"]<3555):
		return "R"
	else:
		return "A"

def JCD(metal):
	if(metal["x"]<2438):
		return JR(metal)

	if(metal["s"]>1077):
		return RZT(metal)

	if(metal["m"]<2916):
		return NB(metal)
	else:
		return KTV(metal)
def TVD(metal):
	if(metal["x"]<2294):
		return "R"

	if(metal["m"]>2968):
		return "R"
	else:
		return "A"

def HR(metal):
	if(metal["m"]<771):
		return "R"

	if(metal["a"]>1871):
		return "A"

	if(metal["m"]<852):
		return "A"
	else:
		return "R"

def STG(metal):
	if(metal["x"]<1998):
		return "R"

	if(metal["a"]<340):
		return "A"
	else:
		return "R"

def VXK(metal):
	if(metal["x"]>1227):
		return "A"
	else:
		return "A"

def XST(metal):
	if(metal["m"]>248):
		return "A"

	if(metal["m"]<115):
		return "A"
	else:
		return "R"

def TZ(metal):
	if(metal["x"]>259):
		return TX(metal)

	if(metal["x"]<147):
		return NGF(metal)

	if(metal["a"]<1602):
		return MNB(metal)
	else:
		return HKV(metal)
def CM(metal):
	if(metal["s"]<1516):
		return "A"
	else:
		return RR(metal)
def FVN(metal):
	if(metal["a"]>1404):
		return VM(metal)

	if(metal["s"]<2362):
		return "A"

	if(metal["s"]<2531):
		return JL(metal)
	else:
		return "A"

def XTK(metal):
	if(metal["a"]<3039):
		return "A"

	if(metal["m"]<873):
		return "A"
	else:
		return "A"

def NZL(metal):
	if(metal["a"]<3148):
		return XRK(metal)
	else:
		return LHL(metal)
def BPJ(metal):
	if(metal["m"]>3236):
		return "A"
	else:
		return "A"

def NQD(metal):
	if(metal["a"]>3052):
		return "A"
	else:
		return "A"

def MRK(metal):
	if(metal["m"]>802):
		return "A"

	if(metal["x"]<3319):
		return "R"

	if(metal["a"]>2546):
		return "R"
	else:
		return "R"

def PT(metal):
	if(metal["x"]<1010):
		return "R"

	if(metal["x"]<1152):
		return "R"

	if(metal["s"]<631):
		return "A"
	else:
		return "R"

def SVD(metal):
	if(metal["m"]<3239):
		return "R"

	if(metal["s"]>1065):
		return "A"

	if(metal["s"]<1042):
		return "A"
	else:
		return "R"

def GXQ(metal):
	if(metal["m"]>348):
		return "A"

	if(metal["m"]<160):
		return "R"
	else:
		return "R"

def RJV(metal):
	if(metal["a"]>3319):
		return "R"

	if(metal["s"]<1384):
		return "A"

	if(metal["a"]<2865):
		return KLG(metal)
	else:
		return "R"

def KSN(metal):
	if(metal["a"]<3369):
		return PC(metal)

	if(metal["s"]<1222):
		return RTC(metal)
	else:
		return NT(metal)
def BT(metal):
	if(metal["x"]<598):
		return VSX(metal)

	if(metal["s"]<2906):
		return GG(metal)

	if(metal["a"]<412):
		return "A"
	else:
		return GN(metal)
def HZ(metal):
	if(metal["s"]>3183):
		return "A"

	if(metal["a"]<1128):
		return TV(metal)
	else:
		return TH(metal)
def VLH(metal):
	if(metal["m"]<2565):
		return "R"

	if(metal["m"]<2572):
		return "A"

	if(metal["m"]<2575):
		return "R"
	else:
		return "A"

def KV(metal):
	if(metal["a"]<881):
		return "A"

	if(metal["s"]>497):
		return "A"

	if(metal["x"]>1630):
		return "R"
	else:
		return "R"

def GG(metal):
	if(metal["x"]<861):
		return "R"

	if(metal["s"]>2562):
		return "A"

	if(metal["a"]<571):
		return "A"
	else:
		return "R"

def XRS(metal):
	if(metal["s"]<3597):
		return "A"

	if(metal["a"]<3736):
		return "R"

	if(metal["x"]>3727):
		return "R"
	else:
		return "R"

def RR(metal):
	if(metal["x"]<3419):
		return "A"

	if(metal["s"]<1585):
		return "A"
	else:
		return "A"

def NX(metal):
	if(metal["m"]>775):
		return "R"

	if(metal["s"]<374):
		return "R"

	if(metal["x"]>96):
		return "R"
	else:
		return "R"

def ZLN(metal):
	if(metal["a"]<598):
		return "A"

	if(metal["x"]>2765):
		return "R"

	if(metal["s"]<3396):
		return "A"
	else:
		return "R"

def HXH(metal):
	if(metal["s"]>428):
		return PT(metal)

	if(metal["a"]<3181):
		return QNV(metal)

	if(metal["s"]>222):
		return RG(metal)
	else:
		return BN(metal)
def ZPM(metal):
	if(metal["s"]>56):
		return NL(metal)

	if(metal["s"]<25):
		return "A"

	if(metal["s"]>37):
		return "A"
	else:
		return RGB(metal)
def FBM(metal):
	if(metal["s"]<3133):
		return JFH(metal)

	if(metal["x"]<3239):
		return SFS(metal)

	if(metal["x"]<3326):
		return "A"
	else:
		return NNH(metal)
def GXZ(metal):
	if(metal["s"]<682):
		return "A"

	if(metal["x"]>3414):
		return CF(metal)

	if(metal["s"]<811):
		return "R"
	else:
		return "R"

def JCS(metal):
	if(metal["s"]<3173):
		return "R"
	else:
		return PG(metal)
def RGF(metal):
	if(metal["x"]<892):
		return "A"

	if(metal["a"]<2290):
		return "A"

	if(metal["s"]<457):
		return "R"
	else:
		return "A"

def HNP(metal):
	if(metal["m"]<480):
		return "A"

	if(metal["s"]>2663):
		return "A"
	else:
		return "R"

def BRR(metal):
	if(metal["x"]<567):
		return "R"

	if(metal["s"]>2706):
		return VPM(metal)
	else:
		return "A"

def KSZ(metal):
	if(metal["x"]>1173):
		return "R"
	else:
		return "R"

def KB(metal):
	if(metal["m"]>971):
		return PJC(metal)

	if(metal["s"]<3100):
		return FR(metal)

	if(metal["a"]>3600):
		return QVB(metal)
	else:
		return QP(metal)
def BP(metal):
	if(metal["x"]>1741):
		return "R"

	if(metal["a"]>3291):
		return "A"

	if(metal["m"]<2240):
		return "A"
	else:
		return "A"

def DH(metal):
	if(metal["x"]<3568):
		return "R"
	else:
		return "R"

def NQP(metal):
	if(metal["x"]>1941):
		return BL(metal)

	if(metal["a"]<3289):
		return RKG(metal)

	if(metal["a"]>3661):
		return XVL(metal)
	else:
		return XG(metal)
def KHJ(metal):
	if(metal["x"]>567):
		return "A"

	if(metal["x"]>479):
		return "A"

	if(metal["a"]>1795):
		return NVX(metal)
	else:
		return "A"

def RT(metal):
	if(metal["x"]>1014):
		return JQ(metal)

	if(metal["m"]>647):
		return XTK(metal)

	if(metal["a"]>3452):
		return CR(metal)
	else:
		return LMZ(metal)
def SLS(metal):
	if(metal["m"]<2332):
		return "A"

	if(metal["s"]>2616):
		return "A"
	else:
		return "R"

def DPR(metal):
	if(metal["a"]>3494):
		return "R"
	else:
		return "A"

def SZ(metal):
	if(metal["m"]<3872):
		return "R"

	if(metal["x"]>2610):
		return "R"

	if(metal["a"]>1233):
		return LDX(metal)
	else:
		return NPF(metal)
def LQ(metal):
	if(metal["a"]>3422):
		return "A"
	else:
		return "R"

def QNV(metal):
	if(metal["m"]>973):
		return "A"
	else:
		return "R"

def HL(metal):
	if(metal["s"]>3243):
		return VD(metal)
	else:
		return QK(metal)
def CVB(metal):
	if(metal["m"]<2489):
		return "R"
	else:
		return "R"

def LFQ(metal):
	if(metal["x"]>3855):
		return "R"

	if(metal["x"]<3735):
		return "A"
	else:
		return "R"

def QVB(metal):
	if(metal["m"]>635):
		return CFR(metal)

	if(metal["a"]>3858):
		return NK(metal)
	else:
		return XRS(metal)
def HXS(metal):
	if(metal["x"]>75):
		return "R"

	if(metal["a"]<3839):
		return "R"
	else:
		return "R"

def NKQ(metal):
	if(metal["a"]<1204):
		return "R"
	else:
		return "R"

def ZG(metal):
	if(metal["a"]>1588):
		return "A"

	if(metal["x"]>1263):
		return "R"

	if(metal["m"]>2439):
		return "A"
	else:
		return "R"

def QJ(metal):
	if(metal["s"]<410):
		return "R"

	if(metal["x"]>2055):
		return "A"
	else:
		return "R"

def PB(metal):
	if(metal["a"]>2581):
		return "A"
	else:
		return "R"

def ZBP(metal):
	if(metal["s"]<3308):
		return "R"

	if(metal["a"]>3214):
		return RDL(metal)
	else:
		return "A"

def MCX(metal):
	if(metal["a"]>1546):
		return "A"

	if(metal["x"]<159):
		return "R"

	if(metal["s"]<342):
		return "A"
	else:
		return "R"

def FND(metal):
	if(metal["s"]>1059):
		return "A"

	if(metal["m"]>1947):
		return "R"

	if(metal["m"]>1824):
		return "R"
	else:
		return "R"

def SDP(metal):
	if(metal["a"]<3225):
		return PBB(metal)

	if(metal["x"]>3443):
		return KB(metal)

	if(metal["a"]>3623):
		return TK(metal)
	else:
		return MD(metal)
def NH(metal):
	if(metal["x"]<1784):
		return "A"

	if(metal["m"]<201):
		return DKP(metal)
	else:
		return JG(metal)