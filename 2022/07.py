
class Algorithm:
    @staticmethod
    def check_is_file(string):
        return string.isnumeric()

    def __init__(self, file_path):
        self.file_path = file_path
        self.sum_per_dir = []

    def go(self):
        file = open(self.file_path)
        lines = file.readlines()

        self.recursive(lines)

        for tuple in self.sum_per_dir:
            print(tuple)

        print(self.total_sum_dir_leq(100000)) # sum
        self.delete_to_free_up_space(70000000, 30000000, 42536714) # on delete

    # max(self.sum_per_dir, key=lambda x: x[1])
    def recursive(self, lines):
        if len(lines) == 3:
            print("Aici")
        if not lines:
            return 0

        # take the name of current dir
        line = lines.pop(0)
        segments = line.replace("\n", "").split(" ")

        # current dir name
        name_parent_dir = segments[2]

        # pop the ls command and get the first line of contents
        lines.pop(0)
        line = lines.pop(0)
        segments = line.replace("\n", "").split(" ")

        sum_dir = 0
        # while we go through current dir
        while segments[0] != self.COMMAND_LINE:

            if self.FILE_ENTITY(segments[0]):
                sum_dir += int(segments[0])
            # if the execution stops in the middle of dir
            if not lines:
                break

            line = lines.pop(0)
            segments = line.replace("\n", "").split(" ")

        # put the command back in list if it's not empty
        if lines:
            lines.insert(0, line)

        # while we don't close de dir
        while lines and (segments[-1] != self.OUT_CMD):
            sum_dir += self.recursive(lines)

            # if the execution stops in the middle of dir
            if not lines:
                break

            line = lines.pop(0)
            segments = line.replace("\n", "").split(" ")
            # put cd-s back in list in order to work with them in next function
            lines.insert(0, line)

        # get out the $ cd .. command
        if lines:
            lines.pop(0)
        self.sum_per_dir.append([name_parent_dir, sum_dir])
        return sum_dir

    def total_sum_dir_leq(self, sum):
        total_sum = 0
        for tuple in self.sum_per_dir:
            if tuple[1] <= sum:
                total_sum += tuple[1]
        return total_sum

    def delete_to_free_up_space(self, space_available, space_needed, space_used):

        collections = []
        for tuple in self.sum_per_dir:
            if space_available - space_used + tuple[1] >= space_needed:
                collections.append(tuple[1])
        minim = min(collections)
        print(minim)

    COMMAND_LINE = "$"
    CHANGE_DIR_CMD = "cd"
    DIRECTORY_ENTITY = "dir"
    FILE_ENTITY = check_is_file
    OUT_CMD = ".."


def print_hi(name):
    algorithm = Algorithm("commands.txt")
    algorithm.go()


if __name__ == '__main__':
    print_hi('PyCharm')

