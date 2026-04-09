#!/usr/bin/env python3
"""
Agent 工厂 - 自动生成 Agent 脚本
用法: python3 generate_agent.py <英文名> <中文名> <描述>
"""

import os
import sys
import json
from datetime import datetime

TEMPLATE_DIR = "/home/hui/agents-factory/templates"
AGENTS_DIR = "/home/hui/agents-factory/agents"

def get_next_id():
    """获取下一个可用编号"""
    existing = [d for d in os.listdir(AGENTS_DIR) if d.startswith("agent_")]
    if not existing:
        return "agent_001"
    nums = []
    for d in existing:
        try:
            num = int(d.split("_")[1])
            nums.append(num)
        except:
            pass
    next_num = max(nums) + 1 if nums else 1
    return f"agent_{next_num:03d}"

def generate_agent(english_name, chinese_name, description):
    agent_id = get_next_id()
    folder_name = f"{agent_id}_{english_name}"
    agent_dir = os.path.join(AGENTS_DIR, folder_name)
    
    os.makedirs(agent_dir, exist_ok=True)
    os.makedirs(os.path.join(agent_dir, "memory"), exist_ok=True)
    os.makedirs(os.path.join(agent_dir, "log"), exist_ok=True)
    
    # 生成 ROLE.json
    role = {
        "agent_id": folder_name,
        "name": chinese_name,
        "identity": description,
        "created_at": datetime.now().isoformat(),
        "version": "1.0.0",
        "description": description
    }
    with open(os.path.join(agent_dir, "ROLE.json"), "w") as f:
        json.dump(role, f, ensure_ascii=False, indent=2)
    
    # 复制模板
    for item in ["SOUL.md", "SKILLS.md", "config.yaml"]:
        src = os.path.join(TEMPLATE_DIR, item)
        if os.path.exists(src):
            with open(src, "r") as f:
                content = f.read()
            content = content.replace("{{NAME}}", chinese_name)
            content = content.replace("{{AGENT_ID}}", folder_name)
            content = content.replace("{{CREATED_AT}}", datetime.now().isoformat())
            content = content.replace("{{DESCRIPTION}}", description)
            with open(os.path.join(agent_dir, item), "w") as f:
                f.write(content)
    
    for item in ["short_term.md", "long_term.md", "user_preferences.md"]:
        src = os.path.join(TEMPLATE_DIR, "memory", item)
        if os.path.exists(src):
            with open(src, "r") as f:
                content = f.read()
            with open(os.path.join(agent_dir, "memory", item), "w") as f:
                f.write(content)
    
    src_log = os.path.join(TEMPLATE_DIR, "log", "README.md")
    if os.path.exists(src_log):
        with open(src_log, "r") as f:
            content = f.read()
        with open(os.path.join(agent_dir, "log", "README.md"), "w") as f:
            f.write(content)
    
    print(f"✅ Agent 创建完成: {folder_name}")
    print(f"   路径: {agent_dir}")
    return folder_name

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("用法: python3 generate_agent.py <英文名> <中文名> <描述>")
        sys.exit(1)
    generate_agent(sys.argv[1], sys.argv[2], sys.argv[3])
