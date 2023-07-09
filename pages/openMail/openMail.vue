<template>
	<view>
		<view class="openMail">公开信</view>
		<!-- 遍历短信信息 -->
		<view class="uni-flex uni-column openMailText" v-for="i in message" :key="i">
			<!-- 公开信息 -->
			<li class="flex-item flex-item-V">
				<!-- 头像 -->
				<view class="msg">
					<img class="img" :src="i.imgUrl" alt="" srcset="">
					<text class="imgName">
						<text class="name">{{i.nickName}}\n</text> 
						<text class="imgTime">{{i.sendTime}}</text></text>
					
				</view>
				<!-- 内容 -->
				<view class="openWords">{{i.mail}}</view>
				<!-- 置顶点赞 -->
				<view class="topWords">
					
				</view>
			</li>


		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				//短信信息
				message: []

			};
		},
		onPullDownRefresh () {
			setTimeout(()=> {
				this.getMailList();
				uni.stopPullDownRefresh();
			}, 1000);
		},
		onShow() {
			this.getMailList()
		},
		onLoad() {
			this.getMailList()
		},
		methods:{
			getMailList(){
				const userPhone = uni.getStorageSync('userPhone');
				uni.request({ //获取该用户的短信详情数量
					url: 'https://1el9898253.oicp.vip/openMailMessage/', 
					success: (res) => {
						this.message=res.data.data
					}
				});
			}
		}
		
	}
</script>

<style lang="less">
	.openMail {
		padding: 10px 15px;
		font-size: 20px;
		font-weight: bold;
	}

	.openMailText {
		margin-right: 10%;
		margin-left: 5%;
		padding: 0;

		li {
			border-radius: 15px;
			background-color: rgb(255, 255, 255);
			width: 95%;
			height: 100%;
			margin-top: 20px;
			padding: 20px 15px;
			background-image: url(https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/email/图钉.png);
			background-size: 30px 30px;
			background-repeat: no-repeat;
			background-position: 5px -5px;
			
			.msg{
				display: flex;
				justify-content: flex-start; //元素沿着主轴起边排列
				height: 100%;
				margin-bottom: 10px;
				.img{
					width: 50px;
					height: 50px;
					border-radius:50%;
					margin-right: 10px;
					
				}
				
				.imgName{
					white-space: pre-line; //识别换行符号
					font-family: 'Comic Sans MS';
					.name{
						position: relative;
						top: 5px;
						
					}
				}
				
				.imgTime{
					font-size: 12px;
					
				}
			}
			
			.openWords{
				font: optional;
				white-space: pre-line; //识别字符串中的换行符‘\n’
			}

		}
	}
</style>
