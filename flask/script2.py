import sys
sys.path.append('E:\\Anaconda3\\envs\\conda_freecad\\Library\\bin')#这里使用你自己的bin目录
sys.path.append('E:\\Anaconda3\\envs\\conda_freecad\\Library\\Mod\\Fem')
import FreeCADGui as Gui
import FreeCAD
import FreeCAD as App
import ObjectsFem
from femtools import ccxtools
from femsolver.run import run_fem_solver
import os
from move import move_file

RESULTS = 3
def runFreeCAD(data):
    try:
        # Gui.runCommand('Std_DlgMacroRecord',0)
        ### Begin command Std_Open
        FreeCAD.openDocument('C:/Users/qwe/Desktop/taoshi_180mm.FCStd')
        App.setActiveDocument("taoshi_180mm")
        App.ActiveDocument=App.getDocument("taoshi_180mm")
        ### End command Std_Open
        #Gui.runCommand('Std_OrthographicCamera',1)
        ### Begin command FEM_Analysis
        analysis_object = ObjectsFem.makeAnalysis(FreeCAD.ActiveDocument, "Analysis")
        print("makeAnalysis done")
        #FemGui.setActiveAnalysis(FreeCAD.ActiveDocument.Analysis)
        #ObjectsFem.makeAnalysis(FreeCAD.ActiveDocument, 'Analysis')
        # solver (we gone use the well tested CcxTools solver object)
        solver_object = ObjectsFem.makeSolverElmer(FreeCAD.ActiveDocument)
        equation1=ObjectsFem.makeEquationElasticity(FreeCAD.ActiveDocument, FreeCAD.ActiveDocument.SolverElmer)
        analysis_object.addObject(solver_object)
        print("FEM_Analysis done")
        ### End command FEM_Analysis
        ### Begin command FEM_MaterialSolid
        material_object = ObjectsFem.makeMaterialSolid(FreeCAD.ActiveDocument, "SolidMaterial")
        mat = material_object.Material
        mat['Name'] = data['MaterialName']
        mat['YoungsModulus'] = data['YoungsModulus']
        mat['PoissonRatio'] = data['PoissonRatio']
        mat['Density'] = data['Density']
        material_object.Material = mat
        analysis_object.addObject(material_object)
        #material_object.References=[(App.ActiveDocument.Part__Feature,"Solid2")]
        print("FEM_MaterialSolid done")
        ### End command FEM_MaterialSolid
        ### Begin command FEM_ConstraintFixed
        fixed_constraint = ObjectsFem.makeConstraintFixed(FreeCAD.ActiveDocument, "FemConstraintFixed")
        fixed_constraint.References = [(App.ActiveDocument.Pad, data['Face'])]
        analysis_object.addObject(fixed_constraint)
        print("FEM_ConstraintFixed done")
        ### End command FEM_ConstraintFixed

        ### Begin command FEM_ConstraintSelfWeight
        self_weight=ObjectsFem.makeConstraintSelfWeight(FreeCAD.ActiveDocument, "FemConstraintForce")
        self_weight.Gravity_z = float(data['Gravity'])
        analysis_object.addObject(self_weight)
        print("FEM_ConstraintSelfWeight done")
        ### End command FEM_ConstraintSelfWeight

        ### Begin command FEM_MeshNetgenFromShape
        femmesh_obj = ObjectsFem.makeMeshGmsh(FreeCAD.ActiveDocument,'FEMMeshGmsh')
        femmesh_obj.Part = FreeCAD.ActiveDocument.Body

        FreeCAD.ActiveDocument.recompute()

        from femmesh.gmshtools import GmshTools as gt
        gmsh_mesh = gt(femmesh_obj)
        error = gmsh_mesh.create_mesh()
        print(error)

        analysis_object.addObject(femmesh_obj)

        print("mesh done")

        #run_fem_solver(solver_object,0)
        #FreeCAD.ActiveDocument.recompute()
        ### End command FEM_MeshNetgenFromShape
        from femsolver.run import run_fem_solver,getMachine
        from femsolver.report import display,displayLog
        machine = getMachine(solver_object)
        if not machine.running:
            machine.reset()
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
        #run_fem_solver(solver_object)
        print("analysis done")
        print(machine.directory)
        possible_post_file_0 = os.path.join(machine.directory, "case0001.vtu")
        possible_post_file_t = os.path.join(machine.directory, "case_t0001.vtu")
        if os.path.isfile(possible_post_file_0):
            postPath = possible_post_file_0
        elif os.path.isfile(possible_post_file_t):
            postPath = possible_post_file_t
        move_file(postPath,'C:\\Users\\qwe\\Desktop')

        return 1
    except Exception as e:
        print(e)
        return 0

