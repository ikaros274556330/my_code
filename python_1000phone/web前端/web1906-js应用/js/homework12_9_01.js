var num = 0
var img_list = new Array()
img_list[1] = 'img/作业bg/bg_1.jpg'
img_list[2] = 'img/作业bg/bg_2.jpg'
img_list[3] = 'img/作业bg/bg_3.jpg'
img_list[4] = 'img/作业bg/bg_4.jpg'
img_list[5] = 'img/作业bg/bg_5.jpg'
img_list[0] = 'img/作业bg/bg_6.jpg'

var radios = new Array()
radios[0] = 'r1'
radios[1] = 'r2'
radios[2] = 'r3'
radios[3] = 'r4'
radios[4] = 'r5'
radios[5] = 'r6'


function change_img(){
	img_obj = document.getElementById('image1')
	radio_obj = document.getElementById(radios[num])
	if(num>5){
		num = 0
	};
	img_obj.src = img_list[num]
	radio_obj.checked = 'checked'
	img_obj.width=600
	img_obj.height=400
	num++
}
setInterval('change_img()',3000)


//for(let x=0;x<=5;x++){
//	new_click = document.getElementById(radios[x])
//	new_click.onclick = function(){
//		img_obj1 = document.getElementById('image1')
//		img_obj1.src=img_list[x]
//	}
//	console.log(x)
//}

function change0(){
	img_obj = document.getElementById('image1')
	img_obj.src = img_list[0]
}

function change1(){
	img_obj = document.getElementById('image1')
	img_obj.src = img_list[1]
}

function change2(){
	img_obj = document.getElementById('image1')
	img_obj.src = img_list[2]
}

function change3(){
	img_obj = document.getElementById('image1')
	img_obj.src = img_list[3]
}

function change4(){
	img_obj = document.getElementById('image1')
	img_obj.src = img_list[4]
}

function change5(){
	img_obj = document.getElementById('image1')
	img_obj.src = img_list[5]
}