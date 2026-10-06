"""Google Colab 环境初始化：挂载 Drive、安装依赖、拷贝个人文件。

高度个人化的脚手架，路径按作者本人的 Colab/Drive 目录结构硬编码，
仅能在 Google Colab notebook 环境中运行，见仓库 README「已知局限」。
"""

import os

from farlog import getLogger
from funshell import run_shell

logger = getLogger("fungoogle")

dir_root = "/content/drive/My Drive/home"
workspace = "/root/workspace"


def run(cmd: str) -> None:
    """执行一条 shell 命令，失败时抛出异常并携带命令上下文。

    Args:
        cmd: 要执行的 shell 命令。

    Raises:
        RuntimeError: 命令以非 0 状态退出。
    """
    logger.info(cmd)
    code = run_shell(cmd)
    if code != "0":
        raise RuntimeError(f"命令执行失败（退出码 {code}）: {cmd}")


def install_drive() -> None:
    """挂载 Google Drive，并创建/切换到工作目录。"""
    from google.colab import drive

    drive.mount("/content/drive")
    run(f"mkdir {workspace}")
    os.chdir(workspace)


def install_bash() -> None:
    """将 ``FUNGOOGLE_EXTRA_PATH`` 加入当前 Python 进程的 ``PATH``。

    未设置该环境变量时不修改环境。多个目录使用当前平台的路径分隔符连接。
    """
    extra_path = os.environ.get("FUNGOOGLE_EXTRA_PATH")
    if not extra_path:
        return

    path = os.environ.get("PATH")
    os.environ["PATH"] = f"{extra_path}{os.pathsep}{path}" if path else extra_path


# 与 pyproject.toml 的 [project.optional-dependencies].colab 保持一致，
# 改动版本下限时两处一起改。
_COLAB_PACKAGES = ("funutil>=1.0.63", "kaggle>=1.6.17")


def packages() -> None:
    """安装 Colab 环境缺省的个人常用依赖（funutil、kaggle）。

    版本下限声明见 pyproject.toml 的 colab extra。已满足下限的已安装版本不会
    被升级；首次安装时由 pip 在该约束范围内解析版本。
    """
    for package in _COLAB_PACKAGES:
        run(f"pip install '{package}'")


def default_import() -> None:
    """把个人 packages 目录加入 sys.path，并检查 pandas 是否可用。"""
    import sys

    import pandas as pd

    sys.path.append(dir_root + "/packages")
    logger.info(f"pd:{pd.__version__}")


def copy_files() -> None:
    """把 Drive 里的个人文件（含隐藏文件）拷贝到 Colab 本地 /root/。"""
    path_f = dir_root + "/local_files/"
    path_t = "/root/"
    run(f"cp -r '{path_f}' {path_t}")
    run(f"cp -r '{path_f}.' {path_t}")


def init() -> None:
    """一键初始化：挂载 Drive、装依赖、拷贝个人文件、做环境检查。"""
    install_drive()
    packages()
    copy_files()
    default_import()
