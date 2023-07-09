<template>
	<view>
		<view class="mySelf">我的</view>
		<!-- 登陆 -->
		<view class="wxLogin">
			<!-- 头像 -->
			<img class="img" :src="message.img" alt="" srcset="" @click="login">
			<text class="imgName" @click="login">
				<text class="name">{{message.name}}\n</text>
				<text class="imgMsg">{{message.msg}}</text>
			</text>
			<button type="warn" size="mini" v-if="isLogin" @click="exitLogin"
				style="margin-right: 0;font-size: 12px;">退出</button>
		</view>

		<!-- 记录 -->
		<view class="records" v-if="isLogin">
			<li class="success">
				<navigator url="../mailBox/mailBox?id=success" hover-class="none">
					<view class="title">发送记录</view>
					<view class="number">
						<view>{{records.success | mailCount}} 条</view>
						<view style="margin-right: 1vw;">></view>
					</view>
				</navigator>
			</li>
			<li class="fail">
				<navigator url="../mailBox/mailBox?id=fail" hover-class="none">
					<view class="title">异常记录</view>
					<view class="number">
						<view>{{records.fail | mailCount}} 条</view>
						<view style="margin-right: 1vw;">></view>
					</view>
				</navigator>
			</li>
			<li class="reply">
				<navigator url="../mailBox/mailBox?id=reply" hover-class="none">
					<view class="title">我的回复</view>
					<view class="number">
						<view>{{records.reply | mailCount}} 条</view>
						<view style="margin-right: 1vw;">＞</view>
					</view>
				</navigator>
			</li>
		</view>

		<!-- 探索更多 -->
		<view class="mySelf" style="margin-top: 2vh;">探索更多</view>

		<view class="explore">
			<li class="question">
				<view class="title">常见问题</view>
				<view class="why">什么情况下会发送失败</view>
				<view class="btn">
					<navigator url="../question/question" hover-class="none">
						<button type="primary" size="mini">点击进入</button>
					</navigator>
				</view>
			</li>
		</view>
		
		<view class="service explore">
			<li class="question">
				<view class="title">联系客服</view>
				<view class="why">问题反馈，订单退款</view>
				<view class="btn">
					<navigator url="../service/service" hover-class="none">
						<button type="primary" size="mini">点击反馈</button>
					</navigator>
				</view>
			</li>
		</view>
		
		

	</view>
</template>

<script>
	export default {
		data() {
			return {
				src:'',
				message: {
					img: 'https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/email/0.png',
					name: '点击登陆',
					msg: '你将成为被宇宙贩卖的快乐'
				},
				isLogin: false, //是否登陆
				records: { //短信条数
					success: 0,
					fail: 0,
					reply: 0
				}
			}
		},
		onLoad() {
			this.getSisson()
		},
		onPullDownRefresh() {
			setTimeout(()=> {
				this.getSisson();
				uni.stopPullDownRefresh();
			}, 1000);
			

		},
		filters: {
			mailCount(e) {
				let res = Number(e)
				if (res > 999) {
					return "999+"
				}else if(!res){
					return 0
				}
				return e
			}
		},
		methods: {
			
			//从缓存中获取头像昵称
			getSisson() {
				const avatarUrl = uni.getStorageSync('avatarUrl');
				const nickName = uni.getStorageSync('nickName');
				const userPhone = uni.getStorageSync('userPhone');
				if (avatarUrl && nickName) {
					this.message.img = avatarUrl;
					this.message.name = nickName;
					this.isLogin = true
					uni.request({ //获取该用户的短信详情数量
						url: 'https://1el9898253.oicp.vip/MailCount/', 
						data: {
							phone: userPhone
						},
						method: 'POST',
						success: (res) => {
							
							if (res.statusCode == 200) { //请求成功获取到数据时
								const mailCount = res.data
								this.records.success = mailCount.successCount
								this.records.fail = mailCount.failCount
								this.records.reply = mailCount.replyCount
							} else { //请求失败获取数据失败时（前端缓存有登陆信息，后端数据库中没有的情况）
								uni.clearStorageSync();
								uni.showToast({
									title: '登陆失效请重新登陆！',
									duration: 2000
								});
								this.message.img =
									'https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/email/0.png';
								this.message.name = '点击登陆';
								this.isLogin = false
							}

						}
					});
				}

			},

			//跳转登陆页面
			login() {
				if (!this.isLogin) {
					uni.navigateTo({
						url: '../login/login'
					});
				}

			},


			//退出登陆，清除登陆信息
			exitLogin() {
				uni.clearStorageSync();
				this.message.img = 'https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/email/0.png';
				this.message.name = '点击登陆';
				this.isLogin = false
				uni.showToast({
					title: '退出成功',
					duration: 1000
				});

			}

			

		}
	}
</script>

<style lang="less">
	.mySelf {
		padding: 10px 15px;
		font-size: 20px;
		font-weight: bold;
	}

	.wxLogin {
		margin-right: 10%;
		margin-left: 5%;
		padding: 20px 15px;
		margin: 5px 15px;
		border-radius: 15px;
		background-color: rgb(255, 255, 255);

		height: 100%;
		display: flex;
		justify-content: flex-start; //元素沿着主轴起边排列
		align-items: center;

		.img {
			width: 70px;
			height: 70px;
			border-radius: 50%;
			margin-right: 10px;

		}

		.imgName {
			white-space: pre-line;
			font-family: 'Comic Sans MS';

			.name {
				position: relative;
				top: 5px;

			}
		}

		.imgMsg {
			font-size: 12px;

		}
	}
	
	.service{
		margin-top: 15px !important;
		.question{
			background-image: url(https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/email/IMG_1856.jpg) !important;
			background-size: 30vw 20vh !important;
			background-position: 63vw 1vh !important;
		}
	}
	.explore {
		margin: 0 15px;
		button{
			margin-top: 10px;
		}
		.question {
			border-radius: 15px;
			background-color: rgb(255, 255, 255);
			height: 100%;
			margin-top: 20px;
			padding: 20px 15px;
			background-image: url(https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/email/question.png);
			background-repeat: no-repeat;
			background-size: 25vw 20vh;
			background-position: 65vw 1vh;
			display: flex;
			flex-direction: column;
			justify-content: space-around;

			.title {
				font-size: 18px;
				font-weight: 500;
			}

			.why {
				font-size: 14px;
			}

		}

	}

	.records {
		display: flex;
		justify-content: space-around;
		padding: 0 15px;
		margin-top: 2vh;

		li {
			margin-right: 10%;
			margin-left: 5%;
			padding: 20px 15px;
			width: 22vw;
			margin: 5px 0;
			border-radius: 15px;
			background-color: rgb(255, 255, 255);

			.title {
				font-weight: bold;
				font-size: 16px;
				color: #4c9e44;
				margin-bottom: 2vh;
				letter-spacing: 0.5vw;
				text-align: center;
			}

			.number {
				font-size: 15px;
				text-indent: 1vw;
				display: flex;
				justify-content: space-between;


			}
		}
	}
</style>
