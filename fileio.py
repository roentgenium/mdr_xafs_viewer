import numpy as np


def guess_file_type(self, fname):
    with open(fname) as f:
        if "9809" in f.readline():
            return "9809"
        else:
            return "unknown"


def load_9809_format(self, fname):
    """
    Load 9809 format XAS data into a XasDatum object.
    Only support the simplest transmission data.
    """
    with open(fname) as f:
        format, beamline = f.readline().strip().split(maxsplit=1)
        file_name, time = f.readline().strip().split(maxsplit=1)
        sample_name = f.readline().strip()
        f.readline()  # Ring energy and current
        _, _, plane, _, distance, _, _, _, _, _ = f.readline().strip().split()
        f.readline()  # Ignore Line 6
        blocksize = int(f.readline().strip().split()[-1]) # Line 7
        f.readline()  # Ignore Line 8 (emtpy line)
        f.readline()  # Ignore Line 9
        for i in range(blocksize):
            f.readline()  # Ignore Blocks
        print(f.readline())  # Ignore Offset
        num_of_detector = int(f.readline().strip().split()[-1])  # Ignore detector line
        dmode = f.readline().strip().split(maxsplit=4)[:-1]
        print(f.readline())  # Ignore Offset
        num_of_columns = len(f.readline().strip().split())
        raw = f.read().strip().split()  # Read all data
        raw = np.array(raw, dtype=float)
        length = int(raw.size / num_of_columns )
        data = np.reshape(raw, [length, num_of_columns])

        self.angle_c = data[:, 0]
        self.angle_o = data[:, 1]
        self.duration = data[:, 2]
        self.i0 = data[:, 3]
        self.i1 = data[:, 4]

        self.energy= 12398.52 / \
            (2.0 * float(distance) *
             np.sin(np.pi * self.angle_o / 180.0))
        self.mu = np.log(self.i0 / self.i1)

        return self


class XasDatum():
    def __init__(self) -> None:
        self.energy = []
        self.mu = []

    def from_file(self, fname):
        type = guess_file_type(self, fname)
        if type == "9809":
            return load_9809_format(self, fname)
