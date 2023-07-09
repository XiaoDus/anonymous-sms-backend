<template>
	<view>

		<uni-notice-bar show-icon scrollable speed=80
			text="由于信息需要经过添加好友传递，可能会导致信息的延迟,因对方不同意无法发送可以联系客服退款.如果您需要尽快传递信息，请选择发送短信." />

		
		<view class="uni-flex uni-column email">

			<!-- 联系方式 -->
			<li class="flex-item flex-item-V phone way">
				<picker style="text-align: center;" @change="bindPickerChange" :value="index" :range="array">
					<view class="uni-input">{{array[index]}}</view>
				</picker>
			</li>

			<!-- 账号 -->
			<li class="flex-item flex-item-V phone">
				<input class="uni-input" type="number" :value="phoneNum" placeholder="请输入对方账号" @input="inputPhone" />
				<icon type="clear" size="15" v-if="showClearIcon" @click="clearIcon" />
			</li>

			<!-- 短信内容 -->
			<li class="flex-item flex-item-V mailText">
				<textarea class="textarea" maxlength="9999" placeholder="点击输入短信内容(表白、祝福、吐槽等...)" v-model="mailText"
					@input="inputText"></textarea>

				<text class="wordNumber">{{words}}/∞</text>
				<view>
					<text class="wordMoney">人工传话不限字数，人工费用10元</text>
				</view>
			</li>

			<!-- 公开信 -->
			<li class="flex-item flex-item-V openMail">
				<view class="openText"><img
						src="https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/email/wenhao.png"
						@click='openClick'>公开展示</view>
				<switch color="#51aa38" @change="switch1Change" style="transform:scale(0.7)" />
			</li>



			<!-- 用户协议 -->
			<li class="flex-item flex-item-V consent">
				<checkbox-group @change="checkboxChange">
					<checkbox :checked="consent" style="margin-right: 5px;" />
					<text class="tys">我已同意<text @click="userAgreement"
							style="color: green">《用户协议》</text>，并遵守和承担相关法律法规</text>
				</checkbox-group>
			</li>
			<li class="flex-item flex-item-V sendMail">
				<button :class="consent?'sendBtn':'sendBtn noBg'" :disabled="!consent"
					@click="sendMail">{{sendText}}发送</button>
			</li>
		</view>
	</view>
</template>

<script>
	import sensitiveWord from '../../static/smsSensitiveWord.js' //敏感词汇列表
	export default {
		data() {
			return {
				array: ['请选择联系方式', '微信', 'QQ', '抖音', '快手', '微博', '小红书'],
				index: 0,
				consent: false, //是否勾选协议
				showClearIcon: false, //清除手机号符号
				openMail: 0, //是否公开 默认关闭
				phoneNum: '', //对方账号
				mailText: '', //短信内容
				words: 0, //字数
				sendText: '私密' //私密发送？公开发送
			};

		},
		onLoad() {
			this.openMail = 0
			this.mailText = ''
			this.phoneNum = ''
			this.userAgreement()

		},
		methods: {
			// 用户条款
			userAgreement() {
				uni.showModal({
					title: '用户协议',
					confirmText: '我已同意',
					showCancel: false,
					content: '为了维护内容质量及友善的社区氛围，平台会依据本规范中的条款对用户和用户发布的内容进行管理。\n\n一、 基本原则\n\n1. 规范适用于所有用户。\n2. 须遵纪守法， 对他人保持友善和尊重。 不得发表违背法律法规及社会公德的内容， 用户需要对自己发表的内容负责， 平台有权删除不符合社区规范的内容。\n3. 用户访问或使用我方产品， 即视为同意接受本规范的全部内容。\n二、平台可能采取删除违规内容、 终止违规用户使用功能等方式， 对以下违法、 不良信息或存在危害的行为进行处理。\n1 违反法律法规： 发布违反国家相关法律法规及管理规定的\n\n* 信息， 包括但不限于以下几点：\n* 反对宪法所确定的基本原则 \n* 危害国家安全， 泄露国家秘密， 颠覆国家政权， 破坏国家统一 \n* 损害国家荣誉和利益 \n* 煽动民族仇恨、 民族歧视， 破坏民族团结 \n* 侮辱、 滥用英烈形象， 否定英烈事迹， 美化粉饰侵略战争行为的 \n* 破坏国家宗教政策， 宣扬邪教和封、建迷信 \n* 散布谣言、扰乱社会秩序、破坏社会稳定宣扬淫秽、 色情、 赌博、 暴力、 凶杀、 恐怖或者教唆犯罪 \n* 煽动非法集会、 结社、 游行、 示威、 聚众扰乱社会秩序*诽谤他人， 泄露他人隐私， 侵害他人合法权 \n* 含有法律、 行政法规禁止的其他内容的信息 \n2. 不友善行为，包括但不限于以下几点：\n\n* 人身攻击及辱骂他人。\n*针对以下群体发表祖咒、歧视、漠视生命尊严等性质的言论，群体包括：国籍、地域、性别、性别认同、性倾向、种族、疾病、宗教、残障群体等。\n*对他人进行诅咒、恐吓或威胁。\n针对他人的私德、观点立场、素质、能力等方面的贬低或不尊重。\n* 讽刺他人，阴阳怪气地表达批评。\n* 对他人使用粗俗用语，并产生了冒犯。\n3. 发布垃圾广告信息：用户以推广曝光为目的，发布影响用户体验、扰乱社区秩序的内容，或进行相关行为，包括但不限于以下几点：\n\n* 多次发布包含售卖产品、提供服务、宣传推广内容的垃圾广告。\n* 使用严重影响用户体验的违规手段进行恶意营销。\n4. 恶意行为：滥用产品功能，进行影响用户体验，危及平台安全及损害他人权益的行为。包括但不限于以下几点：\n* 重复发布干扰正常用户体验的内容。\n* 发布含有潜在危险的内容，或使用第三方网站伪造跳转链接，如钓鱼网站、木马、病毒网站等。\n5. 色情低俗信息，包括但不限于以下几点：\n\n*包含自己或他人性经验的细节描述或露骨的感受描述\n* 涉及色情段子、两性笑话的低俗内容\n* 带有性暗示、性挑逗等易使人产生性联想\n*展现血腥、惊悚、残忍等致人身心不适\n*炒作绯闻、丑闻、劣迹等\n* 宣扬低俗、庸俗、媚俗内容\n6. 不实信息，包括但不限于以下几点：\n\n*可能存在事实性错误或者造谣等内容\n* 存在事实夸大、伪造虛假经历等误导他人的内容\n*伪造身份、冒充他人，通过头像、用户名等个人信息暗示自己具有特定身份，或与特定机构或个人存在关联\n7.传播封建迷信，包括但不限于以下几点：\n\n*宣扬鼓励封建迷信等活动，推广算命等理论\n8. 其他危害行为或内容，包括但不限于以下几点：\n* 可能引1发未成年人模仿不安全行为和违反社会公德行为、诱导末成年人不良嗜好影响末成年人身心健康的\n*不当评述自然灾害、重大事故等灾难的\n* 美化、粉饰侵略战争行为的\n*法律、行政法规禁止，或可能对网络生态造成不良影响的其他内容',

					success: (res) => {
						if (res.confirm) {
							this.consent = true
							const userPhone = uni.getStorageSync('userPhone');
							const nickName = uni.getStorageSync('nickName');
							const avatarUrl = uni.getStorageSync('avatarUrl');
							if (!userPhone && !nickName && !avatarUrl) {
								uni.showModal({
									title: '提示',
									content: '请先登陆',
									showCancel: false,
									success: function(res) {
										if (res.confirm) {
											uni.navigateTo({
												url: '../login/login'
											});
										}
									}
								});
							}
						}
					}
				});
			},

			//输入手机号，出现删除符号
			inputPhone: function(event) {
				this.phoneNum = event.detail.value;
				if (event.detail.value.length > 0) {
					this.showClearIcon = true;
				} else {
					this.showClearIcon = false;
				}
			},
			//清除手机号
			clearIcon: function() {
				this.phoneNum = '';
				this.showClearIcon = false;
			},
			//方式选择器
			bindPickerChange: function(e) {
				this.index = e.detail.value
			},
			//统计字数
			inputText() {
				var num = 0
				for (let i = 0; i < sensitiveWord.length; i++) { //循环敏感词汇列表sensitiveWord
					const word = sensitiveWord[i];
					const regex = new RegExp(word, 'gi');
					const replacement = '*'.repeat(word.length);
					this.mailText = this.mailText.replace(regex, replacement);
				}
				this.words = this.mailText.length //统计字数




			},

			//公开信开关
			switch1Change(e) {
				if (e.detail.value) {
					this.sendText = '公开'
					this.openMail = 1
				} else {
					this.sendText = '私密'
					this.openMail = 0
				}
			},

			//公开解释
			openClick() {
				uni.showModal({
					title: '公开说明',
					content: '开启公开展示，即同意在本程序中公开展示短信内容！\n\n仅展示短信内容，不展示个人信息！',
					showCancel: false,
				});
			},

			//是否勾选用户条款
			checkboxChange() {
				this.consent = !this.consent
			},

			//随机生成订单号
			randomString() {
				var result = '';
				var str = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
				for (var i = 11; i > 0; --i) result += str[Math.floor(Math.random() * str.length)];
				return result;
			},
			//获取本机ip地址
			getIp() {
				const ip = ''
				uni.request({
					url: 'http://pv.sohu.com/cityjson?ie=utf-8',
					method: 'POST',
					success: (res) => {
						const reg = /\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/;
						ip = reg.exec(res.data)[0];

					}
				})
				return ip
			},

			//发送短信
			sendMail() {
				if (this.phoneNum && this.mailText && this.index != 0) {
					//请求订单
					const userPhone = uni.getStorageSync('userPhone');
					const nickName = uni.getStorageSync('nickName');
					const avatarUrl = uni.getStorageSync('avatarUrl');
					const forPhone = this.phoneNum
					const mailText = this.mailText
					const isOpen = this.openMail
					const sendWay = this.index
					const out_trade_no = this.randomString() //订单号

					uni.request({ //生成预订单
						url: 'https://1el9898253.oicp.vip/get_prepay_order/',
						data: {
							userPhone: userPhone,
							body: '发给' + this.array[sendWay] + '用户' + forPhone + '的人工传话',
							out_trade_no: out_trade_no,
							total_fee: 100,
							ip: '127.0.0.1',
						},
						method: 'POST',
						success: (res) => {
							if (res.data.code == 200) {
								uni.requestPayment({
									provider: 'wxpay', // 支付服务提供商，此处为微信支付
									timeStamp: res.data.timeStamp, // 时间戳，从预支付订单中获取
									nonceStr: res.data.nonce_str, // 随机字符串，从预支付订单中获取
									package: 'prepay_id=' + res.data.static, // 订单详情扩展字符串，从预支付订单中获取
									signType: 'MD5', // 签名算法，固定为 MD5
									paySign: res.data.sign,
									success: function(res) {
										uni.request({ //发送该用户的短信详情并保存数据库
											url: 'https://1el9898253.oicp.vip/labour/',
											data: {
												userPhone: userPhone,
												forPhone: forPhone,
												mailText: mailText,
												isOpen: isOpen,
												nickName: nickName,
												avatarUrl: avatarUrl,
												out_trade_no: out_trade_no,
												sendWay: sendWay
											},
											method: 'POST',
											success: (res) => {
												if (res.data.static == 200) {
													const pages =
														getCurrentPages() //获取当前打开的页面，当前页为最后一页
													const beforePage = pages[pages
														.length - 2] //获取上一页
													uni.navigateBack({
														success() {
															// beforePage.onLoad() //执行上一页onLoad()
															if (beforePage
																.$page
																.fullPath ==
																'/pages/index/index'
															) {
																beforePage.$vm
																	.showModal() //同上，同等效果
															}
															
														}
													});
												} else if (res.data.static == 500) {
													uni.showModal({
														title: '提示',
														content: '用户登陆失效，请重新登陆！',
														showCancel: false,
														success: function(
															res) {
															if (res
																.confirm) {
																uni.navigateTo({
																	url: '../login/login'
																});
															}
														}
													});
												}
											}
										});
									},
									fail: function(err) {
										uni.showToast({
											icon: 'error',
											title: '支付失败！',
											duration: 1000,
										});
									}
								});
							} else {
								uni.clearStorageSync();
								uni.showModal({
									title: '提示',
									content: '用户登陆失效，请重新登陆！',
									showCancel: false,
									success: function(res) {
										if (res.confirm) {
											uni.navigateTo({
												url: '../login/login'
											});
										}
									}
								});
							}

						}
					})
				} else if (this.phoneNum && this.index != 0) {
					uni.showToast({
						icon: 'error',
						title: '短信不能为空',
						duration: 1000,
					});
				} else if (this.index != 0 && this.mailText) {
					uni.showToast({
						icon: 'error',
						title: '账号不能为空',
						duration: 1000,
					});
				} else if (this.phoneNum && this.mailText) {
					uni.showToast({
						icon: 'error',
						title: '请选择联系方式',
						duration: 1000,
					});
				} else {
					uni.showToast({
						icon: 'error',
						title: '内容不能为空',
						duration: 1000,
					});
				}
			}
		}
	}
</script>

<style lang="less">


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

		.way {
			display: block !important;
			text-align: center;
		}

		.mailText {
			font-size: 14px;
			background-color: white;
			background-image: url(https://mp-891a44a8-f007-4426-a7a4-607ad2bc43d0.cdn.bspapp.com/email/sk.png);
			background-size: 30% 65%;
			background-repeat: no-repeat;
			background-position: 95% 100%;

			.wordNumber {
				color: #afafaf;
				font-size: 10px;
			}

			.wordMoney {
				color: #77d084;
				font-size: 10px;
			}


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
			margin-top: 50px;

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