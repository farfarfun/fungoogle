# fungoogle

个人 Google Colab 环境初始化脚本：挂载 Google Drive、创建工作目录、安装依赖（`funtool`、`kaggle`）、把 Drive 里的个人文件拷贝到 Colab 本地环境。是作者自用的 Colab 启动脚手架，不是通用工具库，路径（如 `/content/drive/My Drive/home`、`/root/workspace`）都是硬编码的个人配置。

> 注意：本仓库尚未真正发布过版本。PyPI 上已存在一个 `fungoogle`（0.0.1）包，其 wheel 内容只有一个空的 `funapi/__init__.py`，是本组织早年批量占位发布时留下的空壳——metadata 里的作者（`bingtao`）和 homepage（本仓库地址）都指向 farfarfun 组织自己，**不是别人的包**，但内容与当前源码无关。真正发布正式版本前需要先在这个占位版本之上递增版本号，不能假设名字是全新的。

## 安装

暂无正式发布版本，直接从源码安装（依赖 `farlog`、`funshell` 会随之自动安装）：

```bash
pip install git+https://github.com/farfarfun/fungoogle.git
# 或克隆后本地安装
git clone https://github.com/farfarfun/fungoogle.git
cd fungoogle
pip install -e .
```

`google.colab` 仅 Colab notebook 环境自带，无需单独安装；离开 Colab 环境时只有 `install_drive()`/`default_import()` 实际调用到它才会报错，其余函数可正常导入和调用。

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
4. `default_import()`：把 `packages` 目录加入 `sys.path` 并记录 pandas 版本作为环境检查。

## 已知局限（如实说明）

- 这是一份高度个人化的 Colab 初始化脚本，路径、Google Drive 目录结构均按作者本人的习惯硬编码，其他人直接用大概率跑不通，需要按自己的 Drive 目录结构改代码。

---

## 关于 farfarfun

[farfarfun](https://github.com/farfarfun) 是一个专注于实用工具库的开源组织，
涵盖云存储、数据处理、AI、多媒体与开发工具链等方向。

- 🏠 组织主页：<https://github.com/farfarfun>
- 📦 PyPI：<https://pypi.org/user/niuliangtao/>
- 📧 联系：farfarfun@qq.com

本项目基于 [MIT](LICENSE) 协议开源。
