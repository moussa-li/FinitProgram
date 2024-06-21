from OCC.Core.TopLoc import TopLoc_Location  # 引入Occ模型定位模块
from OCC.Extend.DataExchange import read_step_file#STEP文件导入模块
from OCC.Extend.TopologyUtils import TopologyExplorer#STEP文件导入模块后的拓扑几何分析模块

# class Example(QMainWindow):
class Example():
    def __init__(self):
        super().__init__()

#         self.canva = qtViewer3d(self)

        self.initUI()

    def initUI(self):

        self.StepModelExplore()


    def STEP_shape(self):
        stpshp = read_step_file('test.step')# 读取step文件
        return TopologyExplorer(stpshp)# step文件模型解析

    def StepModelExplore(self):
#         self.canva._display.EraseAll()
        self.STEPshp = self.STEP_shape()
        i=1
        j=1
        
        for solid in self.STEPshp.solids():#遍历物体的体
            print("Solid",i)
            i+=1
            for face in self.STEPshp.faces_from_solids(solid):#遍历物体的面
                print("Face",j)
                j+=1
                #用于统计零件数目


if __name__ == '__main__':

    ex = Example()