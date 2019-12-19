

function add_block(){
	box_obj = document.getElementById('box')
	new_block = document.createElement('div')
	new_str = document.getElementById('message').value
	new_p = document.createElement('p')
	new_p.innerText = new_str
	
	new_block.appendChild(new_p)
	new_buttom = document.createElement('button')
	new_buttom.innerText = 'X'
	new_buttom.onclick = function(){
		this.parentElement.remove()
	}
	new_block.appendChild(new_buttom)
	color = random_color()
	new_block.style.backgroundColor=color
	new_buttom.style.backgroundColor=color
	
	box_obj.appendChild(new_block)
	
}

add_=document.getElementById("add_buttom")
add_.onclick=add_block
//console.log(typeof 'aasd') 查询类型