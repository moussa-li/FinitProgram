import subprocess
from flask import Flask, jsonify,render_template,request
from flask_cors import *

#from script2 import runFreeCAD
#from script import runFreeCAD

from ngsolve import *
from netgen.occ import *
from netgen.webgui import Draw
 
app = Flask(__name__)
CORS(app,supports_credentials=True)
 
@app.route('/')
def hello_world(): #主页
    return render_template('index.html')

@app.route('/test',methods=['POST'])
def test():
    test = request.get_data()
    print(test)
    return 'success'

@app.route('/runscript',methods=['POST'])
def run_script():
    if request.method == 'POST':
        nodeList=request.get_json()
        print(nodeList)
        Analogtype=-1
        for node in nodeList:
            if node['Type'] == 'Analogtype':
                if node['label'] == '结构力学':
                    Analogtype=0
                elif node['label'] == '热力学':
                    Analogtype=1
                

        if Analogtype == 0:
            for node in nodeList:
                if node['Type'] == 'ImportModel':
                    ImportFile=node['data']['ImportFile']
                elif node['Type'] == 'Gride':
                    Dimension=node['data']['Dimension']
                    MaxSize=node['data']['MaxSize']
                    MinSize=node['data']['MinSize']
                elif node['Type'] == 'Material':
                    MaterialName=node['data']['Name']
                    Density=node['data']['Density']
                    YoungsModulus=node['data']['YoungsModulus']
                    PoissonRatio=node['data']['PoissonRatio']
                elif node['Type'] == 'Load':
                    Gravity=node['data']['Gravity']
                elif node['Type'] == 'ConstraintFixed':
                    Face=node['data']['Face']
            data={
                'Dimension':Dimension,
                'MaxSize':MaxSize,
                'MinSize':MinSize,
                'MaterialName':MaterialName,
                'Density':Density,
                'YoungsModulus':YoungsModulus+' MPa',
                'PoissonRatio':PoissonRatio+' kg/m^3',
                'Gravity':Gravity,
            }
            #script2.runFreeCAD(data)
        elif Analogtype == 1:
            for node in nodeList:
                if node['Type'] == 'ImportModel':
                    ImportFile=node['data']['ImportFile']
                elif node['Type'] == 'Gride':
                    Dimension=node['data']['Dimension']
                    MaxSize=node['data']['MaxSize']
                    MinSize=node['data']['MinSize']
                elif node['Type'] == 'Material':
                    Name=node['data']['Name']
                    Density=node['data']['Density']
                    YoungsModulus=node['data']['YoungsModulus']
                    PoissonRatio=node['data']['PoissonRatio']
                    ThermalConductivity=node['data']['ThermalConductivity']
                    ExpansionCoefficient=node['data']['ExpansionCoefficient']
                    SpecificHeat=node['data']['SpecificHeat']
                elif node['Type'] == 'TemperatureConstraint':
                    Temperature=node['data']['Temperature']
                    Temperature_Face=node['data']['Face']
                    CFlux=node['data']['CFlux']
                elif node['Type'] == 'Temperature':
                    InitTemperature=node['data']['InitTemperature']
                elif node['Type'] == 'ConstraintFixed':
                    Face=node['data']['Face']
            data={
                'Dimension':Dimension,
                'MaxSize':MaxSize,
                'MinSize':MinSize,
                'Face':Face,
                'Name':Name,
                'Density':Density+' kg/m^3',
                'YoungsModulus':YoungsModulus+' MPa',
                'PoissonRatio':PoissonRatio,
                'ThermalConductivity':ThermalConductivity+' W/m/K',
                'ExpansionCoefficient':ExpansionCoefficient+' m/m/K',
                'SpecificHeat':SpecificHeat+' J/kg/K',
                'InitTemperature':InitTemperature,
                'Temperature':Temperature,
                'Temperature_Face':Temperature_Face,
                'CFlux':CFlux,
            }
            #script.runFreeCAD(data)
        elif Analogtype == -1:
            return jsonify('运行失败,未设置模拟类型')

        out = subprocess.Popen('pvpython -m paraview.apps.visualizer --data  "E:\data"', shell = True)
        return jsonify('运行成功')

# @app.route('/visualizer')

@app.route('/input_files',methods=['GET','POST']) #路由输入STEP文件
def input_file():
    if request.method=='POST':
        file=request.files.get("file").save('cache.step')#前端传入STEP文件存放到服务器本地
        OCC_file = OCCGeometry('cache.step') #读取本地STEP文件
        TopoDS_Shape_file = OCC_file.shape #OCC读取为TopoDS_Shape
        html = Draw(TopoDS_Shape_file,is_web=True) #生成html模型
        data = {'html':html,'Face':['Face1','Face2']}
    return html.GenerateHTML() #传回前端
    
 
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)