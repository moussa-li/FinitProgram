<template>
    <el-form :model="node" ref="dataForm" label-width="100px" class="flowEditForm margin13" size="mini">

<!-- 导入模型 -->
        <el-form-item label="导入模型" v-if="node.Type === 'ImportModel'" >
            <!-- <el-input v-model="node.data.ImportFile" type="file" :autosize="{ minRows: 2, maxRows: 4}" name="file" ></el-input> -->
            <el-upload
                    multiple
                    style="width:350px"
                    ref="upload"
                    :file-list="fileList"
                    action
                    :http-request="input_file"
                    :auto-upload="true"
                >
                    <el-button size="mini" type="primary">点击上传</el-button>
                    <!-- <div slot="tip" class="el-upload__tip">只能上传war文件</div> -->
                </el-upload>
            <!-- <el-button  type="button" @click="upload()" >上传</el-button> -->
        </el-form-item>

<!-- 网格生成 -->
        <el-form-item label="元素维度" v-if="node.Type === 'Gride'">
            <el-select v-model="node.data.Dimension" placeholder="请选择">
                <el-option 
                v-for="item in Dimension_Options"
                :key="item.value"
                :label="item.label"
                :value="item.value"
                >
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="最大尺寸" v-if="node.Type === 'Gride'">
            <el-input v-model="node.data.MaxSize" type="number"></el-input>
        </el-form-item>
        <el-form-item label="最小尺寸" v-if="node.Type === 'Gride'">
            <el-input v-model="node.data.MinSize" type="number"></el-input>
        </el-form-item>

<!-- 结构力学 -->

<!-- 物体材质 -->
        <el-form-item label="物体种类" v-if="node.Type === 'Material'  ">
            <el-select v-model="node.data.Name" placeholder="请选择">
                <el-option :label="'Stell-Genneric'" :value="'Stell-Genneric'" :key="'Stell-Genneric'"></el-option>
                <el-option :label="'Copper'" :value="'Copper'" :key="'Copper'"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="杨氏模量" v-if="node.Type === 'Material' ">
            <el-input v-model="node.data.YoungsModulus" type="text"></el-input>
        </el-form-item>
        <el-form-item label="泊松比" v-if="node.Type === 'Material' ">
            <el-input v-model="node.data.PoissonRatio" type="text"></el-input>
        </el-form-item>
        <el-form-item label="密度(kg/m^3)" v-if="node.Type === 'Material' ">
            <el-input v-model="node.data.Density" type="text"></el-input>
        </el-form-item>

        <el-form-item label="导热系数(W/m/K)" v-if="node.Type === 'Material' && Analogtype(node) === '热力学'">
            <el-input v-model="node.data.ThermalConductivity" type="text"></el-input>
        </el-form-item>
        <el-form-item label="热膨胀系数(μm/m/K)" v-if="node.Type === 'Material' && Analogtype(node) === '热力学'">
            <el-input v-model="node.data.ExpansionCoefficient" type="text"></el-input>
        </el-form-item>
        <el-form-item label="比热容(J/kg/K)" v-if="node.Type === 'Material' && Analogtype(node) === '热力学'">
            <el-input v-model="node.data.SpecificHeat" type="text"></el-input>
        </el-form-item>

<!-- 载荷 -->
        <el-form-item label="重力大小" v-if="node.Type === 'Load'">
            <el-input v-model="node.data.Gravity" type="text" @input="inputEnter"></el-input>
        </el-form-item>

<!-- 固定支撑 -->
        <el-form-item label="固定面" v-if="node.Type === 'ConstraintFixed'">
            <el-select v-model="node.data.Face" placeholder="请选择" multiple>
                <el-option 
                v-for="item in Face_Options"
                :key="item"
                :label="item"
                :value="item"
                >
                </el-option>
            </el-select>
        </el-form-item>

<!-- 温度设置-->
        <el-form-item label="温度" v-if="node.Type === 'TemperatureConstraint'">
            <el-input v-model="node.data.Temperature" type="text" ></el-input>
        </el-form-item>
        <el-form-item label="固定约束" v-if="node.Type === 'TemperatureConstraint'">
            <el-select v-model="node.data.Face" placeholder="请选择" multiple>
                <el-option 
                v-for="item in Face_Options"
                :key="item"
                :label="item"
                :value="item"
                >
                </el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="表面热流密度" v-if="node.Type === 'TemperatureConstraint'">
            <el-input v-model="node.data.CFLux" type="text" ></el-input>
        </el-form-item>

        <el-form-item label="温度" v-if="node.Type === 'Temperature'">
            <el-input v-model="node.data.InitTemperature" type="text" ></el-input>
        </el-form-item>


        <!-- <el-form-item>
            <el-button type="primary" @click="submitForm('dataForm')">确认</el-button>
        </el-form-item> -->
    </el-form>
</template>

<script>
import { EventBus } from '@/store/Finite_Analyze/event-bus';

    export default {
        name:'editNode',
        props:{
            lineList:Array,
            nodeList:Array,
            },
        data() {
            return {
                node: {},
                Dimension_Options: [
                    { value: 1, label: 'From Shape' },
                    { value: 2, label: '1D' },
                    { value: 3, label: '2D' },
                    { value: 4, label: '3D' }
                    ],
                Face_Options: [],
                fileList:[],
            }
        },
        methods: {
            init(data, id) {
                data.nodeList.filter((node) => {
                    if (node.id === id) {
                        this.node = node;
                    }
                })
            },
            input_file(param) //导入step文件
            {
                let fileObj=param.file;
                let data=new FormData();
                let _this = this
                data.append("file",fileObj)
                console.log(data)
                this.$axios({
                    url:"http://127.0.0.1:5000/input_files",
                    method:'POST',
                    headers:{
                        'Content-Type':'multipart/form-data'
                    },
                    data
                }).then(res=>{
                    console.log('成功',res);
                    console.log('res.data',res.data)
                    EventBus.$emit('visaul', {
                    visaul_data:res.data
                    })
                }).catch(error=>{
                    console.log('失败',error);
                })
            },
            submitForm:function(ev)
            {
                console.log(this.$refs[ev])
                console.log(this.node.ImportFile)
            },
            Analogtype:function(node)
            {
                while(node!=null&&node.Type!='Analogtype')
                {
                    var from_node_id=this.getfrom(node)
                    if(from_node_id!=0)
                    {

                        this.nodeList.filter((_node)=>{
                            if(_node.id === from_node_id)
                    {
                        node=_node
                    }
                    })
                    }
                    else
                    {
                        node=null
                    }
                }

                //console.log(node.label)
                return node.label
                
            },
            getfrom(node)
            {
                var lineList=this.lineList
                for(var i in lineList)
                {
                    if(lineList[i].to==node.id)
                    {
                        return lineList[i].from
                    }
                }
                return 0
            },
            inputEnter(value) {
                value = value.replace(/[^\d.-]/g, ""); // 清除"数字"和"."以外的字符 只能输入数字和小数点
                value = value.replace(/\.{2,}/g, "."); // 不能连续输入两个及以上小数点
                value = value
                .replace(".", "$#$")
                .replace(/\./g, "")
                .replace("$#$", "."); // 只保留第一个".", 清除多余的"."
                value = value.replace(
                /^(-)*(\d+)\.(\d\d\d\d\d\d).*$/,
                "$1$2.$3"
                ); // 只能输入六位小数
                // if (
                // this.node.data.Gravity &&
                // this.node.data.Gravity.indexOf(".") < 0 &&
                // this.node.data.Gravity != ""
                // ) {
                // this.node.data.Gravity = parseFloat(this.node.data.Gravity);
                // this.node.data.Gravity = this.node.data.Gravity + "";
                // } // 如果没有小数点，首位不能为类似于 01、02的值
                // // 输入过程中，只能输入六位小数且六位小数都为零，则清空小数点和后面的六个零（如果输入完成了只输入四个零，则在blur事件中处理）
                // if (
                // this.node.data.Gravity.indexOf(".") > 0 &&
                // this.node.data.Gravity.length - this.node.data.Gravity.indexOf(".") > 6
                // ) {
                // let str = this.node.data.Gravity.slice(
                // this.node.data.Gravity.indexOf("."),
                // this.node.data.Gravity.length
                // );
                // if (str / 1 <= 0) {
                // this.node.data.Gravity = this.node.data.Gravity.replace(str, "");
                // }
                // }
                // if (this.node.data.Gravity / 1 > 256) {
                // this.node.data.Gravity = this.node.data.Gravity + "";
                // this.node.data.Gravity = this.node.data.Gravity.slice(0, this.node.data.Gravity.length - 1);
                // }
            }
        }
    }
</script>
