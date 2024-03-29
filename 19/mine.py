from absl import app
import re

class BluePrint:

    def __init__(self, number, ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian) -> None:
        self.number = number
        self.ore_ore = ore_ore
        self.clay_ore = clay_ore
        self.obsidian_ore = obsidian_ore
        self.obsidian_clay = obsidian_clay
        self.geode_ore = geode_ore
        self.geode_obsidian = geode_obsidian

    def max_ore(self):
        # return 10000
        return max(self.ore_ore, self.clay_ore, self.obsidian_ore, self.geode_ore)
    
    def max_clay(self):
        # return 10000
        return self.obsidian_clay
    
    def max_obsidian(self):
        # return 10000
        return self.geode_obsidian

field_size = 10

num_field = 0
time_field = 1 * field_size 
ore_field = 2 * field_size
ore_robots_field = 3 * field_size
clay_field = 4 * field_size
clay_robots_field = 5 * field_size
obsidian_field = 6 * field_size
obsidian_robot_field = 7 * field_size
geode_field = 8 * field_size
geode_robot_field = 9 *field_size

max_geodes = 0
seen_states = set()
ct = 0

time_limit = 24

def process(state, time, blue_print: BluePrint):
    global max_geodes, ct
    state = set_field(time_field, time, state)
    ct += 1
    # if len(seen_states) == 0:
    #     print('Empty seen states')
    if state in seen_states:
        return
    seen_states.add(state)

    
    ore = get_field(ore_field, state)
    clay = get_field(clay_field, state)
    obsidian = get_field(obsidian_field, state)
    geode = get_field(geode_field, state)

    ore_robots = get_field(ore_robots_field, state)
    clay_robots = get_field(clay_robots_field, state)
    obsidian_robots = get_field(obsidian_robot_field, state)
    geode_robots = get_field(geode_robot_field, state)

    istate = [ore_robots, clay_robots, obsidian_robots, geode_robots, ore, clay, obsidian, geode]

    # if istate == [1,0,0,0,0,0,0,0] or istate == [1,0,0,0,1,0,0,0] or istate == [2,0,0,0,1,0,0,0] or istate == [2,1,0,0,2,0,0,0] or istate == [2,2,0,0,3,2,0,0] or istate == [2,3,0,0,2,4,0,0] or istate == [2,4,0,0,3,10,0,0] or istate == [2,4,1,0,3,10,0,0] or istate == [2,4,1,0,2,4,0,0] or istate == [2,4,2,0,5,6,3,0] or istate == [2,4,2,0,7,10,5,0]:
    #     print(f'At {time} with {istate}')

    # time_remaining = (time_limit - time)
    # max_geode_remaining = time_remaining * (time_remaining + 1) / 2 + geode_robots
    # if max_geode_remaining < max_geodes:
    #     # print(f'{max_geode_remaining} < {max_geodes}')
    #     return

    # print(f'state 0 {state:b}')
    if time > time_limit:
        # print(f'ore {ore} ore_robots {ore_robots} clay {clay} clay_robots {clay_robots} obsidian {obsidian} obsidian_robots {obsidian_robots} geode {geode} geode {geode_robots} max_geodes {max_geodes}')
        if geode > max_geodes:  
            max_geodes = geode
            # if geode == 9:
                # print(f'ore {ore} ore_robots {ore_robots} clay {clay} clay_robots {clay_robots} obsidian {obsidian} obsidian_robots {obsidian_robots} geode {geode} geode {geode_robots} max_geodes {max_geodes}')
        return
    



    


    # Mine stones
    state = set_field(ore_field, ore + ore_robots, state)
    state = set_field(clay_field, clay + clay_robots, state)
    state = set_field(obsidian_field, obsidian + obsidian_robots, state)
    state = set_field(geode_field, geode + geode_robots, state)

    n_ore = get_field(ore_field, state)
    n_clay = get_field(clay_field, state)
    n_obsidian = get_field(obsidian_field, state)
    n_geode = get_field(geode_field, state)
    

    # build possible robots
    if ore >= blue_print.ore_ore  and ore_robots < blue_print.max_ore():
        new_state = set_field(ore_robots_field, ore_robots + 1, state)
        new_state = set_field(ore_field, n_ore - blue_print.ore_ore, new_state)
        process(new_state, time + 1, blue_print)
    if ore >= blue_print.clay_ore and clay_robots < blue_print.max_clay():
        new_state = set_field(clay_robots_field, clay_robots + 1, state)
        new_state = set_field(ore_field, n_ore - blue_print.clay_ore, new_state)
        process(new_state, time + 1, blue_print)
    if ore >= blue_print.obsidian_ore and clay >= blue_print.obsidian_clay and obsidian_robots < blue_print.max_obsidian():
        new_state = set_field(obsidian_robot_field, obsidian_robots + 1, state)
        # new_or = get_field(obsidian_robot_field, new_state)
        # print(f'new_or {new_or}')
        new_state = set_field(ore_field, n_ore - blue_print.obsidian_ore, new_state)
        # new_or2 = get_field(obsidian_robot_field, new_state)
        # print(f'new_or2 {new_or2}')
        new_state = set_field(clay_field, n_clay - blue_print.obsidian_clay, new_state)
        # new_or3 = get_field(obsidian_robot_field, new_state)
        # print(f'new_or3 {new_or3}')
        process(new_state, time + 1, blue_print)
    if ore >= blue_print.geode_ore and obsidian >= blue_print.geode_obsidian:
        new_state = set_field(geode_robot_field, geode_robots + 1, state)
        new_state = set_field(ore_field, n_ore - blue_print.geode_ore, new_state)
        new_state = set_field(obsidian_field, n_obsidian - blue_print.geode_obsidian, new_state)
        process(new_state, time + 1, blue_print)
    
    process(state, time + 1, blue_print)
    

    


def set_field(field, value, state):
    global field_size
    r = ((1 << field_size) - 1 << field)
    state = state & ~r
    return state | (value << field)

def get_field(field, state):
    global field_size
    r = ((1 << field_size) - 1 << field)
    # print(f'r {r:b}')
    masked = state & r
    # print(f'masked {masked:b}')
    # print(f'field * field_size {field}')
    f = masked >> field
    # print(f'f {f:b}')
    return f

def main(argv):
    global max_geodes, seen_states
    file_name = '19/test_input.txt'
    if len(argv) >= 2:
        file_name = argv[1]
    
    f = open(file_name)

    total_quality = 0

    while line := f.readline().strip():
        max_geodes = 0
        seen_states = set()
        nums = re.findall(r'\d+', line)
        blue_print = BluePrint(int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3]), int(nums[4]), int(nums[5]), int(nums[6]))
        print(blue_print.__dict__)
        start = set_field(ore_robots_field, 1, 0)
        process(start, 1, blue_print)
        print(f'max: {max_geodes}')
        total_quality += blue_print.number * max_geodes
        
        # print(f'ct {ct}')
        # break

    print(f'total_quality {total_quality}')
    print(f'ct {ct}')
    

    
    # state = set_field(ore_field, 23, 0)
    # state = set_field(clay_field, 45, state)
    # state = set_field(ore_field, 34, state)
    # print(f'state {state:b}')
    # f = get_field(ore_field, state)
    # print(f)

    
if __name__ == "__main__":
    app.run(main)





    