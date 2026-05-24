// storage.js - 本地存储工具

const STORAGE_KEYS = {
  USER_PROFILE: 'user_profile',
  TODAY_CARD: 'today_card',
  IS_FIRST_LAUNCH: 'is_first_launch'
}

/**
 * 保存用户信息
 */
function saveUserProfile(profile) {
  wx.setStorageSync(STORAGE_KEYS.USER_PROFILE, profile)
}

/**
 * 获取用户信息
 */
function getUserProfile() {
  return wx.getStorageSync(STORAGE_KEYS.USER_PROFILE) || null
}

/**
 * 保存今日卡片
 */
function saveTodayCard(card) {
  wx.setStorageSync(STORAGE_KEYS.TODAY_CARD, card)
}

/**
 * 获取今日卡片
 */
function getTodayCard() {
  return wx.getStorageSync(STORAGE_KEYS.TODAY_CARD) || null
}

/**
 * 检查是否首次启动
 */
function isFirstLaunch() {
  return !wx.getStorageSync(STORAGE_KEYS.IS_FIRST_LAUNCH)
}

/**
 * 标记已启动
 */
function markLaunched() {
  wx.setStorageSync(STORAGE_KEYS.IS_FIRST_LAUNCH, true)
}

/**
 * 清除所有数据
 */
function clearAll() {
  Object.values(STORAGE_KEYS).forEach(key => {
    wx.removeStorageSync(key)
  })
}

module.exports = {
  saveUserProfile,
  getUserProfile,
  saveTodayCard,
  getTodayCard,
  isFirstLaunch,
  markLaunched,
  clearAll,
  STORAGE_KEYS
}