// pages/onboarding/onboarding.js
const lunar = require('../../utils/lunar')
const storage = require('../../utils/storage')

Page({
  data: {
    colors: {
      primary: '#6D8B74',
      background: '#F5F1E8',
      card: '#FFFFFF',
      textPrimary: '#333333',
      textSecondary: '#666666'
    },
    // 日期
    date: '',
    dateDisplay: '请选择出生日期',
    // 时辰选项
    shichenList: [
      { label: '子时 (23:00-01:00)', value: 23 },
      { label: '丑时 (01:00-03:00)', value: 1 },
      { label: '寅时 (03:00-05:00)', value: 3 },
      { label: '卯时 (05:00-07:00)', value: 5 },
      { label: '辰时 (07:00-09:00)', value: 7 },
      { label: '巳时 (09:00-11:00)', value: 9 },
      { label: '午时 (11:00-13:00)', value: 11 },
      { label: '未时 (13:00-15:00)', value: 13 },
      { label: '申时 (15:00-17:00)', value: 15 },
      { label: '酉时 (17:00-19:00)', value: 17 },
      { label: '戌时 (19:00-21:00)', value: 19 },
      { label: '亥时 (21:00-23:00)', value: 21 }
    ],
    selectedShichen: -1,
    shichenDisplay: '请选择出生时辰',
    // 出生地
    region: [],
    regionDisplay: '请选择出生地',
    // 经纬度映射（简化版）
    regionCoordinates: {
      '北京市': { jd: 116.4, wd: 39.9 },
      '上海市': { jd: 121.47, wd: 31.23 },
      '广州市': { jd: 113.26, wd: 23.13 },
      '深圳市': { jd: 114.07, wd: 22.62 },
      '杭州市': { jd: 120.15, wd: 30.28 },
      '成都市': { jd: 104.07, wd: 30.67 },
      '武汉市': { jd: 114.30, wd: 30.60 },
      '南京市': { jd: 118.78, wd: 32.06 },
      '西安市': { jd: 108.95, wd: 34.27 },
      '重庆市': { jd: 106.55, wd: 29.57 }
    },
    // 表单校验
    canSubmit: false,
    submitting: false
  },

  onLoad() {
    const profile = storage.getUserProfile()
    if (profile) {
      // 已有信息，直接跳转首页
      wx.reLaunch({ url: '/pages/index/index' })
    }
  },

  // 选择出生日期
  onDateChange(e) {
    this.setData({
      date: e.detail.value,
      dateDisplay: e.detail.value
    })
    this.checkSubmit()
  },

  // 选择时辰
  onShichenTap(e) {
    const index = e.currentTarget.dataset.index
    const item = this.data.shichenList[index]
    this.setData({
      selectedShichen: index,
      shichenDisplay: item.label
    })
    this.checkSubmit()
  },

  // 选择出生地
  onRegionChange(e) {
    this.setData({
      region: e.detail.value,
      regionDisplay: e.detail.value.join(' - ')
    })
    this.checkSubmit()
  },

  // 校验提交
  checkSubmit() {
    const { date, selectedShichen, region } = this.data
    const canSubmit = date && selectedShichen >= 0 && region.length > 0
    this.setData({ canSubmit })
  },

  // 提交
  onSubmit() {
    const { date, shichenList, selectedShichen, region, regionCoordinates } = this.data
    if (this.data.submitting) return

    this.setData({ submitting: true })

    const [year, month, day] = date.split('-')
    const hour = shichenList[selectedShichen].value
    const city = region[1] || region[0]
    const coords = regionCoordinates[city] || { jd: 116.4, wd: 39.9 }

    // 计算四柱
    const pillars = lunar.calculateFourPillars(
      parseInt(year), parseInt(month), parseInt(day), hour
    )

    // 计算时区偏移（简化：中国统一 +480）
    const timezoneOffset = 480

    // 保存用户信息
    storage.saveUserProfile({
      lunar_encrypted: `${pillars.year}${pillars.month}${pillars.day}${pillars.hour}`,
      day_master: pillars.dayMaster,
      day_branch: pillars.dayBranch,
      jingdu: coords.jd,
      weidu: coords.wd,
      timezone_offset: timezoneOffset,
      birthday: date,
      shichen: shichenList[selectedShichen].label
    })

    storage.markLaunched()

    wx.showToast({
      title: '录入完成',
      icon: 'success',
      duration: 1500
    })

    setTimeout(() => {
      wx.reLaunch({ url: '/pages/index/index' })
    }, 1500)
  }
})