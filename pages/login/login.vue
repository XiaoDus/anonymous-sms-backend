<template>
	<view>

		<view class="loginMsg">

			<view class="img">
				<button open-type="chooseAvatar" class="mini-btn" hover-class="none" @chooseavatar="onChooseAvatar">
					<img :src="avatarUrl"><span class="imgText" v-if='showText'>更换图片</span>
				</button>
			</view>

			<view class="nickeName">
				<text>昵称</text>
				<input type="nickname" @focus="getName" @blur="getName" maxlength="8" class="inputName"
					placeholder="请输入昵称" />
			</view>

			


			<view class="loginBtn">
	
				<button type="primary" form-type="submit" size="default" open-type="getPhoneNumber" @getphonenumber="login">登陆</button>
			</view>

		</view>

	</view>
</template>

<script>
	import {
		nextTick
	} from "vue";
	export default {
		data() {
			return {
				avatarUrl: "https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/email/0.png",
				nickName: '',
				upImgurl:'',
				showText: true,
			};
		},
		methods: {

			//选择头像获取url
			onChooseAvatar(e) {
				this.avatarUrl = e.detail.avatarUrl
				this.showText = false
			},

			// 获取昵称
			getName(e) {
				this.nickName = e.detail.value

			},
			
			
			
			//登陆，保存头像昵称到缓存，返回上一页并刷新
			login(e) {
				
				const encryptedData=e.detail.encryptedData
				const iv=e.detail.iv
				
				if(encryptedData&&iv){
					if (this.nickName) {
						wx.cloud.init()
						const filePath = this.avatarUrl
						let cloudPath = "userPhoto/" + this.nickName + Date.now() + ".jpg";
						wx.cloud.uploadFile({
						      cloudPath,
						      filePath: filePath
						    }).then((res)=>{
								this.upImgurl=res.fileID
								console.log(res.fileID)
								//验证openid
								uni.login({
									provider: 'weixin',
									success: (res) => {
										
										// 发送 code 到后端，后端通过 code 获取 session_key 和 openid
										uni.request({
											url: 'https://1el9898253.oicp.vip/getSessionKey/',
											method: 'POST',
											data: {
												code: res.code,
												name: this.nickName,
												url: this.upImgurl,
												iv:iv,
												encryptedData:encryptedData
											},
											success: (res) => {
												if(res.data.phoneNumber){
													uni.setStorageSync('avatarUrl', this.upImgurl);
													uni.setStorageSync('nickName', this.nickName);
													uni.setStorageSync('userPhone', res.data.phoneNumber);
													const pages = getCurrentPages() //获取当前打开的页面，当前页为最后一页
													const beforePage = pages[pages.length - 2] //获取上一页
													uni.navigateBack({
														success() {
															// beforePage.onLoad() //执行上一页onLoad()
															if(beforePage.$page.fullPath=='/pages/myself/myself'){
																beforePage.$vm.getSisson() //同上，同等效果
															}
																		
														}
													});
												}else{
													uni.showToast({
															title: "再试一次！",
															duration: 1000,
															icon: "error"
													})
												}
											}
										});
									}
								})
							})
							
							
							
							
							
								
								
							
						// });
					}
				}
				 else if (!this.nickName) {
						uni.showToast({
							title: "昵称不能为空！",
							duration: 1000,
							icon: "error"
						})
					}else{
						uni.showToast({
							title: "登陆失败！",
							duration: 1000,
							icon: "error"
					})

				}


			}
		}

	}
</script>

<style lang="less">
	.loginMsg {
		display: flex;
		flex-direction: column;
		align-items: center;


		.img {
			margin-bottom: 10px;
			margin-top: 100px;

			button::after {
				border: none;
			}

			img {
				width: 80px;
				height: 80px;
				border-radius: 15px;
				position: relative;
			}

			.imgText {
				position: absolute;
				font-size: 15px;
				color: dimgray;
				right: 22px;
				top: 25px;

			}
		}




		.nickeName {
			width: 100%;
			display: flex;
			justify-content: flex-start;
			border-top: 2px solid rgba(232, 232, 232, 0.5);
			border-bottom: 2px solid rgba(232, 232, 232, 0.5);
			position: relative;

			.inputName {
				// text-align: center;
				padding: 15px 15px;
				position: absolute;
				left: 36vw;


			}

			text {
				padding: 15px 15px;
				font-weight: 400;
			}
		}

		.loginBtn {
			margin-top: 40vh;

			button {
				padding: 0 70px;
			}
		}
	}
</style>
