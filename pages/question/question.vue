<template>
	<view style="padding-top: 5vh;">
		<view class="questions" v-for="i,index in question" :key="index">
			<view class="title">{{i.title}}</view>
			<view class="text">{{i.text}}</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				question: [{
						title: '一、因收件人原因导致失败\n\n',
						text: '1．当收件人手机关机、账户余额不足，停机等情况会导致短信发送失败。\n2．当收件人开通高频骚扰电话拦截业务时短信服务商会发送短信但无法送达。\n\n'
					},
					{
						title: '二、部分违规内容导致失败：\n\n',
						text: '1．内容违规导致发送失败不会退款，其次违规会触发封号，千万注意。\n2. 发送营销内容， 网址， 脏话， 不健康不利于团结等都属于违规内容。\n3. 短信审核非常严格， 有关部门会监管， 请文明用词。 \n4. 人工+智能双重审核， 任何不文明用词都会拦截并被判定违规。\n\n'
					},
					{
						title:'三、系统故障\n\n',
						text:'1.公众号平台可能遇到系统故障或技术问题，导致无法发送匿名短信。这种情况下，建议稍后再试或联系平台客服寻求帮助。\n2.此类短信运营商将在22:00-8:00停止发送短信避免打扰用户。\n\n'
					},
					{
						title:'四、频率限制\n\n',
						text:'公众号平台为了防止滥用，可能对发送匿名短信的频率进行限制。如果发送过于频繁，可能会导致发送失败。\n\n'
					}
					
				]
			};
		}
	}
</script>

<style lang="less">
	.questions{
		padding: 0 3vw;
		.title{
			white-space: pre-line;
			font-size: 15px;
			font-weight: 500;
		}
		.text{
			white-space: pre-line;
			padding-left: 2em;
			font-size: 14px;
		}
	}
</style>
