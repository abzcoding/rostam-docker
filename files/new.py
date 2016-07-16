import sys
sys.path.append("/files/rostam")
from rostam.start import main
from mock import patch


def begin():
    args = ["start.py", "-l", "/data", "-o", "/data/rostam.log"]
    with patch.object(sys, 'argv', args):
        main()

if __name__ == "__main__":
    begin()
