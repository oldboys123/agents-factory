# AGENTS.md - Agent 工厂操作手册

## 启动命令
- `创建一个 agent` / `新建 agent` / `生成一个做XX的agent`

## 工作流程

### Step 1: 接收需求
用户说"帮我创建一个做XX的agent"
- 提取核心功能
- 确定名称（英文+中文）
- 确定技能方向

### Step 2: 分配编号
在 `/home/hui/agents-factory/agents/` 下创建目录：
```
agent_001_xxx/
agent_002_yyy/
...
```
编号自动递增，从现有最大编号+1

### Step 3: 生成基础模板
按以下结构创建所有文件：

```
agent_xxx/
├── ROLE.json        # 身份ID、名称、版本
├── SOUL.md          # 性格人设
├── SKILLS.md        # 技能列表
├── config.yaml      # 模型配置
├── memory/
│   ├── short_term.md
│   ├── long_term.md
│   └── user_preferences.md
└── log/
    └── README.md
```

### Step 4: 填充内容
根据用户需求：
- 编写 SOUL.md（性格、语气、禁忌）
- 编写 SKILLS.md（具体技能列表和触发词）
- 编写 config.yaml（模型、温度、工具权限）

### Step 5: 完成汇报
汇报格式：
```
✅ Agent 创建完成！

【基本信息】
- 名称：xxx
- 编号：agent_xxx
- 路径：/home/hui/agents-factory/agents/agent_xxx/

【核心技能】
- skill 1
- skill 2

【配置文件】
- SOUL.md ✅
- SKILLS.md ✅
- ROLE.json ✅
- config.yaml ✅
- memory/ ✅
```

## 模板文件位置
模板文件在：`/home/hui/agents-factory/templates/`

## 编号规则
- 格式：`agent_{3位数字}_{英文名}`
- 示例：agent_001_customer_service, agent_002_data_analyst
- 编号不重复，创建前检查现有目录
