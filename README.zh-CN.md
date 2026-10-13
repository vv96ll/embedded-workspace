# Embedded Workspace Skill

[English](README.md) | 简体中文

跨 AI Agent 的嵌入式产品工作区 Skill：初始化目录和规则，整理根目录新增资料，维护关键资料索引。适用于不同芯片、SDK、工程工具和多仓库工作区。

## 安装

需要 Python 3.9+，仅使用标准库。当前实际验证环境为 Windows；Linux、macOS 尚未运行验证。无需 SDK 或硬件。

```bash
git clone https://github.com/vv96ll/embedded-workspace.git
```

将仓库内的 **embedded-workspace 文件夹**复制到所用 Agent 支持的 Skill 目录，不要复制整个仓库：

- Codex 默认用户目录：`~/.codex/skills/embedded-workspace/`；设置了 CODEX_HOME 时使用对应目录。
- Claude Code：使用其文档支持的用户或项目目录，例如 `~/.claude/skills/embedded-workspace/` 或 `.claude/skills/embedded-workspace/`。
- 其他 Agent：按工具文档安装。没有自动发现机制但支持文件读取时，可以明确要求读取 [SKILL.md](embedded-workspace/SKILL.md)。

工具未刷新 Skill 列表时开启新会话。桌面聊天应用与编码 Agent 的能力可能不同，详见[适配说明](embedded-workspace/references/agent-adapters.md)。

## 更新已安装的 Skill

直接调用本 Skill 的更新模式即可：

> 调用 embedded-workspace，更新这个 Skill。

Skill 会从上游 main 获取更新并同步当前安装，保留本地修改，不更新已有项目的 AGENTS.md。执行需要网络及安装目录写权限。普通调用不检查更新；其他 Agent 的安装仅在要求时同步。不支持自动发现的工具需先明确加载 SKILL.md。

## 通过 Agent 使用

- “使用 embedded-workspace 初始化指定路径的产品工作区，不创建固件工程、不移动已有资料。”
- “整理工作区根目录新增文件，按用途归类，并更新资料索引；不确定的保留原位。”
- “补齐这个已有工作区的规则和索引，保留现有目录名称和各 Git 仓库。”

Agent 读取必要的文件内容判断分类，然后执行整理并维护索引。没有后台监控，需要你触发整理。

## 初始化结果

```text
workspace/
├── AGENTS.md
├── README.md
├── .gitignore
├── requirements/   # 需求、规格、验收标准
├── hardware/       # 硬件设计与器件资料
├── firmware/       # 固件工程
│   └── AGENTS.md    # 固件专用规则
├── software/       # 配套应用与工具工程
└── docs/           # 项目设计、接口与使用文档
```

按需增加 mechanical、assets、references、tasks、tests、scripts、releases。器件资料放 hardware/references；原厂 SDK 原包放 references/sdk；参与构建的依赖留在所属工程。已有名称和仓库边界保持原样。见[完整分类规则](embedded-workspace/references/layout-and-classification.md)。

根目录 AGENTS.md 承载通用规则；firmware/AGENTS.md 承载 SDK 例程、中断、内存、类型、警告、烧录脚本和验证要求。不支持分层加载的 Agent 应明确读取两份规则。工具特定入口只在适用时生成，不会默认创建所有工具的文件。

## 命令行初始化

从仓库根目录运行，将路径换成实际位置，包含空格时加引号：

```powershell
python embedded-workspace/scripts/workspace_ops.py init "D:/projects/example"
```

脚本创建默认结构和缺失文件，不覆盖已有规则。合并规则、复用不同目录名称、维护索引由 Agent 完成。

## 归类根目录资料

### 资料版本

同一对象、同一资料类型的版本集中放置，保留原始文件名。索引分别记录版本和状态：current（当前采用）、pending（待确认）、superseded（已替代）。新收到的原理图默认待确认，只有用户或项目既定基线明确采用时才切换当前版，并将原基线标记为已替代，保留旧文件。按项目习惯可使用局部 archive 目录。AI 默认使用当前采用版本，不凭时间戳判断，也不因资料到达自动修改固件或依赖。

例如：“归类这份新版原理图，先标为待确认。”或：“采用这份原理图为当前版本，将原版标记为已替代。”

准备 UTF-8 JSON 文件 plan.json，所有路径相对于工作区：

```json
[
  {
    "source": "元器件手册.pdf",
    "destination": "hardware/references/器件名称/元器件手册.pdf"
  }
]
```

```powershell
python embedded-workspace/scripts/workspace_ops.py move "D:/projects/example" plan.json --apply
```

明确的整理任务直接加 --apply 执行；需要预览时去掉 --apply，不要求每批运行两次。目标父目录按需创建。脚本不负责理解资料或更新 Markdown 索引，这些由 Agent 完成。脚本拒绝目录、受保护根目录文件、链接、越界路径及覆盖已有目标。

## 恢复移动

记录保存在 .workspace-ops/moves-<id>.json，包含文件 SHA-256。使用命令输出的实际记录路径：

```powershell
python embedded-workspace/scripts/workspace_ops.py restore "D:/projects/example" "记录文件路径" --apply
```

预览可选。哈希用于恢复时判断文件是否变化，普通复制不再额外重复哈希比对。内容变化或原路径被占用时拒绝恢复。恢复只调整文件位置，之后更新受影响的索引。执行中断时检查 pending 记录和当前路径。

## 验证与边界

```powershell
python -m unittest discover -s tests -v
```

修改脚本行为时运行这些测试；仅修改说明或规则时查看差异即可。测试覆盖规则生成与保留、预览、移动、恢复、中文及空格路径、受保护文件、冲突、内容变化和失败清理。

开发规则以效率为先：明确任务直接做，复用已有环境与脚本，只构建和测试受影响部分一次，成功后停止。无需反复初始化、重新哈希或添加没有实际收益的测试及审计流程。

初始化不创建固件工程、不编译、不烧录、不初始化 Git、不提交、不发布。只有明确要求建立烧录流程且硬件可用时才实际验证；无法执行的硬件验证报告为 NOT_RUN。
