var flag = false


obj_block = document.getElementById('box')
obj_block.onmousedown = function(evt){
	x = evt.offsetX
	y = evt.offsetY
	flag = true
}

obj_block.onmouseup = function(){
	flag = false
}

obj_block.onmousemove=function(evt){
	if(flag){
		this.style.left=evt.clientX-x + 'px'
		this.style.top=evt.clientY-y + 'px'
	}else{
		return
	}
};

(function(){
	console.log('1'+2)
})()
