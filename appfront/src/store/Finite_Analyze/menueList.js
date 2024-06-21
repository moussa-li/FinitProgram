const titleList =
    [
        {
            title: '导入模型',
            menueList: [],
        },
        {
            title: '网格生成',
            menueList: [],
        },
        {
            title: '模拟类型',
            menueList: [],
        },
        {
            title: '物体材质',
            menueList: [],
        },
        {
            title: '边界条件',
            // title: '外界因素',
            menueList: [],
        },
        {
            title: '计算结果',
            menueList: [],
        },
        // {
        //     title: '数据导出',
        //     menueList: [],
        // },
        {
            title: '可视化',
            menueList: [],
        },
    ]

const ImportModelList = [
    {
        name: 'stp',
        Type: 'ImportModel',
        data:{
            ImportFile:'',
        }
    },
    {
        name: 'igs',
        Type: 'ImportModel',
        data:{
            ImportFile:'',
        }
    },
]
for (let i = 0, len = ImportModelList.length; i < len; i++) {
    titleList[0].menueList.push(ImportModelList[i])
}

const GrideList = [
    {
        name: 'netgen',
        Type: 'Gride',
        data:{
            Dimension:'',
            MaxSize:0.0,
            MinSize:0.0,
        }
    },
    {
        name: 'gmsh',
        Type: 'Gride',
        data:{
            Dimension:'',
            MaxSize:0.0,
            MinSize:0.0,
        }
    },
]
for (let i = 0, len = GrideList.length; i < len; i++) {
    titleList[1].menueList.push(GrideList[i])
}

const Analogtype = [
    {
        name: '结构力学',
        Type: 'Analogtype',
        data: {
            Gravity:-9.8,
        }
    },
    {
        name: '热力学',
        Type: 'Analogtype',
    },
]
for (let i = 0, len = Analogtype.length; i < len; i++) {
    titleList[2].menueList.push(Analogtype[i])
}

const Material = [
    // {
    //     name: '墙砖',
    // },
    // {
    //     name: '夯土',
    // },
    // {
    //     name:'地基土',
    // },
    // {
    //     name:'混凝土'
    // },
    // {
    //     name:'木头'
    // },
    {
        name: '材料设置',
        Type: 'Material',
        data:{
        // category:'',
        // material_card:'',
        Name:'',
        Density:'',
        YoungsModulus:'',
        PoissonRatio:'',
        ThermalConductivity:'',
        ExpansionCoefficient:'',
        SpecificHeat:'',
    }
    }
]
for (let i = 0, len = Material.length; i < len; i++) {
    titleList[3].menueList.push(Material[i])
}

const Boundary = [

    {
        name: '载荷',
        Type: 'Load',
        data: {
        Gravity:-9.8,
        }
    },
    {
        name: '固定支撑',
        Type: 'ConstraintFixed',
        data: {
            Face:[],
        }
    },
    {
        name: '温度面约束',
        Type: 'TemperatureConstraint',
        data: {
            Temperature:'',
            Face:[],
            CFlux:'',
        }
    },
    {
        name: '初始温度',
        Type: 'Temperature',
        data: {
            InitTemperature:'',
        }
    },
]
for (let i = 0, len = Boundary.length; i < len; i++) {
    titleList[4].menueList.push(Boundary[i])
}

// const Environment = [
//     {
//         name: '日晒',
//     },
//     {
//         name: '下雨',
//     },
//     {
//         name: '刮风',
//     },
//     {
//         name: '对流',
//     },
//     {
//         name:'辐射'
//     },
// ]
// for (let i = 0, len = Environment.length; i < len; i++) {
//     titleList[4].menueList.push(Environment[i])
// }

const Result = [
    // {
    //     name: '保存文件',
    // },
    // {
    //     name: '运行计算',
    // },
    {
        Type: 'Result',
        name:'结果设置'
    }
]
for (let i = 0, len = Result.length; i < len; i++) {
    titleList[5].menueList.push(Result[i])
}
     

// const Export = [
//     {
//         name: '应变',
//     },
//     {
//         name: '应力',
//     },
//     {
//         name: '总形变',
//     },
// ]

// for (let i = 0, len = Export.length; i < len; i++) {
//     titleList[6].menueList.push(Export[i])
// }

const Visual = [
    // {
    //     name: '形变图',
    // },
    // {
    //     name: '受力图',
    // },
    {
        Type: 'Visual',
        name:'结果可视化'
    }
]

for (let i = 0, len = Visual.length; i < len; i++) {
    titleList[6].menueList.push(Visual[i])
}

export default titleList