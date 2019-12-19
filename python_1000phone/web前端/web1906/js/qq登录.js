var num = 0

function change_bg(){
	var img = Array()
	img[0] = '../img/qq邮箱登录页素材/tg-silence1e9c5d.jpg'
	img[1] = '../img/qq邮箱登录页素材/Snipaste_2019-12-07_11-09-08.png' 
	img[2] = '../img/qq邮箱登录页素材/Snipaste_2019-12-07_11-09-59.png'
	img[3] = '../img/qq邮箱登录页素材/Snipaste_2019-12-07_11-10-16.png'
	
	if(num>3){
		num = 0
	};
	
	var div=document.getElementById('mid11');
	div.style.backgroundImg= "url(../img/qq邮箱登录页素材/Snipaste_2019-12-07_11-09-59.png)"
	num++
}

setInterval('change_bg()',3000)
setInterval(console.log('换图了'),3000)
