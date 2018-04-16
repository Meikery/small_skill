#运行时检测python版本
import sys
if not hasattr(sys, "hexversion") or sys.version_info >= (3, 5):
    print("Sorry,you aren't running on Python 3.5n")
    print("please upgrade to 3.5.n")
    sys.exit(1)
print("Current Python version:", sys.version)
