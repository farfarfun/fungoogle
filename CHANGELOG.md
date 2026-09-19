# Changelog

本项目尚未正式发布版本，以下按时间倒序记录变更，每条归入新增 / 修复 / 变更 / 废弃四类之一。

## [未发布]

### 变更

- 源码迁移到 `src/fungoogle/` 标准布局，`pyproject.toml` 打包配置同步调整为 `src/fungoogle`。
- `run()` 改用 `funshell.run_shell` 执行命令并检查返回码，失败时抛出带命令与退出码上下文的 `RuntimeError`，不再用 `os.system` 静默忽略失败。
- 诊断输出改用 `farlog.getLogger`，不再用 `print`。
- 公开函数（`run`/`install_drive`/`install_bash`/`packages`/`default_import`/`copy_files`/`init`）补充类型标注与中文 docstring。
- `install_bash()` 引用与 `core.py` 同目录的 `bashrc.sh`，不再依赖调用方当前工作目录下是否存在 `fungoogle/init/bashrc.sh`。
- `install_drive()` 内的 `from google.colab import drive` 改为函数内延迟导入，模块本身可在非 Colab 环境正常 `import`（便于测试），只有真正挂载 Drive 时才需要 Colab 环境。
- `script/build.sh`、`script/push.sh` 改为调用 `funbuild build` / `funbuild push`，不再手写 `setup.py build/sdist/bdist_egg/bdist_wheel` + `twine upload` 流程。
- README 补充可执行的安装命令（`pip install git+...` / `pip install -e .`），并更正 PyPI 上 `fungoogle` 0.0.1 占位包的归属说明——该包 metadata 的作者、homepage 均指向本组织自己，不是无关第三方的包。

### 新增

- 新增 `tests/test_core.py`，覆盖 `run()` 成功/失败路径、`install_drive()`/`install_bash()`/`packages()`/`copy_files()`/`default_import()`/`init()` 的行为。

### 修复

- 移除未被实际使用的 `oauth2client` 依赖（源码中从未 import 过，属于历史遗留的空依赖）。

### 说明：`notegoogle` -> `fungoogle` 改名（已完结，无需转发）

- 仓库、导入名、PyPI 发布名已统一为 `fungoogle`（原为 `notegoogle`）。
- `notegoogle` 从未在 PyPI 发布过任何版本，也没有其他仓库把它当作已声明、能工作的依赖使用（见 farfarfun/todo-list#297 的组织内下游扫描），因此不存在需要保留兼容转发或发弃用警告的历史调用方，无需再按「整包改名」流程发最终转发版本。
