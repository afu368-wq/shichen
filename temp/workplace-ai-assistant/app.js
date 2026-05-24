// app.js
App({
  onLaunch() {
    // 检查是否已录入信息，未录入则跳转到 onboarding
    const userProfile = wx.getStorageSync('user_profile')
    if (!userProfile) {
      wx.reLaunch({
        url: '/pages/onboarding/onboarding'
      })
    }
  },
  globalData: {
    // 莫兰迪色系
    colors: {
      primary: '#6D8B74',      // 灰绿色
      secondary: '#5F7161',    // 深灰绿
      accent: '#D0C9C0',       // 米白
      background: '#F5F1E8',   // 浅米黄
      card: '#FFFFFF',         // 白卡
      textPrimary: '#333333',
      textSecondary: '#666666',
      textLight: '#999999'
    }
  }
})