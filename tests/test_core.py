"""测试 fungoogle.init.core 的公开函数。"""

import sys
import types
from unittest.mock import patch

import pytest

from fungoogle.init import core


def test_run_success() -> None:
    """命令成功退出（返回码 "0"）时 run() 不应抛出异常。"""
    with patch("fungoogle.init.core.run_shell", return_value="0") as mock_run_shell:
        core.run("echo hi")
    mock_run_shell.assert_called_once_with("echo hi")


def test_run_failure_raises_with_context() -> None:
    """命令非 0 退出时应抛出 RuntimeError，且异常信息带上命令内容。"""
    with (
        patch("fungoogle.init.core.run_shell", return_value="1"),
        pytest.raises(RuntimeError, match="echo hi"),
    ):
        core.run("echo hi")


def test_packages_installs_funtool_and_kaggle() -> None:
    """packages() 应依次安装 funtool 与 kaggle。"""
    with patch("fungoogle.init.core.run") as mock_run:
        core.packages()
    commands = [call.args[0] for call in mock_run.call_args_list]
    assert any("funtool" in cmd for cmd in commands)
    assert any("kaggle" in cmd for cmd in commands)


def test_copy_files_uses_dir_root_and_target() -> None:
    """copy_files() 应把 dir_root 下的 local_files（含隐藏文件）拷贝到 /root/。"""
    with patch("fungoogle.init.core.run") as mock_run:
        core.copy_files()
    commands = [call.args[0] for call in mock_run.call_args_list]
    assert len(commands) == 2
    assert all(core.dir_root in cmd for cmd in commands)
    assert all("/root/" in cmd for cmd in commands)


def test_default_import_appends_packages_path() -> None:
    """default_import() 应把 dir_root/packages 加入 sys.path。"""
    fake_pandas = types.ModuleType("pandas")
    fake_pandas.__version__ = "0.0.0-fake"

    before = list(sys.path)
    try:
        with patch.dict(sys.modules, {"pandas": fake_pandas}):
            core.default_import()
        assert core.dir_root + "/packages" in sys.path
    finally:
        sys.path[:] = before


def test_install_bash_sources_file_next_to_module() -> None:
    """install_bash() 应引用与 core.py 同目录下的 bashrc.sh，不依赖当前工作目录。"""
    with patch("fungoogle.init.core.run") as mock_run:
        core.install_bash()
    cmd = mock_run.call_args.args[0]
    assert cmd.startswith("source ")
    assert cmd.endswith("bashrc.sh")


def test_install_drive_mounts_and_chdir_to_workspace() -> None:
    """install_drive() 应挂载 Drive、创建 workspace 并切换到该目录。"""
    fake_drive = types.SimpleNamespace(mount=lambda path: None)
    fake_google = types.ModuleType("google")
    fake_colab = types.ModuleType("google.colab")
    fake_colab.drive = fake_drive
    fake_google.colab = fake_colab

    with (
        patch.dict(sys.modules, {"google": fake_google, "google.colab": fake_colab}),
        patch("fungoogle.init.core.run") as mock_run,
        patch("os.chdir") as mock_chdir,
    ):
        core.install_drive()

    mock_run.assert_called_once()
    mock_chdir.assert_called_once_with(core.workspace)


def test_init_runs_steps_in_order() -> None:
    """init() 应按挂载 Drive、装依赖、拷贝文件、环境检查的顺序依次执行。"""
    calls: list[str] = []
    with (
        patch(
            "fungoogle.init.core.install_drive",
            side_effect=lambda: calls.append("install_drive"),
        ),
        patch(
            "fungoogle.init.core.packages", side_effect=lambda: calls.append("packages")
        ),
        patch(
            "fungoogle.init.core.copy_files",
            side_effect=lambda: calls.append("copy_files"),
        ),
        patch(
            "fungoogle.init.core.default_import",
            side_effect=lambda: calls.append("default_import"),
        ),
    ):
        core.init()
    assert calls == ["install_drive", "packages", "copy_files", "default_import"]
