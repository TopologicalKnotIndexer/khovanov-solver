# 从标准输入读取一个 list 作为 PD_CODE
# 将对应扭结的信息输出到标准输出流中
# 将错误信息输出到标准错误流中

import sys

from kho_solver   import kho_solver
from de_k8_r1     import de_k8_r1

def main() -> None:
    all_input = sys.stdin.read().strip() # 获取全部输入信息
    khovanovH = kho_solver(all_input)    # 调用 JavaKh
    print(khovanovH)

if __name__ == "__main__":
    main()