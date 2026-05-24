// pages/index/index.js
const app = getApp()
const lunar = require('../../utils/lunar')
const storage = require('../../utils/storage')

Page({
  data: {
    colors: app.globalData.colors,
    // 用户状态
    hasProfile: false,
    // 今日卡片
    todayCard: null,
    // 十神对应的颜色和图标（简化版）
    tenGodConfig: {
      '伤官': { color: '#E57373', icon: '⚡', name: '伤官日' },
      '食神': { color: '#81C784', icon: '🍃', name: '食神日' },
      '正财': { color: '#64B5F6', icon: '💰', name: '正财日' },
      '偏财': { color: '#7986CB', icon: '💎', name: '偏财日' },
      '正官': { color: '#4DB6AC', icon: '👑', name: '正官日' },
      '七杀': { color: '#9575CD', icon: '⚔️', name: '七杀日' },
      '正印': { color: '#FFB74D', icon: '📚', name: '正印日' },
      '偏印': { color: '#A1887F', icon: '🔮', name: '偏印日' },
      '比肩': { color: '#90A4AE', icon: '🤝', name: '比肩日' },
      '劫财': { color: '#F06292', icon: '⚖️', name: '劫财日' },
      '平和': { color: '#6D8B74', icon: '☯', name: '平和日' }
    },
    // 关系标签配置
    relationConfig: {
      '逢冲': { color: '#FF8A65', text: '今日地支逢冲，注意情绪波动' },
      '逢合': { color: '#4DB6AC', text: '今日地支逢合，适合合作沟通' },
      '平和': { color: '#90A4AE', text: '今日地支平和，按部就班即可' }
    },
    // AI 建议
    adviceList: [],
    // 加载状态
    loading: true,
    // 今日日期
    todayDate: ''
  },

  onLoad() {
    this.checkProfile()
    this.setTodayDate()
  },

  onShow() {
    this.loadTodayCard()
  },

  // 检查用户信息
  checkProfile() {
    const profile = storage.getUserProfile()
    this.setData({ hasProfile: !!profile })
    if (!profile) {
      wx.reLaunch({ url: '/pages/onboarding/onboarding' })
    }
  },

  // 设置今日日期
  setTodayDate() {
    const now = new Date()
    const dateStr = `${now.getFullYear()}年${now.getMonth() + 1}月${now.getDate()}日`
    this.setData({ todayDate: dateStr })
  },

  // 加载今日卡片
  loadTodayCard() {
    const todayCard = storage.getTodayCard()
    const todayStr = new Date().toISOString().split('T')[0]
    
    if (todayCard && todayCard.date === todayStr) {
      // 已有今日卡片
      this.setData({
        todayCard,
        adviceList: todayCard.advice || [],
        loading: false
      })
    } else {
      // 需要重新计算
      this.calculateTodayCard()
    }
  },

  // 计算今日卡片
  calculateTodayCard() {
    this.setData({ loading: true })
    
    const profile = storage.getUserProfile()
    if (!profile) return
    
    // 获取今日干支
    const todayGanZhi = lunar.getTodayGanZhi()
    
    // 计算十神和关系
    const { tenGod, relation } = lunar.calculateTenGod(profile.day_master, todayGanZhi)
    
    // 生成临时卡片
    const tempCard = {
      date: new Date().toISOString().split('T')[0],
      tenGod,
      relation,
      todayGanZhi
    }
    
    this.setData({
      todayCard: tempCard,
      loading: false
    })
    
    // 请求 AI 建议
    this.requestAdvice(tempCard)
  },

  // 请求 AI 建议
  requestAdvice(card) {
    wx.showLoading({ title: '生成建议中...' })
    
    // 模拟云函数调用
    setTimeout(() => {
      const mockAdvice = [
        {
          title: '避免情绪化决策',
          content: '今日能量易受外界影响，建议重要决策延至明日，先处理常规事务。',
          icon: '🚫'
        },
        {
          title: '专注内部沟通',
          content: '适合与团队成员一对一沟通，避免在公开场合表达不同意见。',
          icon: '💬'
        },
        {
          title: '利用碎片时间',
          content: '下午3-5点精力较集中，适合处理需要专注的文档或方案。',
          icon: '⏰'
        }
      ]
      
      const todayCard = {
        ...card,
        advice: mockAdvice
      }
      
      storage.saveTodayCard(todayCard)
      
      this.setData({
        adviceList: mockAdvice,
        todayCard
      })
      
      wx.hideLoading()
      wx.vibrateShort() // 微信振动反馈
    }, 1500)
  },

  // 重新计算
  onRecalculate() {
    this.calculateTodayCard()
  },

  // 跳转到设置
  onGoSettings() {
    wx.navigateTo({ url: '/pages/settings/settings' })
  }
})