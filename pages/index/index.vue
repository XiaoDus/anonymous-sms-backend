<template>
	<view>
		<view class="TopBar">秘名信使</view>

		<view class="card uni-flex uni-column">
			<li class="cardChild cardTop flex-item flex-item-V">
				<view class="cardTopTextTop"><span>你瞧</span><text class="textTop">被人惦记的感觉真好</text></view>
				<view class="cardTopTextBot">
					<view><text>至少在这个世界上</text></view>
					<view><text>你能真真切切的想到我</text></view>
				</view>
				<view class="btn"><button @click="forEmail" type="primary" >发送短信</button></view>
			</li>
			
			
			<li class="cardChild cardTop flex-item flex-item-V bj2"  style="margin-top: 20px;">
				<view class="cardTopTextTop"><span>传话</span><text class="textTop">将心事传递，情感相连</text></view>
				<view class="cardTopTextBot">
					<view><text>如果事与愿违</text></view>
					<view><text>请相信上天另有安排</text></view>
				</view>
				<view class="btn"><button @click="forLabour" type="primary" >人工传话</button></view>
			</li>
		
		</view>
	</view>
</template>
<script>
	export default {
		data() {
			return {
			
			}
		},
		
		methods: {
			showModal(){
				uni.showToast({
					title: '发送成功！',
					duration: 1000
				});
			},
			//跳转到发送短信页面
			forEmail(){
				uni.navigateTo({
					url: '../forEmail/forEmail'
				});
			},
			forLabour(){
				uni.navigateTo({
					url: '../labour/labour'
				});
			}
			
		}
	}
</script>
<style lang="less">
	.TopBar {
		padding: 10px 15px;
		font-size: 20px;
		font-weight: bold;

	}

	.card {
		height: 100%;
		padding: 0 15px;
		
		.bj2{
			background-image: url(https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/email/bj2.png) !important;
			
			background-size: 40% 70% !important;
		}
		.cardTop {
			height: 35vh !important;
			background: url(https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/email/bg.jpg) no-repeat border-box;
			background-size: 50% 100%;
			background-position: 90% 75%;
			padding: 20px 20px !important;
			// margin-top: 50px !important;
			

			.textTop {
				margin-left: 20px;
				font-size: 15px;
			}

			span {
				font-size: 15px;
				background-color: #f6f6f6;
				border-radius: 3px;
			}

			.cardTopTextBot {
				margin-top: 35px;
				font-weight: 500;
			}

			.btn {
				margin-top: 5vh;
				width: 100px;
				height:30px;
			}
		}
		.cardChild:nth-of-type(2){
				margin-top: 5vh;
			}
		.cardChild {
			border-radius: 15px;
			background-color: rgb(255, 255, 255);
			height: 55px;
			
			.cardTopTextTop{
				margin-top: 20px;
			}
			.cardSuperChild{
				display: flex;
				justify-content: space-between;
				align-items: center ;
				
				.text:nth-of-type(1){
					flex-grow: 1;
					width: 50px;
					height: 50px;
					border-radius: 50%;
					margin-right: 3px;
				}
				.text:nth-of-type(2){
					flex-grow: 3;
					:nth-child(1){
						font-size: 14px;
						font-weight:bold;
					}
					:nth-child(2){
						font-size: 10px;
						white-space: pre-wrap;
						overflow: auto;
					}
					
				}
				.text:nth-of-type(3){
					flex-grow: 1;
					transform: translateY(20%);
					button{
						border: #f1f1f1 solid 1px !important;
						border-radius: 20px !important;
					}
				}
				.img1{
					background: url(https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/email/email.png) no-repeat;
					background-size: 55px;
				}
				
				
				
			}
			
			
			

		}
	}
</style>
