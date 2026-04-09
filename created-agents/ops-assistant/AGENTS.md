# 智维 · AGENTS.md

## 巡检流程

### 1. 巡检触发
- 每小时自动触发（通过OpenClaw Cron）
- 可手动触发：`智维 巡检`

### 2. SSH连接巡检
对每个IP执行：
```bash
# CPU使用率
top -bn1 | grep "Cpu(s)" | awk '{print "CPU: " $2}'

# 内存使用率
free -m | grep Mem | awk '{printf "内存: %s/%s MB (%.1f%%)\n", $3, $2, ($3/$2)*100}'

# 磁盘使用率
df -h | grep -E '/$|/dev' | awk '{print "磁盘: " $1 " " $5 " 使用率"}'

# 服务状态（根据配置的服务列表）
systemctl status nginx --no-pager 2>/dev/null | head -3
systemctl status sshd --no-pager 2>/dev/null | head-3

# 近期错误日志
journalctl -n 10 --since "-1 hour" --priority=err 2>/dev/null | tail -5
```

### 3. 结果汇总
汇总格式：
```
🛡️ 智维巡检报告 | 2026-04-08 23:00

【192.168.100.1】
✅ CPU: 23.5%
✅ 内存: 4123/7933 MB (52.0%)
✅ 磁盘: /dev/sda1 67%
✅ 服务: nginx 运行中, sshd 运行中
⚠️ 警告: 内存较昨日增长8%

【192.168.100.2】
...
```

### 4. 发送报告
- 发送到绑定会话：oc_c64be5c98285d23ee006f41980ec3a13
- 报告包含：整体状态 + 各服务器详情 + 问题建议

## 配置管理

### 查看配置
`智维 配置`

### 更新服务器IP
`智维 添加服务器 192.168.100.6`

### 更新巡检内容
`智维 更新服务 nginx,mysql,redis`

### 手动触发巡检
`智维 巡检`

## 注意事项
- SSH凭据需要预先配置
- 服务名称根据实际环境调整
- 巡检命令兼容CentOS/Ubuntu/Debian
