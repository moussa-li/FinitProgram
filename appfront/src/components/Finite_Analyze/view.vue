<template>
    <iframe id="visaul" frameborder="no" style="width:100%;height: calc(100vh - 100px);"></iframe>
    <!--<img style="width:800px;height:500px;" :src="defaultImg" />  -->
</template>

<script>
import $ from 'jquery';
import { EventBus } from '@/store/Finite_Analyze/event-bus'
import deImg from '@/assets/mesh.png'

    export default {
        name:'view_3D',
        data(){
            return{
                visaul_data:'',
                defaultImg:deImg
            }

        },
        ready:function(){
        },
        mounted(){
            EventBus.$on('visaul', param => {
            let iframe=document.getElementById('visaul')
            console.log("this")
            
            iframe.contentWindow.document.open();
	        iframe.contentWindow.document.write(param.visaul_data);
	        iframe.contentWindow.document.close();
            })
        },
        methods:{
            init(){
            },
            test(){
            let iframe=document.getElementById('visaul')
            iframe.src='about:blank'
            console.log(iframe)

            }
        }
    }
// const renderer = new THREE.WebGLRenderer();
// renderer.setSize( '100px', '100px' );
// console.log(document.body)
// console.log($('#WebGL-output')[0])
// $('#WebGL-output')[0].appendChild( renderer.domElement );
// document.body.appendChild( renderer.domElement );


// const camera = new THREE.PerspectiveCamera( 45, window.innerWidth / window.innerHeight, 1, 500 );
// camera.position.set( 0, 0, 100 );
// camera.lookAt( 0, 0, 0 );
// const scene = new THREE.Scene();
// const material = new THREE.LineBasicMaterial( { color: 0x0000ff } );
// const points = [];
// points.push( new THREE.Vector3( - 10, 0, 0 ) );
// points.push( new THREE.Vector3( 0, 10, 0 ) );
// points.push( new THREE.Vector3( 10, 0, 0 ) );

// const geometry = new THREE.BufferGeometry().setFromPoints( points );
// const line = new THREE.Line( geometry, material );
// scene.add( line );
// renderer.render( scene, camera );

// function init() {

// //         // create a scene, that will hold all our elements such as objects, cameras and lights.
// //         var scene = new THREE.Scene();

// //         // create a camera, which defines where we're looking at.
//         var camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);

//         // create a render and set the size
//         var renderer = new THREE.WebGLRenderer();
//         renderer.setClearColorHex();
//         renderer.setClearColor(new THREE.Color(0xEEEEEE));
//         renderer.setSize(window.innerWidth, window.innerHeight);

//         // show axes in the screen
//         // var axes = new THREE.AxisHelper(20);
//         scene.add(axes);

//         // create the ground plane
//         var planeGeometry = new THREE.PlaneGeometry(60, 20);
//         var planeMaterial = new THREE.MeshBasicMaterial({color: 0xcccccc});
//         var plane = new THREE.Mesh(planeGeometry, planeMaterial);

//         // rotate and position the plane
//         plane.rotation.x = -0.5 * Math.PI;
//         plane.position.x = 15;
//         plane.position.y = 0;
//         plane.position.z = 0;

//         // add the plane to the scene
//         scene.add(plane);

//         // create a cube
//         var cubeGeometry = new THREE.BoxGeometry(4, 4, 4);
//         var cubeMaterial = new THREE.MeshBasicMaterial({color: 0xff0000, wireframe: true});
//         var cube = new THREE.Mesh(cubeGeometry, cubeMaterial);

//         // position the cube
//         cube.position.x = -4;
//         cube.position.y = 3;
//         cube.position.z = 0;

//         // add the cube to the scene
//         scene.add(cube);

//         // create a sphere
//         var sphereGeometry = new THREE.SphereGeometry(4, 20, 20);
//         var sphereMaterial = new THREE.MeshBasicMaterial({color: 0x7777ff, wireframe: true});
//         var sphere = new THREE.Mesh(sphereGeometry, sphereMaterial);

//         // position the sphere
//         sphere.position.x = 20;
//         sphere.position.y = 4;
//         sphere.position.z = 2;

//         // add the sphere to the scene
//         scene.add(sphere);

//         // position and point the camera to the center of the scene
//         camera.position.x = -30;
//         camera.position.y = 40;
//         camera.position.z = 30;
//         camera.lookAt(scene.position);

//         // add the output of the renderer to the html element
//         document.getElementById("WebGL-output").appendChild(renderer.domElement);

//         // render the scene
//         renderer.render(scene, camera);
//     }
//     window.onload = init;

// export default {
// }
</script>
