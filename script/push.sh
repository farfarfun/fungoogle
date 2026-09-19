#!/usr/bin/env bash
set -euo pipefail

# 提交并推送代码，统一走 funbuild（见 SPEC.md §4.4）。
# 不传 -m 时由 funbuild 依据改动自动生成提交信息；
# 需要自定义时用: script/push.sh -m "<类型>: <做了什么>"
funbuild push "$@"
