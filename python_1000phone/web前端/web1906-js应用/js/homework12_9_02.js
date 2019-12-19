var reg = /川[A-Za-z][0-9a-zA-Z]{5}/
var mydate=new Date();
console.log(mydate.getDay())
c = [1,2,3]
function cheack_carID(){
	var i = 0
	var num_list=[]
	p_obj = document.createElement('p')
	box_obj = document.getElementById('box')
	car_num = document.getElementById('car_ID').value
	if(reg.test(car_num)){
		for(x of car_num){
			if(/\d/.test(x)){
				i++
				num_list.push(x)
			};
			if(i>=3){
				if(mydate.getDay()==2){
					if(num_list[num_list.length-1]==1||num_list[num_list.length-1]==6){
						p_obj.innerText='今天限号！'
					}else{
						p_obj.innerText='今天不限号！'
					}
					box_obj.appendChild(p_obj)
				}
			}
		}
	}
}
