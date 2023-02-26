import gzip
import glob
import io


def find_robots(filename):
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f, encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.update(fields[0])
    return robots


def find_all_robots(logdir):
    all_robots = set()
    files = glob.glob(logdir + '/*.gz')
    for robots in map(find_robots, files):
        all_robots.update(robots)
    return all_robots


all_robots = find_all_robots('logs')
for ipaddr in all_robots:
    print(ipaddr)
