//function func1(x,y){
//	return x+y
//}

//for(let x=1;x<=100;x++){
//	console.log(x);
//}


nums = new Array()

for(let x=101;x<=200;x++){
	for(let y=1;y<=x;y++){
		if(x%y==0){
			nums.push(x);
		}
	};
	if(nums.length==2){
		console.log(nums[1])
	}
	nums=[]
}

//var num = 0
//
//function change_image(){
//	var img = []
//	img[0] = "img/bg_img/716428.png"
//	img[1] = "img/bg_img/118479.jpg"
//	img[2] = "img/bg_img/d9e1d8d00dd71cf75406b5a2081bef6a.jpg"
//	img[3] = "img/bg_img/image3.jpg"
//	
//	if(num>3){
//		num=0
//	};
//	
//	imgobj = document.getElementById('image1');
//	imgobj.src = img[num]
//	num++
//}
//
//setInterval('change_image()',3000)

//year = 2400
//
//if((year%4==0&&year%100!=0)||year%400==0){
//	console.log(year,'是闰年');
//}else{
//	console.log(year,'不是闰年')
//}


//单词反
//str1 = new String('how are you')
//
//console.log(str1.split(' ').reverse().join(' '))

