# fungoogle

个人 Google Colab 环境初始化脚本：挂载 Google Drive、创建工作目录、安装依赖（`funtool`、`kaggle`）、把 Drive 里的个人文件拷贝到 Colab 本地环境。是作者自用的 Colab 启动脚手架，不是通用工具库，路径（如 `/content/drive/My Drive/home`、`/root/workspace`）都是硬编码的个人配置。

> 注意：本仓库尚未在 PyPI 发布过任何版本。PyPI 上确实存在一个叫 `fungoogle`（0.0.1）的包，但经核对其 wheel 内容只有一个空的 `funapi/__init__.py`，是历史上批量占位发布的空包，**和这个仓库的代码毫无关系**。这意味着未来要把本仓库真正发布到 PyPI 的 `fungoogle` 这个名字下，需要先处理掉这个占位包（联系 PyPI 或使用其他账号协调），发布前请勿假设这个名字可以直接拿来用。

## 安装

暂无可用的发布包，只能从源码使用：

```bash
git clone https://github.com/farfarfun/fungoogle.git
cd fungoogle
```

依赖 `google.colab`（仅 Colab 环境自带），以及外部包 `oauth2client`（`setup.py` 中声明但当前源码未见实际用到）。

## 用法示例

只能在 Google Colab 的 notebook 环境里运行：

```python
from fungoogle.init.core import init

init()
```

`init()` 依次执行：

1. `install_drive()`：挂载 `/content/drive`，创建 `/root/workspace` 工作目录；
2. `packages()`：`pip install` 安装 `git+https://github.com/farfarfun/funtool.git` 和 `kaggle`；
3. `copy_files()`：把 Drive 里 `home/local_files/` 目录下的文件拷贝到 Colab 本地的 `/root/`；
4. `default_import()`：把 `packages` 目录加入 `sys.path` 并打印 pandas 版本作为环境检查。

## 已知局限（如实说明）

- 这是一份高度个人化的 Colab 初始化脚本，路径、Google Drive 目录结构均按作者本人的习惯硬编码，其他人直接用大概率跑不通，需要按自己的 Drive 目录结构改代码。
