const nodeList=[]
const lineList=[]

// var temp1 = {
//     id: '8b6a83ac-daa8-4775-a6b9-4529744d04ef',
//     label: 'stp',
//     top: '40px',
//     left: '90px',
//     Type: 'ImportModel',
//     data:{
//         ImportFile:'',
//     }
// }
// nodeList.push(temp1)
// var temp2 = {
//     id: '41cf9b1e-4b3c-4d65-894f-a2b3b60db567',
//     label: 'gmsh',
//     top: '100px',
//     left: '90px',
//     Type: 'Gride',
//     data:{
//         Dimension:'',
//         MaxSize:0.0,
//         MinSize:0.0,
//     }
// }
// // var temp11 = {
// //     id: '41cf9b1e-4f3c-4d65-894f-a2b3b60db567',
// //     label: 'gmsh',
// //     top: '100px',
// //     left: '40px',
// //     Type: 'Gride',
// //     data:{
// //         Dimension:'',
// //         MaxSize:0.0,
// //         MinSize:0.0,
// //     }
// // }
// nodeList.push(temp2)
// // nodeList.push(temp11)

// var temp3 = {

//     id: '31927691-fc8c-4d5a-8b2d-34bc852ac0b1',
//     label: '结构力学',
//     top: '160px',
//     left: '90px',
//     Type: 'Analogtype',
    
// }
// nodeList.push(temp3)
// var temp4 = {
//     id: '89393871-0072-40fe-aae4-bad2ac837d5d',
//     label: '材料设置',
//     top: '220px',
//     left: '90px',
//     Type:'Material',
//     data:{
//         // category:'',
//         // material_card:'',
//         Name:'',
//         Density:'',
//         YoungsModulus:'',
//         PoissonRatio:'',
//         ThermalConductivity:'',
//         ExpansionCoefficient:'',
//         SpecificHeat:'',
//     }
// }
// nodeList.push(temp4)
// var temp5 = {
//     id: 'eda25fd1-4798-4a70-8aa2-aa54ed13a316',
//     label: '载荷',
//     top: '280px',
//     left: '90px',
//     Type: 'Load',
//     data: {
//         Gravity:-9.8,
//     }
// }
// nodeList.push(temp5)
// var temp6 = {
//     id: '2fceead6-a12b-4ca0-84b1-8d564bb5de1f',
//     label: '固定支撑',
//     top: '340px',
//     left: '90px',
//     Type: 'ConstraintFixed',
//     data: {
//         Face:[],
//     }
// }
// nodeList.push(temp6)
// var temp7 = {
//     id: '311b8299-3668-420e-836e-3a347e8338d9',
//     label: '结果设置',
//     top: '400px',
//     left: '90px',
//     Type: ''
// }
// nodeList.push(temp7)
// var temp8 = {
//     id: '91d301e9-4b7f-4621-8e49-55682bad40fc',
//     label: '结果可视化',
//     top: '460px',
//     left: '83px',
//     Type: ''
// }
// nodeList.push(temp8)

// var line1 = {
//     from:temp1.id,
//     to:temp2.id,
//     label:'',
//     id:'17b814b0-36d4-4db1-8d8f-f8d2c6cfd927',
//     Remark:'',
// }
// var line2 = {
//     from:temp2.id,
//     to:temp3.id,
//     label:'',
//     id: 'f751d353-2611-430f-8d2c-2467fd754736',
//     Remark:'',
// }
// var line3 = {
//     from:temp3.id,
//     to:temp4.id,
//     label:'',
//     id: '0182b6b2-667e-47d1-a69f-8bfece90c8e9',
//     Remark:'',
// }
// var line4 = {
//     from:temp4.id,
//     to:temp5.id,
//     label:'',
//     id: '191004aa-f181-46d1-86ef-a7da6f442a8a',
//     Remark:'',
// }
// var line5 = {
//     from:temp5.id,
//     to:temp6.id,
//     label:'',
//     id: '9763f837-59f0-42cf-a893-c96abb4ab86f',
//     Remark:'',
// }
// var line6 = {
//     from:temp6.id,
//     to:temp7.id,
//     label:'',
//     id: '71790bfa-4f54-42bb-8697-6bcccd26c243',
//     Remark:'',
// }
// var line7 = {
//     from:temp7.id,
//     to:temp8.id,
//     label:'',
//     id: 'd08b47f6-6db9-4e96-8494-42df982950ef',
//     Remark:'',
// }
// lineList.push(line1)
// lineList.push(line2)
// lineList.push(line3)
// lineList.push(line4)
// lineList.push(line5)
// lineList.push(line6)
// lineList.push(line7)

export default {nodeList,lineList}