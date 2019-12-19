
$.ajax({
	type:"get",
	url:"http://rap2api.taobao.org/app/mock/239755/shoppingCart",
	data:{userId:'1111'},
	success: function(result){
		console.log(result)
		renderData(result.goodsList)
	}
});



function renderData(data){

	//1.给商品对象添加新的属性
	for(var goods of data){
		goods.isSelect = false
	}
	
	//2.创建Vue对象
	var app1 = new Vue({
		el: '#app1',
		data:{
			goodsList:data,
			isSelectAll:false
		},
		computed:{
			//统计总价
			totalPrice:function(){
				var sum = 0
				for(let goods of this.goodsList){
					if(goods.isSelect){
						sum += goods.count * goods.price
					}
				}
				return sum.toFixed(2)
			},
			//统计选中的数量
			totalSelectCount:function(){
				var count = 0
				for(let goods of this.goodsList){
					if(goods.isSelect){
						count += goods.count
					}
				}
				return count
			}
		},
		methods:{
//			[9, 11, 23, 2, 3, 30]
//  index = 0; 0<6;  9<10  -> [11, 23, 2, 3, 30];  index=-1; index=0
//  index = 0; 0<5;  11<10 ; index=1
			//删除选中
			delSelect:function(){
				for(var index=0; index<this.goodsList.length;index++){
					if(this.goodsList[index].isSelect){
						this.goodsList.splice(index,1)
						index --
					}
				}
				
			},
			//选中全部
			selectAll:function(){
				for(let goods of this.goodsList){
					goods.isSelect = this.isSelectAll
				}
			},
			//删除商品
			delGoods:function(goods){
				console.log(this.goodsList)
				for(index in this.goodsList){
					if (this.goodsList[index] == goods){
						this.goodsList.splice(index,1)
						break
					}
				}
			},
			//输入数量
			inputCount:function(goods){
				if(goods.count<0){
					goods.count *= -1
				}else if (goods.count == 0){
					goods.count = 1
				}
			},
			//商品数量减少
			subCount:function(goods){
				goods.count --
				if(goods.count<1){
					goods.count = 1
				}
			}
		}
	})
}
