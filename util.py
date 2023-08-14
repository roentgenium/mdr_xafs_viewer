import numpy as np

from larch import xafs, Group

def load_9809_format(self, fname):
    """
    Load 9809 format XAS data into a XasDatum object.
    Only support the simplest transmission data.
    """
    with open(fname, encoding="utf-8") as f:
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
        f.readline()
        num_of_detector = int(f.readline().strip().split()[-1])  # Ignore detector line
        dmode = f.readline().strip().split(maxsplit=4)[:-1]
        f.readline()
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

        dat = Group(energy = self.energy, mu = self.mu)
        xafs.pre_edge(dat, group=dat)
        self.e0 = dat.e0
        self.norm = dat.norm
        self.flat = dat.flat
