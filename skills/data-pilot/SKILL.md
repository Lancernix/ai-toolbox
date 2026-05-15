# DataPilot 🦾

DataPilot 是一个专为处理超大 Excel 文件（百万行、50列级别）设计的高性能数据中心。它基于 Polars 和 Parquet 技术栈，能在低内存（<2GB）环境下实现秒级的数据清洗与透视分析。

## 核心能力

- **高性能导入**：使用 Rust 编写的 Calamine 引擎读取 Excel，速度比传统工具快 5-10 倍。
- **列式存储**：将 Excel 转换为 Parquet 格式，实现 40 倍以上的查询加速。
- **增量更新**：支持将每周新增的 Excel 数据无缝合并到主数据仓库，自动处理表头映射。
- **智能分析**：无需加载全量数据，直接在 Parquet 上进行多维度的透视与聚合。

## 工作流 (Workflow)

### 1. 探测与初始化 (Inspect)
当用户上传一个新的 Excel 文件或需要分析现有数据时，首先探测其结构。
- **命令**：`python3 {SKILL_PATH}/scripts/engine.py --action inspect --file path/to/file.xlsx`
- **AI 动作**：向用户展示表头和前 5 行示例，确认数据格式。

### 2. 增量合并 (Upsert)
将新数据追加到主库 `master.parquet`。
- **重要建议**：在执行前，必须将新旧表头对比展示给用户，确认映射关系（Mapping）。
- **命令**：`python3 {SKILL_PATH}/scripts/engine.py --action upsert --file new_data.xlsx --target master.parquet --mapping '{"原列名": "目标列名"}'`

### 3. 数据分析 (Query)
进行透视表操作或统计分析。
- **命令**：`python3 {SKILL_PATH}/scripts/engine.py --action query --target master.parquet --query '{"group_by": ["地区"], "agg": {"销售额": "sum"}}'`
- **AI 动作**：将返回的 JSON 数据整理成美观的 Markdown 表格，或根据需要生成 Plotly 可视化代码。

## 注意事项

- **禁止直接读取**：严禁使用 `read_file` 或普通的 `pandas.read_excel` 直接打开超过 50MB 的 Excel 文件，否则会导致 OOM。
- **映射确认**：在执行 `upsert` 操作前，务必列出 Mapping 逻辑并获得用户确认。
- **内存安全**：引擎内部已优化内存分配，在 2GB 内存环境下可安全处理百万行数据。

## 技术栈

- **Engine**: Polars (Rust-based data frame library)
- **Format**: Apache Parquet
- **Excel Reader**: Calamine (Rust-based Excel parser)
- **Storage**: Local Workspace
