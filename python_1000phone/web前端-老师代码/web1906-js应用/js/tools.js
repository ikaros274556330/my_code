
// 产生随机颜色
function randowColor(alpha=1){
	r = parseInt(Math.random()*255)
	g = parseInt(Math.random()*255)
	b = parseInt(Math.random()*255)
	//rgba(1, 23, 45, 1)
	return 'rgba('+r+','+g+','+b+','+alpha+')'
}


