#!/usr/bin/env bash
set -euo pipefail

# 版本递增、构建、发布、打 tag 统一走 funbuild（见 SPEC.md §4.4），
# 不再手写 setup.py/twine 流程。
funbuild build "$@"
