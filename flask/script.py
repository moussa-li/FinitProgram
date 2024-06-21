import sys
sys.path.append('E:\\Anaconda3\\envs\\conda_freecad\\Library\\bin')#这里使用你自己的bin目录
sys.path.append('E:\\Anaconda3\\envs\\conda_freecad\\Library\\Mod\\Fem')
#import FreeCADGui as Gui
#import FreeCAD
#import FreeCAD as App
#import ObjectsFem
#from femtools import ccxtools
#from femsolver.run import run_fem_solver
import os
from move import move_file
from femmesh.gmshtools import GmshTools as gt
from femsolver.run import run_fem_solver, getMachine, _DocObserver
from femsolver.report import display, displayLog

i=1
RESULTS = 3

#导入模型
def ImportModel(file_path,file_name):
    FreeCAD.openDocument(file_path)
    App.setActiveDocument(file_name)
    App.ActiveDocument = App.getDocument(file_name)
    print("import done")

#创建分析容器
def set_analysis():
    analysis_object = ObjectsFem.makeAnalysis(FreeCAD.ActiveDocument, "Analysis")
    print("makeAnalysis done")
    return  analysis_object

#设置求解器
def set_solver(analysis_object,elastic=0,heat=0):
    solver_object = analysis_object.addObject(ObjectsFem.makeSolverElmer(FreeCAD.ActiveDocument, "SolverElmer"))[0]
    solver_object.SteadyStateMinIterations = 10
    solver_object.SteadyStateMaxIterations = 100
    if elastic==1:
        eq_heat = ObjectsFem.makeEquationHeat(FreeCAD.ActiveDocument, solver_object)
        eq_heat.Bubbles = True
        eq_heat.Priority = 2
    if heat==1:
        eq_elasticity = ObjectsFem.makeEquationElasticity(FreeCAD.ActiveDocument, solver_object)
        eq_elasticity.Bubbles = True
        eq_elasticity.Priority = 1
        eq_elasticity.LinearSolverType = "Direct"
    print("setsolver done")
    return solver_object





#设置Gmsh
def set_Gride(maxsize,minsize,analysis_object):
    femmesh_obj = ObjectsFem.makeMeshGmsh(FreeCAD.ActiveDocument, 'FEMMeshGmsh')
    femmesh_obj.Part = FreeCAD.ActiveDocument.Body
    femmesh_obj.CharacteristicLengthMax=maxsize
    femmesh_obj.CharacteristicLengthMin=minsize

    FreeCAD.ActiveDocument.recompute()

    gmsh_mesh = gt(femmesh_obj)
    error = gmsh_mesh.create_mesh()
    print(error)
    analysis_object.addObject(femmesh_obj)
    print("mesh done")

def set_Material(analysis_object,data):
    material_obj_bottom = analysis_object.addObject(
        ObjectsFem.makeMaterialSolid(FreeCAD.ActiveDocument, "MaterialCopper")
    )[0]
    mat = material_obj_bottom.Material
    mat["Name"] = "Copper"
    mat["YoungsModulus"] = data['YoungsModulus']
    mat["PoissonRatio"] = data['PoissonRatio']
    mat["SpecificHeat"] = data['SpecificHeat']
    mat["ThermalConductivity"] = data['ThermalConductivity']
    mat["ThermalExpansionCoefficient"] = data['ExpansionCoefficient']
    mat["Density"] = data['Density']
    material_obj_bottom.Material = mat
    analysis_object.addObject(material_obj_bottom)
    print("material done")


def do_analysis(solver_object):
    machine = getMachine(solver_object)
    machine.reset(0)
    machine.target = RESULTS
    machine.start()
    machine.join()  # wait for the machine to finish.
    if machine.failed is True:
        App.Console.PrintError("Machine failed to run.\n")

        displayLog(machine.report)
        if App.GuiUp:
            error_message = (
                "Failed to run. Please try again after all "
                "of the following errors are resolved."
            )

            display(machine.report, "Run Report", error_message)
    print("analysis done")
    return machine.directory

def set_ConstraintFixed(analysis_object,face):
    fixed_constraint = analysis_object.addObject(
        ObjectsFem.makeConstraintDisplacement(FreeCAD.ActiveDocument, name="FemConstraintDisplacment")
    )[0]
    fixed_constraint.xDisplacement = 0.000000
    fixed_constraint.yDisplacement = 0.000000
    fixed_constraint.zDisplacement = 0.000000
    fixed_constraint.xRotation = 0.000000
    fixed_constraint.yRotation = 0.000000
    fixed_constraint.zRotation = 0.000000
    fixed_constraint.xFree = False
    fixed_constraint.xFix = True
    fixed_constraint.yFree = False
    fixed_constraint.yFix = True
    fixed_constraint.zFree = False
    fixed_constraint.zFix = True
    fixed_constraint.rotxFree = False
    fixed_constraint.rotxFix = True
    fixed_constraint.rotyFree = False
    fixed_constraint.rotyFix = True
    fixed_constraint.rotzFree = False
    fixed_constraint.rotzFix = True
    fixed_constraint.References = [(App.ActiveDocument.Pad, "Face5")]
    print("FEM_ConstraintDisplacement done")

#自重约束
def set_ConstraintSelfWeight(data,analysis_object):
    self_weight = ObjectsFem.makeConstraintSelfWeight(FreeCAD.ActiveDocument, "FemConstraintForce")
    self_weight.Gravity_z = float(data['Gravity'])
    analysis_object.addObject(self_weight)
    print("FEM_ConstraintSelfWeight done")

#初始温度约束条件
def set_initialTemp(analysis_object,temp):
    constraint_initialtemp = analysis_object.addObject(
        ObjectsFem.makeConstraintInitialTemperature(FreeCAD.ActiveDocument, "ConstraintInitialTemperature")
    )[0]
    constraint_initialtemp.initialTemperature = temp

    print("FEM_ConstraintinitialTemp done")

#表面温度设置
def set_faceTemp(analysis_object,data):

    # constraint temperature
    constraint_temperature = analysis_object.addObject(
        ObjectsFem.makeConstraintTemperature(FreeCAD.ActiveDocument, "ConstraintTemperature")
    )[0]
    constraint_temperature.References = [
        (App.ActiveDocument.Pad, "Face6"),
        (App.ActiveDocument.Pad, "Face7")
    ]
    constraint_temperature.Temperature = data['Temperature']
    constraint_temperature.CFlux = data['CFlux']
    print("FEM_ConstraintfaceTemp done")


def find_model(model,element):
    for i in model:
        if i==element:
            return True
        else: return False

def runFreeCAD(data):
    global i
    try:
        print(i)
        ImportModel('C:/Users/qwe/Desktop/taoshi_180mm.FCStd', "taoshi_180mm")
        analysis_object=set_analysis()
        solver_object=set_solver(analysis_object,1,1)
        set_Gride(0.0,0.0,analysis_object)
        Material_data={
            'Name':data['Name'],
            'Density':data['Density'],
            'YoungsModulus':data['YoungsModulus'],
            'PoissonRatio':data['PoissonRatio'],
            'ThermalConductivity':data['ThermalConductivity'],
            'ExpansionCoefficient':data['ExpansionCoefficient'],
            'SpecificHeat':data['SpecificHeat'],
        }
        set_Material(analysis_object,Material_data)
        set_initialTemp(analysis_object,data['InitTemperature'])
        faceTemp_data={
            'Temperature_Face':data['Temperature_Face'],
            'Temperature':data['Temperature'],
            'CFlux':data['CFlux']
        }
        set_faceTemp(analysis_object,faceTemp_data)
        Constraint_data={
            'Face':data['Face'],
        }
        set_ConstraintFixed(analysis_object, Constraint_data)
        directory=do_analysis(solver_object)

        print(directory)
        FreeCAD.ActiveDocument.recompute()
        possible_post_file_0 = os.path.join(directory, "case0001.vtu")
        possible_post_file_t = os.path.join(directory, "case_t0001.vtu")
        if os.path.isfile(possible_post_file_0):
            postPath = possible_post_file_0
        elif os.path.isfile(possible_post_file_t):
            postPath = possible_post_file_t
        print(postPath)
        target_path = "C:\\Users\\qwe\\Desktop\\data"
        target_path = os.path.join(target_path, "case_t000" + str(i) + ".vtu")
        move_file(postPath, target_path)
        FreeCAD.closeDocument("taoshi_180mm")
        FreeCAD.setActiveDocument("")
        FreeCAD.ActiveDocument = None
        i = i + 10

        #url="http://localhost:8088/"
        #if(i==1):
            #os.system('pvpython -m paraview.apps.visualizer --data "C:\\Users\\qwe\\Desktop\\data" --port 8088')
        #command="\""+get_browser_path('chrome')+"\""+' http://localhost:8088/'
        return 1
    except Exception as e:
        print(e)
        return 0

if __name__=='__main__':
    runFreeCAD()