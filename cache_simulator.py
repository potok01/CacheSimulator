# Adrian Potok
# CS4541
# 3/18/2023
# adrian.m.potok@wmich.edu

# Imports
import sys
import argparse

class memory_access():
    def __init__(self, access_mode, tag, set_index, block, print_address_and_size):
        self.access_mode = access_mode
        self.tag = tag
        self.set_index = set_index
        self.block = block
        self.print_address_and_size = print_address_and_size

def main():


    # Parse arguments
    parser = argparse.ArgumentParser(description='Cache Simulator using FIFO replacement strategy')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')  
    parser.add_argument('-s', '--sets', type=int, required=True, default=1, help='The number of set index bits')    
    parser.add_argument('-E', '--associativity', type=int, required=True, default=1, help='The number of lines per set')
    parser.add_argument('-b', '--blocks', type=int, required=True, default=1, help='The number of block bits')
    parser.add_argument('-t', '--trace', type=argparse.FileType('r'), required=True, help='The trace file to replay')

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    verbose_flag = args.verbose
    set_index_bits = args.sets
    associativity = args.associativity
    block_bits = args.blocks
    trace_file = args.trace

    # Calculate tag bits
    tag_bits = 64 - (block_bits + set_index_bits)

    # Parse file into array ignoring "I" lines
    try:
        # Read contents from file
        contents = trace_file.read()

        # Create list of lines from contents string
        contents = contents.split("\n")
        
        # Check the first character of each line to skip
        access_info = []
        for line in contents:
            if len(line) < 2 or line[1] not in ("S","M","L"):
                continue
            
            # Extract trace info
            parts = line.split()
            access_mode = parts[0]
            print_address_and_size = parts[1].split(",")
            print_address = print_address_and_size[0]
            if len(print_address) > 1:
                print_address_and_size = parts[1].lstrip("0")
            else:
                print_address_and_size = parts[1]

            address = str(bin(int(parts[1].split(",")[0], 16))[2:]).zfill(64)


            # Extract access info
            tag = address[ : tag_bits]
            set_index = address[tag_bits : set_index_bits + tag_bits]
            block = address[tag_bits + set_index_bits : ]
            access = memory_access(access_mode, tag, int(set_index, 2), block, print_address_and_size)
            access_info.append(access)

    finally:
        trace_file.close()

    # Setup simulated cache  
    cache = []
    for i in range(2 ** set_index_bits):
        inner_list = []
        for j in range(associativity):
            inner_list.append(None)
        cache.append(inner_list)

    # Setup cache indicies list for FIFO replacement
    cache_indicies = []
    for i in range(2 ** set_index_bits):
        cache_indicies.append(0)

    # Run cache simulation
    hits = 0
    misses = 0
    evictions = 0

    x = 0
    while x < len(access_info):
        
        # Verbose prints
        if(verbose_flag):
            print(access_info[x].access_mode + " " +  access_info[x].print_address_and_size + " ", end="")

        # y represents what line within the set we are looking at
        y = 0
        while y < associativity:

            # Current set is int representing which set we are looking at
            current_set = access_info[x].set_index

            if access_info[x].access_mode == "M":
                # Cold miss
                if cache[current_set][y] is None:
                    cache[current_set][y] = access_info[x]
                    if(verbose_flag):
                        print("miss hit")
                    hits += 1
                    misses += 1
                    y = associativity
                
                # Hit twice since access mode is M
                elif cache[current_set][y].tag == access_info[x].tag:
                    cache[current_set][y] = access_info[x]
                    if(verbose_flag):                    
                        print("hit hit")
                    hits += 2
                    y = associativity

                # Pass to increment line index until its 1 less than associativity
                elif cache[current_set][y].tag != access_info[x].tag and y < len(cache[0]) - 1:
                    pass

                # If no cold misses or hits happen we must evict and replace
                elif cache[current_set][y].tag != access_info[x].tag:
                    # Replace the first access to be placed in the cache
                    cache[current_set][cache_indicies[current_set]%associativity] = access_info[x]
                    cache_indicies[current_set] += 1
                    hits += 1
                    misses += 1
                    evictions += 1 
                    if(verbose_flag):    
                        print("miss eviction hit")
            else:
                # Cold miss                
                if cache[current_set][y] is None:
                    cache[current_set][y] = access_info[x]
                    if(verbose_flag):
                        print("miss")
                    misses += 1
                    y = associativity

                # Hit once if tag is equal
                elif cache[current_set][y].tag == access_info[x].tag:
                    cache[current_set][y] = access_info[x]
                    hits += 1
                    if(verbose_flag):
                        print("hit")
                    y = associativity

                # Pass to increment line index until its 1 less than associativity
                elif cache[current_set][y].tag != access_info[x].tag and y < len(cache[0]) - 1:
                    pass

                # If no cold misses or hits happen we must evict and replace               
                elif cache[current_set][y].tag != access_info[x].tag:
                    # Replace the first access to be placed in the cache
                    cache[current_set][cache_indicies[current_set]%associativity] = access_info[x]
                    cache_indicies[current_set] += 1
                    misses += 1
                    evictions += 1
                    if(verbose_flag):
                        print("miss eviction") 
            y = y + 1
        x = x + 1

    print(f"hits:{hits} misses:{misses} evictions:{evictions}", end="")

    return

main()