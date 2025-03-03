# Author: Joseph D Tong
# Date: 3/3/2020
# Description: Defines a XiangqiGame class with a board with XiangqiPieces and
# methods to move the pieces according to the rules of the game.


def pos_coords(position):
    """Returns a position on a XiangqiGame board as [x, y] coordinates."""
    coords = []
    x_coord = 1

    # Iterates through the list of files on a Xiangqi game board and appends the
    # numerical value of the given position's file to coords.
    for letter in "abcdefghi":

        if letter == position[0]:
            coords.append(x_coord)

        else:
            x_coord += 1

    # The rank is cast to int and appended since it's already numerical.
    coords.append(int(position[1: len(position) + 1]))

    return coords


def coords_pos(coords):
    """
    Returns the Xiangqi board position corresponding to the given [x, y]
    coordinates.
    """
    # Indexes into a string of all file labels to get file and concatenates with
    # the y-coordinate cast as a string which is the same as the rank.
    files = "abcdefghi"
    return files[coords[0] - 1] + str(coords[1])


class XiangqiPiece:
    """
    Creates a XiangqiPiece object of the given unit_type belonging to the given
    player at the given position.
    """
    def __init__(self, unit_type, player, position):
        self._unit_type = unit_type
        self._player = player
        self._coords = pos_coords(position)

    def get_unit_type(self):
        """Returns the unit type of the XiangqiPiece."""
        return self._unit_type

    def get_player(self):
        """Returns the color of the player who owns the XiangqiPiece."""
        return self._player

    def get_coords(self):
        """Returns the [x, y] coordinates of the XiangqiPiece"""
        return self._coords

    def set_coords(self, position):
        """
        Sets the [x, y] coordinates of the XiangqiPiece to the given position.
        """
        self._coords = pos_coords(position)


class XQGeneral(XiangqiPiece):
    """Creates a Xiangqi general piece."""
    def __init__(self, unit_type, player, position):
        super().__init__(unit_type, player, position)

    # Each XiangqiPiece subclass contains a __repr__ method that represents the
    # piece with the player who owns it followed by the unit type. Dashes are
    # added on either side to facilitate clear printing of the board.
    def __repr__(self):

        if self._player == "red":
            return "-" + repr(self._player) + repr(self._unit_type) + "--"

        if self._player == "black":
            return repr(self._player) + repr(self._unit_type) + "-"

    def get_moves(self, xiangqi_game):
        """Returns a list of positions the piece can move to."""
        move_list = []

        if self._player == "red":

            # Checks against only the red player's palace since the general
            # can't move outside those nine positions.
            for point in ["d1", "d2", "d3",
                          "e1", "e2", "e3",
                          "f1", "f2", "f3"]:

                # The next four code blocks (one for each orthogonal direction)
                # check whether the position is orthogonal to the piece, then
                # appends the position to the list of available moves if either
                # the position is empty or it contains an enemy piece.
                if False not in [pos_coords(point)[0] == self._coords[0],
                                 pos_coords(point)[1] == self._coords[1] + 1]:

                    if xiangqi_game.get_board()[point] == "-----------------":
                        move_list.append(point)

                    elif xiangqi_game.get_board()[point].get_player() != "red":
                        move_list.append(point)

                if False not in [pos_coords(point)[1] == self._coords[1],
                                 pos_coords(point)[0] == self._coords[0] + 1]:

                    if xiangqi_game.get_board()[point] == "-----------------":
                        move_list.append(point)

                    elif xiangqi_game.get_board()[point].get_player() != "red":
                        move_list.append(point)

                if False not in [pos_coords(point)[0] == self._coords[0],
                                 pos_coords(point)[1] == self._coords[1] - 1]:

                    if xiangqi_game.get_board()[point] == "-----------------":
                        move_list.append(point)

                    elif xiangqi_game.get_board()[point].get_player() != "red":
                        move_list.append(point)

                if False not in [pos_coords(point)[1] == self._coords[1],
                                 pos_coords(point)[0] == self._coords[0] - 1]:

                    if xiangqi_game.get_board()[point] == "-----------------":
                        move_list.append(point)

                    elif xiangqi_game.get_board()[point].get_player() != "red":
                        move_list.append(point)

        if self._player == "black":

            # Checks against only the red player's palace since the general
            # can't move outside those nine positions.
            for point in ["d8", "d9", "d10",
                          "e8", "e9", "e10",
                          "f8", "f9", "f10"]:
                if False not in [pos_coords(point)[0] == self._coords[0],
                                 pos_coords(point)[1] == self._coords[1] + 1]:

                    if xiangqi_game.get_board()[point] == "-----------------":
                        move_list.append(point)

                    elif xiangqi_game.get_board()[
                             point].get_player() != "black":
                        move_list.append(point)

                if False not in [pos_coords(point)[1] == self._coords[1],
                                 pos_coords(point)[0] == self._coords[0] + 1]:

                    if xiangqi_game.get_board()[point] == "-----------------":
                        move_list.append(point)

                    elif xiangqi_game.get_board()[
                            point].get_player() != "black":
                        move_list.append(point)

                if False not in [pos_coords(point)[0] == self._coords[0],
                                 pos_coords(point)[1] == self._coords[1] - 1]:

                    if xiangqi_game.get_board()[point] == "-----------------":
                        move_list.append(point)

                    elif xiangqi_game.get_board()[
                            point].get_player() != "black":
                        move_list.append(point)

                if False not in [pos_coords(point)[1] == self._coords[1],
                                 pos_coords(point)[0] == self._coords[0] - 1]:

                    if xiangqi_game.get_board()[point] == "-----------------":
                        move_list.append(point)

                    elif xiangqi_game.get_board()[
                            point].get_player() != "black":
                        move_list.append(point)

        return move_list


class XQAdvisor(XiangqiPiece):
    """Creates a Xiangqi advisor piece."""

    def __init__(self, unit_type, player, position):
        super().__init__(unit_type, player, position)

    def __repr__(self):

        if self._player == "red":
            return "-" + repr(self._player) + repr(self._unit_type) + "--"

        if self._player == "black":
            return repr(self._player) + repr(self._unit_type) + "-"

    def get_moves(self, xiangqi_game):
        """Returns a list of positions the piece can move to."""
        # Same as the get_moves method in XQGeneral, but checks diagonally
        # rather than orthogonally and only checks the five points Advisors can
        # reach.
        move_list = []

        if self._player == "red":

            for point in ["d1", "d3", "e2", "f1", "f3"]:

                if False not in [pos_coords(point)[0] == self._coords[0] + 1,
                                 pos_coords(point)[1] == self._coords[1] + 1]:

                    if xiangqi_game.get_board()[point] == "-----------------":
                        move_list.append(point)

                    elif xiangqi_game.get_board()[point].get_player() != "red":
                        move_list.append(point)

                if False not in [pos_coords(point)[0] == self._coords[0] - 1,
                                 pos_coords(point)[1] == self._coords[1] + 1]:

                    if xiangqi_game.get_board()[point] == "-----------------":
                        move_list.append(point)

                    elif xiangqi_game.get_board()[point].get_player() != "red":
                        move_list.append(point)

                if False not in [pos_coords(point)[0] == self._coords[0] + 1,
                                 pos_coords(point)[1] == self._coords[1] - 1]:

                    if xiangqi_game.get_board()[point] == "-----------------":
                        move_list.append(point)

                    elif xiangqi_game.get_board()[point].get_player() != "red":
                        move_list.append(point)

                if False not in [pos_coords(point)[0] == self._coords[0] - 1,
                                 pos_coords(point)[1] == self._coords[1] - 1]:

                    if xiangqi_game.get_board()[point] == "-----------------":
                        move_list.append(point)

                    elif xiangqi_game.get_board()[point].get_player() != "red":
                        move_list.append(point)

        if self._player == "black":

            for point in ["d8", "d10", "e9", "f8", "f10"]:

                if False not in [pos_coords(point)[0] == self._coords[0] + 1,
                                 pos_coords(point)[1] == self._coords[1] + 1]:

                    if xiangqi_game.get_board()[point] == "-----------------":
                        move_list.append(point)

                    elif xiangqi_game.get_board()[
                            point].get_player() != "black":
                        move_list.append(point)

                if False not in [pos_coords(point)[0] == self._coords[0] - 1,
                                 pos_coords(point)[1] == self._coords[1] + 1]:

                    if xiangqi_game.get_board()[point] == "-----------------":
                        move_list.append(point)

                    elif xiangqi_game.get_board()[
                            point].get_player() != "black":
                        move_list.append(point)

                if False not in [pos_coords(point)[0] == self._coords[0] + 1,
                                 pos_coords(point)[1] == self._coords[1] - 1]:

                    if xiangqi_game.get_board()[point] == "-----------------":
                        move_list.append(point)

                    elif xiangqi_game.get_board()[
                            point].get_player() != "black":
                        move_list.append(point)

                if False not in [pos_coords(point)[0] == self._coords[0] - 1,
                                 pos_coords(point)[1] == self._coords[1] - 1]:

                    if xiangqi_game.get_board()[point] == "-----------------":
                        move_list.append(point)

                    elif xiangqi_game.get_board()[
                            point].get_player() != "black":
                        move_list.append(point)
        return move_list


class XQElephant(XiangqiPiece):
    """Creates a Xiangqi elephant piece."""

    def __init__(self, unit_type, player, position):
        super().__init__(unit_type, player, position)

    def __repr__(self):
        if self._player == "red":
            return "-" + repr(self._player) + repr(self._unit_type) + "-"
        if self._player == "black":
            return repr(self._player) + repr(self._unit_type)

    def get_moves(self, xiangqi_game):
        """Returns a list of positions the piece can move to."""
        move_list = []

        if self._player == "red":

            # Checks only the seven positions a red elephant can move to.
            for point in ["c1", "g1", "a3", "e3", "i3", "c5", "g5"]:

                # The following code blocks are the same as for XQAdvisor except
                # the moves are checked two points diagonally instead of one and
                # the mid-point is verified to be empty.
                if False not in [pos_coords(point)[0] == self._coords[0] + 2,
                                 pos_coords(point)[1] == self._coords[1] + 2]:

                    # Finds the point between the origin and destination and
                    # checks to make sure it is empty.
                    mid_point = [self._coords[0] + 1, self._coords[1] + 1]

                    if xiangqi_game.get_board()[
                            coords_pos(mid_point)] == "-----------------":

                        if xiangqi_game.get_board()[
                                point] == "-----------------":
                            move_list.append(point)

                        elif xiangqi_game.get_board()[
                                point].get_player() != "red":
                            move_list.append(point)

                if False not in [pos_coords(point)[0] == self._coords[0] - 2,
                                 pos_coords(point)[1] == self._coords[1] + 2]:

                    mid_point = [self._coords[0] - 1, self._coords[1] + 1]

                    if xiangqi_game.get_board()[
                            coords_pos(mid_point)] == "-----------------":

                        if xiangqi_game.get_board()[
                                point] == "-----------------":
                            move_list.append(point)

                        elif xiangqi_game.get_board()[
                                point].get_player() != "red":
                            move_list.append(point)

                if False not in [pos_coords(point)[0] == self._coords[0] + 2,
                                 pos_coords(point)[1] == self._coords[1] - 2]:

                    mid_point = [self._coords[0] + 1, self._coords[1] - 1]

                    if xiangqi_game.get_board()[
                            coords_pos(mid_point)] == "-----------------":

                        if xiangqi_game.get_board()[
                                point] == "-----------------":
                            move_list.append(point)

                        elif xiangqi_game.get_board()[
                                point].get_player() != "red":
                            move_list.append(point)

                if False not in [pos_coords(point)[0] == self._coords[0] - 2,
                                 pos_coords(point)[1] == self._coords[1] - 2]:

                    mid_point = [self._coords[0] - 1, self._coords[1] - 1]

                    if xiangqi_game.get_board()[
                            coords_pos(mid_point)] == "-----------------":

                        if xiangqi_game.get_board()[
                                point] == "-----------------":
                            move_list.append(point)

                        elif xiangqi_game.get_board()[
                                point].get_player() != "red":
                            move_list.append(point)

        if self._player == "black":

            for point in ["c10", "g10", "a8", "e8", "i8", "c6", "g6"]:

                if False not in [pos_coords(point)[0] == self._coords[0] + 2,
                                 pos_coords(point)[1] == self._coords[1] + 2]:

                    mid_point = [self._coords[0] + 1, self._coords[1] + 1]

                    if xiangqi_game.get_board()[
                            coords_pos(mid_point)] == "-----------------":

                        if xiangqi_game.get_board()[
                                point] == "-----------------":
                            move_list.append(point)

                        elif xiangqi_game.get_board()[
                                point].get_player() != "black":
                            move_list.append(point)

                if False not in [pos_coords(point)[0] == self._coords[0] - 2,
                                 pos_coords(point)[1] == self._coords[1] + 2]:

                    mid_point = [self._coords[0] - 1, self._coords[1] + 1]

                    if xiangqi_game.get_board()[
                            coords_pos(mid_point)] == "-----------------":

                        if xiangqi_game.get_board()[
                                point] == "-----------------":
                            move_list.append(point)

                        elif xiangqi_game.get_board()[
                                point].get_player() != "black":
                            move_list.append(point)

                if False not in [pos_coords(point)[0] == self._coords[0] + 2,
                                 pos_coords(point)[1] == self._coords[1] - 2]:

                    mid_point = [self._coords[0] + 1, self._coords[1] - 1]

                    if xiangqi_game.get_board()[
                            coords_pos(mid_point)] == "-----------------":

                        if xiangqi_game.get_board()[
                                point] == "-----------------":
                            move_list.append(point)

                        elif xiangqi_game.get_board()[
                                point].get_player() != "black":
                            move_list.append(point)

                if False not in [pos_coords(point)[0] == self._coords[0] - 2,
                                 pos_coords(point)[1] == self._coords[1] - 2]:

                    mid_point = [self._coords[0] - 1, self._coords[1] - 1]

                    if xiangqi_game.get_board()[
                            coords_pos(mid_point)] == "-----------------":

                        if xiangqi_game.get_board()[
                                point] == "-----------------":
                            move_list.append(point)

                        elif xiangqi_game.get_board()[
                                point].get_player() != "black":
                            move_list.append(point)

        return move_list


class XQHorse(XiangqiPiece):
    """Creates a Xiangqi horse piece."""

    def __init__(self, unit_type, player, position):
        super().__init__(unit_type, player, position)

    def __repr__(self):
        if self._player == "red":
            return "--" + repr(self._player) + repr(self._unit_type) + "---"
        if self._player == "black":
            return "-" + repr(self._player) + repr(self._unit_type) + "--"

    def get_moves(self, xiangqi_game):
        """Returns a list of positions the piece can move to."""
        move_list = []

        # Checks whether a point two to the left is on the board.
        if self._coords[0] - 2 > 0:

            # Checks whether the point directly to the left is empty.
            if xiangqi_game.get_board()[
                coords_pos([self._coords[0] - 1, self._coords[
                    1]])] == "-----------------":

                # Checks whether a point down one is on the board.
                if self._coords[1] - 1 > 0:

                    # The following if/elif checks whether the target point (two
                    # left and one down from the current position) is empty or
                    # contains an enemy unit. In either case, the point is
                    # appended to move_list.
                    if xiangqi_game.get_board()[
                            coords_pos([self._coords[0] - 2, self._coords[
                                1] - 1])] == "-----------------":
                        move_list.append(coords_pos([
                            self._coords[0] - 2, self._coords[1] - 1]))

                    elif xiangqi_game.get_board()[
                            coords_pos([self._coords[0] - 2, self._coords[
                                1] - 1])].get_player() != self._player:
                        move_list.append(coords_pos([
                            self._coords[0] - 2, self._coords[1] - 1]))

                # Checks whether a point up one is on the board.
                if self._coords[1] + 1 < 11:

                    # The following if/elif checks whether the target point (two
                    # left and one up of the current position) is empty or
                    # contains an enemy unit. In either case, the point is
                    # appended to move_list.
                    if xiangqi_game.get_board()[
                            coords_pos([self._coords[0] - 2, self._coords[
                                1] + 1])] == "-----------------":
                        move_list.append(coords_pos([
                            self._coords[0] - 2, self._coords[1] + 1]))

                    elif xiangqi_game.get_board()[
                            coords_pos([self._coords[0] - 2, self._coords[
                                1] + 1])].get_player() != self._player:
                        move_list.append(coords_pos([
                            self._coords[0] - 2, self._coords[1] + 1]))

        # The following conditionals do the same as above, but in different
        # directions. The first block checks right two and up and down one, the
        # second block checks up two and left and right one, and the last block
        # checks down two and left and right one.
        if self._coords[0] + 2 < 10:

            if xiangqi_game.get_board()[
                coords_pos([self._coords[0] + 1, self._coords[
                    1]])] == "-----------------":

                if self._coords[1] - 1 > 0:

                    if xiangqi_game.get_board()[
                            coords_pos([self._coords[0] + 2, self._coords[
                                1] - 1])] == "-----------------":
                        move_list.append(coords_pos([
                            self._coords[0] + 2, self._coords[1] - 1]))

                    elif xiangqi_game.get_board()[
                            coords_pos([self._coords[0] + 2, self._coords[
                                1] - 1])].get_player() != self._player:
                        move_list.append(coords_pos([
                            self._coords[0] + 2, self._coords[1] - 1]))

                if self._coords[1] + 1 < 11:

                    if xiangqi_game.get_board()[
                            coords_pos([self._coords[0] + 2, self._coords[
                                1] + 1])] == "-----------------":
                        move_list.append(coords_pos([
                            self._coords[0] + 2, self._coords[1] + 1]))

                    elif xiangqi_game.get_board()[
                            coords_pos([self._coords[0] + 2, self._coords[
                                1] + 1])].get_player() != self._player:
                        move_list.append(coords_pos([
                            self._coords[0] + 2, self._coords[1] + 1]))

        if self._coords[1] + 2 < 11:

            if xiangqi_game.get_board()[
                coords_pos([self._coords[0], self._coords[
                    1] + 1])] == "-----------------":

                if self._coords[0] - 1 > 0:

                    if xiangqi_game.get_board()[
                            coords_pos([self._coords[0] - 1, self._coords[
                                1] + 2])] == "-----------------":
                        move_list.append(coords_pos([
                            self._coords[0] - 1, self._coords[1] + 2]))

                    elif xiangqi_game.get_board()[
                            coords_pos([self._coords[0] - 1, self._coords[
                                1] + 2])].get_player() != self._player:
                        move_list.append(coords_pos([
                            self._coords[0] - 1, self._coords[1] + 2]))

                if self._coords[0] + 1 < 10:

                    if xiangqi_game.get_board()[
                            coords_pos([self._coords[0] + 1, self._coords[
                                1] + 2])] == "-----------------":
                        move_list.append(coords_pos([
                            self._coords[0] + 1, self._coords[1] + 2]))

                    elif xiangqi_game.get_board()[
                            coords_pos([self._coords[0] + 1, self._coords[
                                1] + 2])].get_player() != self._player:
                        move_list.append(coords_pos([
                            self._coords[0] + 1, self._coords[1] + 2]))

        if self._coords[1] - 2 > 0:

            if xiangqi_game.get_board()[
                coords_pos([self._coords[0], self._coords[
                    1] - 1])] == "-----------------":

                if self._coords[0] - 1 > 0:

                    if xiangqi_game.get_board()[
                            coords_pos([self._coords[0] - 1, self._coords[
                                1] - 2])] == "-----------------":
                        move_list.append(coords_pos([
                            self._coords[0] - 1, self._coords[1] - 2]))

                    elif xiangqi_game.get_board()[
                            coords_pos([self._coords[0] - 1, self._coords[
                                1] - 2])].get_player() != self._player:
                        move_list.append(coords_pos([
                            self._coords[0] - 1, self._coords[1] - 2]))

                if self._coords[0] + 1 < 10:

                    if xiangqi_game.get_board()[
                            coords_pos([self._coords[0] + 1, self._coords[
                                1] - 2])] == "-----------------":
                        move_list.append(coords_pos([
                            self._coords[0] + 1, self._coords[1] - 2]))

                    elif xiangqi_game.get_board()[
                            coords_pos([self._coords[0] + 1, self._coords[
                                1] - 2])].get_player() != self._player:
                        move_list.append(coords_pos([
                            self._coords[0] + 1, self._coords[1] - 2]))

        return move_list


class XQChariot(XiangqiPiece):
    """Creates a Xiangqi chariot piece."""

    def __init__(self, unit_type, player, position):
        super().__init__(unit_type, player, position)

    def __repr__(self):
        if self._player == "red":
            return "-" + repr(self._player) + repr(self._unit_type) + "--"
        if self._player == "black":
            return repr(self._player) + repr(self._unit_type) + "-"

    def get_moves(self, xiangqi_game):
        """Returns a list of positions the piece can move to."""
        move_list = []

        # Special case: XQChariot is in the first file.
        if self._coords[0] == 1:

            # Iterates through the x-coordinates for the second to ninth files.
            for x_coord in range(2, 10):

                # Each point on the same rank as XQChariot is checked in
                # increasing order to determine whether each is empty.
                if xiangqi_game.get_board()[coords_pos([
                        x_coord, self._coords[1]])] != "-----------------":

                    # If the point is NOT empty and the XiangqiPiece at that
                    # point belongs to the current player, the point is not
                    # added and the loop stops checking points along that rank.
                    if xiangqi_game.get_board()[coords_pos([
                            x_coord, self._coords[
                                1]])].get_player() == self._player:
                        break

                    # If the point is NOT empty and the XiangqiPiece at that
                    # point belongs to the other player, the point is added to
                    # move_list and the loop stops iterating through that rank.
                    else:
                        move_list.append(coords_pos([x_coord, self._coords[1]]))
                        break

                # If the point is empty, the point is added to move_list and the
                # loop continues to iterate through the rank.
                else:
                    move_list.append(coords_pos([x_coord, self._coords[1]]))

        # Special Case: XQ Chariot is in the last file.
        elif self._coords[0] == 9:

            # Everything is the same as above except the loop iterates through
            # the eighth to first ranks in decreasing order.
            for x_coord in range(8, 0, -1):

                if xiangqi_game.get_board()[coords_pos([x_coord, self._coords[
                        1]])] != "-----------------":

                    if xiangqi_game.get_board()[coords_pos([
                            x_coord, self._coords[
                                1]])].get_player() == self._player:
                        break

                    else:
                        move_list.append(coords_pos([x_coord, self._coords[1]]))
                        break

                else:
                    move_list.append(coords_pos([x_coord, self._coords[1]]))

        # If the XQChariot is in any file except the first or last.
        else:

            # Iterates through the files from the XQChariot's current location
            # (not including that file) to the first file in decreasing order.
            for x_coord in range(self._coords[0] - 1, 0, -1):

                if xiangqi_game.get_board()[coords_pos([x_coord, self._coords[
                        1]])] != "-----------------":

                    if xiangqi_game.get_board()[coords_pos([
                            x_coord, self._coords[
                                1]])].get_player() == self._player:
                        break

                    else:
                        move_list.append(coords_pos([x_coord, self._coords[1]]))
                        break

                else:
                    move_list.append(coords_pos([x_coord, self._coords[1]]))

            # Iterates through the files from the XQChariot's location
            # (not including that file) to the last file in increasing order.
            for x_coord in range(self._coords[0] + 1, 10):

                if xiangqi_game.get_board()[coords_pos([x_coord, self._coords[
                        1]])] != "-----------------":

                    if xiangqi_game.get_board()[coords_pos([
                            x_coord, self._coords[
                                1]])].get_player() == self._player:
                        break

                    else:
                        move_list.append(coords_pos([x_coord, self._coords[1]]))
                        break

                else:
                    move_list.append(coords_pos([x_coord, self._coords[1]]))

        # The following code blocks do the same as above, except iterating
        # through ranks within the XQChariot's file rather than through files
        # within its rank.
        # Special Case: The XQChariot is in the first rank.
        if self._coords[1] == 1:

            for y_coord in range(2, 11):

                if xiangqi_game.get_board()[coords_pos([
                        self._coords[0], y_coord])] != "-----------------":

                    if xiangqi_game.get_board()[coords_pos([self._coords[
                            0], y_coord])].get_player() == self._player:
                        break

                    else:
                        move_list.append(coords_pos([self._coords[0], y_coord]))
                        break

                else:
                    move_list.append(coords_pos([self._coords[0], y_coord]))

        # Special Case: The XQChariot is in the tenth rank.
        elif self._coords[1] == 10:

            for y_coord in range(9, 0, -1):

                if xiangqi_game.get_board()[coords_pos([self._coords[
                        0], y_coord])] != "-----------------":

                    if xiangqi_game.get_board()[coords_pos([self._coords[
                            0], y_coord])].get_player() == self._player:
                        break

                    else:
                        move_list.append(coords_pos([self._coords[0], y_coord]))
                        break

                else:
                    move_list.append(coords_pos([self._coords[0], y_coord]))

        # The XQChariot is in any rank except the first or tenth.
        else:

            for y_coord in range(self._coords[1] - 1, 0, -1):

                if xiangqi_game.get_board()[coords_pos([self._coords[
                        0], y_coord])] != "-----------------":

                    if xiangqi_game.get_board()[coords_pos([self._coords[
                            0], y_coord])].get_player() == self._player:
                        break

                    else:
                        move_list.append(coords_pos([self._coords[0], y_coord]))
                        break

                else:
                    move_list.append(coords_pos([self._coords[0], y_coord]))

            for y_coord in range(self._coords[1] + 1, 11):

                if xiangqi_game.get_board()[coords_pos([self._coords[
                        0], y_coord])] != "-----------------":

                    if xiangqi_game.get_board()[coords_pos([self._coords[
                            0], y_coord])].get_player() == self._player:
                        break

                    else:
                        move_list.append(coords_pos([self._coords[0], y_coord]))
                        break

                else:
                    move_list.append(coords_pos([self._coords[0], y_coord]))

        # After all points the XQChariot can move to are added to move_list, the
        # list is returned.
        return move_list


class XQCannon(XiangqiPiece):
    """Creates a Xiangqi cannon piece."""

    def __init__(self, unit_type, player, position):
        super().__init__(unit_type, player, position)

    def __repr__(self):
        if self._player == "red":
            return "--" + repr(self._player) + repr(self._unit_type) + "--"
        if self._player == "black":
            return "-" + repr(self._player) + repr(self._unit_type) + "-"

    def get_moves(self, xiangqi_game):
        """Returns a list of positions the piece can move to."""
        move_list = []

        # Special case: XQCannon is in the first file.
        if self._coords[0] == 1:

            jumps = 0

            # Iterates through the x-coordinates for the second to ninth files.
            for x_coord in range(2, 10):

                # If the XQCannon has jumped a XiangqiPiece.
                if jumps == 1:

                    # If the position is not empty...
                    if xiangqi_game.get_board()[coords_pos([
                            x_coord, self._coords[1]])] != "-----------------":

                        # If the position contains a XiangqiPiece belonging to
                        # the current player, the iteration is ended and nothing
                        # more is added to move_list in this direction.
                        if xiangqi_game.get_board()[coords_pos([
                                x_coord, self._coords[
                                    1]])].get_player() == self._player:
                            break

                        # If the position contains an opponent XiangqiPiece, the
                        # position is added to move_list and the iteration is
                        # ended.
                        else:
                            move_list.append(coords_pos([
                                x_coord, self._coords[1]]))
                            break

                # If the XQCannon has not jumped another XiangqiPiece.
                if jumps == 0:

                    # If the position is empty, it is added to move_list.
                    if xiangqi_game.get_board()[coords_pos([
                            x_coord, self._coords[1]])] == "-----------------":
                        move_list.append(coords_pos([x_coord, self._coords[1]]))

                    # If the position is not empty, jumps is set to 1.
                    else:
                        jumps = 1

        # Special Case: XQCannon is in the last file.
        elif self._coords[0] == 9:

            jumps = 0

            # Everything is the same as above except the loop iterates through
            # the eighth to first ranks in decreasing order.
            for x_coord in range(8, 0, -1):

                if jumps == 1:

                    if xiangqi_game.get_board()[coords_pos([
                            x_coord, self._coords[1]])] != "-----------------":

                        if xiangqi_game.get_board()[coords_pos([
                                x_coord, self._coords[
                                    1]])].get_player() == self._player:
                            break

                        else:
                            move_list.append(coords_pos([
                                x_coord, self._coords[1]]))
                            break

                if jumps == 0:

                    if xiangqi_game.get_board()[coords_pos([
                            x_coord, self._coords[1]])] == "-----------------":
                        move_list.append(coords_pos([x_coord, self._coords[1]]))

                    else:
                        jumps = 1

        # If the XQCannon is in any file except the first or last.
        else:

            jumps = 0

            # Iterates through the files from the XQCannon's current location
            # (not including that file) to the first file in decreasing order.
            for x_coord in range(self._coords[0] - 1, 0, -1):

                if jumps == 1:

                    if xiangqi_game.get_board()[coords_pos([
                            x_coord, self._coords[1]])] != "-----------------":

                        if xiangqi_game.get_board()[coords_pos([
                                x_coord, self._coords[
                                    1]])].get_player() == self._player:
                            break

                        else:
                            move_list.append(coords_pos([
                                x_coord, self._coords[1]]))
                            break

                if jumps == 0:

                    if xiangqi_game.get_board()[coords_pos([
                            x_coord, self._coords[1]])] == "-----------------":
                        move_list.append(coords_pos([x_coord, self._coords[1]]))

                    else:
                        jumps = 1

            jumps = 0

            # Iterates through the files from the XQCannon's location
            # (not including that file) to the last file in increasing order.
            for x_coord in range(self._coords[0] + 1, 10):

                if jumps == 1:

                    if xiangqi_game.get_board()[coords_pos([
                            x_coord, self._coords[1]])] != "-----------------":

                        if xiangqi_game.get_board()[coords_pos([
                                x_coord, self._coords[
                                    1]])].get_player() == self._player:
                            break

                        else:
                            move_list.append(coords_pos([
                                x_coord, self._coords[1]]))
                            break

                if jumps == 0:

                    if xiangqi_game.get_board()[coords_pos([
                            x_coord, self._coords[1]])] == "-----------------":
                        move_list.append(coords_pos([x_coord, self._coords[1]]))

                    else:
                        jumps = 1

        # The following code blocks do the same as above, except iterating
        # through ranks within the XQCannon's file rather than through files
        # within its rank.
        # Special Case: The XQCannon is in the first rank.
        if self._coords[1] == 1:

            jumps = 0

            for y_coord in range(2, 11):

                if jumps == 1:

                    if xiangqi_game.get_board()[coords_pos([self._coords[
                            0], y_coord])] != "-----------------":

                        if xiangqi_game.get_board()[coords_pos([self._coords[
                                0], y_coord])].get_player() == self._player:
                            break

                        else:
                            move_list.append(coords_pos([
                                self._coords[0], y_coord]))
                            break

                if jumps == 0:

                    if xiangqi_game.get_board()[coords_pos([
                            self._coords[0], y_coord])] == "-----------------":
                        move_list.append(coords_pos([self._coords[0], y_coord]))

                    else:
                        jumps = 1

        # Special Case: The XQCannon is in the tenth rank.
        elif self._coords[1] == 10:

            jumps = 0

            for y_coord in range(9, 0, -1):

                if jumps == 1:

                    if xiangqi_game.get_board()[coords_pos([self._coords[
                            0], y_coord])] != "-----------------":

                        if xiangqi_game.get_board()[coords_pos([self._coords[
                                0], y_coord])].get_player() == self._player:
                            break

                        else:
                            move_list.append(coords_pos([
                                self._coords[0], y_coord]))
                            break

                if jumps == 0:

                    if xiangqi_game.get_board()[coords_pos([self._coords[
                                        0], y_coord])] == "-----------------":
                        move_list.append(coords_pos([self._coords[0], y_coord]))

                    else:
                        jumps = 1

        # The XQCannon is in any rank except the first or tenth.
        else:

            jumps = 0

            for y_coord in range(self._coords[1] - 1, 0, -1):

                if jumps == 1:

                    if xiangqi_game.get_board()[coords_pos([self._coords[
                            0], y_coord])] != "-----------------":

                        if xiangqi_game.get_board()[coords_pos([self._coords[
                                0], y_coord])].get_player() == self._player:
                            break

                        else:
                            move_list.append(coords_pos([
                                self._coords[0], y_coord]))
                            break

                if jumps == 0:

                    if xiangqi_game.get_board()[coords_pos([
                            self._coords[0], y_coord])] == "-----------------":
                        move_list.append(coords_pos([self._coords[0], y_coord]))

                    else:
                        jumps = 1

            jumps = 0

            for y_coord in range(self._coords[1] + 1, 11):

                if jumps == 1:

                    if xiangqi_game.get_board()[coords_pos([
                            self._coords[0], y_coord])] != "-----------------":

                        if xiangqi_game.get_board()[coords_pos([self._coords[
                                0], y_coord])].get_player() == self._player:
                            break

                        else:
                            move_list.append(coords_pos([
                                self._coords[0], y_coord]))
                            break

                if jumps == 0:

                    if xiangqi_game.get_board()[coords_pos([
                            self._coords[0], y_coord])] == "-----------------":
                        move_list.append(coords_pos([self._coords[0], y_coord]))

                    else:
                        jumps = 1

        return move_list


class XQSoldier(XiangqiPiece):
    """Creates a Xiangqi soldier piece."""

    def __init__(self, unit_type, player, position):
        super().__init__(unit_type, player, position)

    def __repr__(self):
        if self._player == "red":
            return "-" + repr(self._player) + repr(self._unit_type) + "--"
        if self._player == "black":
            return repr(self._player) + repr(self._unit_type) + "-"

    def get_moves(self, xiangqi_game):
        """Returns a list of positions the piece can move to."""
        move_list = []

        if self._player == "red":

            # If the XQSoldier has not reached the other end of the board, it
            # can move forward one point.
            if self._coords[1] < 10:

                # If the point directly ahead of the XQSoldier is blank, it is
                # added to move_list.
                if xiangqi_game.get_board()[coords_pos([self._coords[
                        0], self._coords[1] + 1])] == "-----------------":
                    move_list.append(coords_pos([
                        self._coords[0], self._coords[1] + 1]))

                # If the point directly ahead of the XQSoldier contains an enemy
                # XiangqiPiece, the position is added to move_list.
                elif xiangqi_game.get_board()[coords_pos([self._coords[
                        0], self._coords[1] + 1])].get_player() != self._player:
                    move_list.append(coords_pos([
                        self._coords[0], self._coords[1] + 1]))

            # If the XQSoldier has crossed the river, it can move one point
            # along ranks.
            if self._coords[1] >= 6:

                if self._coords[0] < 9:

                    # If the point directly right of the XQSoldier is blank, it
                    # is added to move_list.
                    if xiangqi_game.get_board()[coords_pos([self._coords[
                            0] + 1, self._coords[1]])] == "-----------------":
                        move_list.append(coords_pos([
                            self._coords[0] + 1, self._coords[1]]))

                    # If the point directly right of the XQSoldier contains an
                    # enemy XiangqiPiece, the position is added to move_list.
                    elif xiangqi_game.get_board()[coords_pos([self._coords[
                            0] + 1, self._coords[
                                1]])].get_player() != self._player:
                        move_list.append(coords_pos([
                            self._coords[0] + 1, self._coords[1]]))

                if self._coords[0] > 1:

                    # If the point directly left of the XQSoldier is blank, it
                    # is added to move_list.
                    if xiangqi_game.get_board()[coords_pos([self._coords[
                            0] - 1, self._coords[1]])] == "-----------------":
                        move_list.append(coords_pos([
                            self._coords[0] - 1, self._coords[1]]))

                    # If the point directly right of the XQSoldier contains an
                    # enemy XiangqiPiece, the position is added to move_list.
                    elif xiangqi_game.get_board()[coords_pos([self._coords[
                            0] - 1, self._coords[
                                1]])].get_player() != self._player:
                        move_list.append(coords_pos([
                            self._coords[0] - 1, self._coords[1]]))

        if self._player == "black":

            # If the XQSoldier has not reached the other end of the board, it
            # can move forward one point.
            if self._coords[1] > 1:

                # If the point directly ahead of the XQSoldier is blank, it is
                # added to move_list.
                if xiangqi_game.get_board()[coords_pos([self._coords[
                        0], self._coords[1] - 1])] == "-----------------":
                    move_list.append(coords_pos([
                        self._coords[0], self._coords[1] - 1]))

                # If the point directly ahead of the XQSoldier contains an enemy
                # XiangqiPiece, the position is added to move_list.
                elif xiangqi_game.get_board()[coords_pos([self._coords[
                        0], self._coords[1] - 1])].get_player() != self._player:
                    move_list.append(coords_pos([
                        self._coords[0], self._coords[1] - 1]))

            # If the XQSoldier has crossed the river, it can move one point
            # along ranks.
            if self._coords[1] <= 5:

                if self._coords[0] < 9:

                    # If the point directly right of the XQSoldier is blank, it
                    # is added to move_list.
                    if xiangqi_game.get_board()[coords_pos([self._coords[
                            0] + 1, self._coords[1]])] == "-----------------":
                        move_list.append(coords_pos([
                            self._coords[0] + 1, self._coords[1]]))

                    # If the point directly right of the XQSoldier contains an
                    # enemy XiangqiPiece, the position is added to move_list.
                    elif xiangqi_game.get_board()[coords_pos([self._coords[
                            0] + 1, self._coords[
                                1]])].get_player() != self._player:
                        move_list.append(coords_pos([
                            self._coords[0] + 1, self._coords[1]]))

                if self._coords[0] > 1:

                    # If the point directly left of the XQSoldier is blank, it
                    # is added to move_list.
                    if xiangqi_game.get_board()[coords_pos([self._coords[
                            0] - 1, self._coords[1]])] == "-----------------":
                        move_list.append(coords_pos([
                            self._coords[0] - 1, self._coords[1]]))

                    # If the point directly right of the XQSoldier contains an
                    # enemy XiangqiPiece, the position is added to move_list.
                    elif xiangqi_game.get_board()[coords_pos([self._coords[
                            0] - 1, self._coords[
                                1]])].get_player() != self._player:
                        move_list.append(coords_pos([
                            self._coords[0] - 1, self._coords[1]]))

        return move_list


class XiangqiGame:
    """
    Creates a XiangqiGame object with a _board (which contains the
    XiangqiPieces), _game_state, _check_red, _check_black, _turn, _red_pieces,
    and _black_pieces. Contains methods for moving the XiangqiPieces over the
    board according to the rules of the game.
    """
    def __init__(self):
        self._game_state = "UNFINISHED"
        self._check_red = False
        self._check_black = False
        self._checked_from = None
        self._turn = "red"

        # XiangqiPieces are created and added to the board at their appropriate
        # positions. Empty positions are initialized with a value of
        # "-----------------" to facilitate clear printing of the board.
        self._board = {"a1": XQChariot("chariot", "red", "a1"),
                       "a2": "-----------------", "a3": "-----------------",
                       "a4": XQSoldier("soldier", "red", "a4"),
                       "a5": "-----------------", "a6": "-----------------",
                       "a7": XQSoldier("soldier", "black", "a7"),
                       "a8": "-----------------", "a9": "-----------------",
                       "a10": XQChariot("chariot", "black", "a10"),
                       "b1": XQHorse("horse", "red", "b1"),
                       "b2": "-----------------",
                       "b3": XQCannon("cannon", "red", "b3"),
                       "b4": "-----------------", "b5": "-----------------",
                       "b6": "-----------------", "b7": "-----------------",
                       "b8": XQCannon("cannon", "black", "b8"),
                       "b9": "-----------------",
                       "b10": XQHorse("horse", "black", "b10"),
                       "c1": XQElephant("elephant", "red", "c1"),
                       "c2": "-----------------", "c3": "-----------------",
                       "c4": XQSoldier("soldier", "red", "c4"),
                       "c5": "-----------------", "c6": "-----------------",
                       "c7": XQSoldier("soldier", "black", "c7"),
                       "c8": "-----------------", "c9": "-----------------",
                       "c10": XQElephant("elephant", "black", "c10"),
                       "d1": XQAdvisor("advisor", "red", "d1"),
                       "d2": "-----------------", "d3": "-----------------",
                       "d4": "-----------------", "d5": "-----------------",
                       "d6": "-----------------", "d7": "-----------------",
                       "d8": "-----------------", "d9": "-----------------",
                       "d10": XQAdvisor("advisor", "black", "d10"),
                       "e1": XQGeneral("general", "red", "e1"),
                       "e2": "-----------------", "e3": "-----------------",
                       "e4": XQSoldier("soldier", "red", "e4"),
                       "e5": "-----------------", "e6": "-----------------",
                       "e7": XQSoldier("soldier", "black", "e7"),
                       "e8": "-----------------", "e9": "-----------------",
                       "e10": XQGeneral("general", "black", "e10"),
                       "f1": XQAdvisor("advisor", "red", "f1"),
                       "f2": "-----------------", "f3": "-----------------",
                       "f4": "-----------------", "f5": "-----------------",
                       "f6": "-----------------", "f7": "-----------------",
                       "f8": "-----------------", "f9": "-----------------",
                       "f10": XQAdvisor("advisor", "black", "f10"),
                       "g1": XQElephant("elephant", "red", "g1"),
                       "g2": "-----------------", "g3": "-----------------",
                       "g4": XQSoldier("soldier", "red", "g4"),
                       "g5": "-----------------", "g6": "-----------------",
                       "g7": XQSoldier("soldier", "black", "g7"),
                       "g8": "-----------------", "g9": "-----------------",
                       "g10": XQElephant("elephant", "black", "g10"),
                       "h1": XQHorse("horse", "red", "h1"),
                       "h2": "-----------------",
                       "h3": XQCannon("cannon", "red", "h3"),
                       "h4": "-----------------", "h5": "-----------------",
                       "h6": "-----------------", "h7": "-----------------",
                       "h8": XQCannon("cannon", "black", "h8"),
                       "h9": "-----------------",
                       "h10": XQHorse("horse", "black", "h10"),
                       "i1": XQChariot("chariot", "red", "i1"),
                       "i2": "-----------------", "i3": "-----------------",
                       "i4": XQSoldier("soldier", "red", "i4"),
                       "i5": "-----------------", "i6": "-----------------",
                       "i7": XQSoldier("soldier", "black", "i7"),
                       "i8": "-----------------", "i9": "-----------------",
                       "i10": XQChariot("chariot", "black", "i10")}

        # Each player's pieces are stored in a dictionary.
        self._red_pieces = {"general": self._board["e1"],
                            "advisor_1": self._board["d1"],
                            "advisor_2": self._board["f1"],
                            "elephant_1": self._board["c1"],
                            "elephant_2": self._board["g1"],
                            "horse_1": self._board["b1"],
                            "horse_2": self._board["h1"],
                            "chariot_1": self._board["a1"],
                            "chariot_2": self._board["i1"],
                            "cannon_1": self._board["b3"],
                            "cannon_2": self._board["h3"],
                            "soldier_1": self._board["a4"],
                            "soldier_2": self._board["c4"],
                            "soldier_3": self._board["e4"],
                            "soldier_4": self._board["g4"],
                            "soldier_5": self._board["i4"]}
        self._black_pieces = {"general": self._board["e10"],
                              "advisor_1": self._board["d10"],
                              "advisor_2": self._board["f10"],
                              "elephant_1": self._board["c10"],
                              "elephant_2": self._board["g10"],
                              "horse_1": self._board["b10"],
                              "horse_2": self._board["h10"],
                              "chariot_1": self._board["a10"],
                              "chariot_2": self._board["i10"],
                              "cannon_1": self._board["b8"],
                              "cannon_2": self._board["h8"],
                              "soldier_1": self._board["a7"],
                              "soldier_2": self._board["c7"],
                              "soldier_3": self._board["e7"],
                              "soldier_4": self._board["g7"],
                              "soldier_5": self._board["i7"]}

    def set_game_state(self, state):
        """Updates the _game_state to the given state."""
        self._game_state = state

    def get_game_state(self):
        """Returns the _game_state."""
        return self._game_state

    def get_board(self):
        """Returns the game board."""
        return self._board

    def is_in_check(self, player):
        """Returns True if the given player is in check or False if not."""
        if player == "red":
            return self._check_red

        if player == "black":
            return self._check_black

    def print_board(self):
        """Prints the game board."""
        # Prints the file labels at the top of the board.
        print("           a         ",
              "         b         ",
              "         c         ",
              "         d         ",
              "         e         ",
              "         f         ",
              "         g         ",
              "         h         ",
              "         i         ")

        # Rank labels are printed on the left of each rank.
        print("1 -", self._board["a1"], "-", self._board["b1"], "-",
              self._board["c1"], "-", self._board["d1"], "-", self._board["e1"],
              "-", self._board["f1"], "-", self._board["g1"], "-",
              self._board["h1"], "-", self._board["i1"])

        # Symbols are printed between each rank to make it look like the lines
        # on  a real board.
        print("           |         ",
              "         |         ",
              "         |         ",
              "         |''''-----",
              "---..... | .....---",
              "-----''''|         ",
              "         |         ",
              "         |         ",
              "         |         ")

        print("2 -", self._board["a2"], "-", self._board["b2"], "-",
              self._board["c2"], "-", self._board["d2"], "-", self._board["e2"],
              "-", self._board["f2"], "-", self._board["g2"], "-",
              self._board["h2"], "-", self._board["i2"])

        print("           |         ",
              "         |         ",
              "         |         ",
              "         |....-----",
              "---''''' | '''''---",
              "-----....|         ",
              "         |         ",
              "         |         ",
              "         |         ")

        print("3 -", self._board["a3"], "-", self._board["b3"], "-",
              self._board["c3"], "-", self._board["d3"], "-", self._board["e3"],
              "-", self._board["f3"], "-", self._board["g3"], "-",
              self._board["h3"], "-", self._board["i3"])

        print("           |         ",
              "         |         ",
              "         |         ",
              "         |         ",
              "         |         ",
              "         |         ",
              "         |         ",
              "         |         ",
              "         |         ")

        print("4 -", self._board["a4"], "-", self._board["b4"], "-",
              self._board["c4"], "-", self._board["d4"], "-", self._board["e4"],
              "-", self._board["f4"], "-", self._board["g4"], "-",
              self._board["h4"], "-", self._board["i4"])

        print("           |         ",
              "         |         ",
              "         |         ",
              "         |         ",
              "         |         ",
              "         |         ",
              "         |         ",
              "         |         ",
              "         |         ")

        print("5 -", self._board["a5"], "-", self._board["b5"], "-",
              self._board["c5"], "-", self._board["d5"], "-", self._board["e5"],
              "-", self._board["f5"], "-", self._board["g5"], "-",
              self._board["h5"], "-", self._board["i5"])

        print("           |         ",
              "                   ",
              "                   ",
              "                   ",
              "                   ",
              "                   ",
              "                   ",
              "                   ",
              "         |         ")

        print("6 -", self._board["a6"], "-", self._board["b6"], "-",
              self._board["c6"], "-", self._board["d6"], "-", self._board["e6"],
              "-", self._board["f6"], "-", self._board["g6"], "-",
              self._board["h6"], "-", self._board["i6"])

        print("           |         ",
              "         |         ",
              "         |         ",
              "         |         ",
              "         |         ",
              "         |         ",
              "         |         ",
              "         |         ",
              "         |         ")

        print("7 -", self._board["a7"], "-", self._board["b7"], "-",
              self._board["c7"], "-", self._board["d7"], "-", self._board["e7"],
              "-", self._board["f7"], "-", self._board["g7"], "-",
              self._board["h7"], "-", self._board["i7"])

        print("           |         ",
              "         |         ",
              "         |         ",
              "         |         ",
              "         |         ",
              "         |         ",
              "         |         ",
              "         |         ",
              "         |         ")

        print("8 -", self._board["a8"], "-", self._board["b8"], "-",
              self._board["c8"], "-", self._board["d8"], "-", self._board["e8"],
              "-", self._board["f8"], "-", self._board["g8"], "-",
              self._board["h8"], "-", self._board["i8"])

        print("           |         ",
              "         |         ",
              "         |         ",
              "         |''''-----",
              "---..... | .....---",
              "-----''''|         ",
              "         |         ",
              "         |         ",
              "         |         ")

        print("9 -", self._board["a9"], "-", self._board["b9"], "-",
              self._board["c9"], "-", self._board["d9"], "-", self._board["e9"],
              "-", self._board["f9"], "-", self._board["g9"], "-",
              self._board["h9"], "-", self._board["i9"])

        print("           |         ",
              "         |         ",
              "         |         ",
              "         |....-----",
              "---''''' | '''''---",
              "-----....|         ",
              "         |         ",
              "         |         ",
              "         |         ")

        print("10-", self._board["a10"], "-", self._board["b10"], "-",
              self._board["c10"], "-", self._board["d10"], "-",
              self._board["e10"], "-", self._board["f10"], "-",
              self._board["g10"], "-", self._board["h10"], "-",
              self._board["i10"])

    def check_check(self, player, ignore_pos):
        """
        Helper function for make_move and is_checkmate. Checks whether the given
        player is in check.
        """

        if player == "red":

            # Checks the moves of all black pieces.
            for piece in self._black_pieces:

                # Does not check any piece at the ignore position if it is the
                # turn of the player being check_check'd so that the moves of a
                # captured XiangqiPiece will not be considered.
                if (self._turn == "red" and coords_pos(self._black_pieces[
                        piece
                        ].get_coords()) != ignore_pos) or self._turn != "red":

                    # Checks whether the position of the red player's general is
                    # in the move_list of any black piece.
                    if self._board[ignore_pos].get_unit_type() == "general":

                        if ignore_pos in self._black_pieces[
                                piece].get_moves(self):
                            return True

                    elif coords_pos(self._red_pieces[
                            "general"].get_coords()) in self._black_pieces[
                                piece].get_moves(self):
                        return True

        # Same as above, but checks the black general against all red pieces.
        if player == "black":

            for piece in self._red_pieces:

                if (self._turn == "black" and coords_pos(self._red_pieces[
                        piece
                        ].get_coords()) != ignore_pos) or self._turn != "black":

                    if self._board[ignore_pos].get_unit_type() == "general":

                        if ignore_pos in self._red_pieces[
                                piece].get_moves(self):
                            return True

                    elif coords_pos(self._black_pieces[
                            "general"].get_coords()) in self._red_pieces[
                                piece].get_moves(self):
                        return True

        # Checks whether the two generals are on the same file.
        if self._red_pieces["general"].get_coords()[
                0] == self._black_pieces["general"].get_coords()[0]:

            # A variable is initialized to store whether any pieces
            # exist between the two generals.
            intervene = False

            # Iterates through each rank between the two generals.
            for rank in range(self._red_pieces["general"].get_coords()[
                    1] + 1, self._black_pieces["general"].get_coords()[1]):

                print(rank)

                # Checks whether each position along the file is
                # empty. If any is not, sets intervene to True and
                # ends the loop.
                if self._board[coords_pos([self._red_pieces[
                        "general"].get_coords()[
                            0], rank])] != "-----------------":
                    intervene = True
                    break

            # If no XiangqiPieces exist between the two generals,
            # returns True.
            if not intervene:
                return True

        # If no check conditions have been met, returns False.
        print(">>>")
        return False

    def is_checkmate(self, player):
        """
        Helper function for make_move. Checks whether the given player is in
        checkmate.
        """

        if player == "red":
            pieces = self._red_pieces

        else:
            pieces = self._black_pieces

        # Iterates through the checked player's pieces.
        for piece in pieces:

            # Iterates through each possible move.
            for move in pieces[piece].get_moves(self):

                # Stores the current values at the origin and destination of
                # each move for later reference.
                save_origin = self._board[
                    coords_pos(pieces[piece].get_coords())]
                save_destination = self._board[move]
                save_coords = pieces[piece].get_coords()

                self._board[move] = self._board[
                    coords_pos(pieces[piece].get_coords())]
                self._board[coords_pos(pieces[
                    piece].get_coords())] = "-----------------"

                # Sets the XiangqiPiece's coordinates to its new position.
                self._board[move].set_coords(move)

                # Checks whether the move got the player out of check. If so,
                # the board and coords are reset and False is returned.
                if not self.check_check(player, move):
                    self._board[move] = save_destination
                    self._board[coords_pos(save_coords)] = save_origin
                    save_origin.set_coords(coords_pos(save_coords))
                    return False

                # If the move did not remove the check on the player, the board
                # is reset and the loop continues.
                self._board[move] = save_destination
                self._board[coords_pos(save_coords)] = save_origin
                save_origin.set_coords(coords_pos(save_coords))

        # If no move removed the check on the player, True is returned.
        return True

    def make_move(self, origin, destination):
        """
        If the origin contains a XiangqiPiece belonging to the current player
        and the destination is a valid move, the XiangqiPiece is moved to the
        destination and any captured enemy XiangqiPiece is removed from the
        board and the opposing player's list of XiangqiPieces.
        """

        # Checks if there is a XiangqiPiece at the origin.
        if self._board[origin] == "-----------------":
            return False

        # Checks if XiangqiPiece at the origin belongs to current player.
        if self._board[origin].get_player() != self._turn:
            return False

        # Checks if the XiangqiPiece at the origin can move to the destination.
        if destination not in self._board[origin].get_moves(self):
            return False

        # Saves the current values at the origin and destination so they can be
        # referred to after the values are updated.
        save_origin = self._board[origin]
        save_destination = self._board[destination]
        save_coords = self._board[origin].get_coords()

        self._board[destination] = self._board[origin]
        self._board[origin] = "-----------------"

        # Sets the XiangqiPiece's coordinates to its new position.
        self._board[destination].set_coords(destination)

        # Checks whether the move has placed the player's own general in check.
        # If so, origin, destination, and XiangqiPiece coords are reset.
        if self.check_check(self._turn, destination):
            self._board[destination] = save_destination
            self._board[origin] = save_origin
            save_origin.set_coords(coords_pos(save_coords))
            return False

        # If the destination was not blank...
        if save_destination != "-----------------":

            # If the XiangqiPiece at the destination belonged to red player.
            if save_destination.get_player() == "red":

                # Iterates through the red player's pieces and deletes the
                # one that was captured.
                for piece in self._red_pieces:

                    if coords_pos(self._red_pieces[
                            piece].get_coords()) == destination:
                        del self._red_pieces[piece]
                        break

            # If the XiangqiPiece at destination belonged to black player.
            if save_destination.get_player() == "black":

                # Iterates through the black player's pieces and deletes the
                # one that was captured.
                for piece in self._black_pieces:

                    if coords_pos(self._black_pieces[
                            piece].get_coords()) == destination:
                        del self._black_pieces[piece]
                        break

        # Checks whether the other player was placed in check. If so, sets that
        # player's in check state to True.
        if self._turn == "red":

            if self.check_check("black", destination):
                self._check_black = True

                # Checks whether the checked player is in checkmate.
                if self.is_checkmate("black"):
                    self._game_state = "RED_WON"

            # Sets red player's check state to False.
            self._check_red = False

        if self._turn == "black":

            if self.check_check("red", destination):
                self._check_red = True

                if self.is_checkmate("black"):
                    self._game_state = "RED_WON"

            self._check_black = False

        # If the move was made successfully, the turn is updated and True is
        # returned after player pieces and check states, board, and game state
        # have all been updated.
        if self._turn == "red":
            self._turn = "black"

        else:
            self._turn = "red"

        return True
