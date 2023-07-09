<template>
	<view class="content">
		<view class="openMail">留言板</view>
		<!-- 输入姓名 -->
		<view class="inputName"><input type="button" v-model="name" placeholder="请输入TA的名字或暗号！"><button
				@click="getMailList" plain='true' size="mini" type="default">搜索</button></view>
		<view style="height: 1px; border-top: 1px solid #979797;margin-top: 10px;">

		</view>
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
			</li>
		</view>

		<navigator url="../writeLeave/writeLeave" hover-class="navigator-hover">
			<uni-fab ref="fab" :pattern="pattern" horizontal="right" vertical="bottom" />
		</navigator>



	</view>
</template>

<script>
	export default {
		data() {
			return {
				//短信信息
				message: [],
				name: '',
				pattern: {
					icon: 'plus-filled',
					backgroundColor:'#949494',
					buttonColor:'#4794e7',
				}

			};
		},

		methods: {
			showModal() {
				uni.showToast({
					title: '发送成功！',
					duration: 1000
				});
			},
			getMailList() {
				const userPhone = uni.getStorageSync('userPhone');
				uni.request({ //获取该用户的短信详情数量
					url: 'https://1el9898253.oicp.vip/leaves/',
					data: {
						forName: this.name
					},
					success: (res) => {
						this.message = res.data.data
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

	.inputName {
		border-radius: 15px;
		background-color: rgb(255, 255, 255);
		height: 100%;
		margin-top: 20px;
		padding: 20px 15px;
		display: flex;
		flex-wrap: nowrap;
		justify-content: space-between;

		input {
			flex-grow: 2;
			padding-top: 5px;
		}

		button {
			flex-grow: 1;
		}

	}

	.openMailText {

		li {
			border-radius: 15px;
			background-color: rgb(255, 255, 255);
			height: 100%;
			margin-top: 20px;
			padding: 20px 15px;
			background-image: url(https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/email/图钉.png);
			background-size: 30px 30px;
			background-repeat: no-repeat;
			background-position: 5px -5px;

			.msg {
				display: flex;
				justify-content: flex-start; //元素沿着主轴起边排列
				height: 100%;
				margin-bottom: 10px;

				.img {
					width: 50px;
					height: 50px;
					border-radius: 50%;
					margin-right: 10px;

				}

				.imgName {
					white-space: pre-line; //识别换行符号
					font-family: 'Comic Sans MS';

					.name {
						position: relative;
						top: 5px;

					}
				}

				.imgTime {
					font-size: 12px;

				}
			}

			.openWords {
				font: optional;
				white-space: pre-line; //识别字符串中的换行符‘\n’
			}

		}
	}



	.content {
		padding: 0 5%;
	}
</style>