<template>
	<view>
		<view class="wMail">短信详情</view>
		<view class="uni-flex uni-column email">

			<!-- 手机号 -->
			<li class="flex-item flex-item-V phone">
				<view class="uni-input">手机号：{{phone}}</view>
			</li>

			<!-- 短信内容 -->
			<li class="flex-item flex-item-V " style="font-size: 14px;" v-if="listName=='reply'?true:false">
				我的短信:  {{myMail}}
			</li>

			<!-- 短信内容 -->
			<li class="flex-item flex-item-V mailText">
				回复我的:  {{text}}
			</li>
			<!-- 公开信 -->
			<li class="flex-item flex-item-V openMail" v-if="listName=='reply'?false:true">
				<view class="openText"><img
						src="https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/email/wenhao.png"
						@click='openClick'>公开展示</view>
				<switch color="#51aa38" :checked="isOpen" :disabled="listName=='fail'?true:false"
					@change="switch1Change" style="transform:scale(0.7)" />
			</li>

			<li class="flex-item flex-item-V sendMail">
				<button type="primary" @click="back">返回</button>
			</li>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				phone: '',
				isOpen: null,
				text: '',
				myMail: '',
				uid: '',
				listName: ''

			};

		},
		onLoad() {
			this.getMailMsg()
		},
		methods: {
			//获取上页面传输的数据
			getMailMsg(e) {
				const eventChannel = this.getOpenerEventChannel();
				// 监听mailMag事件，获取上一页面通过eventChannel传送到当前页面的数据
				eventChannel.on('mailMag', (data) => {
					console.log(data)
					const message = data.data
					if (data.name == 'success') {
						this.phone = message.forPhone
						this.isOpen = message.isOpen
						this.text = message.mail
						this.uid = message.uid
						this.listName = data.name
					} else if (data.name == 'reply') {
						this.phone = message.forPhone
						this.isOpen = message.isOpen
						this.text = message.mail
						this.myMail = message.myMail
						this.uid = message.uid
						this.listName = data.name
					}


				})
			},

			//修改公开匿名
			switch1Change(e) {
				const changeValue = e.detail.value
				if (changeValue) { //后端1为true，0为false
					this.isOpen = 1
				} else {
					this.isOpen = 0
				}

				uni.request({
					url: 'https://1el9898253.oicp.vip/getMailMessage/',
					data: {
						uid: this.uid,
						listName: this.listName,
						isOpen: this.isOpen
					},
					success: (res) => {
						uni.showToast({
							title: '修改成功',
							duration: 1000
						});
					}
				})

			},

			//返回上一页并刷新
			back() {
				const pages = getCurrentPages() //获取当前打开的页面，当前页为最后一页
				const beforePage = pages[pages.length - 2] //获取上一页
				uni.navigateBack({
					success: () => {
						beforePage.$vm.getMailMessage(this.listName); // 执行上一页的onLoad里面的方法方法
					}
				})
			}

		}
	}
</script>

<style lang="less">
	.wMail {
		padding: 10px 15px;
		font-size: 20px;
		font-weight: bold;
	}

	.email {

		margin-right: 10%;
		margin-left: 5%;
		padding: 0;

		li {
			border-radius: 15px;
			background-color: rgb(255, 255, 255);

			width: 95%;
			margin-top: 20px;
			padding: 15px 15px;

		}

		.phone {
			display: flex;
			justify-content: space-between;
			height: 25px;
			font-size: 14px;
			align-items: center;
		}

		.mailText {
			font-size: 14px;
			background-color: white;
			background-image: url(https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/email/sk.png);
			background-size: 30% 65%;
			background-repeat: no-repeat;
			background-position: 95% 100%;
			min-height: 30vh;



		}

		.consent {
			.tys {
				font-weight: bold;
				vertical-align: -3px; //与图标对其

			}
		}

		.openMail {
			display: flex;
			justify-content: space-between;
			align-items: center;

			img {
				width: 18px;
				height: 18px;
				vertical-align: -15%;
				margin-right: 7px;
			}
		}

		.sendMail {
			padding: 0;
			width: 105%;
			margin: 50px 0;

			.sendBtn {
				background-color: #51aa38;
				border: #51aa38;
				border-radius: 25px;
				color: white;
			}
		}
	}

	.noBg {
		background-color: #d7d7d7 !important;
	}
</style>