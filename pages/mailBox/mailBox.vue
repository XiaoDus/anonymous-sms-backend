<template>
	<view>
		<view class="topBar">
			<li @click="changeBtn('success')" :class="showStyle.success?'success showStyle':'success'">已发送</li>
			<li @click="changeBtn('fail')" :class="showStyle.fail?'fail showStyle':'fail'">发送失败</li>
			<li @click="changeBtn('reply')" :class="showStyle.reply?'reply showStyle':'fail'">我的回复</li>
		</view>

		<view class="lists" v-if="list" v-for="(i,index) in list" :key="index">
			<li class="MailText" @click='getMail(index)'>
				<view class="phone"><small><span>对方号码：</span>{{i.forPhone}}</small></view>
				<view class="Mail"><small><span>内容：</span>{{i.mail}}</small></view>
			</li>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				showStyle: { //顶部菜单样式
					success: true,
					fail: false,
					reply: false,
				},
				show: '', //没有信息时显示的照片
				list:[], //显示的短信信息
				listName:'', //当前列表的名称
				//短信信息
				listText: {
					success: null,
					fail: null,
					reply: null
				}
			}
		},
		onLoad(e) {
			// e是上页面传的顶部菜单名称
			this.getMailMessage(e.id)
		},
		onPullDownRefresh() {
			setTimeout(()=> {
				this.getMailMessage(this.listName);
				uni.stopPullDownRefresh();
			}, 1000);
			
		
		},
		methods: {
			getMailMessage(e){
				const userPhone=uni.getStorageSync('userPhone')
				uni.request({
					url: 'https://1el9898253.oicp.vip/getMailMessage/',
					data: {
						phone: userPhone
					},
					method: 'POST',
					success: (res) =>{
						this.listText['success']=res.data.successMail
						this.listText['fail']=res.data.failMail
						this.listText['reply']=res.data.replyMail
						this.changeBtn(e)
					}
				})
			},
			
			// 更换顶部菜单样式
			changeBtn(e) {
				for (var i in this.showStyle) {
					this.showStyle[i] = false
				}
				this.listName=e
				this.list=this.listText[e]
				this.showStyle[e] = true
			},
			
			// 携对应数据跳转到短信详情页
			getMail(e) {
				uni.navigateTo({
				  url: '../mailMessage/mailMessage',
				
				  success: (res)=>{
				    // 通过eventChannel向被打开页面传送数据
				    res.eventChannel.emit('mailMag', { data: this.list[e],name:this.listName })
				  }
				})

			}
		}
	}
</script>

<style lang="less">
	.topBar {
		padding: 20px 15px;
		margin: 5px 15px;
		border-radius: 15px;
		background-color: rgb(255, 255, 255);
		display: flex;
		justify-content: space-between;

		li {
			padding: 1vh 2vw;
		}
	}

	.showStyle {
		color: #4c9e44;
		border-bottom: #4c9e44 1px solid;
	}

	.lists {
		padding: 15px 10px;
		margin: 10px 15px;
		border-radius: 15px;
		background-color: rgb(255, 255, 255);
		display: flex;
		flex-direction: column;

		.MailText {
			background-image: url(https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/email/look.png);
			background-size: 3vh 3vh;
			background-repeat: no-repeat;
			background-position: 80vw 50%;
			span{
				font-weight: 500;
			}

			.Mail {
				margin-top: 1vh;
				text-overflow: ellipsis !important;
				overflow: hidden;
				white-space: nowrap;
				width: 60vw;
				small{
				text-overflow: ellipsis !important;
				overflow: hidden;
				white-space: nowrap;
				width: 60vw;
				}
				

			}
		}
	}
</style>
