# Cache Simulator
Usage: cache_simulator.py [-h] [-v] -s SETS -E ASSOCIATIVITY -b BLOCKS -t TRACE

Cache Simulator using FIFO replacement strategy

Options:
  -h, --help            show this help message and exit
  -v, --verbose         Enable verbose output
  -s SETS, --sets SETS  The number of set index bits
  -E ASSOCIATIVITY, --associativity ASSOCIATIVITY
                        The number of lines per set
  -b BLOCKS, --blocks BLOCKS
                        The number of block bits
  -t TRACE, --trace TRACE
                        The trace file to replay
