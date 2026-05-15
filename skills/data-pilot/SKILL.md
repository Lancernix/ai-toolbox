---
name: data-pilot
description: 高性能数据处理引擎，专为百万级 Excel 文件的清洗、转换和聚合分析而设计，适配低内存环境。
always: false
---

# DataPilot 🦾

DataPilot 是一个高性能数据处理引擎，专为百万级 Excel 文件的清洗、转换和聚合分析而设计。

## 目录结构
- `SKILL.md`: 技能说明文档
- `scripts/engine.py`: 核心处理引擎
- `scripts/requirements.txt`: 依赖说明
- `references/`: 技术文档和 API 参考

## 核心功能

### 1. 结构探测 (Inspect)
探测 Excel 或 Parquet 文件的表头、数据类型及样本。
- **命令**: `python3 {SKILL_PATH}/scripts/engine.py --action inspect --file <path>`

### 2. 数据增量合并 (Upsert)
将 Excel 数据合并到主 Parquet 库，支持列名映射。
- **命令**: `python3 {SKILL_PATH}/scripts/engine.py --action upsert --file <source> --target <master.parquet> [--mapping '{"old": "new"}']`

### 3. 高性能查询 (Query)
对 Parquet 文件进行分组聚合查询。
- **命令**: `python3 {SKILL_PATH}/scripts/engine.py --action query --target <master.parquet> --query '{"group_by": ["col"], "agg": {"val": "sum"}}'`

## 使用规范
1. **路径引用**: 必须使用 `{SKILL_PATH}` 宏来定位脚本。
2. **大数据处理**: 严禁使用 `read_file` 读取大文件，必须通过 `engine.py` 进行流式或块处理。
3. **确认机制**: 在执行 `upsert` 前，务必列出 Mapping 并请用户确认。
