// cloudfunctions/dailyAdvice/index.js
const cloud = require('wx-server-sdk')

cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV
})

/**
 * 云函数 - 获取每日建议
 * 输入：{ tenGod, relation, todayGanZhi }
 * 输出：{ advice: [ { title, content, icon } ] }
 */
exports.main = async (event, context) => {
  const { tenGod, relation, todayGanZhi } = event
  
  // 1. 组装 Prompt（根据方案中的模板）
  const prompt = `
你是一位资深职场心理教练，请将以下数理标签转化为针对职场女性的3条行动建议。

今日数理标签：
- 十神：${tenGod}
- 地支关系：${relation}
- 今日干支：${todayGanZhi}

要求：
1. 输出3条建议，每条包含：标题（≤10字）+ 具体内容（≤50字）
2. 语气：知性、有边界感、不宣扬焦虑
3. 语境：使用“职场博弈、情绪边界、时机管理”等专业词汇
4. 禁止玄学话术，禁止迷信，禁止使用“运势”“命运”等词汇
5. 每条建议前加一个emoji图标（如🚫💬⏰）

请以JSON格式返回：
{
  "advice": [
    { "title": "...", "content": "...", "icon": "..." },
    ...
  ]
}
`
  
  // 2. 调用 AI API（这里用百度文心千帆示例）
  // 实际使用时替换为你的 API Key
  const AI_API_URL = 'https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions'
  const ACCESS_TOKEN = process.env.BAIDU_ACCESS_TOKEN // 从环境变量读取
  
  try {
    const response = await cloud.callFunction({
      name: 'aiProxy',
      data: {
        url: AI_API_URL,
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${ACCESS_TOKEN}`
        },
        data: {
          messages: [{ role: 'user', content: prompt }],
          temperature: 0.7,
          max_tokens: 500
        }
      }
    })
    
    // 解析 AI 返回
    const aiResult = response.result
    let adviceList = []
    
    try {
      // 尝试解析 JSON
      const parsed = JSON.parse(aiResult)
      adviceList = parsed.advice || []
    } catch (e) {
      // 如果 AI 返回的不是 JSON，使用默认建议
      adviceList = getDefaultAdvice(tenGod, relation)
    }
    
    // 3. 内容安全检测（微信 msgSecCheck）
    try {
      for (const advice of adviceList) {
        const checkResult = await cloud.openapi.security.msgSecCheck({
          content: `${advice.title} ${advice.content}`
        })
        if (checkResult.errCode !== 0) {
          // 内容不安全，替换为安全文案
          advice.title = '职场策略提醒'
          advice.content = '今日建议：保持专业态度，专注工作目标。'
        }
      }
    } catch (checkErr) {
      // 检测失败，使用默认安全建议
      adviceList = getDefaultAdvice(tenGod, relation)
    }
    
    return {
      code: 0,
      data: { advice: adviceList },
      message: 'success'
    }
    
  } catch (error) {
    console.error('云函数错误:', error)
    // 降级：返回默认建议
    return {
      code: 0,
      data: { advice: getDefaultAdvice(tenGod, relation) },
      message: 'fallback to default advice'
    }
  }
}

// 默认建议（当 AI 调用失败时使用）
function getDefaultAdvice(tenGod, relation) {
  const baseAdvice = [
    { title: '专注核心任务', content: '今日适合处理重要但不紧急的工作，避免被琐事分散注意力。', icon: '🎯' },
    { title: '注意沟通方式', content: '表达观点时先肯定对方，再提出不同意见，保持职场和谐。', icon: '💬' },
    { title: '合理安排时间', content: '上午处理创造性工作，下午处理执行性任务，效率更高。', icon: '⏰' }
  ]
  
  // 根据关系微调
  if (relation === '逢冲') {
    baseAdvice[0] = { title: '避免冲突决策', content: '今日情绪易波动，重要决策建议延后，先处理常规事务。', icon: '🚫' }
  } else if (relation === '逢合') {
    baseAdvice[1] = { title: '把握合作机会', content: '适合与同事或合作伙伴深入沟通，达成共识。', icon: '🤝' }
  }
  
  return baseAdvice
}