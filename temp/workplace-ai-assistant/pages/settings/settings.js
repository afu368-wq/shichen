// pages/settings/settings.js
const storage = require('../../utils/storage')

Page({
  data: {
    profile: null
  },

  onLoad() {
    const profile = storage.getUserProfile()
    this.setData({ profile })
  },

  // 重新录入
  onResetProfile() {
    wx.showModal({
      title: '确认重新录入？',
      content: '您的基本信息将被清除，需重新填写。',
      confirmColor: '#6D8B74',
      success: (res) => {
        if (res.confirm) {
          storage.clearAll()
          wx.reLaunch({ url: '/pages/onboarding/onboarding' })
        }
      }
    })
  },

  // 查看版本
  onAbout() {
    wx.showModal({
      title: '关于',
      content: '职场时位 v0.1.0 (MVP)\n\n专为职场女性打造的每日时位建议助手。',
      showCancel: false,
      confirmText: '知道了'
    })
  }
})